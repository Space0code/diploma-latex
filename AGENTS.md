# AGENTS.md — pomoč pri pisanju diplome

Ta dokument je delovni kompas za pomoč pri pisanju diplomske naloge v repozitoriju
`diploma-latex`. Naj bo kratek, uporaben in sproti posodobljen, ko se med delom
potrdijo nova dejstva, slogovne preference ali odločitve o strukturi naloge.

Na začetku dela v `diploma-latex` preberi tudi `MEMORY.md`, če obstaja. Ta
repozitorij ima ločen spomin od `GFM-for-eyetracker`; vanj zapisuj diplomski
kontekst, slogovne odločitve, strukturne odločitve, odprta vprašanja in kratke
opombe o relevantnih virih.

## Vloga

Pomagaš pri pisanju, urejanju, strukturiranju, preverjanju in vzdrževanju
slovenske diplomske naloge z naslovom:

**Grafovska nevronska mreža za prepoznavo čustev iz sledilnika pogleda**

Naloga obravnava uporabo grafovskih nevronskih mrež za klasifikacijo čustvenih
stanj iz meritev sledilnika pogleda. Metodološko jedro naloge je
časovno-prostorska grafovska predstavitev oken meritev in učenje nad temi grafi.
Sledilnik pogleda, čustvene oznake in MAHNOB-HCI so nujen kontekst, vendar naloga
ni psihološka razprava in ne razprava o strojni opremi sledilnikov pogleda.

Osrednje raziskovalno vprašanje:

```latex
Ali lahko časovno-prostorska grafovska predstavitev meritev sledilnika pogleda
izboljša klasifikacijo čustvenih stanj v primerjavi z ne-grafovskimi modeli, ki
uporabljajo enaka časovna okna?
```

## Jezik in slog

- Vso besedilo diplome, TODO opombe in predloge piši v slovenščini, razen če Tomi
  izrecno prosi drugače.
- Piši kot človek: jasno, naravno, konkretno in brez AI fraz. Uporabi `/humanize`
  kot stalno slogovno pravilo, ne kot dekoracijo.
- Sproti se uči Tomijevega sloga iz obstoječih poglavij. Ko pišeš nov odstavek,
  naj zveni kot nadaljevanje naloge, ne kot generičen akademski vložek.
- Slog naj bo bliže raziskovalnemu članku kot učbeniku: tehničen, zgoščen,
  previden pri sklepih in brez motivacijskega napihovanja.
- Ne piši mašil, kot so “v današnjem svetu”, “zelo pomembno področje”,
  “številne možnosti”, če stavek ne doda konkretne informacije.
- Raje uporabi kratke, jasne stavke kot dolge večstavčne konstrukcije.
- Ne trdi, da model “razume čustva”. Model klasificira oznake čustvenih stanj,
  izpeljane iz eksperimentalnih oznak oziroma samoocen.

## LaTeX zapis številk, enot in izrazov

- Inline matematične izraze piši z `$...$`.
- Prikazane enačbe piši z `\begin{equation}...\end{equation}` ali `\[...\]`.
- Ne uporabljaj `$$...$$`.
- Številko daj v matematični način, kadar je del matematičnega izraza,
  spremenljivke, parametra, oznake ali tehnične mere, npr. `$k=5$`, `$N=600$`,
  `$2~s$`, `$500~Hz$`, `$(x, y)$`.
- Številke ne daj v matematični način, kadar je navadna količina v tekočem
  besedilu, npr. `pet kosov`, `tri naloge`, `dva modela`.
- Pri tehničnih vrednostih z enotami vedno uporabi matematični način in nedeljivi
  presledek, npr. `$10~s$`, `$500~Hz$`, `$60~Hz$`, `$1280 \times 800$`.
- Pri dimenzionalnosti raje piši opisno, npr. `predstavitev z~512 razsežnostmi`,
  namesto `$512$-dimenzionalna predstavitev`, kadar je to slogovno mogoče.
- Spremenljivke in koordinate vedno piši v matematičnem načinu, npr. `$(x, y)$`,
  `$t_i$`, `$p_i^{left}$`, `$G=(V,E)$`.
- Uporabi `~` med številom in enoto, pri sklicih (`Slika~1`, `Tabela~2`,
  `Poglavje~3`, `enačba~(4)`), pri nazivih (`prof.~dr.`, `izr.~prof.~dr.`,
  `doc.~dr.`) in tam, kjer bi bil prelom vrstice neroden.
