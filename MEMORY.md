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
- Za parametre in mehanizme, ki se med učenjem optimizirajo, uporabljaj
  `učljiv` (npr. `učljive uteži` oziroma `učljiva fuzija`); za njihove konkretne
  vrednosti po učenju pa `naučen` (npr. `naučene uteži`).
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
- Za velikosti leve in desne zenice uporabljaj notacijo `$p_i^{(l)}$` in
  `$p_i^{(r)}$`, ne `$p_{l,i}$`, `$p_{r,i}$` ali `$p^l_i$`. Indeks `$i$`
  označuje meritev oziroma vozlišče, nadpis v oklepaju pa levo/desno oko.
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
- Podatke, ki jih udeleženci podajo po ogledu posnetka, dosledno poimenuj
  `samoocene čustvenega stanja`, ne `čustvene oznake`. Kadar gre za operativni
  izhod klasifikacije po preslikavi teh samoocen, uporabi `ciljni razred` oziroma
  `razred valence`.
- Razreda valence dosledno poimenuj `negativna valenca` in `pozitivna valenca`,
  ne `neprijetna valenca` in `prijetna valenca`. Enaki kratki oznaki `negativna`
  in `pozitivna` naj bosta uporabljeni tudi na slikah in v matrikah zamenjav.
- Za `confusion matrix` dosledno uporabljaj "matrika zamenjav" oziroma v množini
  "matrike zamenjav", ne "matrika zmede" ali "matrike zmede".
- Za primerjave razpoložljivih signalov sledilnika pogleda uporabljaj izraz
  `množica signalov` oziroma `podmnožica signalov`, ne `nabor signalov`. Imena
  glavnih množic so zaenkrat: `samo pogled`, `samo zenici`, `pogled in zenici` in
  `vsi signali`.
- Potrjeni slovenski izrazi za pogoste angleške oznake v diplomi: `eye` v
  matematičnih oznakah prevajaj kot `oči`, `screen` kot `zaslon`,
  `eye-tracking` glede na kontekst kot `sledilnik pogleda`, `podatki sledilnika
  pogleda`, `signali sledilnika pogleda` ali `okna meritev sledilnika pogleda`,
  `gaze` kot `pogled`, `gaze-only` kot `samo pogled`, `pupil-only` kot `samo
  zenici`, `gaze+pupil` kot `pogled in zenici`, `all` kot `vsi signali`,
  `baseline` kot `primerjalni model` oziroma `izhodiščni model`,
  `leave-one-subject-out` kot `LOSO`, `k-fold` kot
  `k-kratno prečno preverjanje`, `plot` kot `graf` ali `prikaz`, `pipeline` kot
  `cevovod`, `edge feature` kot `značilka povezave`, `forward/backward temporal
  separation` kot `ločevanje časovnih povezav naprej in nazaj`, `learnable signed
  edge weights` kot `učljive predznačene uteži povezav`, `self-supervised
  representation learning` kot `samonadzorovano učenje predstavitev` in
  `foundation model` kot `temeljni model`. Izrazu `heatmap` se po možnosti
  izogibaj; kadar je res potreben, uporabi `toplotna karta`.
- Pri proofreadingu ne vračaj Tomijevih ročnih slogovnih popravkov nazaj na
  prejšnje predloge. Če Tomi popravi vezaje, veznike (`in`/`ter`), formulacije
  ali poenostavi zapis, to obravnavaj kot aktualen slogovni signal in ga ohrani,
  razen če gre za očitno LaTeX ali factualno napako.
- Za pretvorbo vhodnih signalov z izračunom povprečja in standardnega odklona na
  učni množici uporabljaj izraz `standardizacija`, ne `normalizacija`.
  `Normalizacija` ostane za druge postopke, kot so softmax, normalizacija uteži,
  normalizacija plasti, relativni čas v intervalu okna in matrike zamenjav.
- `Predobdelava` označuje celoten postopek priprave podatkov pred učenjem modelov,
  vključno z izbiro signalov, čiščenjem, standardizacijo in tvorbo časovnih oken.
  `Čiščenje` je njen ožji del: izbor uporabnih zapisov ter obravnava neveljavnih,
  manjkajočih in osamelih meritev.
