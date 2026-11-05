# THEOREM — Programma matematico RGS–PSU–PRISM–Q6

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
- **Modelli:** [modello cosmologico torsione–Lambda](models/TORSION_LAMBDA_DUST_CLOSURE.md), con implementazione e test riproducibili.
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
| [T017](theorems/T017-q6-dirac-refinement.md) | Raffinamento cubico Q6–Dirac | Raffinamento esplicito \\(C_{2n})^{\\square6}\\); 64 corner zeros naïve; Wilson lift; limite di simbolo provato; convergenza spettrale completa aperta |
| [T019](theorems/T019-q6-free-strong-resolvent.md) | Limite libero di risolvente forte Q6–Wilson | Convergenza forte generalizzata del risolvente sul toro piatto di lato 2; non è convergenza in norma né limite gauge-interagente |
| [T020](theorems/T020-gauge-covariant-q6-strong-resolvent.md) | Limite gauge-covariante del risolvente forte Q6–Wilson | Consistenza cell-average (C) dimostrata con errore O(h); limite del risolvente forte generalizzato provato per connessioni SU(3) lisce fissate; CI audit non abeliano superata (run #9) |
| [T021](theorems/T021-rumin-analytic-torsion-2I.md) | Torsione analitica di Rumin su S³/2I con twist irriducibili di 2I | Molien e continuazione di Hurwitz corretti; identità Gamma esatte in T023 (PR #20 in review); convenzioni operatoriali in dimensione 3 chiuse da T024 |
| [T022](theorems/T022-eventual-hurwitz-rumin-2I.md) | Correzione della coda di Hurwitz per i twist di 2I | Decomposizione eventuale e scala (60^{-2s}) verificate in aritmetica esatta; torsioni confrontate a 70 cifre |
| [T023](theorems/T023-gamma-reflection-rumin-2I.md) | Identità esatte Gamma–seno per i nove twist di Rumin | Riduzione simbolica in (mathbb Q(sqrt5)), inclusa la coda eccezionale (N=62); PR #20 aperta |
| [T024](theorems/T024-rumin-kitaoka-operator-matching-3d.md) | Corrispondenza operatoriale Kitaoka–Rumin–Seshadri in dimensione 3 | Riscalamento identico, Laplaciani uguali, dualità di Hodge e convenzioni torsionali riconciliate; PR #21 aperta |
| [T031](theorems/T031-rumin-2i-equivariance.md) | Equivarianza del complesso di Rumin sotto l'azione binaria icosaedrica | Discesa geometrica e twist unitari; modelli espliciti delle nove irriducibili sviluppati in T034–T036; applicazione alle basi armoniche Rumin ancora aperta |
| [T032](theorems/T032-2i-irrep-molien-projectors.md) | Molien covariants esatti e interfaccia dei proiettori isotypici di 2I | Coefficienti interi dalle nove serie T021; decomposizione dimensionale verificata via test; modelli matriciali e caratteri espliciti ancora aperti |
| [T033](theorems/T033-equivariant-rumin-torsion-synthesis.md) | Decomposizione isotypica del complesso di Rumin e additività della torsione | Teorema astratto di gruppo finito; sintesi T021/T024/T031/T032 sotto ipotesi esplicite; nessun nuovo valore torsionale |
| [T034](theorems/T034-exact-2i-character-table.md) | Tabella esatta dei caratteri irriducibili di 2I | Ricostruzione su Q(√5) dai covarianti Molien T021/T032; ortogonalità e medie Molien sottoposte a test esatti |
| [T035](theorems/T035-exact-binary-icosahedral-model.md) | Modello quaternionico esatto di 2I | 120 vertici 600-cell, tavola di moltiplicazione, classi e rappresentazione fondamentale su Q(√5) |
| [T036](theorems/T036-explicit-2i-irreducible-models.md) | Modelli matriciali esatti delle nove irriducibili di 2I | Estrazione da potenze simmetriche, proiettori centrali, metriche hermitiane invarianti; test non ancora certificati in CI |
| [T034](theorems/T034-explicit-2i-representations.md) | Nove rappresentazioni irriducibili esplicite di 2I, tabella dei caratteri esatta, proiettori e matrix units | Costruzione esatta su Q(√5, i); 19 test esatti eseguiti; Molien da caratteri valido per ogni grado; modelli unitari ortonormali per 3,3′,4′,5,6 e matrici di Rumin ancora aperti (nota: il numero T034 è già usato da `T034-exact-2i-character-table`; sovrapposizione parziale con T036, vedi nota nel teorema; da rinumerare a cura del maintainer) |

La compatibilità tra T012–T017 è registrata nella [matrice Q6 T012–T017](open-problems/Q6-T012-T017-COMPATIBILITY-MATRIX.md).

Il file `001-fixed-lattice-temporal-wilson-limit.md` è un risultato preesistente, non rinumerato nella sequenza T001–T007.

| [T047](theorems/T047-ec-weyssenhoff-spin-scaling.md) | Scaling cosmologico della torsione algebrica in un fluido di Weyssenhoff | Sotto ipotesi esplicite: n∝a⁻³, s²∝a⁻⁶, correzione EC efficace stiff negativa; incompatibilità con identificazione dust-like a⁻³ |

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


## Benchmark dinamica cellulare RGS

Il benchmark iniziale CA è versionato nel repository:
- [Motore Python v0.1](scripts/rgs_cellular_dynamics_benchmark.py)
- [Test automatici](tests/test_rgs_cellular_dynamics_benchmark.py)
- [Guida d'uso](docs/RGS_CELLULAR_DYNAMICS_README.md)
- [Roadmap scientifica](docs/RGS_CELLULAR_DYNAMICS_ROADMAP.md)

Stato: implementazione e smoke test iniziali. Non è ancora un risultato teorico né una validazione statistica dell'evoluzione genetica. Il passo successivo è implementare la ricerca evolutiva con semi appaiati, validazione indipendente e obiettivi multi-criterio.


## Modello cosmologico torsione–Lambda

La chiusura FLRW dust-like è registrata in [models/TORSION_LAMBDA_DUST_CLOSURE.md](models/TORSION_LAMBDA_DUST_CLOSURE.md), con implementazione in `scripts/torsion_lambda_dust_closure.py` e test in `tests/test_torsion_lambda_dust_closure.py`. È un modello fenomenologico di consistenza; non viene presentato come derivazione della torsione algebrica Einstein–Cartan.


## Einstein–Cartan: audit della legge di scala dello spin

T047 dimostra, nel modello minimale di Weyssenhoff con spin per particella conservato e media locale isotropa, che il termine quadratico algebrico di spin scala come a⁻⁶ e ha equazione di stato stiff. Questo esclude l'identificazione diretta con la componente fenomenologica dust-like a⁻³ della PR #77, sotto le ipotesi dichiarate. La derivazione e i test sono in `theorems/T047-ec-weyssenhoff-spin-scaling.md`, `scripts/ec_spin_fluid_scaling.py` e `tests/test_ec_spin_fluid_scaling.py`.
