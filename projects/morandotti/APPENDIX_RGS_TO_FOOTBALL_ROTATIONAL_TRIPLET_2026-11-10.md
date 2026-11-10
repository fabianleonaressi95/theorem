# Dal tripletto RGS al guscio del pallone: costruzione effettiva e interpretazione meccanica

**Dossier Morandotti — appendice operativa**  
**Versione:** 0.3 — 10 novembre 2026

## 1. Correzione concettuale indispensabile: rotazioni non sono (T_{1u})

Nel gruppo cubico completo (O_h), un vettore polare (per esempio una traslazione) trasforma come (T_{1u}). Un vettore assiale (per esempio la velocità angolare o un asse di rotazione) trasforma come (T_{1g}), perché sotto inversione cambia diversamente da un vettore polare.

Di conseguenza:
- le tre traslazioni rigide formano (T_{1u});
- le tre rotazioni rigide formano (T_{1g});
- (T_{2u}) è un'altra irriducibile tridimensionale, non il nome generico della tripletta rotazionale.

La tripletta rotazionale RGS che viene trasferita al pallone è quindi una **tripletta cinematica assiale, (T_{1g})-like nel contesto cubico**, non (T_{1u}) e non (T_{2u}). L'etichetta “-like” è prudente: la verifica completa richiede l'azione di gruppo discreta sullo spazio effettivamente vincolato.

## 2. I due modelli e i loro spazi

### 2.1 Sorgente RGS a 64 siti

Le coordinate sorgente sono (X_i\in\mathbb R^3), (i=1,\ldots,64), quindi lo spazio ambientale è (mathbb R^{192}). I quattro vincoli linearizzati sono tre condizioni di centratura e una condizione radiale:
\[
C\delta x=0,\qquad C\in\mathbb R^{4\times192}.
\]
La base del nucleo (Q\in\mathbb R^{192\times188}) soddisfa
\[
CQ=0,\qquad Q^TQ=I.
\]
Per gli assi cartesiani (e_a), i generatori rotazionali sono
\[
G_a=(e_a\times X_i)_{i=1}^{64},\quad a=1,2,3.
\]
Essi rispettano i vincoli al primo ordine:
\[
CG=0.
\]
Si ortonormalizza la loro immagine, ad esempio con SVD/polar factor di (QQ^TG), ottenendo (U_R\in\mathbb R^{192\times3}). Questa tripletta è costruita dalla cinematica, non estratta dalla Hessiana originale.

### 2.2 Guscio calcistico a 92 nodi

La mesh del pallone è il troncato-icosaedro:
- 60 vertici geometrici;
- 12 pannelli pentagonali e 20 esagonali;
- 32 nodi centrali dei pannelli;
- 92 nodi complessivi;
- 180 triangoli CST;
- 270 cerniere diedrali;
- 90 cuciture fisiche tra pannelli.

Lo spazio cartesiano ambientale ha 276 coordinate. Il modello quaternion-tangent costruisce in ogni nodo una normale (n_i) e due versori tangenti ortonormali (e_{1i},e_{2i}). La matrice locale
\[
T_i=[e_{1i}\ e_{2i}]\in\mathbb R^{3\times2}
\]
viene assemblata in
\[
T=\operatorname{diag}(T_i)\in\mathbb R^{276\times184},
\quad T^TT=I_{184}.
\]
Questa è una riduzione cinematica nodo-per-nodo alla tangente della superficie di riferimento. Non è il nucleo di un Jacobiano arbitrario di vincoli shell: sono due costruzioni diverse. La rigidezza tangente è
\[
K_{tan}=T^TKT\in\mathbb R^{184\times184}.
\]
I quaternioni codificano i frame locali e la loro orientazione.

## 3. Trasferimento geometrico 64 → 92

Non esiste una corrispondenza uno-a-uno tra i 64 siti RGS e i 92 nodi shell. Si usa una mappa geometrica basata sulle direzioni radiali. Per ogni direzione target (n_j), si selezionano (k) direzioni sorgente distinte (u_i) e si risolve
\[
\min_w\|w\|_2^2,\qquad
\sum_iw_i=1,\qquad \sum_iw_iu_i=n_j.
\]
La soluzione di norma minima è
\[
w=C^T(CC^T)^+d,\quad
C=\begin{bmatrix}1&\cdots&1\\u_1&\cdots&u_k\end{bmatrix},
\quad d=\begin{bmatrix}1\\n_j\end{bmatrix}.
\]
Le pesature scalari sono replicate sulle tre componenti cartesiane:
\[
W=W_s\otimes I_3\in\mathbb R^{276\times192}.
\]
Le otto coppie di siti sorgente che condividono la stessa direzione unitaria sono raggruppate prima dell'interpolazione; il peso della direzione viene poi diviso tra i rappresentanti radiali. Questo evita che un pareggio del nearest-neighbour decida arbitrariamente il trasferimento.