- Ko Tomi ročno popravi besedilo za predlogom, iz popravka sklepaj o slogovni
  preferenci in jo uporabljaj v nadaljevanju. Če je vzorec dvoumen ali odvisen od
  konteksta, ga ne posplošuj na slepo, ampak Tomija eksplicitno vprašaj. Konkretna
  potrjena preferenca: razpone tipa `1-2` piši z enim vezajem, ne kot `1--2`,
  razen če Tomi za določen kontekst naroči drugače.
- Tomijevih ročnih popravkov po svojem prejšnjem predlogu ne spreminjaj nazaj,
  razen če gre za očitno LaTeX napako ali factualno napako, ki jo lahko
  nedvoumno preveriš. Če se zdi popravek vsebinsko dvoumen, najprej vprašaj.
- Pri pisanju in pregledovanju poglavij ne ponavljaj istih idej, definicij in
  razlag iz prejšnjih poglavij. Kadar je dodatna razlaga že podana drugje, uporabi
  kratek sklic na ustrezno poglavje, razdelek, tabelo ali sliko, novo besedilo pa
  osredotoči samo na kontekst, ki je potreben na trenutnem mestu.
- Pri strukturnem urejanju naj bodo posegi minimalistični: ne uvajaj novih sekcij,
  kadar je mogoče vsebino smiselno vključiti v obstoječe odstavke. Prednost ima
  ohranitev Tomijevega obstoječega besedila z le potrebnimi spremembami.
- Pri pisanju LaTeX poglavij naj bo praviloma ena poved v eni vrstici. Ne lomi
  ene povedi čez več vrstic samo zaradi širine urejevalnika. Ročno vrstično
  oblikovanje naj sledi stavkom oziroma logičnim enotam, ker Tomi tako lažje
  pregleduje in ureja besedilo.
- Oznak za postavitev okolij `figure` in `table` (npr. `[htbp]`, `[!htbp]`,
  `[H]`, `[t]` ali privzeta postavitev brez oglatih oklepajev) ne spreminjaj.
  
- Konkretna imena modelov v besedilu, tabelah in naslovih razdelkov piši z
  makrom `\ModelName{...}`. To velja za dejanske modelne oznake, kot so
  `\ModelName{SVM}`, `\ModelName{LightGBM}`, `\ModelName{GCN}` in
  `\ModelName{HeteroGCN-MLP-w}`, ne pa za opisna poimenovanja, kot so
  `končni model`, `osnovni grafovski model` ali `predlagani GNN`.

## Vizualna identiteta diplome

- V diplomski nalogi nikoli ne uporabljaj LLM-generiranih ali drugih
  generativno ustvarjenih slik za rezultate, diagrame, grafe ali podatkovne
  prikaze. Vse rezultate vedno plottaj reproducibilno s Python orodji
  (Matplotlib/seaborn oziroma obstoječa projektna orodja), TikZ, SVG ali drugim
  sledljivim programskim postopkom iz konkretnih podatkov. Ob slikah rezultatov
  v LaTeX komentarju zapiši izvorne podatke in skript, ki sliko generira.
- Slike rezultatov naj slogovno sledijo slikam, ki jih generira glavni
  eksperimentalni runner oziroma njegov postprocesirni skript. Posebej za
  toplotne karte in matrike zamenjav uporabljaj isti `seaborn.heatmap` slog,
  barvno shemo `Blues`, bele mrežne črte oziroma runnerjeve nastavitve, format
  deležev med $0$ in $1$ ter vrstično normalizacijo matrik zamenjav. Izjema sta
  trenutni sliki porazdelitve razredov za poglavji 4 in 8, ki sta Tomiju všeč in
  ostaneta v posebej pripravljenem diploma slogu.
- Za vse diagrame, TikZ slike, SVG slike, grafe, sheme cevovodov in druge
  vizualne elemente diplomske naloge uporabljaj konsistentno barvno paleto B:
  `#2F3437` temna siva za tekst/robove, `#8ECAE6` pastelna modra, `#A8DADC`
  pastelna teal, `#B8A1D9` pastelna vijolična, `#F4A261` pastelna oranžna,
  `#E9A6A6` pastelna rožnata in `#F7F7F2` svetlo ozadje.
