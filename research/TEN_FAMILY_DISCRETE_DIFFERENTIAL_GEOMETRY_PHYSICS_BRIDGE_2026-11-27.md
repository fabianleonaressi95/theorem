# Ponte delle dieci famiglie: geometria differenziale discreta e fisica
## RGS / Q6 / PSU / Anti-Twin / PRISM / QLG — 27 novembre 2026

**Tesi organizzativa.** Le dieci famiglie sono componenti di un unico sistema matematico: un complesso cellulare orientato e metrizzato, dotato di cochain, Hodge, trasporto di gauge, coframe, connessione indipendente, curvatura, torsione, rappresentazioni di materia, azione e confronto con il limite continuo. Non sono dieci teorie separate e non vengono ridotte a un unico teorema.

**Legenda:** [E] identità finita esatta; [P] teorema dimostrato sotto ipotesi; [N] audit numerico; [L] risultato della letteratura; [C] ponte condizionale; [H] ipotesi fisica; [O] problema aperto.

## 1. Le dieci famiglie, con identificatori stabili

| ID | Famiglia | Funzione nel sistema comune |
|---|---|---|
| F-Q6 | Q6 / Kirchhoff / esagrammi | carrier finito, incidenza e operatori cellulari |
| F-GOLDEN | cut-and-project / φ | split fisico-interno, generatrici e finestra |
| F-IVM | IVM / FCC / geometria icosaedrica | sistemi di direzioni spaziali e confronto di simmetrie |
| F-CELL | topologia cellulare / Anti-Twin / vesica | orientazioni, catene, involuzioni e due fogli |
| F-REP | rappresentazioni / Clifford / 2I / Rumin | fibre interne, spinori e vincoli spettrali |
| F-SPACETIME | RGS / PSU / Cartan / Lorentz | coframe, metrica, connessione, curvatura e torsione |
| F-ANALYSIS | FEEC / Hodge / Mosco / spettro | stabilità e convergenza al continuo |
| F-DYNAMICS | PRISM / QLG / MHD / sincronizzazione | trasporto, evoluzione, fase e fluidi |
| F-ARITH | φ, ψ, eta, zeta, McKay | coefficienti algebrici e molteplicità spettrali |
| F-MORPH | morfodinamica / deformazioni / difetti | gradienti, baricentri, strain e risposta materiale |

Il comune denominatore non è una simmetria decorativa: è la geometria differenziale discreta, che fornisce gli oggetti su cui le dieci famiglie possono agire.

## 2. Base cellulare e Hodge discreto

Sia K_h un complesso cellulare orientato. Le cochain C^k(K_h;V) sono assegnate alle celle orientate di dimensione k. Il coboundary d_h^k soddisfa esattamente

\[
d_h^{k+1}d_h^k=0.
\]

Questa è la struttura algebrica di base, indipendente dalla metrica. Una geometria richiede inoltre matrici di massa/Hodge M_{h,k}, positive e costruite dalla realizzazione geometrica, da una dualità o da uno spazio FEEC. L'aggiunto è

\[
\delta_h^{k+1}=M_{h,k}^{-1}(d_h^k)^T M_{h,k+1},
\qquad
\Delta_{h,k}=d_h^{k-1}\delta_h^k+\delta_h^{k+1}d_h^k.
\]

I pesi di M_{h,k} non possono essere scelti per far comparire uno spettro desiderato: devono discendere dalla geometria e dalla scala della discretizzazione.

**Distinzione Q6 obbligatoria.** Il grafo Q6 ha 64 vertici, 192 spigoli, grado 6 e 240 quadrati. Il numero β₁=129 è il rango ciclico del grafo 1-scheletro; non è il primo Betti del 2-scheletro cubicale riempito. Ogni calcolo topologico deve specificare il complesso e le matrici di bordo usate. Il cubo a sei dimensioni non è automaticamente una discretizzazione dello spaziotempo 4D.

## 3. Trasporto di gauge e olonomie

A ogni spigolo orientato e=(v,w) si assegna U_e in un gruppo G, con U_{\bar e}=U_e^{-1}. Sotto una trasformazione ai vertici g_v,

\[
U_{(v,w)}\mapsto g_v U_{(v,w)}g_w^{-1}.
\]

Per una faccia f, il prodotto ordinato lungo il bordo U_f trasforma per coniugio al vertice base; quindi tr(U_f) è gauge-invariante. Nel regime di facce piccole e connessione regolare, U_f è l'esponenziale del flusso di curvatura attraverso la faccia, con errori dipendenti dalla regolarità e dalla mesh. Questo è il ponte comune per U(1), SU(2), QLG, PSU–Anti-Twin e le future connessioni di Lorentz.

