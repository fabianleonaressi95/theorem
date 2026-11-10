# Appendice tecnica per la proposta Morandotti — RGS–PRISM

**Repository:** `fabianleonaressi95/theorem`  
**Finalità:** dossier tecnico di accompagnamento; distingue risultati formalizzati nel repository centrale, verifiche finite, modelli esplorativi e materiale storico da archiviare.

## Documento principale collegato

Questa appendice va presentata insieme alla [Nota progettuale Morandotti — RGS–PRISM](NOTA_PROGETTUALE_MORANDOTTI_RGS_PRISM.md), che costituisce il documento principale di interlocuzione. La nota espone domanda scientifica, benchmark proposto, fasi di lavoro e richiesta di confronto; questa appendice documenta basi tecniche, risultati, limiti e stato delle verifiche.

**Ordine di lettura per il destinatario:** prima la nota progettuale; poi questa appendice tecnica come supporto verificabile.

## 1. Criterio documentale

Questa appendice non aggrega numeri eterogenei fingendo che provengano da un unico audit. Ogni risultato è associato al proprio record. In particolare:

- un'identità intera su un complesso finito è un risultato esatto per quel complesso;
- un test numerico certifica l'esecuzione dei controlli implementati, non una proprietà universale;
- un modello dinamico implementato non è automaticamente un modello costitutivo di materiale;
- un framework di convergenza non è una prova di convergenza della specifica sequenza RGS–PRISM;
- risultati storici non ancora trasferiti con sorgenti e test nel repository centrale sono segnalati come tali.

Questa disciplina è essenziale per una valutazione indipendente.

## 2. PRISM: grafo prodotto e raffinamento di riferimento

La struttura prodotto di base è

\[
G_1=C_{64}\square C_6\square C_6\square C_6\square C_5.
\]

Il numero dei vertici è

\[
|V_1|=64\cdot6^3\cdot5=69,120,
\]

e il grado è

\[
\deg(G_1)=2\cdot5=10.
\]

Il numero degli archi non orientati è quindi

\[
|E_1|=\frac{10\cdot69,120}{2}=345,600.
\]

Il repository centrale implementa una famiglia di riferimento piatta a cinque dimensioni:

\[
G_r=C_{64r}\square C_{6r}\square C_{6r}\square C_{6r}\square C_{5r},
\qquad r\in\mathbb N.
\]

Ne seguono esattamente

\[
|V_r|=69,120r^5,\qquad
\deg(G_r)=10,\qquad
|E_r|=345,600r^5.
\]

Il codice non costruisce l'intera matrice di adiacenza: usa indicizzazione row-major, vicini periodici, enumerazione lazy degli archi e simbolo di Fourier. I file verificabili sono:

- `scripts/rgs_prism_product_refinement.py`
- `tests/test_t048_rgs_prism_product_refinement.py`
- `theorems/T048-rgs-prism-mosco-changing-spaces.md`

### 2.1 Misura, conduttanze e metrica intrinseca

Ponendo

\[
h_j=\frac{1}{L_jr},\qquad
m_r=\frac{1}{|V_r|},
\]

per la direzione coordinata (j) il codice usa

\[
b_{r,j}=\frac{m_r}{h_j^2}.
\]

La lunghezza intrinseca dell'arco in direzione (j) è calibrata come

\[
\ell_{r,j}=\frac{h_j}{\sqrt{2d}},\qquad d=5.
\]

Con due archi incidenti per direzione, la condizione intrinseca adottata dal codice è

\[
\sum_{y\sim x}b_r(x,y)d_r(x,y)^2=m_r.
\]

Il residuo di questa identità è testato per i livelli (r=1,2,4,8), con tolleranza (10^{-14}).

### 2.2 Simbolo spettrale e modo di Fourier

Per un modo intero (k=(k_1,\ldots,k_5)), il valore proprio discreto è

\[
\lambda_{r,k}
=4\sum_{j=1}^5(L_jr)^2
\sin^2\!\left(\frac{\pi k_j}{L_jr}\right),
\]

mentre il valore proprio del toro piatto unitario è

\[
\lambda_k=4\pi^2\sum_{j=1}^5k_j^2.
\]

Per ogni modo fissato, lo sviluppo di seno dà la consistenza del simbolo e un errore principale di ordine (O(r^{-2})). I test controllano la diminuzione dell'errore per i livelli (1,2,4,8,16), oltre alla consistenza energetica dei modi coseno campionati.

**Limite dichiarato nel record T048:** questa è una calibrazione su un toro piatto di riferimento. Non è la prova di Mosco per la geometria curva RGS–PRISM, non dimostra il liminf per successioni arbitrarie e non dimostra compattezza uniforme.

## 3. Mosco, risolventi e spettro: stato della dimostrazione

Il record [T048](../theorems/T048-rgs-prism-mosco-changing-spaces.md) definisce gli obblighi per una famiglia di forme su spazi di Hilbert variabili:

\[
(H_h,\mathcal E_h)\longrightarrow(H,\mathcal E).
\]

Sono esplicitati:
- misure sui vertici e conduttanze;
- domini e convenzioni delle forme;
- mappe di identificazione tra discreto e continuo;
- condizione weak-liminf (M1);
- successioni di recupero (M2);
- metriche intrinseche;
- compattezza uniforme / tightness;
- distinzione tra convergenza di risolventi e convergenza spettrale;
- estensione separata alle forme di Hodge di grado superiore.