- Slog vizualnih elementov naj bo akademski, čist, tehničen in primeren za
  diplomsko nalogo oziroma znanstveni članek: dovolj praznega prostora, tanki
  robovi, berljiva tipografija, brez dekorativnih gradientov in brez risankastih
  ikon.
- Barve uporabljaj semantično konsistentno. Isti koncept naj ima skozi celotno
  diplomo vedno isto barvo.
- Če obstoječa slika, TikZ koda, SVG ali graf uporablja barve izven te palete brez
  jasnega razloga, opozori uporabnika in predlagaj popravek na paleto B.
- LaTeX definicije barv:
  `\definecolor{thesisDark}{HTML}{2F3437}`,
  `\definecolor{thesisBlue}{HTML}{8ECAE6}`,
  `\definecolor{thesisTeal}{HTML}{A8DADC}`,
  `\definecolor{thesisPurple}{HTML}{B8A1D9}`,
  `\definecolor{thesisOrange}{HTML}{F4A261}`,
  `\definecolor{thesisPink}{HTML}{E9A6A6}`,
  `\definecolor{thesisBackground}{HTML}{F7F7F2}`.

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

- 2026-07-22 V poglavju 5 naj opis razširjenih povezav znotraj fiksacije ostane
  konceptualen; formalna definicija z enačbami je v dodatku C. Shematska slika
  konstrukcije ostane v glavnem besedilu.
- 2026-07-22 Tabela glavnega besedila za množice signalov združuje značilke
  vozlišč, relacije in značilke povezav v simbolnem zapisu. Podrobna tabela
  značilk povezav je v dodatku C in se uporablja tudi kot sklic pri opisu
  modela \ModelName{HeteroGCN-MLP-w}.
- 2026-07-22 V tabelah grafov uporabljaj semantično barvno kodiranje: časovne
  komponente oranžno, pogled in prostorske komponente modro, zenične komponente
  teal ter dodatne signale in fiksacije vijolično. Barva naj bo uporabljena za
  besedilo oziroma simbole (brez barvne podlage) in naj ne bo edini nosilec
  pomena.
- 2026-07-22 Pri opisu štirih množic signalov poudari primerjavo robustnosti
  modelov glede na razpoložljivost vhodnih signalov in klasifikacijske uspešnosti
  po njihovih tipih. Ne utemeljuj je s pokrivanjem različnih podatkovnih zbirk.
- 2026-07-22 Toplotni prikaz porazdelitve položajev pogleda na Sliki~4.2 uporablja
  divergirajočo lestvico `RdBu_r`: modra pomeni majhno, rdeča pa veliko število
  meritev. Ta izjema od privzete lestvice `Blues` je namenjena semantično jasnemu
  prikazu gostote.
- 2026-07-22 Za validacijski protokol, pri katerem je testni subjekt v posamezni ponovitvi izpuščen, uporabljaj izključno kratico `LOSO` (angl. `leave-one-subject-out`). Izraza `LOO po subjektih` in `LOO po posnetkih` v diplomi ne uporabljaj in ne omenjaj.
- 2026-07-22 Mentor želi, da je pri vsakem od štirih GNN v poglavju 6 podana glavna enačba. Enačbe naj neposredno pokažejo razlikovalni korak posamezne stopnje: homogeno konvolucijo, relacijsko povprečenje, učljivo MLP-fuzijo in uteženo relacijsko posredovanje sporočil.
- 2026-07-21 V poglavju 4 so bile vsebine nekdanjih sekcij `Priprava vhodnih signalov`, `Normalizacija`, `Segmentacija v časovna okna` in `Povzetek predobdelave` združene v sekcijo `Priprava podatkov za učenje` z dvema podsekcijama: `Množice signalov in čiščenje podatkov` ter `Standardizacija in tvorba časovnih oken`. Povzetna tabela predobdelave je na koncu druge podsekcije brez samostojnega naslova.
- 2026-07-21 Sekciji o podatkih sledilnika pogleda in MAHNOB-HCI sta iz poglavja 3, osnovni opis podatkov sledilnika pogleda pa iz poglavja 2, združeni v sekcijo `Podatkovne zbirke sledilnika pogleda` v poglavju 4. V poglavji 2 in 3 ju ne vračaj; poglavje 4 naj ostane edino mesto za opis signalov, splošni pregled zbirk, kratek opis eSEEd in podrobnejši opis MAHNOB-HCI.
- 2026-07-08 Za razdelek o fiksacijskih povezavah v poglavju 5 je dodana slika
  `slike/konstrukcija_grafa/razsirjene_fiksacijske_povezave_F21_kf3_L2_v0.pdf`,
  generirana s skriptom
  `GFM-for-eyetracker/scripts/create_thesis_fixation_dilated_edges_figure.py`.
  Uporablja $F=21$ kot zaokroženo povprečno velikost fiksacijske skupine iz
  analize fiksacijskih povezav, $k_f=3$, $L=2$ in izbrano vozlišče $v=0$.
