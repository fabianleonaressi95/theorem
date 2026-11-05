# THEROEM — Programma matematico RGS–PSU–PRISM–Q6

Repository centrale della ricerca: biblioteca organizzata, mappa dei progetti, inventario delle fonti, registro delle evidenze e dimostrazioni.

## Struttura effettiva

```text
theroem/
├── README.md
├── library-inventory/
│   └── README.md
├── manuscripts/
│   └── README.md
├── monographs/
│   ├── books-and-edited-volumes/
│   ├── chapters/
│   ├── theses/
│   └── long-form-reviews/
├── bibliography/
│   ├── spin-glasses/
│   ├── wyler-hua/
│   ├── gauge-wilson-qft/
│   ├── spin-geometry-quaternionic/
│   ├── quantum-light-foundations/
│   ├── gravity-teleparallel/
│   ├── holography-emergent-spacetime/
│   ├── discrete-geometry-combinatorics/
│   ├── information-theory/
│   └── critical-and-nonstandard/
├── projects/
├── models/
├── evidence/
├── open-problems/
└── theorems/
```

Le directory sono state create. Le directory models/evidence/open-problems contengono registri iniziali; si aggiungeranno sottosezioni solo quando popolate.

## Indice
- **Inventario Library:** [fonti recuperate](library-inventory/README.md). La Library è stata scandita a livello di metadati: 388 elementi totali, 118 documenti PDF/testo/Markdown. L'inventario registra le fonti già identificate e segnala quelle ancora da classificare.
- **Manoscritti:** [registro](manuscripts/README.md), separato dalla letteratura pubblicata.
- **Monografie e capitoli:** [catalogo](monographs/README.md), con indice dei 99 contributi di *Gravitational Energy Control*, capitoli di *Against the Tide* e tesi di Maurice Weiler.
- **Estrazione delle formule:** [registro maestro](bibliography/FORMULA_EXTRACTION_REGISTER.md), con schede di trascrizione e verifica delle equazioni delle fonti.
- **Bibliografia:** [catalogo generale](bibliography/README.md), con vetri di spin, Wyler/Hua, gauge/Wilson/QCD, geometria spinoriale e quaternionica, luce, gravità, olografia, geometria discreta e fonti non standard.
- **Progetti:** [mappa dei filoni](projects/README.md).
- **Dimostrazioni:** [theorems/](theorems/).
- **Verifiche esterne:** [matrice delle verifiche matematiche](open-problems/EXTERNAL_MATHEMATICAL_VALIDATION_MATRIX.md), con criteri di accettazione e registro delle risposte.
- **Compatibilità Q6–Dirac–barioni:** [matrice T012–T017](open-problems/Q6-T012-T017-COMPATIBILITY-MATRIX.md), con definizioni, operatori, dipendenze e problemi aperti.

## Registro dei teoremi

| ID | Oggetto | Stato / perimetro |
|---|---|---|
| T001 | Teorema di Liouville | Teorema classico dimostrato; applicazione PSU condizionale |
| T002 | Densità di Bergman su D5 | Calcolo geometrico; definizione del dominio da sottoporre ad audit |
| T003 | No-go marginale atomica | Dimostrato per push-forward atomico esatto; non esclude limiti deboli |
| T004 | Riemann sums verso Bergman | Dimostrato sotto ipotesi di compattezza e bordo nullo; non è una derivazione Wilson |
| T005 | Supporto marginale Wilson Q6 | Formula e positività; non genera cutoff duro a beta finito |
| T006 | Quoziente gauge 5-toro | Identificazione tramite reticoli dei caratteri |
| T007 | Serie gauge-averaged | Espansione di Fourier assolutamente convergente |
| T008 | Criterio Wilson–Bergman | Criterio sufficiente quantitativo; applicazione Q6 ancora aperta |
| T009 | Forma quadratica efficace Wilson | Identità rank(Q_eff)=rank(C)−rank(RC); ipotesi di rango Q6 e limite theta ancora da verificare |
| [T010](theorems/T010-rumin-spectrum-poincare-sphere.md) | Riduzione spettrale di Rumin su S³/2I | Teorema di proiezione per quozienti finiti; benchmark scalare verificato; spettro Rumin completo ancora da calcolare |
| T016 | Nielsen–Ninomiya e audit Q6 | Ipotesi/topologia ricostruite; identità finite Q6 verificate; nessuna evasione del no-go theorem |
| [T017](theorems/T017-q6-dirac-refinement.md) | Raffinamento cubico Q6–Dirac | Raffinamento esplicito \((C_{2n})^{\square6}\); 64 corner zeros naïve; Wilson lift; limite di simbolo provato; convergenza spettrale completa aperta |

La compatibilità tra T012–T017 è registrata nella [matrice Q6 T012–T017](open-problems/Q6-T012-T017-COMPATIBILITY-MATRIX.md).

Il file `001-fixed-lattice-temporal-wilson-limit.md` è un risultato preesistente, non rinumerato nella sequenza T001–T007.

## Collegamento con il filone Nielsen/Hopf

La bibliografia citata nel manoscritto di Jennifer Lorraine Nielsen è registrata separatamente in [nielsen-hopf-manuscript.md](bibliography/source-bibliographies/nielsen-hopf-manuscript.md). T010 sviluppa un risultato matematico indipendente sul quoziente Hopf/Seifert (S^3/2I); non attribuisce il teorema a Nielsen e non considera il suo manoscritto una validazione delle affermazioni qui dimostrate.

## Regole scientifiche

1. Un teorema per volta, con enunciato, ipotesi, lemmi, prova e conseguenze.
2. Niente workflow giganteschi e niente script come sostituti di dimostrazioni.
3. Distinguere dimostrato, condizionale, verificato numericamente, candidato, ipotesi e aperto.
4. Non ripetere audit già conclusi senza una ragione matematica.
5. Le fonti si catalogano tutte; si usano in una prova solo quando sostengono un passaggio preciso.
6. Non inventare titoli, DOI, autori o metadati: le lacune restano visibili.
7. Le teorie non standard sono conservate e analizzate criticamente, non assunte vere né scartate senza esame.

## Stato del riordino

La struttura bibliografica è stata avviata e collegata ai materiali recuperati dalla Library. Il catalogo non è ancora esaustivo: restano file con nomi generici, capitoli citati in conversazione ma non reperiti come file autonomi e riferimenti bibliografici da disambiguare.