La conclusione epistemica è esplicita: **la convergenza di Mosco della sequenza curva RGS–PRISM resta aperta**. Anche una volta ottenuta la convergenza forte dei risolventi, la convergenza di autovalori isolati, molteplicità e sottospazi spettrali richiede un ulteriore argomento di compattezza collettiva.

Questo punto è una possibile area di collaborazione diretta con un gruppo esperto di calcolo delle variazioni e omogeneizzazione.

## 4. Q6: complesso cubicale e Anti-Twin

Il record [T068](../theorems/T068-q6-cubical-topological-synchronization-audit.md) definisce il 2-scheletro del cubo a sei dimensioni:

\[
|V|=64,\qquad |E|=192,\qquad |F_2|=240.
\]

Le matrici intere di bordo hanno dimensioni

\[
B_1\in\mathbb Z^{64\times192},\qquad
B_2\in\mathbb Z^{192\times240}.
\]

È verificata esattamente

\[
B_1B_2=0.
\]

Il rango del ciclo spazio del grafo è (192-64+1=129); il record riporta (\operatorname{rank}B_2=129). Per il 2-scheletro troncato si ha quindi

\[
b_1=0,\qquad b_2=240-129=111.
\]

Il valore (b_2=111) dipende dall'omissione delle celle tridimensionali. Non è il secondo Betti del cubo completo, che è contrattile.

Il complemento bitwise

\[
c(g)=g\oplus111111
\]

induce mappe segnate (J_0,J_1,J_2) e il record verifica

\[
J_0B_1=B_1J_1,\qquad
J_1B_2=B_2J_2,\qquad
J_k^2=I.
\]

Pertanto l'Anti-Twin, in questa istanza, è definito rigorosamente come involuzione cellulare del complesso cubicale. Un'interpretazione fisica ulteriore richiede una derivazione distinta.

## 5. Dinamica topologica e benchmark di isteresi

T068 registra due dinamiche finite NL e NLT per fasi sui 64 nodi e sui 192 archi. Le equazioni sono una trascrizione del modello di sincronizzazione topologica della letteratura, con sostituzione delle facce simpliciali triangolari con facce quadrate cubicali.

La sorgente di riferimento è:

Ghorbanchian et al., *Higher-order simplicial synchronization of coupled topological signals*, Communications Physics 4, 120 (2021), DOI: https://doi.org/10.1038/s42005-021-00605-4.

L'estensione cubicale Q6 è una generalizzazione implementata, non una conclusione già contenuta nell'articolo.

Il protocollo multi-seed e multi-rate è documentato nel progetto `projects/q6_hysteresis_benchmark/`. Il codice separa le sequenze casuali delle frequenze intrinseche da quelle delle fasi iniziali; forward e backward sweep usano gli stessi campioni di frequenze. La prima versione esplorativa, che non garantiva questa parità, è stata scartata.

**Precisazione sui numeri:** il record T068 nel repository centrale classifica la robustezza dell'isteresi Q6 come problema aperto. Le tabelle quantitative eventualmente riportate in un rapporto CI devono essere accompagnate dall'artefatto JSON del run specifico e dalla sua configurazione. Non si deve trasformare una differenza tra rami a velocità finita in una prova di isteresi quasi-statica.

### 5.1 Isteresi costitutiva: baseline separate

Il progetto fornisce implementazioni di riferimento per:
- Preisach discreto;
- Prandtl–Ishlinskii;
- Bouc–Wen.

Sono disponibili metriche di area del ciclo, RMSE e separazione loading/unloading. Le implementazioni e i test sono plumbing software e benchmark sintetici: non è dichiarata una validazione industriale né una superiorità rispetto ai modelli di riferimento.

Per un caso magnetico occorre aggiungere Jiles–Atherton con convenzione parametrica esplicita e dati (B-H) misurati. Per plasticità ciclica o attuatori servono cicli sperimentali con carico, frequenza, temperatura e precondizionamento documentati.

## 6. Geometria cubicale e risultati esatti correlati

Il registro principale del repository documenta ulteriori risultati utili per una collaborazione su discretizzazioni conformi e operatori geometrici:

| Record | Risultato | Stato registrato |
|---|---|---|
| T055 | Suddivisione dyadica del 2-scheletro Q6; 496 vertici, 1344 archi, 960 facce raffinate e mappe di catena commutanti | Prova finita esatta |
| T056 | Coniugio per permutazione tra matrice di trasferimento Phase 21 e trigrammi; stessa radice di Perron | Identità esatta; nessun intertwiner geometrico di celle stabilito |
| T057 | Relazione di similarità quadrata con rotazione di 45° e fattore \(\sqrt2\), e relazione a due stadi a 90°/fattore 2 | Esatta sotto la geometria dichiarata |
| T058 | Audit di faccia planare 12-centri/15-linee | Teorema condizionale sotto l'embedding dichiarato |
| T059 | Complesso cellulare Kathara e operatori di Hodge; \(B_1B_2=0\), ranghi (11,10), Betti (1,0,0) | Identità intere esatte, condizionate al riempimento delle facce |
| T060 | Mappa di catene Kathara–Q3 | Candidato; esecuzione del test ancora pendente |
| T061 | Omotopia tra due convenzioni di cammino | Prova esplicita; selezione della faccia dipendente dalla convenzione |
| T062 | Mappa integrale Kathara–Q6 | Esistenza dimostrata nella codifica dichiarata; collassa le dieci 2-celle |
| T063 | Quaternioni Hamiltoniani, SU(2) e doppio rivestimento SO(3) | Prova algebrica |
| T064 | Covarianza di trasporto SU(2) e invarianza delle tracce di Wilson | Prova algebrica |
| T065 | Suddivisione cubicale e naturalità rispetto alle 48 simmetrie signed-permutation in 3D | Prova integrale |
| T066 | Conformità affine delle facce condivise nelle celle di parità | Teorema condizionale |
| T067 | Commutazione di Stokes dell'interpolatore cubicale di integrali di faccia | Prova esatta; quadrature numeriche finite |

Questi record mostrano una linea verificabile su complessi, mappe di catena, simmetrie, interpolazione e commutazione di Stokes. Non dimostrano, da soli, la convergenza di un modello di difetti o la corrispondenza con una struttura Krist-All.

## 7. Geometria RGS a 188 dimensioni: dossier da consolidare

Il programma RGS include una costruzione geometrica su 64 punti con spazio tangente discreto di dimensione 188. Nei report di audit precedentemente prodotti sono stati registrati:

- (X_{O_h}\in\mathbb R^{64\times3});
- (Q\in\mathbb R^{192\times188});
- (K_{\mathrm{tangent}}\in\mathbb R^{188\times188});
- (B_{T2u,TAN}\in\mathbb R^{188\times3});
- 188 direzioni tangenti e 4 direzioni normali;
- residuo (\|Q^TQ-I\|\) dell'ordine di (1.31\times10^{-14});
- residuo KKT circa (4.39\times10^{-8});
- residuo di commutazione con (O_h) circa (5\times10^{-16});
- spettro riportato con 29 autovalori negativi, 3 modi rotazionali quasi nulli e 156 positivi.

Questi valori sono qui riportati come **risultati storici di audit da riallegare**, non come risultati verificati dai test T048/T068 del repository centrale. Prima della trasmissione al gruppo Morandotti occorre archiviare nel repository:
1. i file NPZ/NPY originali;
2. lo script che ricostruisce (X_{O_h}), (Q), (K_{\mathrm{tangent}}) e i proiettori;
3. la definizione esatta dei prodotti scalari e delle convenzioni;
4. il report completo con spettro, residui e soglie;
5. i test automatici che rigenerano i numeri.

Finché questo trasferimento non è completato, non è corretto presentare la lista come un audit riproducibile dal repository pubblico.

## 8. PRISM–Krist-All: stato di provenienza

Nel programma di ricerca sono stati precedentemente riportati:
- 11.725 classi Krist-All;
- residuo (W_0\) circa (5.22\times10^{-16});
- 108 cicli di riferimento di lunghezza 640;
- gap spettrale riportato (0.009630546656);
- relazione algebrica riportata (K^3=K^2+I);
- valore numerico di \(\psi\) circa (1.465571231876768\).

**Questi valori non sono certificati dai record T048 o T068 e non vanno attribuiti ai relativi workflow.** Nel repository centrale consultato per questa appendice non è stato individuato un audit Krist-All autonomo con definizioni, dati, script e test sufficienti a ricostruirli integralmente.

Per renderli presentabili a un revisore esterno occorre un dossier dedicato con:
- definizione non ambigua dell'insieme di oggetti e della relazione di equivalenza che produce le classi;
- algoritmo di enumerazione e prova di completezza;
- definizione di (W_0), (K) e del relativo spazio;
- matrice o operatore da cui si ricava il gap;
- convenzioni di normalizzazione;
- test indipendenti e dati grezzi.

Non si afferma in questa appendice che tali numeri siano falsi: si afferma che la loro provenienza riproducibile deve essere consolidata prima di usarli come evidenza nella proposta.

## 9. Collegamento scientifico con Morandotti

Il possibile contributo non è proporre un altro metodo FEM generico né rivendicare una nuova teoria dei difetti già validata. La domanda è se la struttura discreta e gli audit geometrici possano fornire un livello aggiuntivo di:

1. rappresentazione topologica delle incompatibilità e dei difetti;
2. verifica delle identità di catena, simmetrie e vincoli;
3. costruzione di energie discrete;
4. studio della convergenza variazionale e della compattezza;
5. collegamento con evoluzioni dissipative e modelli costitutivi.

Il primo esperimento condiviso dovrebbe essere deliberatamente piccolo: scegliere un modello di dislocazioni/disclinazioni già presente nella letteratura del gruppo, fissare le variabili cinematiche e il funzionale, costruire una discretizzazione RGS–PRISM compatibile e confrontare errore, stabilità, costo e comportamento al raffinamento con la formulazione di riferimento.

## 10. Criteri di successo e di arresto

Il progetto dovrebbe proseguire oltre la fase iniziale soltanto se supera criteri concordati:

- **Matematico:** il modello discreto è ben definito e il funzionale ha proprietà di esistenza dimostrabili.
- **Geometrico:** le mappe di bordo/cobordo e i vincoli sono compatibili con le simmetrie dichiarate.
- **Numerico:** il benchmark è riproducibile e non peggiora sistematicamente rispetto al riferimento.
- **Convergenza:** esistono prove o evidenze controllate per liminf, recovery e compattezza; le affermazioni sono graduate secondo l'evidenza.
- **Applicativo:** il modello migliora una metrica utile su dati sperimentali non usati nella calibrazione.
- **Trasferimento:** il vantaggio è sufficientemente specifico da giustificare software specialistico, licenza, servizio o Proof of Concept.

Se non emerge un vantaggio rispetto alla formulazione esistente, il risultato corretto è documentare il limite e non avviare una startup sulla base del solo interesse matematico.

## 11. Riferimenti primari del repository

- [README e indice THEOREM](../README.md)
- [T048 — Mosco e spazi variabili](../theorems/T048-rgs-prism-mosco-changing-spaces.md)
- [T068 — Q6, Anti-Twin e sincronizzazione](../theorems/T068-q6-cubical-topological-synchronization-audit.md)
- [Mappa dei filoni di ricerca](../projects/README.md)
- [Script di raffinamento PRISM](../scripts/rgs_prism_product_refinement.py)
- [Test del raffinamento PRISM](../tests/test_t048_rgs_prism_product_refinement.py)
- [Benchmark Q6 isteresi](../projects/q6_hysteresis_benchmark/README.md)
- [Matrice di validazione esterna](../open-problems/EXTERNAL_MATHEMATICAL_VALIDATION_MATRIX.md)

## 12. Messaggio scientifico essenziale

Il patrimonio già formalizzato nel repository dimostra che il programma dispone di costruzioni discrete concrete, identità combinatorie esatte, audit di operatori e un quadro esplicito delle questioni di convergenza ancora aperte. Il passo proposto al gruppo Morandotti è trasformare una di queste strutture in un modello variazionale di difetti e sottoporlo a confronto matematico e numerico con le formulazioni esistenti.

La proposta non chiede di accettare un'interpretazione fisica complessiva RGS–PSU. Chiede di verificare un'interfaccia matematica circoscritta, falsificabile e potenzialmente utile.

**FLN**


---

# ADDENDUM DI RECUPERO FORENSE E RIPRODUCIBILITÀ — 9 NOVEMBRE 2026

Questa sezione prevale su eventuali formulazioni meno precise nelle sezioni A.12–A.13 e nei riferimenti storici. È stata aggiunta dopo il recupero e il ricalcolo dei materiali d'archivio.

## A.20. Audit PRISM 69.120: ricostruzione riproducibile

È stato recuperato e rieseguito lo script di generazione delle matrici di incidenza. La struttura è il toro prodotto

\[
C_{64}\square C_6\square C_6\square C_6\square C_5.
\]

I risultati ricalcolati sono:

| Quantità | Risultato |
|---|---:|
| Vertici | 69.120 |
| Archi | 345.600 |
| Facce quadrate | 691.200 |
| Non nulli di B1 | 691.200 |
| Non nulli di B2 | 2.764.800 |
| Residuo esatto B1 B2 | 0 non nulli |
| Rango ciclico del grafo E−V+1 | 276.481 |
| Gap del Laplaciano sui vertici | 0,009630546655606143 |
| Molteplicità del gap | 2 |

L'hash strutturale delle matrici sparse B1 e B2, secondo la serializzazione documentata dallo script, è

\[
\texttt{c2f15e070e0e1dc99f4e2d8142290acc0b32bcc9222707d6cc655ef442bf6eb9}.
\]

La cella-count del toro prodotto è

\[
(69120,345600,691200,691200,345600,69120)
\]

e i Betti dichiarati sono

\[
(b_0,b_1,b_2,b_3,b_4,b_5)=(1,5,10,10,5,1).
\]

**Precisazione:** i Betti sono quelli del prodotto di cinque circonferenze e sono riportati mediante la struttura prodotto. Lo script pubblicato rigenera B1 e B2 e verifica B1B2=0 esattamente; non calcola ancora i ranghi di tutti gli operatori B_k per k=1,...,5. Non va quindi detto che l'intera omologia sia stata ricalcolata tramite una diagonalizzazione completa di tutte le matrici di bordo.

Script e report:
- `scripts/audit_prism_69120.py`
- `reports/prism_69120_audit.json`
- `reports/RECOVERY_MANIFEST.md`

## A.21. Audit 188D: risultati riprodotti e correzione dell'interpretazione Anti-Twin

È stato recuperato il bundle `188D_FINAL_BUNDLE.zip` e l'archivio matriciale `actual_original_X_report_matrices.npz`. Quest'ultimo contiene le matrici derivate per l'audit: Q_tangent, K0, P_G, Pi_AT, R_geo_tangent, A_raw, i frame ortonormali e l'estensione sul kernel. Non contiene però le coordinate originali X_Oh (64×3).

I controlli ricalcolati sulle matrici archiviate danno:

| Controllo | Residuo |
|---|---:|
| QᵀQ−I, norma Frobenius | 1,3145×10⁻¹⁴ |
| P_G²−P_G | 5,0765×10⁻¹⁵ |
| K0 P_G | 7,9998×10⁻¹² |
| P_G K0 | 7,9999×10⁻¹² |
| [K0,P_G] | 5,3775×10⁻¹⁴ |
| R_geoᵀ−R_geo | 4,4476×10⁻¹⁵ |
| R_geo²−I | 3,8258×10⁻¹⁴ |
| [R_geo,P_G] | 9,2279 |
| [R_geo,K0] | 83,8316 |
| Involuzione Pi_AT²−I | 0 |

Lo spettro di K0 presenta 64 autovalori quasi nulli e 124 positivi, con massimo 12,8 e primo modo dinamico a 0,5. P_G è un proiettore simmetrico di rango 64 e K0 annulla la sua immagine entro i residui riportati.

Il controllo indipendente dell'allineamento geometrico restituisce coseni degli angoli principali compresi tra

\[
0,00265018\quad\text{e}\quad0,93108124,
\]

con

\[
\|P_GA-A\|_F=6,53706.
\]

Ne segue che **la specifica identificazione geometrica memorizzata da R_geo_tangent non commuta con il proiettore del kernel e non è certificata come intertwiner canonico**.

L'estensione `R_AT_kernel_extension` ha invece residuo di involuzione circa 2,33×10⁻¹³ e commutatore con K0 circa 1,19×10⁻¹². Ma tale estensione è costruita direttamente sulla decomposizione del kernel; la sua commutazione con K0 è conseguenza della costruzione e non costituisce una prova indipendente dell'identificazione geometrica tra i 64 vertici e il kernel.

**Verdetto corretto:**
- kernel e proiettore intrinseci: verificati numericamente;
- involuzione astratta estesa sul kernel: verificata numericamente;
- identificazione geometrica canonica Anti-Twin/kernel: non verificata;
- ricostruzione indipendente delle coordinate X_Oh: ancora da completare, perché il file delle coordinate non è nel bundle matriciale recuperato.

Script e report:
- `scripts/audit_188d_antitwin.py`
- `tests/test_188d_antitwin_audit.py`
- `reports/188d_antitwin_audit.json`
- `reports/RECOVERY_MANIFEST.md`

## A.22. Krist-All: stato della documentazione recuperata

È stato recuperato l'archivio `PRISM_KristAll_recovered_sources.zip`. Contiene un manoscritto sul livello di codifica a 64 stati, lo spazio prodotto da 69.120 stati, una pipeline Merkle schematica, script di figure e note Python supplementari.

L'archivio non contiene tuttavia:
1. la definizione formale della relazione di equivalenza che produce le classi Krist-All;
2. la tabella completa dei 11.725 rappresentanti o classi;
3. il programma deterministico di enumerazione e un test di completezza;
4. le definizioni operative e le matrici dell'operatore K e del residuo W0;
5. un test riproducibile dell'identità K³=K²+I.

Pertanto i valori 11.725, W0≈5,22×10⁻¹⁶ e K³=K²+I restano **risultati storici da recuperare e verificare**, non risultati certificati dall'archivio appena esaminato. Questo è un limite di provenienza documentale, non una dimostrazione che le affermazioni siano false.

Documento di stato:
- `reports/KRISTALL_RECOVERY_STATUS.md`

## A.23. Implicazione per la proposta a Morandotti

La proposta può ora poggiare su un audit PRISM concreto e su una parte sostanziale dell'audit 188D. Deve però presentare con chiarezza anche il risultato negativo relativo all'intertwiner geometrico Anti-Twin e lasciare Krist-All in stato aperto fino al recupero del generatore delle classi e degli operatori.

Questa scelta rende il dossier più forte scientificamente: espone dati riproducibili, limita le conclusioni ai controlli effettivamente eseguiti e identifica con precisione i problemi matematici sui quali chiedere una collaborazione.


## A.24. Correzione dell'audit Anti-Twin: equivarianza geometrica e identificazione del kernel sono questioni distinte

L'ispezione dello script originale `RGS_PSU_construct_geometric_intertwiner.py` e del report `actual_original_X_report.json` permette di precisare il risultato precedente.

La costruzione definisce:
- l'involuzione antipodale sui 64 siti, \(\Pi_{AT}\);
- una base tangente \(Q\in\mathbb R^{192\times188}\);
- una mappa geometrica \(A\in\mathbb R^{188\times64}\), ottenuta dal frame locale e dalla sua polarizzazione;
- l'azione tangente \(R_{geo}\in\mathbb R^{188\times188}\).

La relazione di equivarianza geometrica è verificata direttamente:

\[
R_{geo}A=A\Pi_{AT},
\qquad
\|R_{geo}A-A\Pi_{AT}\|_F
=1,6473\times10^{-14}.
\]

Sono inoltre verificati, entro precisione numerica, la simmetria e l'involuzione di \(R_{geo}\), nonché la simmetria e l'involuzione di \(\Pi_{AT}\). Pertanto è corretto affermare che **la mappa geometrica costruita è Anti-Twin-equivarante**.

Questo non dimostra però che la sua immagine coincida con il kernel del particolare operatore \(K_0\). Per il proiettore \(P_G\) archiviato:

\[
\|P_GA-A\|_F=6,53706,
\]

e i coseni degli angoli principali tra \(\operatorname{Im}(A)\) e \(\operatorname{Im}(P_G)\) variano da 0,00265018 a 0,93108124. La coincidenza dei due sottospazi non è quindi dimostrata.

La costruzione successiva \(U_{geom}=\operatorname{polar}(P_GA)\) produce invece una base ortonormale contenuta nel kernel numerico; l'estensione dell'involuzione su tale base commuta con \(K_0\) entro circa \(1,19\times10^{-12}\). Questa commutazione è però conseguenza della costruzione sul kernel e non prova indipendentemente che la mappa geometrica non proiettata coincida con il kernel originario.

Infine, i commutatori diretti \([R_{geo},P_G]\) e \([R_{geo},K_0]\) sono riportati come diagnostica condizionale: il loro significato richiede la conferma che le matrici siano espresse nella medesima base tangente di dimensione 188. Il report originale stesso contiene questa avvertenza. Non vanno dunque presentati come confutazione della geometria Anti-Twin.

**Verdetto aggiornato:**
- involuzione antipodale sui 64 siti: verificata numericamente;
- equivarianza della mappa geometrica Anti-Twin: verificata numericamente;
- kernel/proiettore intrinseco di dimensione 64: verificato numericamente;
- identificazione tra immagine della mappa geometrica non proiettata e kernel: non dimostrata;
- commutazione diretta di \(R_{geo}\) con \(K_0\): subordinata alla verifica della base comune;
- coordinate originali \(X_{O_h}\): ancora da recuperare come array binario originale; il PDF recuperato documenta il codice e i nomi dei file salvati, ma non contiene l'array stesso.

Il codice sorgente recuperato è archiviato in `archive/recovered_188d/RGS_PSU_construct_geometric_intertwiner.py`. Il report JSON e lo script di audit principale sono stati aggiornati coerentemente.


## A.25. Anisotropia pentagono–esagono nel pallone pressurizzato

È stato aggiunto un dossier autonomo in `docs/FOOTBALL_PENTAGON_HEXAGON_ANISOTROPY.md`, con implementazione in `models/football_anisotropy.py`, runner in `scripts/run_football_anisotropy_audit.py` e test in `tests/test_football_anisotropy.py`.

La geometria ideale è il icosaedro troncato: 60 vertici, 12 pentagoni, 20 esagoni e 90 adiacenze tra pannelli, delle quali 60 pentagono–esagono e 30 esagono–esagono. Il modello meccanico corrente assegna uno spostamento normale scalare a ciascun pannello e minimizza un'energia quadratica con rigidezza efficace (C_5) o (C_6), accoppiamento lungo i bordi condivisi e carico uniforme.

**Baseline puramente modellistica** ((p=0.01, C_5/C_6=1.25, gamma=0.15)): spostamento medio dei pentagoni (0.00875363), degli esagoni (0.00962570), contrasto pentagono meno esagono (-8.72071\times10^{-4}), residuo relativo del sistema lineare (2.64\times10^{-16}). Il controllo isotropo (C_5=C_6=1) restituisce spostamento uniforme (p/C=0.01) e anisotropia incrementale nulla entro precisione numerica.

Questi numeri verificano soltanto il modello discreto dichiarato. (C_5/C_6=1.25) è un valore dimostrativo, non una misura del pallone reale. Non sono ancora implementati shell nonlineare, cuciture, ortotropia tessile, deformazioni di bordo compatibili, campo di curvatura o calibrazione sperimentale. La metrica della superficie radiale continua è specificata nel dossier, ma non è stata numericamente ricostruita dal modello a centri di pannello.

Il risultato è quindi classificato come **modello fenomenologico numericamente verificato**, non come spiegazione sperimentale già dimostrata della non-sfericità osservata. Il passo successivo con Morandotti è identificare (C_5,C_6,gamma) da dati di materiale e cucitura, sostituire i gradi di libertà scalari con una discretizzazione shell conforme e confrontare forma e deformazioni con scansioni 3D a pressione controllata.


## A.26. Estensione a shell discreta ortotropa e geometria cubo–sfera

L'estensione del modello pallone integra esplicitamente il precedente lavoro RGS sul cubo e sulla sfera inscritta. Si riutilizzano
\[
r_C(\mathbf n)=a/\|\mathbf n\|_\infty,\quad r_S=a,\quad
\chi_{CS}(\mathbf n)=1/\|\mathbf n\|_\infty-1,
\quad H_4(\mathbf n)=n_x^4+n_y^4+n_z^4-3/5.
\]
La prima quantità è l'eccesso radiale esatto cubo–sfera; \(H_4\) è il modo armonico cubico di grado quattro. Sono due campi geometrici distinti dall'anisotropia costitutiva dei pannelli pentagonali ed esagonali.

