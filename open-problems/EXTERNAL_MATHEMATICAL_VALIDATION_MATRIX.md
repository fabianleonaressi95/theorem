# Matrice delle verifiche matematiche esterne

Questa matrice collega i risultati e i teoremi del repository alle richieste di revisione indipendente. **Non costituisce approvazione esterna**: un contatto inviato non equivale a una risposta o a una validazione.

## Stati epistemici

- **Dimostrato:** prova completa sotto ipotesi esplicite.
- **Verificato numericamente:** audit riproducibile su dati o matrici finiti.
- **Condizionale:** derivazione valida se valgono ipotesi ancora da verificare.
- **Candidato:** costruzione identificata, ma proprietà geometriche/analitiche non dimostrate.
- **Aperto:** manca una prova, un limite uniforme o una verifica indipendente.

## Matrice delle priorità

| ID | Problema / risultati collegati | Verifica richiesta | Criterio di accettazione | Stato |
|---|---|---|---|---|
| E1 | Q6–D5, T005–T009: marginale Wilson, reticolo delle fibre, quoziente di rango 5 | Verificare kernel saturo e rango; derivare la somma theta esatta sulle fibre; confrontare con l'approssimazione gaussiana tramite Poisson summation | Stima uniforme esplicita del resto e delle code, uniforme nel parametro di raffinamento; controllo della normalizzazione | **Aperto** per limite uniforme e push-forward Bergman |
| E2 | Wilson–Bergman, T002–T004 e T008 | Distinguere identità locale della densità di Bergman, convergenza di misure atomiche e applicazione effettiva alla marginale Wilson | Costruire la famiglia \(\mu_k\), la mappa verso D5, mesh \(\delta_k\), errore di massa \(E_k\) e massa esterna \(\ell_k\); dimostrare le ipotesi del criterio T008 | **Aperto** per l'applicazione Q6; T002–T004 hanno perimetri propri |
| E3 | Ellis–RGS: Mosco curvo G5/G6 | Dimostrare compattezza uniforme, liminf e recovery sequence nella stessa struttura di Hilbert | Shape regularity, ellitticità metrica uniforme, controllo Jacobiani e compattezza discreta; non trasferire il teorema P1 su toro piatto alla famiglia curva | **Aperto** |
| E4 | Operatori Dirac/Laplace, audit tangente 188D e gap | Stabilire autoaggiuntezza, convergenza degli operatori e stabilità delle proiezioni spettrali | Spazi di Hilbert e domini dichiarati; convergenza di risolventi o forma; controllo di molteplicità, kernel e gap | **Verificato numericamente** a dimensione finita; limite continuo **aperto** |
| E5 | Costruzioni quaternioniche, spinoriali e twistor | Verificare esistenza e compatibilità delle strutture differenziali, non solo identità algebriche finite | Strutture globali compatibili, integrabilità/parallelismo e condizioni di curvatura appropriate alla geometria dichiarata | **Candidato** |
| E6 | G2/Spin(7), calibrations e instantoni | Costruire le forme definenti e controllarne la torsione; verificare le equazioni di instantone | Equazioni differenziali e stime analitiche; torsione-free dimostrato dove richiesto | **Aperto** |
| E7 | Azione RGS–PSU/TEGR/gauge | Formulare un'unica azione e derivarne le equazioni | Variabili e simmetrie dichiarate, equazioni di Eulero–Lagrange, identità di Bianchi e limiti controllati | **Aperto** |

## Collegamento ai teoremi già catalogati

- **T002:** densità di Bergman su D5; identità geometrica sotto la normalizzazione specificata. Non dimostra che la marginale Wilson produca tale misura.
- **T003:** impossibilità di uguaglianza esatta tra marginale atomica e misura assolutamente continua non nulla; non esclude convergenza debole.
- **T004:** convergenza di somme di Riemann pesate verso la misura troncata sotto le ipotesi dichiarate; non è una derivazione da Wilson.
- **T005:** positività del supporto della marginale Wilson a beta finito; non produce cutoff duro.
- **T006–T007:** struttura del quoziente gauge e media di Fourier; non dimostrano la misura di Bergman.
- **T008:** criterio quantitativo sufficiente per convergenza Wilson–Bergman; applicazione Q6 non ancora verificata.
- **T009:** forma quadratica efficace gaussiana condizionale; il reticolo intero produce una somma theta, non automaticamente il suo integrale gaussiano.

