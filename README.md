# THEROEM — Programma matematico RGS–PSU–PRISM–Q6

Questo repository è l'indice centrale della ricerca. Non deve essere soltanto una sequenza di teoremi: contiene una biblioteca organizzata, una mappa dei progetti, un registro delle evidenze e una sezione separata per le dimostrazioni.

## Struttura effettiva

```text
theroem/
├── README.md
├── monographs/\n│   ├── books-and-edited-volumes/\n│   ├── chapters/\n│   ├── theses/\n│   └── long-form-reviews/\n├── bibliography/
│   ├── README.md
│   ├── spin-glasses/
│   ├── wyler-hua/
│   ├── gauge-wilson-qft/
│   ├── spin-geometry-quaternionic/
│   ├── quantum-light-foundations/
│   ├── gravity-teleparallel/
│   └── critical-and-nonstandard/
├── projects/
│   └── README.md
├── theorems/
│   ├── T001-liouville-theorem.md
│   ├── T002-d5-bergman-volume-density.md
│   ├── T003-wilson-atomic-marginal-no-go.md
│   ├── T004-riemann-sums-bergman-weak-limit.md
│   ├── T005-q6-wilson-fiber-marginal-support.md
│   ├── T006-q6-wilson-five-torus-quotient.md
│   ├── T007-q6-gauge-average-fourier-marginal.md
│   └── 001-fixed-lattice-temporal-wilson-limit.md
└── (altre sezioni verranno aggiunte solo quando popolate)
```

Le cartelle di bibliografia sono già create e popolate con il catalogo ricostruito. Le sezioni models/evidence/open-problems sono previste ma non ancora popolate: non le dichiaro completate.

## Indice di lavoro

- **Monografie e capitoli:** [catalogo monografico](monographs/README.md), con indice dei 99 contributi di *Gravitational Energy Control*, capitoli di *Against the Tide* e tesi di Maurice Weiler.\n- **Bibliografia degli articoli:** [catalogo generale](bibliography/README.md). Include esplicitamente vetri di spin, Wyler/Hua, gauge/Wilson/QCD, geometria spinoriale e quaternionica, luce topologica/OAM, gravità/teleparallelismo e fonti critiche/non standard.
- **Progetti:** [mappa dei filoni](projects/README.md).
- **Dimostrazioni:** [theorems/](theorems/).

## Registro dei teoremi

| ID | Oggetto | Stato / perimetro |
|---|---|---|
| T001 | Teorema di Liouville | Teorema classico dimostrato; applicazione PSU condizionale |
| T002 | Densità di Bergman su D5 | Calcolo geometrico; definizione del dominio richiede audit/correzione prima di usarlo |
| T003 | No-go marginale atomica | Dimostrato per push-forward atomico esatto; non esclude limiti deboli |
| T004 | Riemann sums verso Bergman | Dimostrato sotto le ipotesi di compattezza e bordo nullo; non è una derivazione Wilson |
| T005 | Supporto marginale Wilson Q6 | Formula e positività; non genera cutoff duro a beta finito |
| T006 | Quoziente gauge 5-toro | Dualità dei caratteri; richiede mantenere le ipotesi esatte sul reticolo intero |
| T007 | Serie gauge-averaged | Espansione di Fourier assolutamente convergente |

Il file `001-fixed-lattice-temporal-wilson-limit.md` è un risultato preesistente del repository, non rinumerato nella sequenza T001–T007.

## Regole scientifiche

1. Un teorema per volta, con enunciato, ipotesi, lemmi, prova e conseguenze.
2. Niente workflow giganteschi e niente script come sostituti di dimostrazioni.
3. Distinguere **dimostrato**, **condizionale**, **verificato numericamente**, **candidato**, **ipotesi** e **aperto**.
4. Non ripetere audit già conclusi senza una ragione matematica.
5. Le fonti si catalogano tutte; si usano in una prova solo quando sostengono un passaggio preciso.
6. Non inventare titoli, DOI, autori o metadati: le lacune restano visibili nel catalogo.
7. Le teorie non standard sono conservate e analizzate criticamente, non assunte vere né scartate senza esame.

## Priorità di riordino

La prima priorità è completare la biblioteca delle fonti già inviate dall'utente e associare ogni articolo a uno o più filoni. Solo dopo si decide quale teorema affrontare.