- 2026-06-22 Tomi je zaklenil strukturo končnega eksperimentalnega protokola za
  poglavje 7: glavna naloga je binarna klasifikacija valence, 3-razredne naloge
  in vzburjenost se ne poročajo kot glavni eksperimenti, temveč se po potrebi
  pojavijo v dodatku oziroma pri razlagi izbire hiperparametrov. Glavni
  validacijski protokol je 7-kratno prečno preverjanje po subjektih. LOO po
  subjektih omenimo kot predhodno preverjanje na množici `vsi signali`; v dodatku
  naj bo primerjalna tabela za valenco med subject 7-fold in subject LOO.
  Ločene ablacijske študije v diplomi ni več. Primerjava po signalnih množicah
  je del glavne primerjave, vse štiri signalne množice (`samo pogled`, `samo
  zenici`, `pogled in zenici`, `vsi signali`) so enakovredne. Zamrznjene
  predstavitvene modele v protokolarni tabeli združi v eno vrstico
  `GazeMAE/MOMENT`.
- 2026-06-22 Pri MAHNOB-HCI ciljnih oznakah `target_aggregation` nima resne
  vsebinske vloge, ker so ciljni razredi znotraj posameznega 10-sekundnega okna
  konstantni. Razliko med `mean` in `constant` zato ne obravnavaj kot pomembno
  metodološko razliko za končne rezultate.
- 2026-06-15 Tomi je zaklenil novo glavno zgodbo diplome: fokus ostane na GNN
  za podatke sledilnika pogleda, ne na razvoju najboljšega možnega modela za
  prepoznavo čustev. Glavno vprašanje naj bo v smeri, kako dobro GNN kodirajo
  podatke sledilnika pogleda za klasifikacijo čustvenih oznak. Podatki
  sledilnika pogleda so osrednji vhodni signal in jih je treba opisati dovolj za
  razumevanje grafovske konstrukcije; čustva so predvsem oznake, zato se naloga
  ne sme poglobiti v psihologijo čustev. Glavni eksperimenti so štiri množice
  signalov: `samo pogled`, `samo zenici`, `pogled in zenici` in `vsi signali`.
  Delitev je motivirana
  s tipično dostopnostjo signalov pri sledilnikih pogleda: pogosto imamo samo
  pogled, samo zenici ali oboje, redkeje pa dodatne signale, ki so prisotni v
  tej podatkovni zbirki. Glavna naloga je samo binarna low/high klasifikacija
  valence; 3-razredne rezultate izključi iz glavnega besedila, razen kot opombo
  pri definiciji razredov in pri utemeljitvi izbire hiperparametrov, kjer povej,
  da je bil grid search izveden v preliminarnih 3-razrednih poskusih. Pri
  definiciji razredov naj se najprej pojasni izvorna 3-razredna preslikava in
  nato zapiše, da je naloga poenostavljena z izključitvijo razreda 1. Izogibaj
  se izrazu `predlagani model`; za zadnjo stopnjo arhitekturne lestvice lahko
  uporabiš `končni model`, vendar samo v pomenu končne stopnje, ne najboljšega
  ali predlaganega modela. Ločene ablacijske študije v glavni zasnovi ne
  potrebujemo več.
- Glavno raziskovalno vprašanje diplome je: `Kako učinkovita je grafovska
  predstavitev podatkov sledilnika pogleda pri klasifikaciji čustvenih oznak v
  primerjavi z uveljavljenimi negrafovskimi pristopi?`
- Izbrani delovni naslov diplome je `Grafovske nevronske mreže za klasifikacijo
  čustvenih oznak iz podatkov sledilnika pogleda`. Angleški delovni naslov:
  `Graph Neural Networks for Classification of Emotional Labels from Eye-Tracking
  Data`.