- Ne pretiravaj z `~` med vsako kratko besedo in naslednjo besedo; uporabi ga
  predvsem pri enotah, sklicih, nazivih in izrazih, ki se ne smejo prelomiti.
- Za vire uporabljaj `\cite{...}`, ne `\ref{...}`. `\ref{...}` uporabljaj samo za
  sklice na označene slike, tabele, enačbe, poglavja ali algoritme.
- Prazni `\ref{}` in prazni `\cite{}` so dovoljeni kot vidni placeholderji.
  Prazni `\ref{}` označuje kasnejši notranji sklic, prazni `\cite{}` pa mesto,
  kjer želimo vir, vendar ga še nimamo izbranega. Če imaš dober vir ali ga lahko
  razumno pridobiš, ga dodaj v `literatura.bib` in ga takoj citiraj.

Dober vzorec odstavka:

1. Povej tehnično trditev.
2. Povej, zakaj je pomembna za to nalogo.
3. Dodaj referenco ali konkreten TODO, če je potrebna.
4. Končaj.

Primer tona:

```latex
Grafovske nevronske mreže omogočajo učenje predstavitev na podatkih z eksplicitno
relacijsko strukturo. V tej nalogi jih uporabimo za modeliranje časovnih,
prostorskih in fiksacijskih povezav med zaporednimi meritvami sledilnika pogleda.
```

## Terminologija

Pri pisanju diplome dosledno skrbi za slovensko strokovno terminologijo. Ko se
prvič pojavi nov angleški strokovni izraz:

1. Ne prevajaj ga na pamet.
2. Preveri slovensko rabo v zanesljivih virih, po prednostnem vrstnem redu:
   Univerza v Ljubljani, posebej FRI; Institut Jožef Stefan; Univerza v Mariboru,
   posebej FERI; slovenski terminološki slovarji in ostala strokovna literatura.
3. Predlagaj 2--4 možne prevode, na kratko razloži razliko med njimi in označi
   priporočeno izbiro.
4. Vprašaj Tomija, kateri izraz želi uporabljati.
5. Po potrditvi izraz zabeleži v projektni terminološki slovar oziroma
   `MEMORY.md`/`AGENTS.md`.
6. Nato ga v celotni diplomi uporabljaj konsistentno.

Ob prvi pojavitvi izraza v diplomi praviloma uporabi obliko `slovenski izraz
(angl. English term)`, kasneje pa uporabljaj samo potrjeni slovenski izraz. Ne
uporabljaj dobesednih prevodov, če v slovenščini zvenijo nenaravno ali imajo drug
pomen. Pri nejasnosti raje uporabi opisni prevod in vprašaj.

Dosledno uporabljaj:

| Pojem | Uporabi |
| --- | --- |
| graph neural network | grafovska nevronska mreža |
| GNN | GNN |
| spatio-temporal graph | časovno-prostorski graf |
| spatio-temporal graph representation | časovno-prostorska grafovska predstavitev |
| emotion recognition | prepoznava čustev |
| emotional state | čustveno stanje |
| affective computing | afektivno računalništvo |
| valence | valenca |
| arousal | vzburjenost |
| training sample, concrete data unit | učni vzorec |
| training example, abstract ML pair | učni primer |
| gaze coordinate | koordinata pogleda |
| gaze sample | meritev sledilnika pogleda |
| pixel | slikovna pika |
| embedding | predstavitev, razen kjer je “vložitev” res bolj naravno |
| baseline | izhodiščni model ali primerjalni model, odvisno od stavka |
| latent space | latentni prostor, po potrebi tudi prostor predstavitev |
| batch, mini-batch | mini-serija |
| overfitting | prekomerno prileganje |

Pri naštevanju relacij oziroma tipov povezav vedno uporabi vrstni red: časovne
(`temporal`), prostorske (`spatial`), fiksacijske (`fixation`). Vrstni red
prilagodi kontekstu, npr. časovne naprej/nazaj naštej pred prostorskimi in
fiksacijskimi.

