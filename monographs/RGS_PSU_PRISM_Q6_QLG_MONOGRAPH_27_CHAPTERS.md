# RGS–PSU–PRISM–Q6–QLG
## Monografia integrata del programma matematico e fisico
**Edizione di lavoro 1.0 — 9 novembre 2026**  
**Repository:** `fabianleonaressi95/theorem`  
**Funzione:** testo di sintesi principale, con rinvii ai record di prova, ai dati, ai codici, ai test e ai dossier di provenienza.

---

## Premessa: che cosa unifica davvero il programma

Il programma RGS–PSU–PRISM–Q6–QLG non va presentato come una teoria fisica già unificata e verificata. È un programma di ricerca che contiene risultati matematici finiti, costruzioni geometriche, modelli di campo, benchmark numerici e ipotesi interpretative. La sua unità attuale è **architetturale e metodologica**: combinatoria cellulare, operatori, simmetrie, forme quadratiche, raffinamento e possibili limiti continui. La sua unità fisica complessiva è invece un obiettivo, non un risultato acquisito.

Questa monografia svolge quattro compiti:
1. fissa le definizioni che non devono essere confuse;
2. raccoglie i risultati effettivamente documentati;
3. collega i filoni tramite interfacce matematiche esplicite;
4. elenca le dimostrazioni e le verifiche che mancano per passare dalla struttura discreta a una teoria geometrico-fisica.

### Convenzione epistemica

- **[E]** legge o teorema standard, indipendente dal progetto;
- **[P]** dimostrazione matematica completa nel perimetro e sotto le ipotesi dichiarate;
- **[N]** verifica numerica/computazionale su una specifica istanza;
- **[C]** risultato condizionale a ipotesi esplicite;
- **[M]** modello o fenomenologia implementata;
- **[H]** ipotesi o interpretazione non derivata;
- **[O]** problema aperto.

Un test che passa non trasforma automaticamente [N] in [P]. Un'identità geometrica non dimostra una legge fisica. Un modello simulato non costituisce una validazione industriale.

---

# PARTE I — FONDAMENTI DISCRETI E ALGEBRICI

## Capitolo 1 — Architettura logica RGS–PSU–PRISM–Q6

La catena di lavoro di riferimento è

\[
\text{geometria RGS}
\longrightarrow \text{complessi e cochain}
\longrightarrow \text{operatori}
\longrightarrow \text{forme quadratiche}
\longrightarrow \text{raffinamento}
\longrightarrow \text{limite}.
\]

Q6 fornisce un laboratorio finito esatto per incidenza, coomologia, simmetrie, operatori e gauge. PRISM estende la costruzione a grafi prodotto e a famiglie di raffinamento. RGS/PSU fornisce la motivazione geometrica, le coordinate, i coframe e le proposte di interpretazione spazio-temporale. Il settore quaternionico e 2I studia strutture di rappresentazione e operatori spettrali. QLG cerca un'interfaccia spinoriale. QAT e Anti-Twin propongono interpretazioni geometriche della luce e della doppia struttura.

I collegamenti sono accettati soltanto se sono fornite: (i) una mappa fra spazi; (ii) la trasformazione delle variabili; (iii) un'identità di intertwining o una derivazione variazionale; (iv) un controllo dei domini e delle ipotesi. Non basta che due matrici abbiano dimensioni compatibili o che due numeri coincidano.

**Riferimenti:** [catalogo delle leggi](../foundations/ESTABLISHED_AND_RGS_LAW_CATALOGUE.md), [mappa dei progetti](../projects/README.md), [matrice di validazione esterna](../open-problems/EXTERNAL_MATHEMATICAL_VALIDATION_MATRIX.md).

## Capitolo 2 — Il cubo booleano Q6: grafo, Fourier e Laplaciano

La definizione canonica è
\[
Q_6=\operatorname{Cay}(\mathbb Z_2^6,\{e_1,\ldots,e_6\}).
\]
Ha 64 vertici, 192 archi non orientati e grado 6. Le traslazioni coordinate soddisfano
\[
T_i^2=I,\qquad T_i^{-1}=T_i.
\]
I caratteri
\[
\chi_k(x)=(-1)^{k\cdot x},\quad k\in\mathbb Z_2^6
\]
formano una base di Fourier esatta. Lo spettro del Laplaciano combinatorio è
\[
\lambda_m=2m,\qquad \operatorname{mult}(\lambda_m)=\binom 6m,
\quad m=0,\ldots,6.
\]
La bipartizione ha 32 vertici per parte.

Il rango del bordo del grafo connesso è 63, quindi il suo numero ciclico è
\[
\beta_1^{\rm graph}=192-64+1=129.
\]
Questo numero appartiene al solo grafo. Non è il primo Betti del complesso dopo aver riempito le facce quadrate.

**Stato:** [P] identità combinatorie e spettrali standard, controllabili esattamente.  
**Riferimenti:** T015, T016; `scripts/verify_q6_laws.py`.

## Capitolo 3 — Il 2-scheletro cubicale e l'Anti-Twin cellulare

Il 2-scheletro del cubo a sei dimensioni contiene
\[
|V|=64,\quad |E|=192,\quad |F_2|=240.
\]
Le matrici intere di bordo sono
\[
B_1\in\mathbb Z^{64\times192},\qquad
B_2\in\mathbb Z^{192\times240},
\]
e soddisfano esattamente
\[
B_1B_2=0.
\]
Nel 2-scheletro troncato, il rango di \(B_2\) è 129; ne segue
\[
b_1=0,\qquad b_2=240-129=111.
\]
Il valore 111 è dovuto al fatto che non sono state incluse le celle tridimensionali. Il cubo completo è contrattile e ha tutti i Betti positivi nulli.

Il complemento bitwise
\[
c(g)=g\oplus 63
\]
induce mappe cellulari segnate \(J_0,J_1,J_2\). T068 verifica
\[
J_0B_1=B_1J_1,\quad J_1B_2=B_2J_2,\quad J_k^2=I.
\]
Quindi l'Anti-Twin ha una definizione matematica precisa come involuzione cellulare in questa istanza. L'interpretazione come doppio foglio fisico, antimateria o recupero della simmetria Lorentz non segue da queste identità.

**Stato:** [P]/[N] identità di catena esatte per il complesso implementato; interpretazione fisica [H].  
**Riferimento:** T068, `models/q6_topological_synchronization.py`, `tests/test_q6_topological_synchronization.py`.

## Capitolo 4 — Trigrammi, codifica dei bit e geometria Kathara

La codifica a coppie di bit
\[
(2b_0+b_1,\;2b_2+b_3,\;2b_4+b_5)
\]
organizza i 64 stati in tre blocchi binari a due bit. Una seconda lettura raggruppa i sei bit in due triplette e li interpreta come trigrammi. Le due codifiche sono diverse e devono essere dichiarate quando si costruiscono mappe o classi.

I record T055–T062 trattano suddivisioni, mappe di catena, omotopie, similarità e audit di geometrie quadrate/Kathara. I risultati di catena possono essere riutilizzati come struttura algebrica: mappe che commutano con il bordo, omotopie di catena e compatibilità Hodge. La corrispondenza fra classi, trigrammi, quadrati, linee o livelli Kathara deve però essere quella effettivamente definita dal generatore e dai record, non una reinterpretazione retroattiva.

**Regola:** ogni classe deve avere un'etichetta canonica, un rappresentante, una relazione di equivalenza e un algoritmo deterministico di enumerazione. Senza questi elementi non si può affermare un conteggio di classi.

**Stato:** i singoli lemmi di catena sono registrati in T055–T062; la classificazione globale richiede il rispettivo generatore e dati canonici.

## Capitolo 5 — Q6 come complesso, coomologia e Hodge

Per un complesso cellulare orientato, le mappe di bordo soddisfano
\[
\partial_k\partial_{k+1}=0.
\]
Con prodotti scalari sulle celle, il Laplaciano di Hodge è
\[
\Delta_k=\partial_{k+1}\partial_{k+1}^*
+\partial_k^*\partial_k.
\]
Il suo nucleo rappresenta la coomologia finita del complesso. Occorre tenere separati:
- Laplaciano del grafo (solo vertici e archi);
- Laplaciano del 2-scheletro (con facce quadrate);
- Laplaciani del complesso cubico completo;
- operatori pesati o gauge-covarianti.

Il rango e i Betti vanno ricalcolati dalle matrici di bordo della stessa istanza. La formula del numero ciclico del grafo non può essere riutilizzata dopo il riempimento delle facce.

**Riferimenti:** T059, T060, T062, T065, T067, T068; audit FEEC in `projects/de_rham_benchmark`.

## Capitolo 6 — SU(2), SU(3), link e covarianza di gauge

Una variabile di link orientato \(U_{vw}\in G\) trasforma come
\[
U_{vw}\mapsto g_vU_{vw}g_w^{-1},\qquad
\psi(v)\mapsto g_v\psi(v).
\]
Il trasporto lungo un cammino è il prodotto ordinato dei link; l'holonomia di faccia è il prodotto lungo il bordo. Per SU(3), la contrazione con \(\epsilon_{abc}\) costruisce un singoletto di colore per tre campi fondamentali.

