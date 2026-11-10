# Appendice tecnica — cinematica vincolata, shell, cuciture, triplette e quaternioni

**Documento associato:** Nota progettuale Morandotti  
**Versione:** 0.1 — 10 novembre 2026  
**Funzione:** rendere espliciti gli oggetti matematici e le verifiche che collegano la geometria del pallone alla meccanica dei pannelli.

## A. Geometria e discretizzazione

### A.1 Campo radiale cubo-sfera

Per (x=rn), (n\in S^2), il bordo del cubo centrato (C_a=[-a,a]^3) è raggiunto quando
\[
r\max_i|n_i|=a.
\]
Quindi
\[
r_C(n)=\frac{a}{\|n\|_\infty},\qquad r_S(n)=a,
\qquad \Delta r(n)=a\left(\frac1{\|n\|_\infty}-1\right).
\]
Sui vertici diagonali del cubo (|n|_\infty=1/\sqrt3), perciò (r_C=\sqrt3a); sulle direzioni normali alle facce (|n|_\infty=1), (r_C=a). Questo misura la variazione radiale del cubo rispetto alla sfera inscritta.

Una parametrizzazione di superficie (X(\theta,\phi)) va scelta separatamente: il campo radiale non è da solo una mesh né una legge di deformazione. Dopo la proiezione/pannellizzazione, si definisce una mappa globale (Phi) sui nodi e sugli elementi. La stessa (Phi) deve essere usata sui due lati di un bordo condiviso, così la coincidenza geometrica è esatta a livello di parametrizzazione.

### A.2 Conteggi del modello discreto di riferimento

La configurazione già usata come audit preliminare ha:
\[
N_v=92,\quad N_{\rm CST}=180,\quad N_{\rm hinge}=270,\quad N_s=90.
\]
I 92 nodi con tre coordinate danno 276 coordinate cartesiane prima dei vincoli. I 180 triangoli sono gli elementi membranali CST; le 270 cerniere rappresentano il contributo flessionale discreto; le 90 cuciture costituiscono interfacce meccaniche identificate. Questi conteggi descrivono la discretizzazione corrente, non garantiscono da soli qualità della mesh, correttezza topologica o convergenza.

Per ogni elemento triangolare si memorizzano: connettività, normale, base tangente locale, spessore, orientamento materiale e appartenenza al pannello. Per ogni cucitura: coppie di bordi, orientazione, lunghezza, legge costitutiva e parametri calibrabili.

## B. Cinematica e varietà dei vincoli

### B.1 Configurazione e vincoli

Sia (X\in\mathbb R^{3N}) il vettore di coordinate nodali. La configurazione ammissibile appartiene a
\[
\mathcal M=\{X:c_1(X)=\cdots=c_r(X)=0\}.
\]
Il Jacobiano dei vincoli è
\[
J(X)=\begin{bmatrix}\nabla c_1(X)^T\\\vdots\\\nabla c_r(X)^T\end{bmatrix}.
\]
Una variazione infinitesima (\delta X) è tangente alla varietà se
\[
J(X)\delta X=0.
\]
Se (J) ha rango costante (r), la dimensione locale dello spazio tangente è (3N-r).

Si costruisce una base ortonormale (Q\in\mathbb R^{3N\times(3N-r)}) del nucleo:
\[
JQ=0,\qquad Q^TQ=I,\qquad P_T=QQ^T.
\]
Ogni variazione ammissibile si scrive (\delta X=Q\xi). La verifica numerica minima riporta (|JQ|_2), (|Q^TQ-I|_2), rango di (J), rango di (Q) e condizionamento.

### B.2 Due discretizzazioni, due basi tangenti

Nel framework (O_h) già auditato:
\[
X_{64}\in\mathbb R^{192},\quad \operatorname{rank}J=4,\quad
Q_{64}\in\mathbb R^{192\times188}.
\]
La matrice (Q_{64}) è una base tangente per quel sistema a 64 punti.

Nel modello shell a 92 nodi:
\[
X_{\rm sh}\in\mathbb R^{276}.
\]
Se i vincoli indipendenti shell hanno rango (r_{\rm sh}), allora
\[
Q_{\rm sh}\in\mathbb R^{276\times(276-r_{\rm sh})}.
\]
Non è corretto trasferire (Q_{64}) direttamente al sistema shell. Serve una mappa di interpolazione/proiezione (T:\mathbb R^{192}\to\mathbb R^{276}), costruita dalla corrispondenza geometrica tra i 64 punti e i 92 nodi; poi si verifica se (TQ_{64}) è tangente ai vincoli shell o si proietta sul nuovo nucleo:
\[
Q_{\rm sh}\,Q_{\rm sh}^T TQ_{64}.
\]
La perdita di rango e il residuo (J_{\rm sh}TQ_{64}) sono diagnostiche, non dettagli implementativi.