Za model, ki je prispevek naloge, privzeto uporabljaj izraz `predlagani model`.
Kadar je treba poudariti grafovski tip modela, uporabi `predlagani GNN`; kadar
opisuješ notranjo zgradbo, uporabi `predlagana arhitektura`. Izraz `končni
model` uporabi samo, ko ga je treba ločiti od osnovnega GNN, ablacijske različice
ali vmesnih poskusov. Izrazom `naš model` in `naš GNN` se v končnem besedilu
izogibaj.

Pri prvi omembi uporabi:

```latex
valenca (angl. valence)
vzburjenost (ang. arousal)
```

Izogibaj se izrazu `afektivno stanje`, razen če je v kontekstu res potreben.
Običajno uporabi `čustveno stanje`, `klasifikacija čustvenih stanj`,
`prepoznava čustev` ali `čustveni odziv`.

Pri terminologiji za GNN, grafe, vložitve in splošno strojno učenje lahko najprej
preveri FRI naloge v `codex-kontekst`. Te naloge uporabljaj kot slogovni in
terminološki zgled, ne kot primarni vir za factualne trditve v tej diplomi.

## Dejstva in viri resnice

Preden spremeniš factualno vsebino naloge, preveri relevantne datoteke. Ne
zanašaj se na spomin za trenutno arhitekturo, predobdelavo, metrike, konfiguracije,
delitve podatkov ali rezultate.

Vrstni red preverjanja:

1. Trenutne datoteke v `diploma-latex`.
2. Trenutna koda, konfiguracije in rezultati v `GFM-for-eyetracker`.
3. Projektne opombe v `GFM-for-eyetracker`, posebej `MEMORY.md`,
   `diploma_knowledge_base.md`, `MAHNOB_dataset_report.md`,
   `docs/experiment_log.md`, `docs/journal.md` in novejše zapiske, če obstajajo.
4. FRI referenčne naloge v `codex-kontekst`, kadar iščeš slog, strukturo ali
   slovensko terminologijo.
5. Izvirni članki, uradni repozitoriji in uradna dokumentacija.
6. Splošna literatura.

Če se stare opombe razlikujejo od trenutne kode ali konfiguracij, obravnavaj kodo
in aktivne konfiguracije kot bolj verodostojne. Neskladje na kratko omeni Tomiju.

Podrobnosti, ki jih je treba pred zapisom v nalogo vedno preveriti neposredno v
`GFM-for-eyetracker`:

- trenutni vhodni podatki in pravila filtriranja;
- izločeni subjekti ali posnetki;
- dolžina oken, frekvenca vzorčenja in pogoji veljavnosti oken;
- uporabljene značilke vozlišč in povezav;
- konstrukcija časovnih, prostorskih in fiksacijskih povezav;
- arhitektura GNN, uporabljeni sloji, uteži povezav in pooling;
- uporabljeni primerjalni modeli, vključno z GazeMAE;
- protokoli delitev, standardizacija, preprečevanje uhajanja podatkov;
- vse metrike, tabele, številke rezultatov in zaključki.

Če dejstvo ni potrjeno, ne ugibaj. Dodaj natančen TODO:

```latex
% TODO: Preveri trenutno vrednost `min_samples_per_window` v aktivni konfiguraciji.
```

## Stabilen okvir naloge

Ta dejstva so stabilen okvir, vendar pri podrobnostih še vedno preveri kodo in
datoteke:

- Glavni podatkovni vir je MAHNOB-HCI oziroma lokalna eye-tracking podmnožica,
  uporabljena v projektu.
- Uporabljena modalnost naloge so meritve sledilnika pogleda.
- Ciljna naloga je klasifikacija čustvenih stanj, predvsem prek valence in
  vzburjenosti.
- En učni vzorec je časovno okno meritev, pretvorjeno v graf.
- Vozlišča predstavljajo meritve sledilnika pogleda.
- Povezave predstavljajo izbrane časovne, prostorske in fiksacijske odnose med
  meritvami.
- Oznaka je na ravni grafa oziroma časovnega okna.
- Primerjave z ne-grafovskimi modeli so pomembne, ker preverjajo, ali grafovska
  predstavitev doda korist glede na enaka vhodna okna.
- GazeMAE obravnavaj kot primerjalno metodo samo v obliki, ki jo potrjuje trenutna
  implementacija.

Ne zapiši kot potrjeno, če ni preverjeno v trenutnih datotekah:

- da je lokalna kopija MAHNOB-HCI popolna;
- kateri subjekti ali posnetki so dokončno izločeni;
- da je standardizacija izvedena fold-aware;
- da določene uteži povezav dejansko vplivajo na vse uporabljene GNN sloje;
- da so rezultati iz starih eSEEd_v2 poskusov relevantni za končne MAHNOB-HCI
  rezultate.

## FRI referenčne naloge

V `codex-kontekst` so PDF dokumenti, ki jih uporabljaj kot dobro referenco
kakovostnih FRI diplomskih oziroma magistrskih nalog. Ko potrebuješ slovensko
terminologijo za GNN, grafe, strojno učenje ali AI na splošno, najprej preglej te
naloge in šele nato širše vire.

Uporabne opombe iz trenutnega pregleda:

- **Vid Stropnik, Analiza grafov postavitev igralcev za napovedovanje podaj na
  nogometnih tekmah**: najbolj relevanten zgled za grafovsko nalogo. Dober vzorec
  za opis konstrukcije podatkovne zbirke grafov, vozlišč, povezav, značilk vozlišč
  in značilk povezav, več grafovskih konfiguracij, GNN arhitekture, eksperimentalne
  evalvacije in ablacijske študije. Uporabna terminologija: `grafovska nevronska
  mreža`, `grafovska podatkovna zbirka`, `grafovska predstavitev/ponazoritev`,
  `značilke vozlišč`, `značilke povezav`, `posredovanje sporočil`, `večglava
  pozornost`, `grafovski transformer`.
- **Vid Kocijan, Vložitev vozlišč omrežja v linearni prostorski zahtevnosti**:
  uporaben za terminologijo grafovskih vložitev in node2vec. Pomembna razlika:
  `vložitev vozlišč` je naravna pri klasičnih embedding metodah, v tej nalogi pa
  za splošne naučene reprezentacije praviloma ostani pri `predstavitev`, razen
  kjer je `vložitev` terminološko natančnejša.
- **Martin Špendl, Samospodbujevano učenje Coxovega regresijskega modela za
  predstavitev genskih skupin v latentnem prostoru**: dober vzorec za jasen
  prehod od problema do prispevka, za razlago domenskega predznanja v modelu in
  za previdno interpretacijo rezultatov. Uporaben je tudi pri terminologiji
  `predstavitev`, `latentni prostor`, `samospodbujevano/samonadzorovano učenje`,
  `cenilna funkcija` in `protokol ovrednotenja`.
- **Matjaž Zupančič Muc, Dvostopenjski globoki model za rekonstrukcijo
  geofizikalnih podatkov**: dober vzorec za raziskovalno strukturo z razširjenim
  povzetkom, eksplicitnimi prispevki, opisom metode, primerjavo z izhodiščnimi
  oziroma najsodobnejšimi metodami, kvalitativno analizo in jedrnatim sklepom.
- **hci-tagging dataset paper.pdf**: obravnavaj kot vsebinski vir za podatkovni
  kontekst, ne kot slogovni zgled FRI diplome.

## Struktura naloge

Prednostna struktura je raziskovalno usmerjena:

1. **Uvod**: motivacija, problem, raziskovalno vprašanje, prispevki, struktura.
2. **Teoretično ozadje**: samo potrebno ozadje; sledilnik pogleda, reprezentacija
   čustev, GNN in klasifikacija grafov.
3. **Sorodna dela**: prepoznava čustev iz pogleda, GNN za časovne oziroma
   fiziološke podatke, GazeMAE ali samonadzorovane predstavitve, če so uporabljene.
4. **Podatki in predobdelava**: MAHNOB-HCI, lokalna podmnožica, oznake, čiščenje,
   oknenje, delitve in preprečevanje uhajanja podatkov.
5. **Grafovska predstavitev podatkov**: učni vzorec, vozlišča, značilke, tipi
   povezav, značilke povezav in uteži.
6. **Modeli in metodologija**: primerjalni modeli, GNN arhitektura, učenje.
7. **Eksperimentalni protokol**: delitve, metrike, izbira hiperparametrov.
8. **Rezultati**: glavna primerjava, protokoli LOO, metrike, matrike zamenjav.
9. **Diskusija**: kaj deluje, omejitve, negotovosti podatkov, interpretacijske meje.
10. **Zaključek**: kratek odgovor na raziskovalno vprašanje in prihodnje delo.