Il nuovo codice è in \`models/football_shell.py\`. La superficie di riferimento può includere i due modi geometrici con ampiezze esplicite \(\alpha_C,\alpha_4\), entrambe nulle per default. La geometria del pallone è il icosaedro troncato con 60 vertici, 12 pentagoni, 20 esagoni e 90 cuciture; la triangolazione conforme usa 92 nodi includendo i centri dei pannelli, 180 elementi CST e 270 cerniere diedrali.

Il modello meccanico comprende:
- elementi triangolari CST di membrana con legge ortotropa in tensione piana (\(E_1,E_2,G_{12},\nu_{12}\)) e assi materiali locali per pannello;
- flessione discreta mediante cerniere sull'angolo diedro firmato fra triangoli adiacenti;
- irrigidimento di cucitura indipendente, con termine assiale lineare opzionale e moltiplicatore flessionale;
- pressione integrata sulle facce di riferimento e sei vincoli di gauge per rimuovere i modi rigidi;
- confronto opzionale con nuvole di punti CSV/XYZ/OBJ/PLY tramite ICP rigido e distanze simmetriche campionate.

**Classificazione:** modello shell discreto linearizzato, implementato e sottoposto a test numerici; non è ancora un modello a deformazioni finite geometricamente non lineare. Non sono inclusi contatto, pieghe, danno adesivo o omogeneizzazione alla scala dei filati. Nessuna scansione sperimentale o misura di provini è stata fornita: il confronto ICP nei test è sintetico e non costituisce validazione sperimentale. I valori costitutivi di default sono parametri dimostrativi, non proprietà misurate del pallone.

Il dossier operativo e i comandi riproducibili sono in \`docs/FOOTBALL_ORTHOTROPIC_DISCRETE_SHELL.md\`; il runner è \`scripts/run_football_shell_audit.py\`; i test sono in \`tests/test_football_shell.py\`. L'identificazione di \(\alpha_C,\alpha_4,E_1,E_2,G_{12}\) e dei parametri di cucitura richiede misure indipendenti e validazione su scansioni non usate per il fit.


## A.27. Aggiornamento 2026: baseline CIP-DG e specifica del ponte RGS discreto

### Riferimento continuo e numerico aggiornato

La linea bibliografica più direttamente pertinente comprende ora:
- P. Cesana, L. De Luca, M. Morandotti (2024), formulazione semi-discreta Airy per disclinazioni a cuneo e dislocazioni di bordo;
- P. Cesana, E. Fabbrini, M. Morandotti (2025), formulazione variazionale dell'elasticità lineare piana con cinematica incompatibile;
- P. Cesana, E. Fabbrini, A. A. León Baldelli, M. Morandotti (2026), *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, preprint arXiv:2609.29614.

Il lavoro 2026 considera elasticità isotropa linearizzata in piano di deformazione, sorgenti di Burgers e Frank, regolarizzazione mediante core radius e un problema ellittico del quarto ordine per la funzione di Airy. La formulazione numerica usa elementi finiti con continuous interior penalty discontinuous Galerkin (CIP-DG) e un numero finito di problemi locali di cell formula; una volta calcolate le soluzioni fondamentali, configurazioni di difetti possono essere composte in post-processing. Il lavoro dichiara confronti con benchmark analitici e configurazioni d'interazione.

Questo costituisce la baseline numerica da riprodurre e non un dettaglio da ignorare. La proposta RGS–PRISM deve confrontarsi con essa a parità di dominio, materiale, sorgenti, core radius, condizioni al contorno e osservabili. Non è scientificamente corretto descrivere RGS–PRISM come la prima soluzione discreta del problema.

### Equazioni da usare come riferimento

Per la deformazione simmetrica piana \(\epsilon\), la sorgente distribuzionale di incompatibilità è
\[
\operatorname{inc}\,\epsilon=\zeta,
\qquad
\zeta=
\sum_{j=1}^{J}|b^j|\,
\partial_{(b^j)^\perp/|b^j|}\delta_{x^j}
-
\sum_{k=1}^{K}s^k\delta_{y^k}.
\]
I vettori (b^j) sono i vettori di Burgers; (s^k) sono gli angoli di Frank. Nel caso isotropo lineare piano, introducendo la funzione di Airy (v), il riferimento del lavoro FEM è
\[
\sigma=\operatorname{cof}(D^2v),
\qquad
\frac{1-\nu^2}{E}\Delta^2v=\zeta,
\]
e la parte quadratica dell'energia di Airy è
\[
\mathcal G(v;\Omega)
=\frac12\frac{1+\nu}{E}
\int_\Omega
\left(|D^2v|^2-\nu(\Delta v)^2\right)\,dx.
\]
La regolarizzazione core-radius rimuove dischi attorno ai difetti e trasferisce le sorgenti sui bordi dei core. Per la riproduzione numerica si devono mantenere le stesse convenzioni di segno, dati di sorgente e condizioni al bordo del paper di riferimento.

### Specifica discreta RGS da dimostrare

Il complesso cinematico discreto può essere scritto
\[
C^0_h\xrightarrow{d_{0,h}}C^1_h
\xrightarrow{d_{1,h}}C^2_h,
\qquad d_{1,h}d_{0,h}=0.
\]
L'identità (d_{1,h}d_{0,h}=0) è la chiusura del complesso: **non** rappresenta la sorgente di difetto. Il difetto deve entrare tramite un operatore di incompatibilità che agisce sulla deformazione simmetrica discreta, costruita dal gradiente cinematico e dalla metrica/material tensor:
\[
\epsilon_h=\operatorname{sym}G_h u_h
\quad\text{(oppure una variabile di deformazione indipendente, se la formulazione lo richiede),}
\]
\[
\operatorname{Inc}_h\epsilon_h=\zeta_h.
\]
La sorgente (\zeta_h) deve approssimare separatamente i contributi traslazionali di Burgers e quelli rotazionali di Frank, inclusa la regolarizzazione del core. La costruzione di (\operatorname{Inc}_h), (\zeta_h), della condizione al bordo e della forma energetica è ancora da progettare e dimostrare.

Il gradiente RGS locale e i pesi geometrici possono contribuire alla costruzione di (G_h) e della metrica discreta. Non si deve però identificare il gradiente scalare Q6 con l'operatore tensoriale \(\operatorname{Inc}_h\), né assumere che la sola identità di catena produca automaticamente la legge di incompatibilità elastica. Le formule già disponibili per gradienti locali least-squares e metriche (g_i=E_i^TE_i) sono ingredienti candidati; la loro compatibilità con la forma di Airy deve essere dimostrata sul benchmark piano.

### Test di equivalenza e criteri di confronto

1. **Test di sorgente:** riprodurre la distribuzione di Burgers/Frank e il suo trasferimento al core discreto.
2. **Test cinematico:** verificare (d_{1,h}d_{0,h}=0) esattamente e controllare separatamente la relazione (\operatorname{Inc}_h\epsilon_h=\zeta_h).
3. **Test energetico:** confrontare la forma RGS con la forma di Airy su campi di prova e sulle soluzioni minimizzanti.
4. **Test di bordo:** riprodurre le condizioni di trazione libera nella formulazione di Airy.
5. **Test numerico:** confrontare CIP-DG e RGS su energia, (L^2)-stress, Hessiana di Airy, residuo, condizionamento, tempo e memoria.
6. **Test di raffinamento:** almeno tre livelli, con studio separato dell'errore spaziale e della dipendenza dal core radius.

Solo dopo questi test ha senso chiedere una convergenza variazionale: liminf, successioni di recupero e compattezza devono essere trattati separatamente. La convergenza di Mosco della famiglia curva RGS–PRISM rimane aperta.

### Implicazione per il caso calcistico

Il guscio calcistico rimane un secondo benchmark, con variabili di superficie, anisotropia ortotropa e cuciture. Non va identificato direttamente con il dominio piano del problema Airy: il trasferimento richiede una formulazione su patch curve e una derivazione delle curvature/incompatibilità superficiali. Le condizioni di cucitura già derivate costituiscono un bilancio meccanico di interfaccia; non sono la stessa sorgente \(\zeta\) del modello di difetti cristallini.

**Stato:** riferimento continuo e baseline CIP-DG identificati; specifica di ricerca RGS discreta formulata; nessuna equivalenza numerica RGS–CIP-DG, nessuna prova di convergenza e nessuna superiorità sono ancora dichiarate.

Per la classificazione bibliografica completa si veda [Matrice bibliografica Morandotti–RGS–PRISM](MATRICE_BIBLIOGRAFICA_MORANDOTTI_RGS_PRISM.md).

## Documento applicativo complementare

Il [Documento di raccordo calcistico](DOCUMENTO_RACCORDO_CALCISTICO_MORANDOTTI_RGS_PRISM.md) collega le strutture shell già implementate al problema variazionale dei difetti, distinguendo analogie meccaniche, identificazioni matematiche ancora da costruire e validazioni sperimentali mancanti.


## Giunzioni: raccordo di Darmois–Israel e legge elastica di interfaccia

Il documento di raccordo calcistico include ora una sezione dedicata alle condizioni di Darmois–Israel. Per l'uso nel progetto si distingue esplicitamente:
- continuità della prima forma fondamentale e, nel caso di Darmois senza strato singolare, della seconda forma fondamentale;
- salto di curvatura estrinseca e tensore superficiale di Israel nella relatività generale;
- salto diedrale/di curvatura e trazioni/momenti di linea nella shell elastica, da derivare dal funzionale costitutivo.

Il tensore (S_{ab}) di Israel non viene identificato con la tensione della cucitura. La trasposizione al pallone è strutturale e geometrica; la legge fisica di giunzione deve essere derivata indipendentemente dalla shell energy e, se necessario, calibrata sperimentalmente.

Riferimento interno: [Documento di raccordo calcistico — sezione 5-bis](DOCUMENTO_RACCORDO_CALCISTICO_MORANDOTTI_RGS_PRISM.md).


## A.28. Derivazione dei sottospazi tangenti, quaternioni e triplette

La derivazione completa, con Jacobiano dei quattro vincoli, costruzione di Q, proiettore tangente, Hessiana del Lagrangiano, triplette rotazionali, distinzione T1u/T2u, frame quaternionici, trasferimento 192→276 e angoli principali, è raccolta nel [Capitolo metodologico dedicato](CAPITOLO_SOTTOSPAZI_TANGENTI_QUATERNIONI_TRIPLETTE_MORANDOTTI.md). Il capitolo va letto insieme ai report A14 e agli audit della geometria 188D: non identifica automaticamente K0 con la Hessiana vincolata originale e non promuove i cluster numerici a rappresentazioni irriducibili senza verifica dei caratteri e dei commutatori.