- V poglavju 4 je treba utemeljiti, da vzburjenost ni več glavna ciljna naloga,
  ker se oznake vzburjenosti slabše ujemajo s samoocenami in so zato za to
  diplomsko evalvacijo šumnejše. Kot dokaz uporabiti oziroma v dodatek povezati
  artefakte iz `GFM-for-eyetracker/docs/figures/hci-tagging/mentors meeting
  2026-05-13/label_noise_analysis/2026-05-13_table6_self_report_alignment`.
- `vsi signali` pomeni koordinate pogleda, velikosti zenic, oddaljenost od
  sledilnika pogleda in fiksacijsko informacijo. Za `distance to ET` privzeto
  uporabljaj opisni izraz `oddaljenost od sledilnika pogleda`, dokler Tomi ne
  potrdi drugačne terminologije.
- Za signalno množico s podatki obeh zenic uporabljaj izraz `zenici` in pri tem
  dosledno upoštevaj slovensko dvojino. Signalne množice so: `samo pogled`,
  `samo zenici`, `pogled in zenici` in `vsi signali`.
- 2026-06-21 Tomi je izrecno zaklenil, da je `samo zenici` enakovreden glavni
  eksperiment ostalim trem signalnim množicam. V glavnih rezultatih obravnavaj
  vse štiri signalne množice: `samo pogled`, `samo zenici`, `pogled in zenici`
  in `vsi signali`.
- 2026-06-21 Pri glavnih rezultatih je glavna metrika `accuracy` oziroma
  `točnost`. V glavni toplotni karti model × množica signalov naj barva celic
  sledi točnosti; makro F1 ostane druga številka v celicah in spremljevalna
  metrika.
- V uvodu naj se zgodba začne pri GNN oziroma grafovskem modeliranju, nato naj se
  poveže s podatki sledilnika pogleda, šele nato naj se omeni čustvene oznake kot
  evalvacijsko nalogo. Glavno raziskovalno vprašanje naj bo v uvodu motivirano,
  dobesedno pa naj se pojavi v razdelku `Raziskovalna vprašanja`.
- V uvodu še ne naštevaj imen posameznih GNN modelov. Uporabi samo splošni izraz
  `arhitekturna lestvica grafovskih modelov`; tehnična imena sodijo v poglavje 6.
- V splošni diskusiji je dovoljeno uporabiti `končni model` za zadnjo stopnjo
  arhitekturne lestvice, kadar je jasno, da pomeni končno stopnjo in ne najboljši
  model. Pri tehničnih primerjavah uporabljaj konkretna imena modelov:
  `GCN`, `HeteroGCN-mean`, `HeteroGCN-MLP` in `HeteroGCN-MLP-w`.
- Kadar tabela, slika ali stavek našteva več GNN modelov skupaj, za zadnjo
  različico vedno uporabi tehnično ime `HeteroGCN-MLP-w`, ne `končni GNN`.
  Izraz `končni GNN` uporabi samo v tekočem besedilu, ko omenjaš samo ta model
  oziroma ga ne postavljaš neposredno ob ostale GNN različice.
- GazeMAE/MOMENT v diplomi obravnavaj previdno kot `zamrznjene prednaučene
  predstavitvene modele`, ne kot polno primerjavo z vsemi temeljnimi modeli ali
  kot reprodukcijo njihovega predtreniranja.
- V tabeli računske zahtevnosti naj ima vrstica `GazeMAE/MOMENT` v stolpcu
  `Vhod` vrednost `signal`, ker kodirnika kot vhod prejmeta signal, čeprav
  klasifikacijska glava nato uporablja njune predstavitve.
- V naslovu, povzetku in motivacijskem kontekstu lahko ostane izraz `prepoznava
  čustev`, v glavnem tehničnem besedilu pa raje uporabljaj `klasifikacija
  čustvenih oznak`, ker modeli napovedujejo eksperimentalno izpeljane oznake.