### B.3 Hessiana vincolata

Per energia potenziale (Pi(X)) e vincoli (c(X)=0), la lagrangiana è
\[
\mathcal L(X,\lambda)=\Pi(X)+\lambda^Tc(X).
\]
La Hessiana vincolata è
\[
H_L=\nabla_X^2\Pi(X)+\sum_{j=1}^r\lambda_j\nabla_X^2c_j(X),
\]
e la Hessiana ridotta
\[
H_T=Q^TH_LQ.
\]
La stabilità lineare locale richiede positività di (H_T) dopo aver rimosso i modi rigidi non vincolati. Autovalori negativi indicano instabilità; quasi-zeri vanno classificati distinguendo simmetrie esatte, vincoli incompleti e meccanismi della mesh.

## C. Elementi shell e deformazione

### C.1 Cinematica geometrica

Per una mappa di deformazione (x=\varphi(X)), il gradiente è (F=\nabla_X\varphi). La deformazione di Green–Lagrange è
\[
E=\frac12(F^TF-I).
\]
È oggettiva rispetto a rotazioni rigide: se (F=R) con (R^TR=I), allora (E=0). Questa proprietà è essenziale quando il pallone subisce grandi rotazioni e deformazioni.

In una shell di spessore (h), la cinematica separa deformazione della superficie media e variazione di curvatura attraverso lo spessore. Nella teoria di Kirchhoff–Love la normale resta normale alla superficie media; in Reissner–Mindlin si ammette deformazione di taglio trasversale. La scelta deve dipendere dal rapporto spessore/luce e dalle misure disponibili.

### C.2 CST membranale

Per un triangolo piano a tre nodi, il campo di spostamento lineare produce deformazione membranale costante per elemento (CST). In coordinate locali:
\[
\epsilon_m=B_m u_e.
\]
La rigidezza elementare è
\[
K_e^{(m)}=tA\,B_m^T D_m B_m,
\]
con spessore (t), area (A) e matrice costitutiva (D_m). La formulazione è semplice e riproducibile, ma non descrive da sola la flessione: per questo nel modello corrente si aggiungono cerniere/hinges o una formulazione shell con DOF rotazionali.

### C.3 Ortotropia nel piano

Con assi materiali principali 1 e 2:
\[
D_m=
\begin{bmatrix}
Q_{11}&Q_{12}&0\\Q_{12}&Q_{22}&0\\0&0&Q_{66}
\end{bmatrix},
\quad
\nu_{21}=\nu_{12}E_2/E_1,
\]
\[
Q_{11}=\frac{E_1}{1-\nu_{12}\nu_{21}},\quad
Q_{22}=\frac{E_2}{1-\nu_{12}\nu_{21}},\quad
Q_{12}=\frac{\nu_{12}E_2}{1-\nu_{12}\nu_{21}},\quad
Q_{66}=G_{12}.
\]
La matrice va ruotata nel sistema globale con la trasformazione tensoriale appropriata per l'angolo di trama (\alpha). La matrice ruotata non si ottiene ruotando soltanto i tre coefficienti: si trasformano tensori di deformazione e tensione, rispettando la convenzione ingegneristica per (\gamma_{12}).

Per la flessione di una laminazione ortotropa si introducono matrici (A,B,D) di rigidezza membranale, accoppiamento e flessione. Per un singolo strato omogeneo e simmetrico rispetto al piano medio, (B=0); per laminati asimmetrici (B) può essere non nullo. La semplificazione a ortotropia piana è una prima approssimazione, non un modello completo del tessuto composito se la struttura presenta strati, coating o rinforzi.

## D. Cerniere e cuciture

### D.1 Energia di cerniera

Per due triangoli adiacenti con normale (n_1,n_2), l'angolo diedro è
\[
\theta=\operatorname{atan2}\bigl(\hat e\cdot(n_1\times n_2),n_1\cdot n_2\bigr).
\]
Una legge flessionale discreta lineare attorno all'angolo di riferimento (	heta_0) può essere
\[
E_h=\frac12 k_h(\theta-\theta_0)^2.
\]
La dipendenza di (k_h) da modulo flessionale, spessore e lunghezza del bordo deve essere derivata dalla discretizzazione adottata o calibrata; non va fissata con una formula presa da un'altra mesh senza verificarne la consistenza dimensionale.

### D.2 Interfaccia di cucitura