Per Anti-Twin restano esatte le identità già registrate:
\[
J_{\rm AT}=I\otimes\tau_1,\quad J_{\rm AT}^2=I,\quad
Q=q_0\tau_3,\quad J_{\rm AT}QJ_{\rm AT}^{-1}=-Q,
\]
e U_e^{(-)}=(U_e^{(+)})^* nel caso U(1). Lo scambio di foglio non è torsione di Cartan.

## 4. Il ponte Cartan mancante

Per la fisica gravitazionale occorre un vero complesso cellulare 4D K_h^(4), non soltanto il grafo Q6. Su di esso servono:

1. coframe discreto e_e, con vettori orientati riferiti a frame locali;
2. trasporti indipendenti Λ_e in SO⁺(1,3), o loro sollevamenti in Spin⁺(1,3);
3. metrica indotta e non-degenerazione del coframe;
4. campi di materia e gauge nelle rappresentazioni appropriate.

Per una faccia f, la curvatura discreta è misurata dall'olonomia lorentziana

\[
R_f=\overrightarrow{\prod_{e\subset\partial f}}\Lambda_e^{\epsilon(f,e)}.
\]

La torsione discreta deve invece misurare il difetto di chiusura del coframe dopo aver trasportato tutti i vettori nello stesso frame. Uno schema possibile è

\[
T_f=\sum_{e\subset\partial f}\epsilon(f,e)\,
\Lambda_{\gamma(e\to f)}e_e.
\]

La definizione diventa matematica soltanto dopo aver fissato percorso γ, punto base, dualità, orientazione e legge di trasformazione. Non presentiamo questa formula schematica come teorema già dimostrato.

Il bersaglio continuo è la coppia di Cartan

\[
T^a=de^a+\omega^a{}_b\wedge e^b,\qquad
R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b.
\]

Curvatura e torsione sono indipendenti. Il ramo teleparallelo impone R=0 ma può avere T≠0; il ramo Riemann–Cartan generico può avere entrambi non nulli; il ramo torsione-libera è un'ulteriore condizione. Non si deve usare la connessione di Levi-Civita come connessione fondamentale quando si vuole variare indipendentemente la connessione di Cartan.

**Gate dimensionale.** T129/T161 costruiscono uno split euclideo 6D in 3+3 e una finestra interna 3D. Non selezionano una direzione temporale. Servono un complesso spacetime 4D, un coframe lorentziano non degenere e transizioni Spin⁺(1,3). Il coframe spaziale RGS e le variabili PSU–Anti-Twin sono dati d'ingresso, non una derivazione già compiuta dello spaziotempo.

## 5. Azione comune: dove entra la fisica

Dopo aver definito geometria e trasporto, il modello deve dichiarare un'azione discreta

\[
S_h[e_h,\Lambda_h,U_h,\Psi_h,\Phi_h;M_{h,k}]
=S_{\rm grav,h}+S_{\rm gauge,h}+S_{\rm matter,h}
+S_{\rm fluid,h}+S_{\rm coupling,h}.
\]

I termini non sono determinati dalla sola geometria. Vanno ricavati da un bersaglio continuo dichiarato e discretizzati con variabili compatibili. La variazione rispetto a e_h e Λ_h indipendenti è essenziale per ricavare le equazioni gravitazionali e la sorgente di torsione; non basta inserire a posteriori una formula di torsione in un'azione che varia soltanto la metrica.

Il ponte fisico deve inoltre verificare: covarianza di gauge; identità di Bianchi discrete; conservazione compatibile con le simmetrie; stabilità; unità dimensionali; osservabili calibrabili; limite di raffinamento o dichiarazione esplicita di validità a risoluzione finita.

## 6. Crosswalk delle dieci famiglie