- 2026-06-09 je Tomi poslal Lovru, v CC tudi Gašperju, mentorski update o
  stanju diplome. V mailu je povedal, da je diploma v grobem napisana do
  rezultatov, da so po pravičnejšem eksperimentalnem protokolu tabularni modeli
  bistveno boljši, predlagani GNN pa je med slabšimi po opazovanih metrikah.
  Predlagana nova zgodba diplome je primerjalna in ablacijska študija: ne
  dokazovati na silo, da je GNN najboljši, temveč analizirati, kateri signali,
  grafovska predstavitev in arhitekturne komponente pomagajo ali škodijo. GNN
  ostane metodološki fokus diplome, sklep pa mora biti pošten: trenutni GNN ni
  premagal močnejših tabularnih modelov, vendar naloga pokaže smiselno grafovsko
  predstavitev podatkov sledilnika pogleda, njene omejitve in smeri za nadaljnje
  delo. Če Lovro ne odgovori z vsebinsko močno spremembo, to ostane delovni plan
  za rezultate, diskusijo in zaključek.
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
- 2026-06-17 zaklenjena odločitev o grafovskem operatorju: v glavnih poskusih
  ostane `GCNConv`. Dodatni poskus na množici `pogled in zenici` je pokazal, da bi pri
  izključno najboljšem rezultatu za neuteženi model izbrali `GINConv`, za
  uteženo arhitekturo pa `GraphConv`, vendar bi to po nepotrebnem zakompliciralo
  eksperimentalno zasnovo. V glavnem besedilu povej kratko: preizkusili smo štiri
  različice, razlike niso bile velike, `GCNConv` je bil konsistenten sredinski
  kompromis, zato smo ga ohranili. Podrobno utemeljitev in tabelo rezultatov
  poročaj v dodatku.
- Odločitev za osnovne modele v eksperimentih: ne uporabljamo surove konkatenacije
  signalov in ne PCA različice kot glavne primerjave. Negrafovski modeli
  (`LightGBM`, `SVM`, `MLP`) naj dobijo razširjene agregirane statistike istih
  signalov kot GNN, vključno z informacijo o oddaljenosti od zaslona in
  fiksacijah/trajanju fiksacij.
- Odločitev za grafovske primerjave v poglavju 6: osnovni grafovski model naj bo
  arhitekturni baseline, ki uporablja iste signale kot predlagani GNN, vendar
  poenostavi arhitekturo. Načrtovana implementacija je majhen ločen modelni
  razred s homogenim `GCNConv`, enotno potjo posredovanja sporočil, brez učljivih
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
- 2026-06-18 diagnostiko najboljših GNN iz reteniranega runa
  `GFM-for-eyetracker/results/quick_v1_v2_comparison/RETAIN_2026-06-12_16-29-08`
  obravnavamo informativno, ne kot primer prekomernega glajenja. V glavnem
  besedilu naj bo največ ena poved, da se GNN pri glavnih signalnih množicah uči
  razločevalnih predstavitev in ne kaže jasnega kolapsa; tabela z vrednostmi
  sodi v dodatek `D_diagnostika_predstavitev.tex`.
- Uredniški plan vizualizacij: glavno besedilo naj ima omejeno število močnih
  slik, približno eno sliko porazdelitve podatkov, eno osrednjo sliko grafovske
  predstavitve, eno do dve sliki glavnih rezultatov, eno sliko napak oziroma
  matrik zamenjav, eno ablacijsko sliko in po potrebi eno diagnostično sliko.
  Podrobne porazdelitve, dodatne metrike, per-fold grafe, dodatne matrike zamenjav,
  ločene relacijske vizualizacije grafov in sekundarne diagnostike sodijo v
  dodatke. UMAP je kandidatna kvalitativna slika: v glavno besedilo gre samo, če
  je berljiva, stabilna in interpretativno koristna; sicer gre v dodatek ali se
  izpusti.
- Slike za konstrukcijo grafa v `slike/konstrukcija_grafa` naj v naslovu ne
  vsebujejo metapodatkov posnetka. Za osrednji naslov uporabi
  `Majhen primer konstrukcije grafa iz podatkov sledilnika pogleda`, metapodatke
  kandidata pa zapiši v ime datoteke.
- Za vsak izbrani primer konstrukcije grafa naj skripta poleg zgornjega kolaža
  ustvari še podmapo z datotekami `kolaz`, `vse_povezave`,
  `vse_povezave_brez_oznak`, `casovne`, `prostorske` in `fiksacijske` v formatih
  SVG in PNG. Samostojni paneli naj imajo večje pisave in več prostora za
  oznake, da so uporabni kot ločene slike v PDF-ju.