T013 dimostra l'invarianza del singoletto nel perimetro dichiarato; T014 dimostra la covarianza del particolare operatore di grafo accoppiato ai link. T063 registra il doppio rivestimento \(SU(2)\to SO(3)\); T064 tratta la covarianza delle olonomie finite SU(2).

Queste identità non costituiscono ancora una teoria QCD completa: occorrono azione, misura, vincoli di Gauss, dinamica fermionica, proprietà di positività, limite e osservabili. SU(3) di colore e SU(3) di sapore non sono intercambiabili.

**Stato:** risultati algebrici [P]; dinamica QCD e limite interagente [O].  
**Riferimenti:** T012–T014, T063–T064, `open-problems/Q6-GAUGE-COVARIANT-WILSON-OPERATOR.md`.

## Capitolo 7 — Q6-D5: quoziente intero, fibre Wilson e toro annihilator

Il settore D5 seleziona un sottospazio razionale di cinque modi. Sia \(C\) la matrice dei cicli interi e \(H=D_1^TD_1\) l'operatore di edge Hodge. La mappa razionale
\[
\Pi_5:\mathbb Z^{129}\to\mathbb Q^5,\qquad
c\mapsto cCV
\]
ha rango 5. Il kernel intero saturo
\[
K_{\mathbb Z}=\mathbb Z^{129}\cap\ker_{\mathbb Q}\Pi_5
\]
ha rango 124. La decomposizione di Smith certifica che il quoziente è privo di torsione e che il kernel usato è quello intero completo, non un sottoreticolo di indice finito.

Il peso di Wilson puntuale
\[
w(c)=\prod_e\frac{I_{|n_e|}(\beta)}{I_0(\beta)},\quad n=cC
\]
non è costante sulle fibre del quoziente. Il peso corretto è la somma
\[
W_{\rm eff}([c])=\sum_{k\in K_{\mathbb Z}}w(c+k).
\]
La convergenza assoluta segue dal bound fattoriale dei coefficienti di Bessel e dalla crescita della norma del vettore di flusso.

In coordinate di flusso, il reticolo della fibra ha rango 124 in \(\mathbb Z^{192}\). Il suo sottogruppo annihilator ha dimensione 68; per la specifica matrice Q6, i fattori invarianti di Smith sono tutti 1 e quindi l'annihilator è il toro connesso \(\mathbb T^{68}\). La formula di Fourier su tale sottogruppo è esatta. La valutazione numerica QMC rimane una stima, non un intervallo certificato.

Il bound globale della coda è costruito con
\[
T_\beta(S)=\sum_{s\ge S}2^{192}
\binom{s+191}{191}\frac{(96\beta)^s}{s!},
\]
e la parte asintotica viene maggiorata geometricamente quando il rapporto dei termini è minore di uno.

**Dimostrato/implementato:** rango, kernel saturo, identità di Fourier, positività e convergenza della somma, maggiorante della coda.  
**Aperto:** valutazione numerica certificata della somma completa, settore spaziale canonico, misura completa su D5, identificazione Hua/Bergman e riduzione fisica 3+1D.  
**Aggiornamento di certificazione 9 novembre 2026:** il workflow 42644467074 ha superato 21 test focalizzati; il report `reports/q6_d5_exact_integer_fiber_audit_2026-11-09.json` certifica identità di Smith esatta, kernel saturo di rango 124, quoziente di rango 5, splitting unimodulare con determinante 1, inversa esatta e annullamento esatto. La parte quantitativa resta aperta: per beta=2 e cutoff l1=500 il bound globale ha log-bound 555.23765 (bound circa 1.37×10^241), quindi è finito ma inutilmente largo; non è stata prodotta una finestra certificata utile per la somma completa. Nessuna valutazione esaustiva della fibra 124D è dichiarata.

**Riferimenti:** `docs/Q6_D5_INTEGER_FIBER_QUOTIENT.md`, `docs/Q6_D5_SATURATED_KERNEL_AND_TAIL_BOUND.md`, `docs/Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md`, `reports/q6_d5_exact_integer_fiber_audit_2026-11-09.json`, `src/rgs_q6_d5_*`, issue #84.

## Capitolo 8 — Wilson, marginale, Bergman e Hua: no-go e criterio

La distinzione logica è essenziale:
- T003 esclude l'uguaglianza esatta tra una marginale atomica e una misura assolutamente continua non nulla;
- T004 dimostra una convergenza di somme di Riemann sotto ipotesi;
- T005 stabilisce positività del supporto Wilson a beta finito, non un cutoff duro;
- T006–T007 descrivono quotient e media di Fourier;
- T008 fornisce un criterio sufficiente di convergenza;
- T009 ricava una forma quadratica efficace condizionale.

Nessuno di questi passaggi dimostra automaticamente che la marginale Wilson Q6 converga alla densità Bergman su D5. Per l'applicazione concreta servono la famiglia di misure \(\mu_k\), la mappa flussi→D5, la mesh, gli errori di massa interna ed esterna e la stima uniforme richiesta dal criterio T008.

La derivazione Q6-D5 del capitolo precedente rafforza il settore elettrico, ma non crea da sola la misura di fase-spazio a dieci dimensioni e non determina il cutoff Hua. Il parametro di regolazione non può essere fissato per fitting se il programma richiede una derivazione geometrica.

**Stato:** teoremi locali [P]/[C]; ponte Wilson–Bergman applicato a Q6 [O].  
**Riferimenti:** T002–T009, `open-problems/WILSON_BERGMAN_CONVERGENCE_AUDIT.md`.

## Capitolo 9 — Clifford, Dirac discreto e Nielsen–Ninomiya

Le matrici Clifford soddisfano
\[
\{\Gamma_i,\Gamma_j\}=2\delta_{ij}I.
\]
T015 definisce sul grafo base
\[
D_+=\sum_{i=1}^6\Gamma_i(T_i-I).
\]
Sui caratteri,
\[
D_+(k)=-2\sum_{i:k_i=1}\Gamma_i,\qquad
D_+(k)^2=4|k|I.
\]
È una costruzione finita esatta. Poiché sul cubo booleano \(T_i=T_i^{-1}\), la differenza centrata è identicamente nulla: non va confusa con l'operatore sulla famiglia raffinata.

T017 usa invece
\[
Q_{6,n}^{\rm cyc}=(C_{2n})^{\square6}
\]
e il simbolo centrato \(D_n(p)=i h_n^{-1}\sum_j\Gamma_j\sin p_j\). Il simbolo ingenuo ha 64 corner zeros; il termine di Wilson solleva i 63 corner non centrali. È dimostrato il limite del simbolo a momento fisico fissato con errore dichiarato. Non è dimostrata la convergenza completa di risolventi o il limite interagente gauge.

Nielsen–Ninomiya resta un vincolo per gli operatori che soddisfano le sue ipotesi. Il modello Q6 finito non costituisce un'evasione. La famiglia ciclica di raffinamento è un oggetto distinto dal grafo booleano e da eventuali torri con lato potenza di due.

**Riferimenti:** T014–T020, `open-problems/Q6-T012-T017-COMPATIBILITY-MATRIX.md`, `scripts/verify_nielsen_ninomiya_q6.py`.

---

# PARTE II — GEOMETRIA SPINORIALE E SPETTRALE

## Capitolo 10 — Gruppo binario icosaedrale 2I e quoziente di Poincaré

Il gruppo binario icosaedrale \(2I\) è un sottogruppo finito di SU(2), di ordine 120, che copre il gruppo icosaedrale rotazionale. Il quoziente sferico \(S^3/2I\) è la varietà di Poincaré. La sua analisi richiede rappresentazioni, caratteri, proiettori di Reynolds, decomposizioni in irriducibili e compatibilità con gli operatori differenziali.

I record T026–T045 sviluppano la parte rappresentazionale e la costruzione di blocchi spettrali. Le identità di carattere, le molteplicità di McKay e i certificati matriciali sono risultati algebrici verificabili. La loro estensione a un operatore Rumin completo richiede inoltre dominio, differenziale, condizioni al bordo, normalizzazione e determinanti zeta coerenti.

## Capitolo 11 — Complesso di Rumin, torsione analitica e determinanti

La sequenza T021–T046 costruisce una catena di risultati per l'analisi Rumin sul quoziente icosaedrale: blocchi di grado medio, fattorizzazione polare, matrici Gram, differenziali ridotti, settori di bordo, funzioni zeta di Barnes, determinanti e torsione twistata.

La progressione corretta è:
1. definire il complesso differenziale e le convenzioni;
2. dimostrare l'equivarianza rispetto a 2I;
3. decomporre in rappresentazioni irriducibili;
4. determinare kernel e blocchi armonici;
5. costruire zeta e continuazione analitica;
6. calcolare la parte finita e il determinante;
7. verificare la torsione completa e i twist.

Un'identità di molteplicità non è un calcolo di torsione; un blocco finito non è lo spettro completo; un determinante zeta dipende dalla prescrizione analitica e dalle convenzioni.