| Famiglia | Oggetto differenziale discreto condiviso | Risultati/ancore esistenti | Interfaccia fisica | Obbligo ancora aperto |
|---|---|---|---|---|
| Q6 | C^k, d_h, incidenza e Laplaciani | conteggi Q6; T130 gradienti/baricentri; T149 ostacolo spettrale esatto | carrier finito di campi e trasporti | costruire una successione K_h, non usare solo il seed a 64 stati |
| GOLDEN | P_parallel, P_perp, generatori e zonotopo | T129 frame ortogonale; T161 finestra come somma di segmenti | geometria spaziale candidata | derivare Hodge e pesi dalla geometria, senza parametri arbitrari |
| IVM | sei assi antipodali e azione dei gruppi | T146 carrier a 64 stati; T161 distinzione O_h/I_h | frame spaziale e direzioni elastiche | mappa metrica/equivarante, non identificazione per analogia |
| CELL | celle orientate, mappe di bordo e involuzioni | identità di catena; T148 lock Anti-Twin | conservazione e collocazione dei due fogli | definire complesso 4D, orientazione e dualità |
| REP | fibre locali, Clifford e rappresentazioni | T027 McKay–Molien; T049D Weyl; T147 Spin(6) | materia spinoriale | sollevare gli effettivi trasporti lorentziani a Spin(1,3), controllando cociclo e doubling |
| SPACETIME | coframe, connessione indipendente, olonomie e difetto di torsione | T115 Clifford da coframe statico prescritto; T148 lock condizionale; T161 algebra lorentziana condizionale | Einstein–Cartan, teleparallelismo e Dirac | derivare coframe e connessione da un'azione discreta |
| ANALYSIS | Hilbert discreti, Hodge, mappe di confronto | T048 esplicita gli obblighi Mosco; FEEC/DEC in letteratura | limiti Maxwell, elasticità, Dirac e gravità | stabilità uniforme, compattezza quando necessaria, Mosco e convergenza spettrale |
| DYNAMICS | trasporto su spigoli, olonomie, flussi e azioni | PRISM/Krist-All e QLG come strutture finite | gauge, fluidi, MHD, fasi e sincronizzazione | derivare evoluzione e conservazioni da azione/modello costitutivo calibrato |
| ARITH | parametri algebrici, ricorrenze e coefficienti | T027 identità esatta; φ e ψ come rami algebrici distinti | coefficienti spettrali e di scala | mostrare l'ingresso in osservabili dimensionalmente coerenti; nessuna inferenza numerologica |
| MORPH | gradienti, baricentri, difetti e strain | T130 identità finite; teoremi Morandotti/deformazioni | elasticità e risposta materiale | legge costitutiva calibrata e convergenza indipendente dalla mesh |

Questa tabella assegna interfacce da verificare. Non afferma che esista già un'unica azione fisica che accoppi tutte le dieci famiglie.

## 7. Architettura commutativa unica

\[
\begin{array}{ccccc}
Q_6/\text{celle}&\xrightarrow{d_h,\partial_h}&
\text{complesso differenziale}&\xrightarrow{M_{h,k}}&\text{geometria Hodge}\\
&&\downarrow\text{trasporto}&&\downarrow\text{variazione}\\
\text{fogli PSU--AT}&\longrightarrow&
\text{olonomie gauge/Cartan}&\longrightarrow&\text{equazioni discrete}\\
&&\downarrow\text{coframe + connessione}&&\downarrow J_h,I_h\\
\text{golden/IVM}&\longrightarrow&
\text{complesso lorentziano 4D}&\longrightarrow&\text{PDE/ osservabili}\\
&&\downarrow\text{sollevamento Spin}&&\\
&&\text{materia QLG/Dirac}&&
\end{array}
\]

La famiglia aritmetica fornisce coefficienti e molteplicità; quella morfodinamica variabili geometriche e costitutive; quella dinamica trasporto ed evoluzione. Entrano nello stesso sistema, non in teorie parallele.

Le quattro compatibilità da dimostrare sono:
1. commutazione cochain/interpolazione, d I_h = I_h d_h, nel quadro FEEC appropriato;
2. covarianza di gauge delle olonomie;
3. compatibilità delle curvature/torsioni discrete con le equazioni di Cartan sotto raffinamento;
4. convergenza dell'operatore di materia discreto all'operatore Dirac/gauge desiderato.

## 8. Ordine di lavoro e test falsificabili

**A — base combinatoria e metrica**
- separare grafo Q6, 2-scheletro cubicale e cubo completo;
- fissare orientazioni e test esatti d_h²=0;
- costruire M_{h,k} dalla geometria golden/IVM e verificarne positività e scaling;
- riutilizzare T130 soltanto quando valgono rango e calibrazione.

**B — gauge e Cartan**
- definire link, punti base e olonomie di faccia;
- definire separatamente curvatura da olonomia e torsione da difetto di chiusura del coframe;
- testare covarianza e identità di Bianchi;
- mantenere distinti i rami torsione-libera, Riemann–Cartan e teleparallelo.