Sui due lati della cucitura si definiscono salti di traslazione e rotazione:
\[
[u]=u^+-u^-,\qquad[\theta]=\theta^+-\theta^-.
\]
Un potenziale d'interfaccia iniziale:
\[
\Pi_s=\frac12\int_{\Gamma_s}
[u]^TK_u[u]+[\theta]^TK_\theta[\theta],ds.
\]
Le matrici (K_u,K_\theta) possono distinguere direzione tangenziale, normale e rotazione attorno al bordo. Le trazioni e i momenti derivano dalla variazione di (Pi_s). Si devono confrontare almeno tre limiti: cucitura libera (rigidezza bassa), cucitura finita (parametri identificati) e continuità ideale (rigidezza alta). La dipendenza dalla mesh e la stabilità numerica nel limite rigido devono essere controllate.

## E. Triplette, simmetria cubica e quaternioni

### E.1 Modi rigidi e triplette

Per (a=1,2,3), i generatori infinitesimi di rotazione sono
\[
(G_a)_i=e_a\times X_i.
\]
I tre vettori (G_a) generano le rotazioni rigide. Le traslazioni (T_a) sono invece ((T_a)_i=e_a). Se il sistema non è vincolato, i sei modi rigidi devono essere nel nucleo della Hessiana elastica ideale. Se il pallone è fissato o soggetto a contatto, alcuni o tutti vengono rimossi.

Non ogni autospazio triplo è una rotazione rigida. Una tripletta spettrale è soltanto un autospazio di dimensione tre; la sua natura si determina applicando i generatori del gruppo e confrontando i caratteri/proiettori.

### E.2 Rappresentazioni (O_h)

Per un gruppo finito (G), il proiettore sull'irriducibile (alpha) è
\[
P_\alpha=\frac{d_\alpha}{|G|}
\sum_{g\in G}\chi_\alpha(g)^*\,D(g).
\]
I sottospazi (T_{1u}) e (T_{2u}) sono rappresentazioni tridimensionali distinte del gruppo cubico completo (O_h). La loro distinzione è data dai caratteri e dall'azione dei generatori, non dalla sola dimensione tre. Nei dati preliminari del framework a 64 punti sono stati riportati ranghi diversi per i proiettori (P_{T_{1u}}) e (P_{T_{2u}}); tali ranghi si riferiscono al numero totale di copie dell'irriducibile nel grande spazio, non alla dimensione della singola rappresentazione. Vanno ricalcolati sul modello shell con l'azione di (O_h) effettivamente preservata dalla mesh e dai materiali.

### E.3 Quaternioni e frame dei pannelli