**Stato:** diversi lemmi e audit algebrici sono formalizzati nei record T021–T046; ogni risultato va citato al proprio perimetro.  
**Riferimenti:** `src/t032_2i_molien.py`–`src/t046_hadamard_finite_part_determinants.py`, `audits/t025_*`–`audits/t035_*`.

## Capitolo 12 — Quaternioni, SU(2), SO(3) e intertwiners

Il doppio rivestimento \(SU(2)\to SO(3)\) è il ponte standard fra spinori e rotazioni. T063 ne fissa la struttura algebrica; T049C classifica gli intertwiners spaziali per la rappresentazione SU(2) dichiarata. Per due copie dello spin fondamentale,
\[
\operatorname{Hom}_{SU(2)}(\mathbb C^2,\mathbb C^2\oplus\mathbb C^2)
\cong\mathbb C^2,
\]
con isometria quando \(|\alpha|^2+|\beta|^2=1\).

Questo non determina il boost Lorentziano. T049D aggiunge una scelta di estensione Weyl/Lorentz e corregge la convenzione del generatore di boost. Le relazioni di commutazione sono verificate numericamente con le matrici date; la scelta del boost resta un'estensione, non una conseguenza dell'azione spaziale SU(2).

**Riferimenti:** T049C, T049D, T063; audit tecnico `manuscripts/T047_T049D_TECHNICAL_AUDIT.md`.

---

# PARTE III — RGS, PSU E GEOMETRIA DELLO SPAZIO-TEMPO

## Capitolo 13 — Ricostruzione RGS 188D e audit delle coordinate

Il filone 188D comprende coordinate geometriche, vincoli, basi tangenti/normali, Hessiane, proiettori e operatori. Il trasferimento di provenienza registra archivi A13/A14, matrici e report, ma dichiara anche che i binari originali non sono tutti presenti nel repository centrale.

L'audit A14 conferma il rango 4 del Jacobiano dei vincoli e il kernel tangente di dimensione 188 per il dataset e le matrici dichiarati. Non certifica la Hessiana originale 192×192 né lo spettro 29/3/156. Il report recuperato consente di verificare un'identità di equivarianza della mappa geometrica con residuo circa \(1.65\times10^{-14}\), ma la mappa grezza non è contenuta nel kernel del proiettore: il residuo \(\|P_GA-A\|_F\) è circa 6.537. L'estensione polare proiettata nel kernel soddisfa la proprietà per costruzione e non costituisce prova geometrica indipendente.

Il file originale \\(X_{O_h}\\) e il bundle matriciale sono stati recuperati ed è stato eseguito localmente lo script originale con \\(K_0\\) e \\(P_G\\), non con il proxy. Il replay riporta equivarianza antipodale della mappa con residuo \\(1.65\\times10^{-14}\\), ma distanza della mappa grezza dal kernel \\(\\|P_GA-A\\|_F=6.53706\\) e coseno principale minimo \\(0.00265018\\). La mappa geometrica non identifica quindi il kernel 64D. L'estensione polare proiettata ha commutatore \\(1.42\\times10^{-14}\\), ma ciò segue dalla sua costruzione nel kernel e non prova l'identificazione. Il report completo e il bundle di matrici prodotti dal replay non sono ancora committati né verificati in CI clean-checkout: il risultato resta una verifica locale da rendere riproducibile.

**Conclusione:** la ricostruzione 188D è un importante dossier computazionale, ma la certificazione geometrica completa richiede i binari originali, hash, allineamento delle basi, rerun e test indipendenti.  
**Riferimenti:** `docs/RGS_PSU_SOURCE_TRANSFER.md`, `reports/RECOVERY_MANIFEST.md`, `reports/188d_antitwin_audit.json`, `scripts/audit_188d_antitwin.py`, archivio `archive/recovered_188d`.

## Capitolo 14 — PSU, Anti-Twin e simmetria Lorentz

PSU è stato usato nel programma con espansioni terminologiche diverse. La monografia non sceglie arbitrariamente una di esse: il significato operativo deve essere quello fissato dal singolo modello o dal file sorgente. Analogamente, Anti-Twin può indicare:
- l'involuzione cellulare Q6 del capitolo 3;
- una mappa antipodale o geometrica nella ricostruzione 188D;
- un'interpretazione a doppio foglio dello spazio-tempo.

Questi tre oggetti non sono identici finché non è costruita una mappa che li identifichi e ne preservi strutture e operatori. Il recupero 188D mostra che l'equivarianza di una mappa geometrica e l'appartenenza al kernel spettrale sono questioni distinte.

La simmetria Lorentz richiede una rappresentazione del gruppo o dell'algebra di Lie, una metrica di firma dichiarata, una legge di trasformazione dei campi e un'azione o un operatore covariante. Un'involuzione discreta non dimostra da sola l'invarianza Lorentz.

## Capitolo 15 — PRISM: prodotto di cicli e scala 69.120

Il grafo prodotto di riferimento è
\[
G_1=C_{64}\square C_6\square C_6\square C_6\square C_5.
\]
Ha
\[
|V_1|=64\cdot6^3\cdot5=69,120,\qquad
\deg G_1=10,\qquad |E_1|=345,600.
\]
La famiglia piatta di raffinamento implementata è
\[
G_r=C_{64r}\square C_{6r}^{\square3}\square C_{5r},
\]
con \(|V_r|=69,120r^5\), grado 10 e \(|E_r|=345,600r^5\).

La costruzione usa indicizzazione row-major, vicini periodici, enumerazione lazy e simboli di Fourier, evitando di materializzare matrici dense gigantesche. Il test di consistenza del simbolo per modi fissati dà l'errore atteso di ordine \(O(r^{-2})\) rispetto al toro piatto di riferimento.

Il grafo prodotto è una discretizzazione piatta a cinque dimensioni. Non è, senza ulteriori mappe, una varietà curva fisica 3+1D. I numeri storici di cicli, gap e Betti vanno sempre associati alla matrice di incidenza e al complesso preciso che li ha prodotti.

**Riferimenti:** `manuscripts/APPENDICE_TECNICA_MORANDOTTI_RGS_PRISM.md`, T048, `scripts/rgs_prism_product_refinement.py`, `scripts/audit_prism_69120.py`.

## Capitolo 16 — Krist-All: recupero, classi e limiti di provenienza

Il materiale recuperato Krist-All contiene manoscritti e appunti, schemi Merkle/Q-PROOF, figure e un modello separato a 14 siti cubo–ottaedro. Non contiene tuttavia il generatore deterministico e la tabella canonica necessari a riprodurre le 11.725 classi, né una definizione completa della relazione di equivalenza e delle matrici che produrrebbero \(K^3=K^2+I\) e il residuo \(W_0\).

Il modello a 14 siti è un oggetto distinto: il grafo corretto ha 48 archi e non va confuso con la classificazione PRISM/Krist-All. Il manifesto di recupero afferma esplicitamente che le quantità 11.725, \(W_0\simeq5.22\times10^{-16}\) e \(K^3=K^2+I\) restano non certificate dal pacchetto recuperato.

La via per chiudere il filone è concreta: pubblicare relazione di equivalenza, serializzazione canonica, enumeratore, tabella dei rappresentanti, definizioni delle matrici, hash degli input e test indipendente. Fino ad allora i numeri sono risultati storici da recuperare, non invarianti dimostrati.

**Riferimenti:** `reports/KRISTALL_RECOVERY_STATUS.md`, `reports/RECOVERY_MANIFEST.md`, `archive/README.md`.

## Capitolo 17 — FEEC, de Rham cubicale e geometria curvilinea

Il benchmark de Rham/FEEC implementa il complesso tensoriale cubicale di ordine minimo \(Q^-_1\Lambda^k\), con pullback covariante e gradi di libertà integrali sulle facce orientate. L'audit indipendente conferma:
- il coefficiente di bordo cubicale \((-1)^p(2s-1)\);
- la base tensoriale dichiarata, con orientamento ordinato;
- la matrice di massa coerente con il pullback delle k-forme;
- l'assemblaggio globale tramite identificatori di facce;
- la formula del codifferenziale discreto \(\delta_h^k=M_{h,k-1}^{-1}D_{k-1}^TM_{h,k}\).

L'audit corregge una precedente trascrizione errata del segno: il codice usa già il segno standard, quindi non è necessaria una modifica dell'incidenza. Le proiezioni commutanti, la loro limitatezza uniforme e il teorema di approssimazione non risultano implementati nell'audit. Nemmeno Mosco, compattezza, convergenza norm-resolvent o stabilità dei kernel armonici sono dimostrati.

**Riferimenti:** `projects/de_rham_benchmark/docs/INDEPENDENT_MATHEMATICAL_AUDIT.md`, `docs/FEEC_PROJECTIONS.md`, T065, T067.

## Capitolo 18 — Raffinamenti aurei e superaurei: φ e ψ

Il rapporto aureo soddisfa
\[
\varphi^2=\varphi+1,
\]
mentre la costante supergolden è la radice reale positiva di
\[
\psi^3-\psi^2-1=0,\qquad \psi^3=\psi^2+1.
\]
Sono unità algebriche in campi diversi. La loro presenza in una schedulazione di raffinamento può semplificare identità di scala, ma non garantisce stabilità delle proiezioni, compattezza o convergenza delle forme.

