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

- Pri naslednjem delu na poglavjih preveri, ali se trenutna struktura v
  `AGENTS.md` ujema z dejansko strukturo `diploma.tex` in poglavij.