Dopo il trasferimento si elimina la componente normale al guscio:
\[
U_{R\to sh}=\operatorname{orth}\bigl(TT^TWU_R\bigr).
\]
In coordinate tangenti, la base trasferita è (T^TU_{R\to sh}\). Si confronta con gli autovettori della rigidezza tangente mediante angoli principali.

## 4. Che cosa misura l'angolo principale

Siano (A,B\in\mathbb R^{n\times3}) basi ortonormali di due sottospazi tridimensionali. Gli angoli principali sono definiti da
\[
\cos\theta_i=\sigma_i(A^TB),\qquad
0\leq\theta_1\leq\theta_2\leq\theta_3\leq\pi/2.
\]
Angoli piccoli significano che i due sottospazi sono geometricamente vicini dopo la mappa scelta. Non dimostrano:
- identità degli operatori energetici;
- equivalenza delle leggi costitutive;
- una simmetria comune;
- un'identificazione microscopica;
- una validazione sperimentale.

La robustezza va valutata cambiando il numero di direzioni sorgente usate nell'interpolazione, la mesh, i parametri materiali e le cuciture.

## 5. Audit di robustezza già registrato

Il test di trasferimento ha valutato (k=8,12,16,24,32) direzioni sorgente distinte. I tre angoli principali (gradi) sono:

| k | θ1 | θ2 | θ3 |
|---:|---:|---:|---:|
| 8 | 5.6259 | 5.6337 | 5.6431 |
| 12 | 3.2543 | 3.2642 | 3.2656 |
| 16 | 2.4055 | 2.4070 | 2.4089 |
| 24 | 2.5595 | 2.5945 | 2.6220 |
| 32 | 2.2535 | 2.2620 | 2.2848 |

Il massimo angolo osservato è 5.6431°. L'escursione massimo-minimo per modo è circa 3.37°. La dipendenza non è monotona: non si può dichiarare convergenza rispetto a (k). Il risultato supporta un buon allineamento geometrico nel ventaglio testato, non una coincidenza esatta né un'identità fisica.

Il test end-to-end confronta inoltre la tripletta trasferita con i tre modi più bassi della rigidezza tangente del guscio non bloccato. L'interpretazione va accompagnata dal gap tra terzo e quarto autovalore e dal residuo normalizzato (\|K_{tan}B\|/(\|K_{tan}\|\|B\|)). Un tripletto basso può essere vicino ai modi rigidi o a modi molli: la classificazione richiede l'ispezione delle forme modali e dei vincoli di gauge.

## 6. Lettura meccanica dei tre modi sul pallone

La tripletta trasferita fornisce tre campi di spostamento tangenziale. Per ogni modo (u^{(a)}), (a=1,2,3), si devono ricostruire:
\[
u_i^{(a)}=T_i\eta_i^{(a)},\qquad \eta_i^{(a)}\in\mathbb R^2.
\]
Poi si valutano separatamente:
1. deformazione membranale per triangolo;
2. variazione degli angoli diedri/energia di hinge;
3. energia e scorrimento sulle 90 cuciture fisiche;
4. proiezione sulle direzioni materiali 1 e 2 di ciascun pannello;
5. spostamento normale escluso dalla riduzione tangente, che deve essere studiato in un modello shell più completo se l'inflazione è rilevante.

Le tre componenti sono una base del sottospazio, non tre risposte indipendenti da interpretare separatamente: una diversa combinazione lineare delle tre basi descrive lo stesso sottospazio. Per una lettura fisica stabile bisogna usare invarianti del sottospazio, oppure fissare una convenzione di orientazione della base.

## 7. Come verificare se le cuciture rompono o accoppiano il tripletto

Si definiscano le matrici di rigidezza con e senza rinforzo di cucitura, (K_0) e (K_s). Sul sottospazio trasferito (B), la matrice efficace è
\[
K_{eff}=B^T K_{tan}B\in\mathbb R^{3\times3}.
\]
Gli autovalori di (K_{eff}) misurano la rigidezza nelle tre combinazioni interne al sottospazio. La loro separazione è uno splitting del tripletto rispetto alla metrica/normalizzazione adottata. Si confronta:
\[
\Delta K_{seam}=B^T(K_s-K_0)B.
\]
Per separare contributi si assemblano anche (K_{mem}), (K_{hinge}), (K_{seam}) e si riportano le tre matrici proiettate (B^TK_{(\cdot)}B).