La sintesi FEEC mostra identità algebriche esatte e un quadro condizionale. Le condizioni analitiche rimangono quelle FEEC/Mosco: proiezioni commutanti, convergenza degli aggiunti, shape regularity, controllo Jacobiani, stime uniformi e stabilità armonica.

**Riferimenti:** `GOLDEN_SUPERGOLDEN_FEEC_SYNTHESIS.md`, `PHI_PSI_FEEC_SYNTHESIS.md`, T056.

## Capitolo 19 — Mosco e limite geometrico: la soglia decisiva

Per spazi di Hilbert variabili \((H_h,\mathcal E_h)\), la convergenza di Mosco richiede:
1. una nozione precisa di identificazione discreto-continuo;
2. weak-liminf per ogni successione convergente;
3. recovery sequence per ogni elemento del dominio limite;
4. compattezza uniforme quando si vogliono conseguenze spettrali;
5. controllo delle forme di Hodge e dei modi armonici, non soltanto del Laplaciano scalare.

T048 e il benchmark ciclico dimostrano una calibrazione piatta per modi di Fourier fissati. Non dimostrano il caso curvo RGS–PRISM. L'audit tecnico T047–T049D lo ribadisce: non è ancora presente la sequenza curva con mappe di confronto, stime di compattezza e prova M1/M2.

Il limite Laplace–Beltrami–Yang–Mills è quindi un obiettivo aperto. Anche una convergenza forte dei risolventi non implica automaticamente convergenza degli autovalori senza compattezza collettiva e controllo di molteplicità.

**Riferimenti:** T048, `manuscripts/MOSCO_CURVED_CUBICAL_REFINEMENT_OPEN_PROBLEM.md`, `open-problems/EXTERNAL_MATHEMATICAL_VALIDATION_MATRIX.md`.

---

# PARTE IV — CAMPI, GRAVITÀ E FENOMENOLOGIA

## Capitolo 20 — Einstein–Cartan, spin e fluido di Weyssenhoff

Il settore Einstein–Cartan collega torsione algebrica e densità di spin. T047 tratta la scalatura nel modello di fluido di Weyssenhoff sotto ipotesi dichiarate. La continuità dà densità fisica \(n\propto a^{-3}\); con spin per particella conservato e chiusura isotropa locale specificata, \(s^2\propto n^2\propto a^{-6}\). Per la componente \(\rho_s=p_s=-A s^2\), il rapporto è \(w=1\).

Questo risultato è condizionale alla chiusura e non è una derivazione microscopica dal modello RGS–PSU. T049 e T049A–D trattano invarianti e correlatori di spin, ma manca ancora un dataset spinoriale fisico con normalizzazione, trasporto gauge-covariante e prescrizione di rinormalizzazione del contatto.

**Riferimenti:** T047, T049, T049A, T049B, audit tecnico `T047_T049D_TECHNICAL_AUDIT.md`.

## Capitolo 21 — Teleparallelismo, vierbein e azioni scalar–torsion

La formulazione teleparallel richiede un tetrad/coframe e una connessione di spin inerziale coerenti. La torsione dipende dalla coppia tetrad–spin-connection, non dal solo tensore metrico. Vanno distinti:
- connessione Levi-Civita;
- connessione Weitzenböck;
- torsione teleparallel;
- torsione algebrica Einstein–Cartan;
- formulazione covariante con connessione inerziale;
- formulazione pure-tetrad, che può essere dipendente dal frame.

T052 dimostra la variazione scalare per una specifica azione scalar–torsion e sotto la convenzione dichiarata. Non è una soluzione completa delle equazioni tetrad e spin-connection. L'audit critico di FORMULAZIONE corregge un termine variazionale e segnala l'incompatibilità di alcune scelte di tetrad e spin connection nel materiale storico.

La chiusura torsione–Lambda dust-like è fenomenologica, non una derivazione dalle equazioni Einstein–Cartan. Il benchmark Kerr–Schild e i residui di torsione sono verifiche di una costruzione numerica, non evidenza di una soluzione dinamica generale.

**Riferimenti:** T052, T047, `manuscripts/SCALAR_TORSION_VARIATIONAL_IDENTITY.md`, `models/TORSION_LAMBDA_DUST_CLOSURE.md`, `manuscripts/FORMULAZIONE_CRITICAL_AUDIT.md`.

## Capitolo 22 — QLG: interfaccia spinoriale e corrente assiale

Il filone QLG classifica intertwiners spaziali, estensioni Lorentziane e correnti assiali. La decomposizione SU(2) spaziale non fissa da sola la rappresentazione dei boost. T049D corregge la convenzione del generatore di boost per rispettare
\[
[J_i,J_j]=i\epsilon_{ijk}J_k,\quad
[J_i,K_j]=i\epsilon_{ijk}K_k,\quad
[K_i,K_j]=-i\epsilon_{ijk}J_k.
\]
I residui matriciali riportati sono a precisione macchina per le matrici specificate. I boost sono non hermitiani nella base finita e ciò non va descritto come unitarietà.

Per un ponte fisico occorrono un campo spinoriale definito sul complesso, trasporto gauge-covariante, azione fermionica, limite continuo e accoppiamento alla connessione geometrica. Il correlatore assiale non diventa un osservabile fisico finché non sono fissate normalizzazione di Noether, contatto e rinormalizzazione.

## Capitolo 23 — QAT, luce topologica e geometria cubo–sfera

Il modello QAT propone una geometria in cui la sfera inscritta nel cubo, il centro evento, il cono nullo e due fogli geometrici sono usati per interpretare la propagazione luminosa e una possibile struttura topologica. Il linguaggio del toroide/ovaloide, dei quaternioni e delle variabili di mixing può suggerire un programma matematico, ma ogni oggetto deve essere definito come varietà, campo, mappa o operatore.

La verifica deve partire dalle equazioni di Maxwell, dai modi, dalla polarizzazione, dalle condizioni al contorno, dalla dispersione e dalle quantità conservate. La proposta che il tempo rappresenti la velocità di riconnessione dei coni o che la luce abbia la struttura topologica suggerita è [H] finché non si deriva un'equazione del moto e una predizione distinguibile dai modelli standard.

Fonti non standard come Legge del Ritmo ed etere verticale sono oggetti di ricostruzione critica, non premesse fisiche accettate.

**Riferimenti:** `projects/README.md`, `bibliography/quantum-light-foundations`, `bibliography/critical-and-nonstandard`, `manuscripts/FOUR_PDF_CONSOLIDATED_AUDIT.md`.

## Capitolo 24 — Wormhole, modelli EMS e stabilità

Le ansatz statiche sferiche, le coordinate radiali proprie e le equazioni di Klein–Gordon possono essere studiate matematicamente. T054 registra una riduzione radiale statica. Le compilazioni storiche su wormhole, bounce, QNM e stabilità contengono però passaggi non derivati, convenzioni non uniformi e risultati numerici non accompagnati da sorgenti riproducibili.

Un profilo numerico di BVP, un Hessiano finito o un fattore \(e^{-S_E}\) non certificano una soluzione di campo, stabilità fisica o un processo di tunnelling. Occorrono un'unica azione, variazioni complete, condizioni al contorno, controllo delle gauge, convergenza di griglia e analisi spettrale con domini ben definiti.

**Riferimenti:** T054, `manuscripts/FORMULAZIONE_CRITICAL_AUDIT.md`, `manuscripts/FOUR_PDF_CONSOLIDATED_AUDIT.md`.

## Capitolo 25 — Spin glass, correlatori e dinamica cellulare

Il modello spin glass su Q6 è distinto dal gauge SU(2) finché non viene dimostrato un ponte. Le correlazioni microscopiche richiedono una convenzione per spin, unità, volume, media su repliche e contatto. L'identità fra norma della somma degli spin e termini self/pair è algebrica, ma non è automaticamente un operatore quantistico rinormalizzato.

Il programma XCont integra automi cellulari, evoluzione di regole/condizioni iniziali, co-evoluzione a due popolazioni, codifica simbolica di rotazioni e billiard. Sono strumenti computazionali per cercare dinamiche e codifiche; non dimostrano una legge fisica emergente. Ogni benchmark deve separare regole, semi, metriche, baseline e generalizzazione.

**Riferimenti:** T049–T051, `models/prism_cellular_automata.py`, `models/prism_ca_evolution.py`, `models/prism_billiard_coding.py`, `manuscripts/XCONT_EMERGENT_DYNAMICS_INTEGRATION.md`.

## Capitolo 26 — Sincronizzazione topologica, isteresi e applicazioni industriali

T068 implementa modelli NL e NLT sul 2-scheletro cubicale Q6. La campagna multi-seed/multi-rate del 9 novembre 2026 usa cinque semi, 21 valori di accoppiamento, quattro dwell time e lo stesso campione di frequenze per i rami avanti/indietro. I risultati mostrano dipendenza dal rate: nel modello NL alcuni gap diminuiscono molto rallentando lo sweep; nel modello NLT restano separazioni apprezzabili ai tempi di dwell provati. Il risultato è finito e qualitativo: non stabilisce un loop quasi-statico rate-independent o un limite termodinamico.