## Assegnazione delle richieste agli esperti già contattati

| Contatti | Tema da sottoporre a controllo |
|---|---|
| Luigi Del Debbio, Peter Boyle, Alessio Martini, Anita Maria Tabacco | E1–E2: fibre intere, Poisson, controllo delle code, armonica e push-forward |
| Ralf Hiptmair, Ragnar Winther, Douglas Arnold | E3: FEEC/DEC curvo, compattezza e Mosco |
| Luis Wirth, Kaushik Kalyanaraman | E3–E4: confronto implementativo DEC/FEEC e benchmark riproducibili |
| Pierre Albin, Thomas Ourmières-Bonafos, Giovanni Landi | E4: operatori di Dirac, kernel, gap, indice e convergenza spettrale |
| Andrei Moroianu, Simon Salamon, Nobuhiro Honda | E5: spinori, twistor e integrabilità quaternionica |
| Andrew J. Clarke, Spiro Karigiannis, Jason D. Lotay | E6: G2/Spin(7), torsione, calibrazioni e instantoni |
| Jeff Viaclovsky, Ioana Șuvaina, Jacopo Stoppa | E5–E7: analisi ellittica, geometria quadridimensionale e compatibilità Kähler |
| Alessandro Lucantonio | Benchmark applicativo in meccanica computazionale e calcolo geometrico discreto |

Le assegnazioni indicano pertinenza tematica, non disponibilità o adesione degli studiosi. Verificare affiliazioni e recapiti prima di eventuali nuovi invii.

## Protocollo per le risposte

Per ogni risposta effettivamente ricevuta:
1. registrare data, domanda inviata, risposta e riferimenti citati;
2. estrarre un'ipotesi, lemma, controesempio o benchmark preciso;
3. creare un solo artefatto minimo nel repository (nota di prova, test o issue);
4. indicare commit e risultati riproducibili;
5. aggiornare lo stato epistemico soltanto dopo aver superato il criterio di accettazione.

**Ordine tecnico consigliato:** E1 (stima uniforme della somma theta), E3 (Mosco curvo G5/G6), E4 (convergenza spettrale). Non aprire un'altra ondata di contatti sovrapposti prima di raccogliere e organizzare le risposte già inviate.

## Registro delle risposte

Nessuna risposta è inferita dal fatto che un'email sia stata preparata o inviata. Aggiornare questa tabella solo sulla base di corrispondenza reale.

| Gruppo | Tema | Stato |
|---|---|---|
| Hiptmair, Winther, Arnold | Mosco curvo | In attesa / non registrato |
| Del Debbio, Boyle, Martini, Tabacco | Wilson e Bergman | In attesa / non registrato |
| Wirth, Kalyanaraman | DEC/FEEC | In attesa / non registrato |
| Albin, Ourmières-Bonafos, Landi | Dirac e spettro | In attesa / non registrato |
| Honda, Șuvaina, Stoppa, Viaclovsky, Moroianu, Cherkis, Clarke, Karigiannis, Lotay, Salamon | Geometria speciale, spin e gauge | In attesa / non registrato |
| Lucantonio | Meccanica computazionale | In attesa / non registrato |


## E1 — Q6–D5 Wilson fibre: source transfer and next proof gate

The mathematical specifications are now present in THEOREM:
- [Integer-fibre quotient](../docs/Q6_D5_INTEGER_FIBER_QUOTIENT.md)
- [Saturated kernel and factorial tail bound](../docs/Q6_D5_SATURATED_KERNEL_AND_TAIL_BOUND.md)
- [Five-torus Wilson marginal](../docs/Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md)

The exact quotient and convergence arguments are not the same as a certified numerical evaluation of the complete fibre sum. The implementation and tests still need to be ported into this repository with all dependencies resolved. The next acceptance gate is: (i) exact reconstruction of the cycle matrix and rational top-mode map; (ii) Smith-certified saturated kernel basis and unimodular splitting; (iii) independently checked tail enclosure; (iv) a reproducible finite enumeration plus rigorous remainder; (v) explicit comparison of the resulting effective quadratic form with the Poisson-summed theta representation. Do not claim a Hua/Bergman limit from this finite-coupling work.
