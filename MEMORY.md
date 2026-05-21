# MEMORY.md — diploma-latex

Kratek delovni spomin za pisanje diplome. Uporabljaj ga ločeno od spomina v
`GFM-for-eyetracker`; sem spadajo samo informacije, ki pomagajo pri pisanju,
urejanju, strukturi, slogu in virih diplomske naloge.

## Stalne preference

- Besedilo diplome naj bo v slovenščini, jasno, tehnično in zgoščeno.
- Uporabljaj `/humanize`: piši naravno in človeško, brez generičnih AI fraz.
- Sproti se uči Tomijevega sloga iz obstoječih poglavij in ga uporabljaj pri novih
  odstavkih.
- Konkretnim podrobnostim o modelu, podatkih, rezultatih in konfiguracijah ne
  zaupaj iz spomina; preveri jih v `GFM-for-eyetracker`.
- Pri zapisu števil v slovenskem besedilu uporabljaj decimalno vejico in piko za
  ločevanje tisočic: npr. `1,2`, `1.200`, `1.123.456,789`. V LaTeX matematičnem
  načinu decimalno vejico piši kot `{,}`, npr. `$45{,}7\,\%$`.
- Za angleški izraz `signed value` ne uporabljaj izraza "podpisana vrednost",
  temveč "predznačena vrednost".
- Kratico SOTA v diplomi uporabljaj kot SOTA. Samo ob prvi pojavitvi jo definiraj
  z besedilom "predstavnik najsodobnejših modelov (angl. \emph{state of the
  art}, SOTA) za podatke sledilnika pogleda". Ne prevajaj je kot "stanje
  tehnike".
- Pri novih angleških strokovnih izrazih ne prevajaj na pamet. Najprej preveri
  slovensko rabo v zanesljivih virih, po možnosti v tem vrstnem redu: Univerza v
  Ljubljani/FRI, Institut Jožef Stefan, Univerza v Mariboru/FERI, slovenski
  terminološki slovarji in druga strokovna literatura. Predlagaj 2--4 možne
  prevode, na kratko pojasni razliko, označi priporočilo in vprašaj Tomija za
  potrditev. Po potrditvi izraz zapiši v projektni terminološki slovar oziroma
  `MEMORY.md`/`AGENTS.md` in ga nato uporabljaj konsistentno.
- Pri urejanju LaTeX besedila uporabljaj `$...$` za inline matematiko,
  `\begin{equation}...\end{equation}` ali `\[...\]` za prikazane enačbe in nikoli
  `$$...$$`. Tehnične vrednosti z enotami piši v matematičnem načinu z nedeljivim
  presledkom, npr. `$10~s$`, `$500~Hz$`, `$500~ms$`. Spremenljivke, koordinate,
  parametre in matematične oznake vedno piši v matematičnem načinu, navadne
  količine v tekočem besedilu pa praviloma z besedo ali brez matematičnega načina.
- Pri sklicih uporabljaj nedeljivi presledek: `Slika~1`, `Tabela~2`,
  `Poglavje~3`, `enačba~(4)`. Za vire uporabljaj `\cite{...}`, ne `\ref{...}`;
  `\ref{...}` uporabljaj samo za označene slike, tabele, enačbe, poglavja ali
  algoritme. Nikoli ne pusti praznega `\ref{}` ali `\cite{}`.

## Referenčni kontekst

- PDF-ji v `codex-kontekst` so dobri zgledi kakovostnih FRI diplomskih in
  magistrskih nalog.
- Pri terminologiji za GNN, grafe, vložitve, strojno učenje in AI najprej preveri
  te naloge, nato širše vire.
- Stropnik je trenutno najpomembnejši zgled za grafovsko metodologijo in GNN
  terminologijo.
- Kocijan je uporaben za terminologijo grafovskih vložitev; v tej diplomi naj bo
  privzeti izraz za `embedding` še vedno `predstavitev`, razen kjer je `vložitev`
  natančnejša.
- Špendl in Zupančič Muc sta uporabna zgleda za raziskovalno strukturo,
  eksplicitne prispevke, eksperimentalni protokol in previdno interpretacijo.
- `hci-tagging dataset paper.pdf` je vsebinski vir za podatkovni kontekst, ne
  slogovni zgled FRI diplome.

## Odprte opombe

- Odločitev za osnovne modele v eksperimentih: ne uporabljamo surove konkatenacije
  signalov in ne PCA različice kot glavne primerjave. Negrafovski modeli
  (`LightGBM`, `SVM`, `MLP`) naj dobijo razširjene agregirane statistike istih
  signalov kot GNN, vključno z informacijo o oddaljenosti od zaslona in
  fiksacijah/trajanju fiksacij.
- Pri naslednjem delu na poglavjih preveri, ali se trenutna struktura v
  `AGENTS.md` ujema z dejansko strukturo `diploma.tex` in poglavij.