Va distinta l'isteresi di sincronizzazione (biforcazione/continuazione di ordine) dall'isteresi costitutiva di materiali (relazione ingresso-uscita dipendente dalla storia). Il repository implementa baseline Preisach, Prandtl–Ishlinskii e Bouc–Wen, metriche di area del loop, RMSE e separazione dei rami. Sono benchmark software su segnali sintetici. Jiles–Atherton richiede ancora un comparatore con convenzioni fissate e dati B-H misurati.

Per una validazione industriale servono:
- dataset di materiali/attuatori con metadati e unità;
- split train/validation/test identici per ogni modello;
- protocolli di eccitazione e frequenze di sweep controllati;
- errore di predizione, area/energia del loop e punti di inversione;
- generalizzazione su cicli e condizioni non viste;
- costo computazionale, latenza e robustezza;
- confronto con compensatori industriali e baseline fisiche.

**Risultato attuale:** studio numerico Q6 multi-rate riproducibile; validazione industriale [O].  
**Riferimenti:** T068, `projects/q6_hysteresis_benchmark/RESULTS_2026-11-09.md`, `docs/INDUSTRIAL_HYSTERESIS_DATASETS.md`, `models/constitutive_hysteresis.py`, `models/hysteresis_metrics.py`.

---

# PARTE V — SINTESI E PROGRAMMA DI CHIUSURA

## Capitolo 27 — Una teoria unitaria: requisiti minimi e ordine di lavoro

Una teoria unitaria non si ottiene sommando i nomi RGS, PSU, PRISM, Q6, QLG, QAT, Yang–Mills ed Einstein–Cartan. Deve essere costruita con una sequenza di derivazioni.

### 27.1 Oggetti da fissare una volta sola

1. Spazio discreto, complesso cellulare e famiglia di raffinamento.
2. Coordinate, misure, orientazioni e convenzioni di segno.
3. Spazio delle configurazioni e azione delle simmetrie.
4. Campi indipendenti: coframe, connessione, link gauge, spinori e campi ausiliari.
5. Azione totale e condizioni al contorno.
6. Osservabili, unità e procedura di misura.

### 27.2 Ponti da dimostrare

**Ponte A — Q6 → D5/Wilson.** Il quoziente intero e il peso di fibra sono costruiti. Manca la misura canonica completa e il collegamento con il settore spaziale.

**Ponte B — Q6 → Dirac/QLG.** Gli operatori finiti e le intertwiners sono disponibili. Mancano convergenza gauge-covariante completa, controllo dei modi e identificazione 3+1D.

**Ponte C — PRISM → geometria curva.** Il benchmark piatto è implementato. Manca Mosco curvo, compattezza e convergenza delle forme di Hodge.

**Ponte D — 188D → Anti-Twin geometrico.** Sono stati recuperati dati e identità di equivarianza. Mancano audit fresco dei binari, compatibilità delle basi e dimostrazione indipendente dell'intertwiner geometrico nel kernel richiesto.

**Ponte E — coframe/torsione → gravità.** Esistono identità e modelli scalar–torsion. Manca un'azione completa e una derivazione coerente delle equazioni per tetrad, connessione e materia.

**Ponte F — QAT → elettromagnetismo.** Manca una derivazione da Maxwell e una predizione falsificabile distinta.

**Ponte G — Q6 → isteresi industriale.** Esiste un benchmark di sincronizzazione e un framework di modelli costitutivi. Manca la validazione su dati sperimentali indipendenti.

### 27.3 Priorità operative

1. Completare il recupero e il fingerprint dei binari RGS 188D e riprodurre i risultati da zero.
2. Chiudere la pipeline Q6-D5: enumerazione certificata della fibra, bound di coda, misura e settore spaziale.
3. Consolidare i teoremi T001–T068 in un registro claim→ipotesi→prova→script→test→CI.
4. Costruire la famiglia curva PRISM e affrontare Mosco/FEEC con revisione esterna.
5. Scrivere una specifica QLG con rappresentazioni, operatori e limite distinti.
6. Formulare una sola azione geometrico-gauge-spinoriale, poi variarla integralmente.
7. Testare QAT e i modelli di luce contro Maxwell.
8. Portare l'isteresi su dati industriali misurati e confronti fuori campione.
9. Solo dopo, formulare una sintesi fisica complessiva e sottoporla a revisione indipendente.

### 27.4 Criterio di pubblicabilità

Ogni risultato pubblicabile deve avere: definizione, ipotesi, dimostrazione o protocollo numerico, codice, dati, test, limiti, riferimenti e confronto con letteratura primaria. Le affermazioni fisiche devono produrre osservabili e predizioni. Le affermazioni industriali devono essere valutate su dati e metriche concordate.


### 27.5 — La spina dorsale unitaria: topologia, connessione, difetti, dinamica e limite

L'integrazione dei risultati successivi a T068 non aggiunge una seconda teoria accanto alla monografia: completa il percorso già fissato nei capitoli 1–27. La struttura comune è la seguente:

\[
\boxed{
\text{complesso cellulare}
\to \text{cochain e Hodge}
\to \text{connessioni/olonomie}
\to \text{difetti cinematici}
\to \text{energia elastica}
\to \text{misura/dinamica}
\to \text{risposta e rinormalizzazione}
\to \text{limite continuo}.
}
\]

Ogni freccia indica un'interfaccia matematica da costruire o un risultato già disponibile nel proprio perimetro; non afferma che tutti i modelli fisici siano già derivati da un'unica azione.

**A. Supporto discreto e topologia.** Q6 conserva i 64 esagrammi come siti distinti, 192 archi e 240 facce quadrate del 2-scheletro. La distinzione fra grafo e cubo riempito resta essenziale: il numero ciclico del grafo è 129, mentre il cubo completo è contrattile. T055–T067 forniscono mappe di catena, naturalità, conformità e Stokes per le costruzioni effettivamente specificate; T099 fissa la rete di Kirchhoff e il Gray-torus cinematico; T103–T104 classificano connessioni \(\mathbb Z_2\), cicli, cocicli, flussi e olonomie sul cubo. Questi risultati sono il substrato comune, non una misura di carica fisica.

**B. Campi di fase, cariche e moiré.** T100–T101–T105 costituiscono una sola catena: cariche e correlazioni sui 64 esagrammi; due famiglie di fasi misurate sui due cerchi; sollevamento delle fasi a tutti i 64 siti; ricostruzione dei due campi complessi; interferenza e vettore moiré. Le medie sui soli otto trigrammi non sostituiscono i 64 dati individuali. L'identità di interferenza è esatta una volta dati i campi, ma l'embedding, le ampiezze, le fasi e la legge costitutiva carica–fase richiedono calibrazione. T105 vieta di inferire una legge di carica dal solo conteggio combinatorio.

**C. Connessione e difetti.** T091–T097 uniscono la meccanica di Morandotti al linguaggio geometrico: composizione tensoriale Frank–Burgers con termine misto firmato; trasporto \(SE(2)\); connessione di Cartan; curvatura e torsione; ricostruzione cinematica da gradiente e mismatch strutturato. T096 è un vincolo cruciale: il campo di deformazione simmetrico ricavato da Airy non determina da solo la parte antisimmetrica della distorsione e quindi non identifica univocamente la chiusura di Burgers. Per estrarre olonomie dai dati FEM occorre una variabile cinematica indipendente (spostamento/distorsione plastica), una microrotazione con legge costitutiva, oppure un problema di gauge/recovery esplicitamente posto.

Il significato fisico delle quattro quantità deve rimanere separato:
- winding di fase su un plaquette;
- chiusura traslazionale/Burgers;
- olonomia rotazionale/Frank;
- flusso magnetico \(\mathbb Z_2\) di T103–T104.

Una mappa fra esse è un teorema ulteriore, non una convenzione di nomenclatura. T106 chiarisce inoltre che un vettore reciproco calibrato e un ordine traslazionale sono necessari per inferire Burgers; un campo di orientazione locale e la simmetria del reticolo sono necessari per inferire Frank.

**C1. Sorgente di Frank–Read: soglia, geometria del difetto e dinamica vincolata.** T124 aggiunge il livello di attivazione della dislocazione al settore Frank–Burgers, senza sostituire la ricostruzione cinematica già formalizzata. Nel modello circolare a tensione di linea costante,
\[
\tau_c=\frac{2T}{bL}.
\]
Con la convenzione specifica \(T\simeq Gb^2/2\), segue \(\tau_c\simeq Gb/L\); la formula \(2Gb/L\) richiede una diversa convenzione per \(T\). Questa soglia è un risultato del modello ridotto, non una soglia universale indipendente dal carattere della dislocazione, dal core e dai pinning.

Il collegamento ai risultati già verificati è il seguente:

1. **T091 — interazione tensoriale Frank–Burgers.** Fornisce la decomposizione dei settori Frank, Burgers e del termine misto firmato, con identità tensoriali e sensibilità variazionale nel perimetro dichiarato.
2. **T092–T095 — geometria locale, trasporto \(SE(2)\) e Cartan.** Forniscono la descrizione ordinata della chiusura traslazionale e rotazionale; T096 impedisce di ricavare Burgers dalla sola deformazione simmetrica di Airy.
3. **T097–T098 — ricostruzione cinematica e dualità dei due cerchi.** Collegano gradiente, mismatch strutturato, frame rotazionale e covarianza baricentrica, sotto le ipotesi dei rispettivi record.
4. **T099 — ricostruzione bicircolare/annulare e raffinamento.** Fornisce una pipeline di misura della deformazione e dei residui; il replay a cinque esperimenti è manufactured-data, non validazione su un cristallo.
5. **T124 — Frank–Read.** Aggiunge il criterio di instabilità del segmento vincolato e identifica ciò che manca per passare dalla soglia al loop emesso: legge di evoluzione della curva, regola di cutting/reconnection e rigenerazione della sorgente.

**Azioni GitHub già eseguite e verificate nel ramo Morandotti:** [PR #161 audit](https://github.com/fabianleonaressi95/theorem/pull/161), con [run 43051485760](https://github.com/fabianleonaressi95/theorem/actions/runs/43051485760), verifica la decomposizione dei salti di trazione Frank/Burgers e il termine misto; [PR #162 raffinamento](https://github.com/fabianleonaressi95/theorem/pull/162), con [run a cinque livelli 43052448456](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448456) e [audit base 43052448351](https://github.com/fabianleonaressi95/theorem/actions/runs/43052448351), verifica la pipeline DOLFINx a cinque scale e conserva report e campi FE. Queste esecuzioni verificano la decomposizione e la pipeline di ricostruzione Morandotti; **non** verificano direttamente la soglia Frank–Read, il cutting/reconnection, la convergenza continua o la fisica del core.

Le azioni dedicate [T096](../.github/workflows/t096-airy-holonomy-identifiability.yml) e [T097](../.github/workflows/t097-barycentric-kinematic-law.yml) costituiscono ulteriori gate riproducibili: la prima controlla la non-identificabilità da Airy strain, la seconda le identità della ricostruzione cinematica. [T094](../.github/workflows/t094-se2-holonomy-audit.yml) è invece un workflow specifico per olonomie Cartan/\(SE(2)\), il cui stato di esecuzione va controllato separatamente prima di chiamarlo verificato.

La catena multiscala da chiudere è
\[
\text{core atomistico/DFT}
\to (E_{\rm core},\,V_{\rm Peierls})
\to (T_{\rm line},\,\text{mobilità})
\to \text{curva vincolata}
\to \text{loop Frank–Read}
\to \text{densità e interazione dei difetti}.
\]
Il passaggio DFT→parametri efficaci richiede una procedura di coarse-graining; l'eventuale tunnelling quantistico richiede un'azione efficace e un tasso di transizione calcolato, non segue dalla soglia classica. La corrispondenza con il gas vettoriale KTHNY richiede inoltre di estrarre Burgers, energia di core e fugacità da un modello elastico 2D calibrato.

**C2. Interfaccia variazionale Q6/PRISM–Frank–Read (T125).** T125 formalizza il livello successivo senza trasformare il supporto combinatorio in una legge materiale. Su un grafo finito embedded nel piano di scorrimento, con etichette di Burgers in un reticolo dichiarato, l'energia di linea più core e lavoro esterno produce per variazione prima un bilancio nodale esatto. Per un flusso gradiente autonomo con mobilità positiva segue inoltre la dissipazione monotona dell'energia. L'aggiunta di un ciclo chiuso conserva il contenuto agli estremi, ma non definisce l'istante né la regola di cutting/reconnection: serve una mappa di evento separata che rispetti orientazione e carica di Burgers e rigeneri la sorgente.

Il collegamento operativo è: **Q6/PRISM** fornisce una possibile struttura d'incidenza; **T091 e le Actions Morandotti** forniscono una ricostruzione indipendentemente verificata dei salti di trazione; **T096–T099** delimitano l'identificabilità cinematica; **T124** fornisce la soglia circolare ridotta; **T125** specifica energia, prima variazione e flusso dissipativo per una rete a topologia fissata. L'embedding fisico, il reticolo di Burgers, tensione, core, mobilità e pinning restano input da calibrare. Le Actions 43051485760, 43052448456 e 43052448351 non sono test del modello di linea T125 né della riconnessione.

**Classificazione T125:** identità di variazione prima e dissipazione [P, per grafo finito e modello dichiarato]; dati materiali e scelta costitutiva [M]; derivazione da Q6/PRISM, limite Γ e convergenza dell'evoluzione [O]; emissione Frank–Read e topological update [O]. Il risultato chiude la specifica variazionale a topologia fissa, non la dimostrazione della moltiplicazione Frank–Read.


**Classificazione integrata:** soglia circolare T124 [P, condizionata al modello]; decomposizione/ricostruzione Morandotti [P/N secondo i singoli record e le Actions citate]; parametro materiale e dinamica completa [M/O]; limite RGS–PRISM e raccordo KTHNY [O].

**D. Statistica, FDT e trasporto.** T100, T105, T106 e T107 sono il livello dinamico dello stesso sistema: correlazioni complete \(64\times64\), correnti sui 192 archi, continuità di Kirchhoff, ensemble stazionario, risposta a campo debole e verifica indipendente della relazione Kubo/FDT. Il teorema Born/Haar in T106 dà una misura uniforme sul simplesso per stati puri complessi Haar; non dà una dinamica termica. Il modello Gibbs/diffusione reversibile di T107 è una realizzazione statistica distinta e dichiarata. La formula Green–Kubo richiede corrente fisica, unità, normalizzazione areale/volumica, ipotesi di equilibrio e controllo della convergenza; il Green operator del grafo non è l'integrale Green–Kubo.

**E. KTHNY: limite termodinamico dei difetti bidimensionali.** KTHNY è la teoria di riferimento per la fusione 2D mediata da difetti. Nel regime triangolare e nelle ipotesi in cui lo scenario a due transizioni è valido, l'unbinding delle coppie di dislocazioni porta dal solido alla fase esatica; l'unbinding successivo delle disclinazioni porta al liquido isotropo. Il gas di Coulomb vettoriale di Young conserva sia interazioni radiali sia angolari. Con la convenzione standard
\[
K=\frac{Y a^2}{k_B T},
\]
il criterio alla soglia di unbinding delle dislocazioni è
\[
K_R=16\pi,
\]
dove \(K_R\) è la rigidità di Young **rinormalizzata**; non è un valore universale del modulo elastico nudo. Fugacità, energia di core, anisotropia, substrato e interazioni possono modificare o pre-emptare lo scenario semplice.

La connessione già contenuta in T106 è quindi sostanziale: T091–T097 forniscono i settori cinematici Frank/Burgers e il benchmark elastico; T100–T107 forniscono correlazioni, risposta e test FDT; KTHNY fornisce il quadro RG termodinamico nel quale verificare proliferazione, screening e perdita degli ordini traslazionale/orientazionale. Non si assume che Q6 abbia già una transizione KTHNY: occorrono una geometria 2D calibrata, energia di core, fugacità, interazione difetto-difetto e flusso RG misurati o derivati.

Gli operatori Wilson–'t Hooft sono classificati da cariche elettriche e magnetiche (dipendenti dal gruppo di gauge e dalla sua forma globale). Il parametro complesso di accoppiamento è
\[
\tau_{\rm YM}=\frac{\theta}{2\pi}+\frac{4\pi i}{g_{\rm YM}^2},
\]
e la trasformazione S agisce come \(\tau_{\rm YM}\mapsto-1/\tau_{\rm YM}\) nel caso autoduale, con la corrispondente trasformazione del gruppo di gauge nella formulazione generale.

Il collegamento più concreto con il programma non è il numero sei del cubo, ma il **toro**. Harvey–Moore–Strominger studiano la compactificazione di \(D=4,\ \mathcal N=4\) Yang–Mills su \(T^2\): nel limite infrarosso la teoria efficace è descritta da una SCFT bidimensionale con struttura orbifold proposta, e la dualità \(S\) si traduce nella dualità \(T\), scambiando stati elettrici/magnetici con settori di momento/avvolgimento. Questo offre un'interfaccia naturale con i tori PRISM, i cicli Q6 e il gas di cariche KTHNY.

La corrispondenza da costruire è precisa: identificare il reticolo di Burgers e quello delle cariche angolari/Frank, la forma quadratica d'interazione del gas di Coulomb, le fugacità e le dimensioni di scala degli operatori di difetto; confrontarli con i settori momento/avvolgimento e gli operatori di vertice della SCFT toroidale. La mappa deve preservare forma bilineare, regole di fusione/OPE e funzioni di partizione o correlatori. Occorre inoltre tenere distinti il parametro di accoppiamento \(\tau_{\rm YM}\), il parametro complesso di struttura del toro \(\tau_{T^2}\) e la rigidità elastica KTHNY \(K_R\): non sono la stessa variabile e non si identifica \(K_R\) con \(\operatorname{Im}\tau_{\rm YM}\) senza una derivazione. Solo se questa mappa è costruita si potrà identificare il gas vettoriale dei difetti KTHNY con un settore di cariche/momento-avvolgimento della teoria efficace toroidale. Per ora è un programma di confronto, non un'equivalenza dimostrata.

La distinzione già esplicitata in T102 è vincolante: la supersimmetria cubicale del complesso de Rham/Hodge di Q6 è una supersimmetria finito-dimensionale di meccanica quantistica; **non** costruisce il multipletto, l'algebra, la dinamica conforme o la dualità di \(\mathcal N=4\) SYM. Le sei direzioni del cubo non sono automaticamente i sei scalari aggiunti di SYM. Per un embedding in SYM servono connessione \(SU(N)\), sei scalari aggiunti, quattro fermioni di Weyl, trasformazioni supersimmetriche, algebra di chiusura, simmetria \(SU(4)_R\) e controllo del limite.

### 27.6 — Diagramma delle interfacce e obblighi di prova

\[
\begin{array}{c}
\text{Q6 / PRISM: celle, cicli, cochain, Hodge}\
\downarrow\
\text{campi di fase, link gauge, connessione }SE(2)\
\downarrow\
\text{cariche per esagramma, moiré, olonomie}\
\downarrow\
\text{Burgers / Frank / torsione / curvatura}\
\downarrow\
\text{Morandotti: incompatibilità, Airy, KKT, C0-IPDG}\
\downarrow\
\text{Gibbs, FDT, Kubo/Green--Kubo}\
\downarrow\
\text{KTHNY: gas vettoriale, fugacità, RG, melting 2D}
\end{array}
\qquad
\begin{array}{c}
\mathcal N=4\text{ SYM in 4D}\
\downarrow\
\text{compactificazione su }T^2\
\downarrow\
\text{SCFT 2D / reticolo momento-avvolgimento}\
\downarrow\
\text{confronto di dualità con il settore toroidale}\
\updownarrow\
\text{PRISM / cicli Q6 / gas di cariche KTHNY}
\end{array}
\]

Il diagramma a destra incontra quello a sinistra nel settore toroidale e nel linguaggio dei reticoli di carica; non autorizza una freccia di equivalenza senza la mappa di cui sopra.

Obblighi prioritari:
1. congelare la convenzione dei sei bit e il pairing inferiore/superiore, mantenendo i 64 esagrammi;
2. collegare T101/T105 a misure reali dei due campi e alle correnti del circuito;
3. ricostruire indipendentemente spostamento/distorsione e orientazione per estrarre Burgers e Frank dai campi Morandotti;
4. derivare energia di core, fugacità e interazione del gas di difetti e confrontare il flusso RG con KTHNY;
5. validare FDT confrontando correlazioni e risposta debole indipendente;
6. definire il toro fisico e il reticolo di cariche, poi confrontare il settore KTHNY con il reticolo momento-avvolgimento della SYM compactificata;
7. solo dopo, formulare un'azione efficace comune e provarne simmetrie, positività/stabilità, limiti e osservabili.

### 27.7 — Registro integrato dei teoremi T091–T109

| Record | Ruolo nel programma unitario | Stato da conservare |
|---|---|---|
| T091 | Composizione tensoriale Frank–Burgers e termine misto | Identità finite provate; benchmark numerico a due core; limite/legge costitutiva aperti |
| T092–T094 | Geometria a due cerchi, trasporto \(SE(2)\), Cartan e audit | Teoremi locali/identità; audit numerico; estrazione da core FEM e limite singolare aperti |
| T096 | Non-identificabilità della chiusura Burgers dai soli dati Airy simmetrici | Proposizione provata e witness numerico |
| T097–T099 | Ricostruzione cinematica, barycentri, bicircolare e rete | Identità/risultati condizionali; calibrazione fisica e convergenza da completare |
| T100–T101 | Cariche individuali, correlazioni, moiré e fasi sui 240 plaquette | Identità di grafo e definizioni; embedding e dati fisici aperti |
| T102 | Supersimmetria cubicale e heat supertrace | Risultato finito esatto; distinto da \(\mathcal N=4\) SYM |
| T103–T104 | Connessione magnetica \(\mathbb Z_2\), cicli/cocicli e olonomie | Classificazione finita provata; interpretazione fisica aperta |
| T105 | Legge circuito–carica–moiré sui 64 siti | Identità di circuito/interferenza; legge costitutiva da misurare |
| T106 | Born/Haar, FDT, difetti e raccordo KTHNY | Teoremi di misura e Kubo standard; ponte fisico condizionale |
| T107 | Modello Gibbs reversibile, FDT e test preregistrati Frank/Burgers | Modello matematico definito; interpretazione materiale aperta |
| T108–T109 | Influenze booleane, Laplaciano Qn e confronto AA | Identità Fourier/Laplaciane provate; non equivalgono a una legge fisica dei difetti |
| T110 | XY su toro 2D/3D, winding, vortici e confronto KTHNY | Identità di reticolo esatte; simulazione finita e transizioni da verificare |

I record T001–T110 sono una rete di dipendenze, non una lista di teoremi tutti dello stesso rango. Ogni record conserva la propria classificazione [E]/[P]/[N]/[C]/[M]/[H]/[O]. In particolare T108–T109 sono un ramo matematico sul cubo booleano: la loro vicinanza a Q6 e alla congettura Aaronson–Ambainis non li trasforma in una dinamica di cariche o in una legge KTHNY.

### 27.8 — Risultati preesistenti da riutilizzare, non riscoprire

Il lavoro precedente contiene già oggetti denominati \(R_0,R_1,R_2\) come mappe di catena di dimensioni registrate rispettivamente \(64\times12\), \(192\times21\), \(240\times10\), con \(R_2=0\) nella costruzione degenerata e identità di commutazione registrate nell'audit storico. Vanno recuperati i file e le convenzioni originali prima di riutilizzarli; non vanno sostituiti con nuove mappe né dichiarati canonici o face-preserving senza verifica. Questo uso dei simboli non va confuso con il dossier radiale del wormhole: lì \(r_*\simeq0.9907068184\), \(R_0\simeq2.7178138074\), \(r_1\simeq1.089778\), \(r_2\simeq1.981414\); il parametro maiuscolo \(R_1\) non è stato determinato e non va identificato con \(r_1\).

### 27.9 — Riferimenti primari per i due raccordi fisici

**KTHNY / melting 2D**
1. D. R. Nelson and B. I. Halperin, “Dislocation-mediated melting in two dimensions,” *Phys. Rev. B* 19 (1979), 2457. DOI: [10.1103/PhysRevB.19.2457](https://doi.org/10.1103/PhysRevB.19.2457).
2. A. P. Young, “Melting and the vector Coulomb gas in two dimensions,” *Phys. Rev. B* 19 (1979), 1855. DOI: [10.1103/PhysRevB.19.1855](https://doi.org/10.1103/PhysRevB.19.1855).
3. J. M. Kosterlitz, “Kosterlitz–Thouless physics: a review of key issues,” *Rep. Prog. Phys.* 79 (2016), 026001. DOI: [10.1088/0034-4885/79/2/026001](https://doi.org/10.1088/0034-4885/79/2/026001).

**\(\mathcal N=4\) SYM / dualità / torus**
4. J. A. Harvey, G. Moore, A. Strominger, “Reducing S duality to T duality,” *Phys. Rev. D* 52 (1995), 7161–7167. DOI: [10.1103/PhysRevD.52.7161](https://doi.org/10.1103/PhysRevD.52.7161), arXiv:[hep-th/9501022](https://arxiv.org/abs/hep-th/9501022).
5. A. Kapustin, “Wilson–’t Hooft operators in four-dimensional gauge theories and S-duality,” *Phys. Rev. D* 74 (2006), 025005. DOI: [10.1103/PhysRevD.74.025005](https://doi.org/10.1103/PhysRevD.74.025005).
6. A. Kapustin and N. Saulina, “The algebra of Wilson–’t Hooft operators,” *Nucl. Phys. B* 814 (2009), 327–365. DOI: [10.1016/j.nuclphysb.2009.02.004](https://doi.org/10.1016/j.nuclphysb.2009.02.004).
7. J. Gomis and T. Okuda, “S-duality, ’t Hooft operators and the operator product expansion,” *JHEP* 09 (2009), 072. DOI: [10.1088/1126-6708/2009/09/072](https://doi.org/10.1088/1126-6708/2009/09/072).
8. Y. Hatsuda and T. Okazaki, “S-duality of boundary lines in \(\mathcal N=4\) SYM theories and supersymmetric indices,” *JHEP* 08 (2025), 127. DOI: [10.1007/JHEP08(2025)127](https://doi.org/10.1007/JHEP08(2025)127).

La nota [KTHNY_N4_SYM_RGS_PRISM.md](../docs/KTHNY_N4_SYM_RGS_PRISM.md) va letta come appendice bibliografico-tecnica di questo capitolo, non come teoria autonoma. Il testo canonico è questa monografia e i theorem record richiamati.

### 27.10 — XY su tori: BKT in 2D e loop di vortice in 3D

Il controllo XY è separato dal modello Gibbs/FDT di T107 nel record [T110](../theorems/T110-xy-torus-vortex-kthny-bkt.md), con implementazione in scripts/audit_xy_torus_kthny_bkt.py. Sul toro 2D, il winding di plaquette è una carica intera globalmente neutra; i due winding armonici sui cicli non contrattibili sono dati distinti. La transizione BKT si diagnostica tramite la rigidità di elicità rinormalizzata, con salto universale \\(\\Upsilon_R/(k_BT)=2/\\pi\\), non identificando il correlatore firmato delle cariche con il potenziale logaritmico.

Nel toro 3D, i winding delle tre famiglie di plaquette diventano flussi sui link del reticolo duale, con divergenza discreta nulla e supporto in reti di loop chiuse. Il caso \\(C_4^3\\) è il controllo combinatorio a 64 siti; il caso 2D \\(C_4^2\\) è il controllo di sezione/quotiente. Nessuno dei due è automaticamente una geometria materiale calibrata.

**Separazione fisica essenziale:** BKT è il riferimento XY 2D a vortici scalari; KTHNY è il melting di un cristallo 2D attraverso dislocazioni vettoriali e disclinazioni, con \\(K_R=16\\pi\\) alla soglia di unbinding delle dislocazioni. Il modello XY 3D ha proliferazione di loop e non riceve la soglia KTHNY 2D. Il raccordo con Burgers/Frank richiede quindi un modello elastico 2D autonomo e dati di calibrazione; T110 non identifica vortici XY, cariche dei 64 esagrammi, Burgers, Frank e flusso \\(\\mathbb F_2\\) di T104.

---

# APPENDICE A — Registro dei risultati e dei riferimenti canonici

| Area | Record principali | File eseguibili/documentali | Stato sintetico |
|---|---|---|---|
| Q6 grafo e Dirac | T015–T017 | `scripts/verify_q6_laws.py`, `scripts/verify_nielsen_ninomiya_q6.py` | identità finite; limite completo aperto |
| Gauge e baryon | T012–T014, T020 | `scripts/t020_gauge_covariant_q6_audit.py` | covarianza; dinamica QCD aperta |
| Q6-D5 Wilson | T003–T009 e note D5 | `src/rgs_q6_d5_*`, `scripts/run_q6_d5_*` | kernel e formula esatti; misura completa aperta |
| 2I/Rumin | T021–T046 | `src/t032_*`–`src/t046_*`, `audits/t025_*`–`t035_*` | risultati algebrici/spettrali per perimetro |
| RGS 188D | A14, recovery manifest | `scripts/audit_188d_antitwin.py`, `reports/188d_antitwin_audit.json` | recupero parziale; rerun completo pendente |
| PRISM | T048, audit 69,120 | `scripts/rgs_prism_product_refinement.py`, `scripts/audit_prism_69120.py` | prodotto piatto; curva aperta |
| FEEC/de Rham | T055, T065, T067 | `projects/de_rham_benchmark/` | complesso/massi coerenti; proiezioni e Mosco aperti |
| EC/spin | T047, T049–T052 | `scripts/ec_spin_fluid_scaling.py`, correlatori | chiusure condizionali |
| QLG | T049C–T049D | `scripts/q6_qlg_dirac_intertwiner.py`, `scripts/q6_qlg_dirac_lorentz_chirality.py` | algebra finita; embedding fisico aperto |
| QAT/luce | bibliografia e note critiche | `bibliography/quantum-light-foundations/` | ipotesi da confrontare con Maxwell |
| Isteresi | T068 | `scripts/run_q6_hysteresis_sweep_study.py`, `models/constitutive_hysteresis.py` | benchmark multi-rate; dati industriali mancanti |
| XCont/CA | note XCont | `models/prism_cellular_automata.py`, `models/prism_ca_evolution.py` | strumenti computazionali |
| Frank–Burgers / Morandotti | T091–T099 | record T091–T099; `docs/rgs_defect_benchmark/` | identità finite, benchmark numerici e ponti cinematici condizionali |
| Frank–Read / dislocation activation | T091–T099, T124 | `theorems/T124-frank-read-source-line-tension-atomistic-core.md`; PR #161/#162 Actions; DOLFINx two-core reports | soglia circolare [P condizionata]; decomposizione e ricostruzione numeriche verificate; cutting, core, evoluzione e limite continuo [O] |
| Moiré, cariche, FDT e difetti | T100–T107 | records T100–T107; `scripts/audit_t103*`, `tests/test_t103*` | identità Q6 esatte; calibrazione fisica, dinamica e embedding aperti |
| Influenze booleane e AA | T108–T109 | records T108–T109 | identità Fourier/Laplaciane; teorema AA dimension-uniforme distinto |
| XY/BKT e vortici 3D | T110 | scripts/audit_xy_torus_kthny_bkt.py, tests/test_xy_torus_kthny_bkt.py | identità di winding/chiusura; scaling critico ancora da eseguire |
| KTHNY | Nelson–Halperin; Young; T106 | capitolo 27.5 e bibliografia primaria | teoria standard 2D; applicazione al sistema Q6/Morandotti condizionale |
| \(\mathcal N=4\) SYM | Harvey–Moore–Strominger; Kapustin; T102 | capitolo 27.5 e nota bibliografica subordinata | dualità/linee e compactificazione toroidale; mappa verso KTHNY/Q6 aperta |

## Registro completo dei theorem record

Il registro canonico è la directory [theorems](../theorems/). I record T001–T068 non sono omogenei per natura: alcuni sono teoremi classici applicati sotto ipotesi, altri lemmi nuovi, audit, costruzioni numeriche o risultati condizionali. Il singolo record governa sempre l'enunciato e il livello di prova. Le duplicazioni di numerazione (ad esempio due T010, T021, T024, T030, T032, T033, T034 e T045 con soggetti distinti) sono mantenute come identificatori storici e vanno risolte in un indice univoco senza rinumerare i riferimenti già citati.

## Appendice B — Fonti non standard e materiale storico

I PDF esplorativi e le fonti non standard sono conservati per provenienza e ricostruzione critica. L'audit di quattro PDF e quello di FORMULAZIONE mostrano che alcune narrazioni contenevano errori variazionali, convenzioni incompatibili o conclusioni fisiche non supportate. Il materiale valido viene estratto in note ristrette e theorem record; il resto rimane quarantinato.

Non si cancellano risultati negativi, correzioni o no-go. Sono parte integrante della storia scientifica del programma.

---

**Dichiarazione finale.** Questa monografia è la sintesi di orientamento e dipendenze del repository al 9 novembre 2026. Non sostituisce i record matematici originali e non certifica automaticamente i risultati numerici riportati in archivi non riprodotti. Il suo scopo è rendere possibile una prosecuzione cumulativa, verificabile e scientificamente onesta del programma RGS–PSU–PRISM–Q6–QLG.


---

# Appendice di programma — Tre gas di difetti e ponte QLG–N=4 SYM–stringhe

Il dossier operativo [Three defect gases and QLG–RGS–N=4 SYM–IIB bridge](../docs/THREE_DEFECT_GASES_QLG_N4_IIB_BRIDGE.md) sviluppa tre calcoli separati:

- **BKT 2D:** vortici scalari, fugacità e flusso della rigidità di fase; criterio rinormalizzato \(\Upsilon_R/(k_BT)=2/\pi\).
- **XY 3D:** flussi vorticosi interi sul reticolo duale, chiusura esatta, omologia delle reti e distribuzione delle lunghezze con convenzione esplicita.
- **KTHNY 2D:** gas vettoriale di Burgers, settore separato di Frank, kernel elastico derivato e criterio \(Y_Ra^2/(k_BT)=16\pi\).

Questi tre settori sono collegati alla geometria Q6/QLG solo tramite mappe esplicite. La catena verso \(\mathcal N=4\) SYM e stringhe IIB è un programma di derivazione: T102 resta una supersimmetria cubicale finita, non una costruzione di SYM; AdS/CFT è il ponte consolidato della teoria standard, mentre l'embedding RGS/QLG è aperto.

**Gate di accettazione:** definizioni e normalizzazioni; derivazione o approssimazione dichiarata; codice e dati riproducibili; controlli di taglia finita/incertezza; criteri di falsificazione. Nessun esponente, punto critico o dualità QLG–stringhe viene assunto in anticipo.


## Appendice — Estensione QHD–Euler–MHD e flussi vorticosi

Il dossier centrale è stato esteso con il ponte tra idrodinamica quantistica (Madelung/Gross–Pitaevskii), vorticità di Euler, flusso magnetico MHD, superconduttori di tipo II e QHD dei plasmi. Il nucleo comune è la geometria dei flussi, delle circolazioni, delle classi di omologia e delle leggi di trasporto; non si identificano però vortici neutri, linee di vorticità classiche e tubi di flusso magnetico. La quantizzazione del flusso magnetico richiede il condensato carico e l'accoppiamento gauge.

Il programma di verifica comprende: confronto T110–Gross–Pitaevskii sotto raffinamento; conservazione di Kelvin e Alfvén nei rispettivi regimi ideali; riconnessione quantistica e magnetica; benchmark Ginzburg–Landau/London; estensione a modelli QHD multi-specie con termine di Bohm e legge di Ohm generalizzata. Le equazioni, le unità e le condizioni di validità sono registrate in `docs/THREE_DEFECT_GASES_QLG_N4_IIB_BRIDGE.md`, §VI.
