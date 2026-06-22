"""Generira slike rezultatov za 8. poglavje diplome iz numeričnih CSV artefaktov.

Skript ne uporablja generativnih slikovnih modelov. Vse slike nastanejo
iz rezultatnih tabel s knjižnicama pandas in matplotlib.

Primer uporabe iz korena repozitorija `diploma-latex` z aktivnim okoljem `gfm`:

    python skripte/generiraj_slike_rezultatov.py

Privzeto bere rezultate iz sosednjega repozitorija `GFM-for-eyetracker`:
`results/quick_v1_v2_comparison/RETAIN_2026-06-12_16-29-08/tables`.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


SIGNAL_ORDER = ["gaze_only", "pupil_only", "gaze_pupil", "all_signals"]
SIGNAL_LABELS = {
    "gaze_only": "samo pogled",
    "pupil_only": "samo zenici",
    "gaze_pupil": "pogled in zenici",
    "all_signals": "vsi signali",
}

CLASS_LABELS = {
    "Low valence": "nizka valenca",
    "High valence": "visoka valenca",
}

CLASS_SHORT_LABELS = {
    "Low valence": "nizka",
    "High valence": "visoka",
}

CONFUSION_MODEL_LABELS = {
    "SVM": "SVM",
    "HeteroGCNMLPWeights": "HeteroGCN-MLP-w",
}


def parse_args() -> argparse.Namespace:
    script_path = Path(__file__).resolve()
    diploma_root = script_path.parents[1]
    workspace_root = script_path.parents[2]
    default_tables_dir = (
        workspace_root
        / "GFM-for-eyetracker"
        / "results"
        / "quick_v1_v2_comparison"
        / "RETAIN_2026-06-12_16-29-08"
        / "tables"
    )

    parser = argparse.ArgumentParser(
        description="Generira reproducibilne Matplotlib slike za poglavje Rezultati."
    )
    parser.add_argument(
        "--tables-dir",
        type=Path,
        default=default_tables_dir,
        help="Mapa z rezultati CSV iz eksperimentalnega repozitorija.",
    )
    parser.add_argument(
        "--results-figures-dir",
        type=Path,
        default=diploma_root / "slike" / "rezultati",
        help="Izhodna mapa za slike rezultatov.",
    )
    parser.add_argument(
        "--data-figures-dir",
        type=Path,
        default=diploma_root / "slike" / "podatki",
        help="Izhodna mapa za slike porazdelitve podatkov.",
    )
    parser.add_argument("--dpi", type=int, default=300, help="Ločljivost izhodnih PNG slik.")
    return parser.parse_args()


def format_decimal(value: float) -> str:
    return f"{value:.1f}".replace(".", ",")


def style_axes(ax: plt.Axes) -> None:
    ax.tick_params(axis="both", length=0, labelsize=9)
    for spine in ax.spines.values():
        spine.set_visible(False)


def load_main_metrics(tables_dir: Path) -> pd.DataFrame:
    path = tables_dir / "thesis_signal_set_model_metrics.csv"
    df = pd.read_csv(path)
    expected_columns = {"signal_set", "model_order", "model", "accuracy", "macro_f1"}
    missing = expected_columns.difference(df.columns)
    if missing:
        raise ValueError(f"V {path} manjkajo stolpci: {sorted(missing)}")
    return df


def generate_main_comparison_heatmap(df: pd.DataFrame, output_path: Path, dpi: int) -> None:
    df = df[df["signal_set"].isin(SIGNAL_ORDER)].copy()
    df["display_model"] = df["model"]
    df["display_signal"] = df["signal_set"].map(SIGNAL_LABELS)

    ordered_models = (
        df[["model_order", "display_model"]]
        .drop_duplicates()
        .sort_values("model_order")["display_model"]
        .tolist()
    )

    macro_f1 = (
        df.pivot(index="display_model", columns="display_signal", values="macro_f1")
        .loc[ordered_models, [SIGNAL_LABELS[key] for key in SIGNAL_ORDER]]
    )
    accuracy = (
        df.pivot(index="display_model", columns="display_signal", values="accuracy")
        .loc[ordered_models, [SIGNAL_LABELS[key] for key in SIGNAL_ORDER]]
    )
    annotations = accuracy.copy().astype(object)
    for row_label in accuracy.index:
        for column_label in accuracy.columns:
            annotations.loc[row_label, column_label] = (
                f"{accuracy.loc[row_label, column_label]:.3f} / "
                f"{macro_f1.loc[row_label, column_label]:.3f}"
            )

    fig, ax = plt.subplots(figsize=(8.6, 6.4))
    sns.heatmap(
        accuracy,
        annot=annotations,
        fmt="",
        cmap="Blues",
        vmin=0.0,
        vmax=1.0,
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"label": "točnost"},
        ax=ax,
    )
    ax.set_title("Primerjava modelov po signalnih množicah - točnost", fontsize=12, pad=10)
    ax.set_xlabel("množica signalov")
    ax.set_ylabel("model")
    ax.tick_params(axis="x", rotation=0)
    ax.tick_params(axis="y", rotation=0)
    fig.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def load_confusion_matrices(tables_dir: Path) -> pd.DataFrame:
    path = tables_dir / "confusion_matrices.csv"
    df = pd.read_csv(path)
    expected_columns = {
        "signal_set",
        "summary_model_name",
        "true_class_name",
        "pred_class_name",
        "row_normalized",
    }
    missing = expected_columns.difference(df.columns)
    if missing:
        raise ValueError(f"V {path} manjkajo stolpci: {sorted(missing)}")
    return df


def confusion_matrix_values(df: pd.DataFrame, signal_set: str, model_name: str) -> np.ndarray:
    """Vrne vrstično normalizirano matriko zmede v vrstnem redu razredov iz runnerja."""
    subset = df[(df["signal_set"] == signal_set) & (df["summary_model_name"] == model_name)]
    if subset.empty:
        raise ValueError(f"Ni matrike zmede za signal_set={signal_set}, model={model_name}.")

    class_order = ["Low valence", "High valence"]
    return (
        subset.pivot(index="true_class_name", columns="pred_class_name", values="row_normalized")
        .loc[class_order, class_order]
        .to_numpy()
    )


def draw_confusion_matrix(ax: plt.Axes, matrix: np.ndarray, title: str) -> None:
    labels = ["Low valence", "High valence"]
    sns.heatmap(
        matrix,
        annot=True,
        fmt=".2f",
        cmap="Blues",
        vmin=0.0,
        vmax=1.0,
        cbar=False,
        ax=ax,
        xticklabels=labels,
        yticklabels=labels,
    )
    ax.set_xlabel("predicted")
    ax.set_ylabel("true")
    ax.set_title(title, fontsize=11)
    ax.tick_params(axis="y", rotation=90)
    for label in ax.get_yticklabels():
        label.set_horizontalalignment("center")
        label.set_verticalalignment("center")


def generate_confusion_matrix(
    df: pd.DataFrame,
    signal_set: str,
    model_name: str,
    output_path: Path,
    dpi: int,
) -> None:
    matrix = confusion_matrix_values(df, signal_set, model_name)

    fig, ax = plt.subplots(figsize=(4.6, 3.7))
    display_model_name = CONFUSION_MODEL_LABELS.get(model_name, model_name)
    draw_confusion_matrix(ax, matrix, f"{display_model_name}\nsubject_kfold (row-normalized)")
    fig.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def generate_confusion_matrices_panel(
    df: pd.DataFrame,
    signal_set: str,
    model_names: list[str],
    output_path: Path,
    dpi: int,
) -> None:
    fig, axes = plt.subplots(1, len(model_names), figsize=(9.6, 3.8))
    if len(model_names) == 1:
        axes = np.asarray([axes])

    for ax, model_name in zip(axes, model_names):
        matrix = confusion_matrix_values(df, signal_set, model_name)
        display_model_name = CONFUSION_MODEL_LABELS.get(model_name, model_name)
        draw_confusion_matrix(ax, matrix, f"{display_model_name}\nsubject_kfold (row-normalized)")

    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def load_label_distribution(tables_dir: Path) -> pd.DataFrame:
    path = tables_dir / "label_distribution_aggregate.csv"
    df = pd.read_csv(path)
    expected_columns = {"signal_set", "class_name", "count", "proportion"}
    missing = expected_columns.difference(df.columns)
    if missing:
        raise ValueError(f"V {path} manjkajo stolpci: {sorted(missing)}")
    return df[df["signal_set"].isin(SIGNAL_ORDER)].copy()


def generate_label_distribution_plots(df: pd.DataFrame, data_figures_dir: Path, dpi: int) -> None:
    df["display_signal"] = df["signal_set"].map(SIGNAL_LABELS)
    df["display_class"] = df["class_name"].map(CLASS_LABELS)

    signals = [SIGNAL_LABELS[key] for key in SIGNAL_ORDER]
    classes = [CLASS_LABELS["Low valence"], CLASS_LABELS["High valence"]]
    colors = ["#8ECAE6", "#B8A1D9"]

    proportions = (
        df.pivot(index="display_signal", columns="display_class", values="proportion")
        .loc[signals, classes]
        .to_numpy()
        * 100.0
    )
    counts = df.pivot(index="display_signal", columns="display_class", values="count").loc[signals, classes].to_numpy()

    for values, ylabel, output_name, annotate_as_percent in [
        (proportions, "delež oken [%]", "porazdelitev_razredov_delezi_retain_2026-06-12.png", True),
        (counts, "število oken", "porazdelitev_razredov_stevila_retain_2026-06-12.png", False),
    ]:
        fig, ax = plt.subplots(figsize=(6.2, 3.6), constrained_layout=True)
        x = np.arange(len(signals))
        bottom = np.zeros(len(signals))
        for class_index, class_label in enumerate(classes):
            ax.bar(x, values[:, class_index], bottom=bottom, color=colors[class_index], label=class_label, width=0.68)
            for signal_index, value in enumerate(values[:, class_index]):
                if annotate_as_percent:
                    text = f"{format_decimal(value)} %"
                else:
                    text = f"{int(value)}"
                ax.text(
                    signal_index,
                    bottom[signal_index] + value / 2,
                    text,
                    ha="center",
                    va="center",
                    fontsize=8,
                    color="#2F3437",
                )
            bottom += values[:, class_index]

        ax.set_xticks(x)
        ax.set_xticklabels(signals, fontsize=8.5)
        ax.set_ylabel(ylabel, fontsize=9)
        ax.legend(frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(0.5, 1.12), fontsize=8.5)
        ax.grid(axis="y", color="#E6E6E6", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#B0B0B0")
        ax.spines["bottom"].set_color("#B0B0B0")
        if annotate_as_percent:
            ax.set_ylim(0, 100)

        output_path = data_figures_dir / output_name
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
        plt.close(fig)


def main() -> None:
    args = parse_args()
    print(f"tables_dir={args.tables_dir}")
    print(f"results_figures_dir={args.results_figures_dir}")
    print(f"data_figures_dir={args.data_figures_dir}")
    print(f"dpi={args.dpi}")

    main_metrics = load_main_metrics(args.tables_dir)
    generate_main_comparison_heatmap(
        main_metrics,
        args.results_figures_dir / "glavna_primerjava_modelov_heatmap.png",
        args.dpi,
    )

    confusion_matrices = load_confusion_matrices(args.tables_dir)
    generate_confusion_matrix(
        confusion_matrices,
        signal_set="gaze_pupil",
        model_name="SVM",
        output_path=args.results_figures_dir / "matrika_zmede_pogled_zenici_svm.png",
        dpi=args.dpi,
    )
    generate_confusion_matrix(
        confusion_matrices,
        signal_set="gaze_pupil",
        model_name="HeteroGCNMLPWeights",
        output_path=args.results_figures_dir / "matrika_zmede_pogled_zenici_koncni_gnn.png",
        dpi=args.dpi,
    )
    generate_confusion_matrices_panel(
        confusion_matrices,
        signal_set="gaze_pupil",
        model_names=["SVM", "HeteroGCNMLPWeights"],
        output_path=args.results_figures_dir / "matrike_zmede_pogled_zenici_svm_heterogcn_mlp_w.png",
        dpi=args.dpi,
    )

    label_distribution = load_label_distribution(args.tables_dir)
    generate_label_distribution_plots(label_distribution, args.data_figures_dir, args.dpi)


if __name__ == "__main__":
    main()