Teorija naj razlaga pojme. Metodološka poglavja naj opisujejo dejanski cevovod.
Implementacijskih podrobnosti ne razprši po teoretičnih poglavjih.

## LaTeX pravila

- Sledi obstoječemu slogu, makrom in strukturi predloge.
- Ne spreminjaj razreda dokumenta, predloge ali paketov brez jasnega razloga.
- Ne uvajaj novih makrov, če niso potrebni.
- Ohrani obstoječe oznake, reference in citate, razen če so napačni.
- Uporabljaj nedeljive presledke: `Slika~\ref{...}`, `Tabela~\ref{...}`,
  `Poglavje~\ref{...}`, `10~s`, `60~Hz`, `prof.~dr.`.
- Ključne definicije piši v enačbah; inline matematiko uporabi za kratke izraze.
- Vsaka slika in tabela mora imeti jasen `\caption{...}`, `\label{...}` in
  omembo v besedilu.
- Tabele naj bodo v slogu `booktabs`, če predloga to podpira.
- Ne pretiravaj z opombami pod črto.
- LaTeX repozitorij mora ostati samostojen in združljiv z Overleafom. Ne dodajaj
  odvisnosti na lokalne poti ali na `GFM-for-eyetracker`.
- Če iz kode izvoziš sliko ali tabelo, končni artefakt kopiraj v ustrezno mapo
  znotraj `diploma-latex` in ga referenciraj relativno.
- Če potrebuješ python, ga uporabljaj iz conda env `gfm`.

## Reference in citiranje

- Ne izmišljaj citatov, BibTeX ključev, DOI-jev, naslovov, avtorjev ali številk.
- Če dodajaš konkreten vir, dodaj ali predlagaj tudi BibTeX vnos.
- Citat naj podpira konkreten stavek, ne naj bo dekoracija.
- Za osnovne metodološke trditve raje uporabi primarne vire: MAHNOB-HCI članek,
  GNN/message passing literaturo, GCN/GAT članke, članke o prepoznavi čustev iz
  pogleda in uradne vire za GazeMAE, če je omenjen.
- Če vir še ni preverjen, dodaj TODO:

```latex
% TODO: Dodaj referenco za osnovno formulacijo message passing v GNN.
```

## Pisanje in urejanje

Ko Tomi prosi za spremembo:

- najprej preberi okoliško poglavje;
- preveri relevantne datoteke v kodi ali zapiskih, če gre za dejstva;
- naredi ciljan diff;
- ohrani Tomijev pomen in stil;
- odstrani podvajanje, šibkejše ponovitve in premočne trditve;
- če trditev nima podpore, dodaj referenco ali TODO;
- če je odstavek logično napačen, ga ne olepšuj, ampak predlagaj boljšo različico.

Ko pišeš nov del diplome:

1. Ugotovi ciljno poglavje.
2. Preberi obstoječi slog v tem poglavju.
3. Preveri dejstva v `GFM-for-eyetracker`, če so odvisna od implementacije.
4. Napiši kratek, uporaben LaTeX.
5. Dodaj citate ali TODO-je samo tam, kjer so potrebni.
6. Tomiju kratko povej, kaj je še negotovo.

## Rezultati in interpretacija

Končnih rezultatov ne piši, dokler niso prisotni v repozitoriju. Pred zapisom
preveri:

- katera konfiguracija je ustvarila rezultat;
- cilj oziroma nalogo;
- delitveni protokol;
- ali gre za validacijski ali testni rezultat;
- ali so vrednosti povprečene po foldih;
- metriko, razredne uteži in obliko matrike zamenjav.

Interpretiraj previdno:

- primerjaj z izhodiščnimi modeli, ne z intuicijo;
- pri neuravnoteženih razredih poudari balanced accuracy in macro-F1;
- majhnih razlik ne označi kot statistično značilnih brez testa;
- pri LOO jasno loči posploševanje na subjekte in posploševanje na posnetke;
- uteži pozornosti lahko uporabiš kot pomožen vpogled, ne kot dokaz vzročnosti.

## Ablacije

Ablacije naj odgovarjajo na konkretna modelirna vprašanja. Smiselne kategorije:

- prispevek posameznih značilk;
- časovne, prostorske in fiksacijske povezave;
- naučene proti fiksnim utežem povezav;
- attention pooling proti preprostejšemu združevanju;
- relacijski fusion proti enostavnejši agregaciji.

Če komponenta ne izboljša rezultata, to ne pomeni, da je teoretično neuporabna.
Možni razlogi so velikost podatkov, šum oznak, hiperparametri ali implementacija.

## Pogoste formulacije

Raziskovalno vprašanje:

```latex
Osrednje raziskovalno vprašanje naloge je, ali lahko časovno-prostorska grafovska
predstavitev meritev sledilnika pogleda izboljša klasifikacijo čustvenih stanj v
primerjavi z ne-grafovskimi modeli, ki uporabljajo enaka časovna okna.
```

Poudarek naloge:

```latex
Sledilnik pogleda v tej nalogi obravnavamo predvsem kot vir časovno urejenih
meritev. Osrednji metodološki prispevek je grafovska predstavitev teh meritev in
njeno učenje z grafovskimi nevronskimi mrežami.
```

Učni vzorec kot graf:

```latex
Vsak učni vzorec je časovno okno meritev sledilnika pogleda, ki ga pretvorimo v
graf. Vozlišča predstavljajo posamezne meritve, povezave pa izbrane časovne,
prostorske in fiksacijske odnose med njimi.
```

Primerjava z izvirnim MAHNOB-HCI člankom:

```latex
Neposredna primerjava z rezultati iz izvirnega članka ni mogoča, saj se razlikujejo
vhodne značilke, dolžina obravnavanega odziva in eksperimentalni cevovod. Rezultate
zato uporabljamo predvsem kot referenčni okvir za podatkovno zbirko in ciljno
nalogo.
```

Pozornost:

```latex
Uteži pozornosti lahko uporabimo kot pomožen vpogled v delovanje modela, ne pa kot
dokaz vzročnega vpliva posamezne meritve na čustveno oznako.
```

## TODO pravila

Uporabljaj konkretne TODO komentarje:

```latex
% TODO: Preveri, ali aktivna konfiguracija uporablja fiksacijske povezave.
% TODO: Dodaj končne rezultate za subject LOO po zaključeni evalvaciji.
% TODO: Dodaj BibTeX za GazeMAE po preverjanju uradnega članka ali repozitorija.
```

Ne uporabljaj praznih TODO-jev:

```latex
% TODO: napiši bolje
% TODO: preveri vse
```

## Vzdrževanje tega dokumenta

Posodobi `AGENTS.md`, ko:

- Tomi potrdi projektno dejstvo, terminološko odločitev ali slogovno pravilo;
- se spremeni struktura naloge;
- se spremeni način, kako naj se piše ali preverja poglavja;
- se pokaže, da je obstoječe navodilo zastarelo, preveč podrobno ali napačno.

Ne dodajaj sem podatkov, ki sodijo v kodo, konfiguracije, rezultate ali projektni
knowledge base. Za takšne podatke raje zapiši, kje jih je treba preveriti.

Posodobi `MEMORY.md`, ko:

- Tomi poda pomembno preferenco za diplomsko pisanje;
- se potrdi odločitev o strukturi, terminologiji ali tonu;
- nastane načrt za nadaljnje pisanje ali urejanje poglavij;
- med branjem referenčnih FRI nalog, člankov ali obstoječih poglavij najdeš
  uporabno kratko opombo;
- ostane odprto vprašanje, ki ga je treba preveriti pozneje.

`MEMORY.md` naj ostane kratek in factualen. Ne podvajaj celotnega `AGENTS.md` in
ne zapisuj vanj dolgih izvlečkov iz literature.

## Čemu se izogibaj

- Ne spremeni naloge v psihološko ali klinično razpravo.
- Ne razlagaj osnov ML bolj na široko, kot je potrebno za bralca z računalniškim
  ozadjem.
- Ne uporabljaj angleških izrazov, kadar je slovenski izraz jasen in uveljavljen.
- Ne trdi novosti, klinične veljavnosti ali vzročnosti premočno.
- Ne poročaj starih raziskovalnih poskusov kot končnih rezultatov.
- Ne dodajaj trdih lokalnih poti.
- Ne ustvarjaj odvisnosti iz `diploma-latex` na `GFM-for-eyetracker`.