- Pri slikah konstrukcije grafa SVG shranjuj s transparentnim ozadjem, PNG pa
  lahko obdrži svetlo ozadje za pregledovanje. Na teh slikah ne uporabljaj mreže
  osi, ker pri polprosojnih povezavah povzroča vidne artefakte.
- Pri naslednjem delu na poglavjih preveri, ali se trenutna struktura v
  `AGENTS.md` ujema z dejansko strukturo `diploma.tex` in poglavij.
- Za glavno primerjavo velikosti in praktične zahtevnosti modelov poročamo o
  končnih 3-razrednih `subject LOO` eksperimentih za valenco in vzburjenost.
  Primerjani modeli so `LightGBM`, `SVM`, `MLP`, `GazeMAE_MLP`, `Osnovni GCN` in
  `predlagani GNN`. V glavno besedilo naj gre ozek nabor: število učljivih
  parametrov, število vseh parametrov, čas učenja na okno/graf, čas inference na
  okno/graf ter skupni stolpec `accuracy`/`macro-F1`. Za `GazeMAE_MLP` zabeleži
  učljive parametre glave in skupno število parametrov zamrznjenih enkoderjev z
  glavo. Za klasična modela `LightGBM` in `SVM` število nevronskih parametrov ni
  neposredno primerljivo; v glavnem poročilu ga označi kot nerelevantno oziroma
  nedoločeno, modelno specifične mere pa lahko ostanejo v surovem artefaktu.
- Implementacija poročanja v `GFM-for-eyetracker` zdaj ob končnih multiclass
  tekih z `benchmarking.enabled=true` zapiše fold-level benchmark JSON-e,
  agregirane CSV-je in glavni `main_model_complexity_report.csv/.md`.
- Grid search hiperparametrov predlaganega GNN naj v diplomi ostane majhen
  podporni poskus za izbiro konfiguracije. Metodološki opis in utemeljitev izbire
  sodita v poglavje 7 pri glavni primerjavi modelov; v poglavju 8 ga omeni le
  kratko ali ga po potrebi prestavi v dodatek. Izbrana konfiguracija je
  `num_layers=2`, `hidden_channels=64`, `kt=1`, `ks=1`, `kf=3`; predlagani GNN
  ima pri tej nastavitvi 101.143 učljivih parametrov.
- 2026-06-10 je bila v eksperimentalnem repozitoriju zaklenjena čista
  arhitekturna lestvica grafovskih modelov: `BasicGCN`, `HeteroGCNMean`,
  `HeteroGCNMLP` in `HeteroGCNMLPWeights`. Vsi uporabljajo attention readout,
  enako globino/širino in enako grafovsko konstrukcijo; razlika je postopno
  dodajanje heterogenih relacij, MLP združevanja relacij in učljivih
  predznačenih uteži povezav. Deskriptivno ime končnega modela v kodi je
  `HeteroGCNMLPWeights`, ne `ProposedGNN` ali `GNN_v2`.
- Izbira `GCNConv` naj bo v glavnem besedilu utemeljena kratko v poglavju 7,
  podrobnejša primerjava operatorjev pa sodi v dodatek z dodatnimi rezultati.
  Poglavje 10 lahko druge plasti (`GATConv`, `GraphSAGE`, `GIN`, grafovski
  transformerji) omeni samo previdno kot nadaljnje delo.
- 2026-06-21 pri preurejanju poglavja 6 je Tomi potrdil, da je `samo zenici`
  ena od glavnih množic signalov. Negrafovske modele brez grafovske predstavitve
  in brez zamrznjenega prednaučenega kodirnika imenuj `negrafovski osnovni
  modeli`. Znotraj njih loči zelo preprosta izhodiščna klasifikatorja
  (`Naključni`, `Večinski`) od klasičnih modelov strojnega učenja (`SVM`,
  `LightGBM`, `MLP`). Zamrznjene prednaučene predstavitvene modele obravnavaj
  ločeno; v glavnem besedilu jih poimenuj `GazeMAE` oziroma `MOMENT`, brez
  dodatka `+ MLP`, čeprav se za klasifikacijo tehnično uči MLP glava.
