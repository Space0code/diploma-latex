# Diploma v LaTeXu

Ta repozitorij vsebuje samostojno LaTeX verzijo diplomske naloge, pripravljeno iz FRI LaTeX predloge. Projekt nima odvisnosti od raziskovalnega repozitorija `GFM-for-eyetracker`.

Glavna datoteka je:

```bash
diploma.tex
```

Lokalni prevod iz terminala:

```bash
latexmk diploma.tex
```

Vmesne datoteke in PDF se zapišejo v `gradnja/`.

Struktura:

- `uvodni_del/`: povzetek, abstract in seznam kratic.
- `poglavja/`: glavna poglavja diplome.
- `dodatki/`: dodatki na koncu naloge.
- `slike/`: slike, namenjene diplomi.
- `tabele/`: tabele, namenjene diplomi.
- `podporno/`: podporne datoteke FRI predloge.