**C — spacetime e spin**
- costruire una raffinazione lorentziana 4D e derivare la direzione temporale;
- sollevare i trasporti a Spin⁺(1,3), controllando cociclo e struttura spin;
- confrontare T149 con operatori raffinati/overlap/domain-wall e testare località, specie, spectral flow e anomalie.

**D — fisica e limite continuo**
- fissare l'azione e variare indipendentemente coframe e connessione;
- ricavare equazioni e leggi di conservazione;
- provare stabilità e convergenza Mosco/strong-resolvent/spettrale per la successione scelta;
- calibrare almeno un osservabile per ogni settore fisico rivendicato.

## 9. Letteratura: strumenti già disponibili

1. Arnold, Falk, Winther, “Finite element exterior calculus, homological techniques, and applications”, Acta Numerica 15 (2006), 1–155, DOI 10.1017/S0962492906210018. Complessi FEEC, proiezioni commutanti, Hodge, Maxwell ed elasticità.
2. Hirani, Discrete Exterior Calculus, tesi PhD Caltech (2003), DOI 10.7907/ZHY8-V329. Forme discrete e operatori su complessi primali e duali.
3. Desbrun, Hirani, Leok, Marsden, Discrete Exterior Calculus (2005). Forme e operatori discreti su complessi simpliciali.
4. Regge, “General Relativity Without Coordinates”, Nuovo Cimento 19 (1961), 558–571. Geometria simpliciale piecewise-flat e curvatura sui hinge.
5. Christiansen, “On the definition of curvature in Regge calculus”, IMA Journal of Numerical Analysis 44 (2024), 2698–2715, DOI 10.1093/imanum/drad095. Risultato di convergenza per smoothing in ipotesi specifiche.
6. Schmidt, Kohler, “Torsion Degrees of Freedom in the Regge Calculus as Dislocations on the Simplicial Lattice”, General Relativity and Gravitation 33 (2001), 1799–1807, DOI 10.1023/A:1013031402382. Dislocazioni e torsione in una costruzione Einstein–Cartan discreta.
7. Xue, “Quantum Regge Calculus of Einstein–Cartan theory”, Physics Letters B 682 (2009), 300–304, DOI 10.1016/j.physletb.2009.10.082. Variabili tetrade e connessione di spin su complessi simpliciali.
8. Cho, “Gauge theory of Poincaré symmetry”, Physical Review D 14 (1976), 3335, DOI 10.1103/PhysRevD.14.3335. Connessione lorentziana, curvatura e torsione nella teoria di gauge di Poincaré.
9. Wilson, “Confinement of quarks”, Physical Review D 10 (1974), 2445, DOI 10.1103/PhysRevD.10.2445. Azione di gauge su reticolo e variabili di plaquette.

Questa letteratura legittima strumenti e metodi nelle rispettive ipotesi; non dimostra che la specifica costruzione Q6–golden–IVM–PSU possieda già il limite lorentziano e fisico richiesto.

## 10. Registro di stato

| Affermazione | Stato |
|---|---|
| carrier Q6 e conteggi finiti | [E] |
| frame golden T129 | [E]/[N] secondo la scheda |
| identità zonotopica T161 | [E], audit di posizione generale [N] |
| gradienti/baricentri/resistenza T130 | [P] sotto ipotesi di rango e dissipazione; test [N] |
| identità McKay–Molien T027 | [E] audit intero esatto |
| Clifford curvo T115 da coframe prescritto | [P], coframe e tempo statici assunti |
| lock fogli/chiralità T148 | [E] algebra; interpretazione fisica [H] |
| embedding Weyl T049D | [P] nelle convenzioni gamma dichiarate |
| FEEC/DEC/Regge/Einstein–Cartan discreti | [L] nelle rispettive ipotesi |
| unico complesso spacetime RGS 4D e azione | [O] |
| derivazione dinamica della gamba temporale PSU–AT | [O] |
| curvatura e torsione indipendenti sul complesso RGS/Q6 | [O] |
| limite Dirac QLG in Spin⁺(1,3) | [O] |
| modello fisico unificato con osservabili calibrati | [H]/[O] |

**Conclusione.** Il ponte mancante non è un'ulteriore analogia geometrica: è un sistema discreto Cartan–Hodge–gauge, con le dieci famiglie come interfacce compatibili, un'azione che produca le equazioni e un limite di raffinamento che recuperi la fisica continua. I teoremi esistenti forniscono ingredienti reali; la costruzione unificante resta da dimostrare.
