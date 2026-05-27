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
  algoritme.
- Tomi želi, da so prazni `\ref{}` in prazni `\cite{}` dovoljeni kot vidni
  placeholderji. Prazni `\ref{}` označuje kasnejši notranji sklic, prazni
  `\cite{}` pa mesto, kjer želimo vir, vendar ga še nimamo izbranega. Če imaš
  dober vir ali ga lahko razumno pridobiš, ga dodaj v `literatura.bib` in ga
  takoj uporabi.
- Pri naštevanju relacij oziroma tipov povezav vedno uporabi vrstni red:
  časovne (`temporal`), prostorske (`spatial`), fiksacijske (`fixation`). Vrstni
  red prilagodi kontekstu, npr. časovne naprej/nazaj pred prostorskimi in
  fiksacijskimi.
- Za model, ki je prispevek naloge, privzeto uporabljaj izraz "predlagani model".
  Kadar je treba poudariti grafovski tip modela, uporabi "predlagani GNN"; kadar
  opisuješ notranjo zgradbo, uporabi "predlagana arhitektura". Izraz "končni
  model" uporabi samo, ko ga je treba ločiti od osnovnega GNN, ablacijske
  različice ali vmesnih poskusov. Izrazom "naš model" in "naš GNN" se v končnem
  besedilu izogibaj.
- Za `latent space` uporabljaj "latentni prostor". Kadar je slogovno bolj
  nevtralno ali konkretno, je dopusten tudi izraz "prostor predstavitev".
- Za `batch` in `mini-batch` uporabljaj "mini-serija", ne "paket".
- Za `overfitting` uporabljaj "prekomerno prileganje", ne "preprileganje".
- Za `arousal` dosledno uporabljaj "vzburjenost", ne "vzburjenje". Samo pri prvi
  omembi v diplomi dodaj angleški izraz v oklepaju: `vzburjenost (ang. arousal)`.

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
- Izvirni MAHNOB-HCI članek pri baseline prepoznavi čustev uporablja
  participant-independent evalvacijo z leave-one-participant-out CV. V vsakem
  koraku so vsi vzorci enega udeleženca testni, SVM z RBF jedrom se uči na
  ostalih udeležencih, parameter $\gamma$ izberejo na učni množici z 20-fold CV
  po povprečnem F1, $C=1$, izbor značilk pa naredijo z enosmerno ANOVA samo na
  učni množici. Poročani `Average F1` je povprečje F1 po razredih, tj. makro
  povprečje v sodobni terminologiji; članek ga ne označi kot uteženega.

## Odprte opombe

- Glavni eksperiment diplome je 3-razredna klasifikacija valence in vzburjenosti
  po protokolu MAHNOB-HCI, ker omogoča primerjavo z izvirno formulacijo naloge.
  Binarni low/high poskusi za valenco in vzburjenost so dodatni eksperimenti, ki
  jih prav tako poročamo v glavnem besedilu, predvsem kot čistejšo in lažjo
  formulacijo brez srednjega/nevtralnega razreda.
- Stare interne različice grafovskega modela ostanejo dovoljene samo kot
  raziskovalna referenca v eksperimentalnem repozitoriju. V diplomi jih ne
  poročamo in jih ne omenjamo. Za diplomsko primerjavo je treba uporabiti
  Osnovni GCN, usklajen z opisom grafovskega osnovnega modela v poglavju 6.
- Končni rezultati v diplomi naj uporabljajo `subject LOO` kot glavni protokol in
  `recording LOO` kot dodatni poročani protokol. `kfold` ne uporabljamo za glavne
  rezultate, ga pa omenimo pri ablacijski študiji: zaradi časovne ekonomičnosti
  bodo ablacijski poskusi izvedeni s subject kfold protokolom, trenutno z
  `k=5`, ob pojasnilu, da so rezultati dovolj primerljivi z LOO za analizo vpliva
  komponent.
- Ablacijska študija naj poleg časovne, prostorske/gaze, zenice in razdalje do
  zaslona vključuje tudi odstranitev fiksacijske informacije.
- Diplomsko ime za homogeni grafovski baseline je `Osnovni GCN`. V glavnih
  tabelah rezultatov naj bosta samo `accuracy` in `macro-F1`; podrobnejše metrike
  sodijo v dodatek.
- Odločitev za osnovne modele v eksperimentih: ne uporabljamo surove konkatenacije
  signalov in ne PCA različice kot glavne primerjave. Negrafovski modeli
  (`LightGBM`, `SVM`, `MLP`) naj dobijo razširjene agregirane statistike istih
  signalov kot GNN, vključno z informacijo o oddaljenosti od zaslona in
  fiksacijah/trajanju fiksacij.
- Odločitev za grafovske primerjave v poglavju 6: osnovni grafovski model naj bo
  arhitekturni baseline, ki uporablja iste signale kot predlagani GNN, vendar
  poenostavi arhitekturo. Načrtovana implementacija je majhen ločen modelni
  razred s homogenim `GCNConv`, enotno potjo posredovanja sporočil, brez naučenih
  skalarnih uteži povezav in zaenkrat brez različice `GATConv`. Ablacijska
  študija naj bo ločena: tam arhitektura ostane finalna, odstranjuje pa se en
  informacijski vir naenkrat. Ko odstranimo signal, odstranimo vse informacije,
  ki iz njega izhajajo: značilke vozlišč, značilke povezav in povezave, zgrajene
  na podlagi tega signala. Načrtovane skupine ablacijski poskusov so časovna
  informacija, položaj pogleda/prostorska informacija, velikost zenic in
  oddaljenost od zaslona.
- Pri diagnostiki učenja naj glavno besedilo poroča samo ključne diagnostične
  grafe in ugotovitve. Podrobnejše diagnostične tabele, dodatne slike kolapsa
  predstavitev in relacijske porazdelitve uteži povezav sodijo v dodatek
  `D_diagnostika_predstavitev.tex`.
- Uredniški plan vizualizacij: glavno besedilo naj ima omejeno število močnih
  slik, približno eno sliko porazdelitve podatkov, eno osrednjo sliko grafovske
  predstavitve, eno do dve sliki glavnih rezultatov, eno sliko napak oziroma
  matrik zmede, eno ablacijsko sliko in po potrebi eno diagnostično sliko.
  Podrobne porazdelitve, dodatne metrike, per-fold grafe, dodatne matrike zmede,
  ločene relacijske vizualizacije grafov in sekundarne diagnostike sodijo v
  dodatke. UMAP je kandidatna kvalitativna slika: v glavno besedilo gre samo, če
  je berljiva, stabilna in interpretativno koristna; sicer gre v dodatek ali se
  izpusti.
- Pri naslednjem delu na poglavjih preveri, ali se trenutna struktura v
  `AGENTS.md` ujema z dejansko strukturo `diploma.tex` in poglavij.