Un quaternione unitario
\[
q=(\cos(\alpha/2),\,\hat n\sin(\alpha/2))
\]
rappresenta una rotazione di angolo (alpha) attorno a (hat n). Un vettore (v\in\mathbb R^3) si rappresenta come quaternione puro e ruota secondo (v'=qvq^{-1}). Il doppio rivestimento (SU(2)\to SO(3)) identifica (q) e (-q) con la stessa rotazione fisica.

Per ciascun pannello (p), il quaternione (q_p) può orientare il frame materiale rispetto al frame globale. Le differenze relative tra pannelli e lungo le cuciture possono essere espresse con
\[
q_{+-}=q_+^{-1}q_-.
\]
La parte vettoriale/logaritmica di (q_{+-}) fornisce un vettore di rotazione relativa, con attenzione al ramo dell'angolo vicino a (pi). La legge di cucitura può allora penalizzare la componente di rotazione relativa, separandola dallo scorrimento traslazionale.

La riduzione tangente e i quaternioni svolgono ruoli complementari: (Q) elimina variazioni incompatibili con i vincoli; i quaternioni rappresentano in modo regolare orientazioni e rotazioni finite. Non si deve identificare il vettore a tre componenti del quaternione con una tripletta spettrale senza un intertwiner esplicito.

## F. Trasferimento tra framework a 64 punti e shell a 92 nodi

Per rendere il ponte verificabile occorre costruire una corrispondenza geometrica (T) tra i punti del modello (O_h) e i nodi/punti di controllo shell. Le verifiche sono:

1. riproduzione esatta delle coordinate di riferimento sui punti coincidenti;
2. trasformazione corretta sotto ogni generatore (g\in O_h), cioè (T D_{64}(g)\simeq D_{\rm sh}(g)T);
3. rispetto dei vincoli: (|J_{\rm sh}TQ_{64}|);
4. stabilità del rango dell'immagine (TQ_{64});
5. confronto degli spettri ridotti solo dopo aver definito masse e prodotti scalari coerenti.

Se il modello shell non conserva esattamente la simmetria cubica (ad esempio per pannelli, cuciture o proprietà materiali non equivalenti), le rappresentazioni (O_h) sono una simmetria del riferimento o un'approssimazione, non una simmetria esatta dell'operatore deformato. In tal caso si quantifica la rottura mediante commutatori
\[
\|K_{\rm sh}D(g)-D(g)K_{\rm sh}\|.
\]

## G. Protocollo scansioni → calibrazione → previsione

### G.1 Dati minimi

Per ogni campione: scansione 3D a riposo, pressione interna, temperatura, massa, spessore, materiali e orientazione delle fibre/trame, posizione delle cuciture, carico applicato, condizioni di appoggio, tempo di acquisizione e incertezza strumentale. Per il comportamento dinamico: video ad alta velocità o tracking 3D, velocità/rotazione iniziali, pressione e condizioni ambientali.

### G.2 Registrazione e residui

Dopo registrazione rigida della scansione (S_{\rm exp}) sulla mesh (S_h), si calcolano:
- distanza point-to-surface e surface-to-point;
- errore normale e distribuzione dei residui per pannello;
- errore di curvatura;
- errore localizzato sulle cuciture;
- variazione di volume e area;
- residuo rispetto a carichi e pressioni misurati.

La registrazione rigida deve essere distinta dalla deformazione: non si deve lasciare che l'algoritmo di allineamento assorba la deformazione che il modello dovrebbe prevedere.

### G.3 Identificazione

Si separano dati di calibrazione e dati di validazione. I parametri ((E_1,E_2,\nu_{12},G_{12},t,k_h,K_u,K_\theta)) sono stimati con un problema inverso regolarizzato:
\[
\min_{p}\;\|W^{1/2}(y_{\rm model}(p)-y_{\rm exp})\|^2
+\lambda\,\mathcal R(p),
\]
con vincoli di positività e intervalli fisicamente misurati. Si riportano intervalli di confidenza/sensibilità e correlazioni tra parametri. Una buona corrispondenza su un'unica scansione non identifica univocamente tutti i parametri.

## H. Collegamento alla traiettoria e all'effetto Magnus

Il modello shell determina forma, deformazione, massa distribuita e possibili condizioni iniziali dopo il contatto. La forza di Magnus richiede anche un modello del flusso. Un modello di volo minimo:
\[
m\dot v=mg+F_D(v,\omega,\mathcal G)+F_M(v,\omega,\mathcal G),
\qquad
I\dot\omega=\tau_{\rm aero}+\tau_{\rm contact}.
\]
Qui (mathcal G) rappresenta geometria, rugosità e cuciture. Le dipendenze di (F_M) e (F_D) devono essere identificate sperimentalmente o calcolate con CFD. Il modello strutturale può fornire la geometria istantanea e l'orientazione delle cuciture, ma non dimostra da solo né la direzione né l'intensità dell'effetto Magnus.

## I. Test numerici obbligatori

1. **Geometria:** chiusura, orientazione coerente, area/volume, qualità triangoli, bordi non-manifold.
2. **Oggettività:** energia membranale e flessionale nulla (entro tolleranza) per traslazione e rotazione rigida.
3. **Costitutiva:** simmetria e definita positività della matrice ortotropa; test di rotazione degli assi.
4. **Cuciture:** limiti libero/finito/rigido; bilancio di forze e momenti; dipendenza dalla mesh.
5. **Vincoli:** rango di (J), residui (JQ), ortonormalità di (Q), Hessiana ridotta.
6. **Modi:** identificazione dei sei modi rigidi, classificazione delle triplette e commutatori di simmetria.
7. **Quaternioni:** norma unitaria, composizione, inversione, confronto con matrice di rotazione.
8. **Convergenza:** almeno tre raffinamenti, confronto di energia, spostamenti, frequenze e residui.
9. **Validazione:** dati non usati in calibrazione, incertezza e confronto scansione/mesh.

## J. Risultati preliminari e limiti

Sono già registrati nel filone di lavoro: framework (O_h) a 64 punti con (Q\in\mathbb R^{192\times188}), audit di ortogonalità della base tangente, Hessiana ridotta e decomposizione in sottospazi; modello shell discreto dimostrativo a 92 nodi, 180 CST, 270 hinges e 90 cuciture; formulazione ortotropa e deformazione di Green–Lagrange.

Questi elementi non costituiscono ancora una validazione del pallone reale: il framework 64/188 e la shell 92/276 sono spazi distinti; i parametri di materiale sono dimostrativi finché non vengono misurati; le scansioni e i dati di prova devono ancora essere collegati al problema inverso. La relazione tra cuciture e Magnus resta un'ipotesi da testare con aerodinamica accoppiata.

## K. Criterio di completamento per la presentazione

Il dossier è pronto per una discussione tecnica quando contiene:
- geometria e topologia riproducibili;
- definizione esplicita dei vincoli e base tangente shell;
- formulazione shell/ortotropa e legge di cucitura con unità;
- distinzione tra modi rigidi, triplette spettrali e irriducibili;
- cinematica quaternionica verificata;
- scansioni e prove con incertezza;
- confronto predittivo su dati indipendenti.

Fino ad allora va presentato come proposta modellistica con risultati preliminari, non come prodotto industriale validato.