Se la tripletta è un sottospazio esattamente protetto da una simmetria tridimensionale irriducibile e l'operatore conserva tale simmetria, Schur impone una forma scalare sul fattore irriducibile (a parità di molteplicità isolata). Nel pallone troncato-icosaedrico la simmetria geometrica naturale è icosaedrica, mentre il modello RGS sorgente ha struttura cubica: non si deve imporre (O_h) al pallone né trasferire automaticamente le etichette (T_{1g},T_{1u},T_{2u}). Le cuciture e i materiali possono ridurre ulteriormente la simmetria effettiva.

## 8. Quaternioni: cosa fanno e cosa non fanno

Ogni frame locale destrorso ((e_{1i},e_{2i},n_i)) viene rappresentato da un quaternione unitario (q_i\). Un vettore tangente locale, scritto come quaternione puro (p=(0,v)), è portato nel frame globale da
\[
p_{glob}=q_i p q_i^{-1}.
\]
La coppia (q_i,-q_i) descrive la stessa rotazione in (SO(3)). I controlli numerici verificano:
- norma unitaria del quaternione;
- corrispondenza tra (qvq^{-1}) e la matrice di rotazione;
- composizione delle rotazioni;
- doppio rivestimento (q\sim-q).

Il quaternione qui è una rappresentazione cinematica del frame locale. Non è un nuovo grado di libertà fisico indipendente, a meno che si introduca una legge costitutiva/dinamica per la microrotazione, come in una teoria Cosserat o micropolare.

## 9. Procedura sperimentale che trasforma il risultato in una spiegazione del pallone

Per verificare se i tre modi abbiano una conseguenza osservabile:
1. acquisire scansioni 3D del pallone a riposo e sotto più pressioni/carichi;
2. tracciare i 90 bordi di cucitura e gli assi trama/ordito;
3. stimare i parametri ortotropi da provini e le rigidezze d'interfaccia da prove di cucitura;
4. misurare spostamenti/forme modali con DIC o scansione ripetuta sotto eccitazioni controllate;
5. confrontare i tre campi modali predetti con i campi misurati, usando correlazione modale, angoli principali e incertezza;
6. ripetere con mesh raffinata e parametri perturbati.

Per studiare l'effetto Magnus, questo modello strutturale deve poi essere accoppiato a un modello del flusso: i modi del guscio possono modificare forma, rugosità e orientazione delle cuciture, ma non generano da soli la forza aerodinamica.

## 10. Stato della prova

| Affermazione | Stato |
|---|---|
| Tripletta rotazionale RGS costruita da (e_a\times X_i) e contenuta nel tangente 188D | Verificata numericamente nel test |
| Trasferimento geometrico 64→92 con riproduzione affine delle direzioni | Verificato numericamente |
| Proiezione sul tangente nodo-per-nodo 184D del guscio | Implementata e testata |
| Angoli principali nel grid (k=8,12,16,24,32) | Calcolati; sensibilità non monotona, nessuna convergenza dimostrata |
| Quaternioni come lift (SU(2)\to SO(3)) dei frame | Identità algebrica e test numerici |
| Tripletta uguale a un modo (T_{2u}) originale | Non dimostrato; non va affermato |
| Simmetria protetta comune cubica/icosaedrica | Non dimostrata |
| Cuciture responsabili di uno splitting specifico | Da calcolare con ablation e parametri misurati |
| Validazione con scansioni e provini reali | Aperta |

## 11. Messaggio tecnico per Morandotti

Abbiamo costruito una tripletta rotazionale dal modello RGS vincolato a 64 siti, l'abbiamo trasferita geometricamente alla mesh del pallone a 92 nodi e proiettata sul piano tangente locale del guscio. La shell ha 184 gradi di libertà tangenziali e una rigidezza ridotta (K_{tan}=T^TKT). La robustezza del trasferimento è stata misurata per cinque scelte del vicinato: gli angoli principali restano sotto 5.65°, ma variano in modo non monotono. I quaternioni codificano i frame locali e rendono coerente la cinematica delle rotazioni. Il passo successivo è proiettare separatamente energia membranale, flessionale e di cucitura sul sottospazio trasferito, per capire quali parti del pallone sostengano o rompano la risposta a tre componenti. Questo è un risultato numerico preliminare e verificabile, non ancora una prova di simmetria protetta o una validazione sperimentale.
