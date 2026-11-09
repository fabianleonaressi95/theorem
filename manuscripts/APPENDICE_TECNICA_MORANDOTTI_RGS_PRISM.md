# Appendice tecnica per la proposta Morandotti — RGS–PRISM

**Repository:** `fabianleonaressi95/theorem`  
**Finalità:** dossier tecnico di accompagnamento; distingue risultati formalizzati nel repository centrale, verifiche finite, modelli esplorativi e materiale storico da archiviare.

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
