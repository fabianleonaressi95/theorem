# Nota progettuale per Morandotti — pallone, pannellizzazione, cuciture e risposta anisotropa

**Versione:** 0.1 — dossier di lavoro, 10 novembre 2026  
**Scopo:** presentare un percorso di modellazione e validazione di un involucro sferico/poliedrico deformabile, collegando geometria, elementi shell, cuciture, proprietà ortotrope, scansioni sperimentali e cinematica dei sottospazi tangenti.  
**Perimetro:** meccanica della struttura e raccordo con la geometria del pallone. Non è una proposta cosmologica e non assume QLG o interpretazioni speculative come premesse.

## 1. Problema ingegneristico

Il problema è costruire un modello geometrico-meccanico capace di rispondere a cinque domande verificabili:

1. Come si passa da una geometria di riferimento cubica/poliedrica a un involucro curvo chiuso?
2. Come incidono pannelli, elementi shell e cuciture sulla rigidezza globale?
3. Come si rappresentano trama, ordito e direzioni preferenziali del materiale mediante costitutive ortotrope?
4. Come si confrontano spostamenti, curvature e deformazioni calcolate con scansioni 3D e prove meccaniche?
5. Come si separano i moti rigidi, i modi rotazionali e le deformazioni ammissibili, collegando tale riduzione a triplette e quaternioni?

Il risultato atteso non è soltanto una mesh visualizzabile: è un modello identificabile, calibrabile e falsificabile con dati sperimentali.

## 2. Catena geometrica: cubo → sfera → pannelli → cuciture

Si parte da una geometria di riferimento centrata. Per il cubo (C_a=[-a,a]^3), il raggio nella direzione unitaria (n) è
\[
r_C(n)=\frac{a}{\|n\|_\infty}.
\]
La sfera inscritta ha (r_S(n)=a); la differenza
\[
\Delta r(n)=a\left(\frac1{\|n\|_\infty}-1\right)
\]
quantifica l'anisotropia radiale del cubo rispetto alla sfera. È un dato geometrico, non ancora una legge costitutiva.

La geometria viene poi discretizzata in pannelli. La prima istanza di lavoro già usata nel dossier è:
- 92 nodi geometrici;
- 180 triangoli CST per la parte membranale;
- 270 cerniere/hinges per il contributo flessionale discreto;
- 90 cuciture/interfacce.

Questa è una discretizzazione di riferimento, non una mesh sperimentale certificata. Vanno conservati identificativi dei pannelli, orientamento locale, bordo condiviso, materiale e famiglia di cucitura.

La mappa globale che deforma la mesh di riferimento deve essere la stessa su entrambi i lati di ogni bordo condiviso. In tal modo la geometria dei bordi coincide per costruzione; la continuità cinematica e la trasmissione degli sforzi attraverso la cucitura sono poi imposte dal modello d'interfaccia. Non vanno confuse conformità geometrica e perfetta adesione meccanica.

## 3. Modello shell e costitutiva ortotropa

Per ogni pannello si definisce una terna locale: direzione 1 (ordito/trama principale), direzione 2 (direzione trasversa nel piano), direzione 3 (normale). In ipotesi di ortotropia piana e stato di tensione piano:
\[
\begin{bmatrix}\sigma_{11}\\\sigma_{22}\\\tau_{12}\end{bmatrix}
=
\begin{bmatrix}
Q_{11}&Q_{12}&0\\
Q_{12}&Q_{22}&0\\
0&0&Q_{66}
\end{bmatrix}
\begin{bmatrix}\epsilon_{11}\\\epsilon_{22}\\\gamma_{12}\end{bmatrix},
\]
con
\[
Q_{11}=\frac{E_1}{1-\nu_{12}\nu_{21}},\quad
Q_{22}=\frac{E_2}{1-\nu_{12}\nu_{21}},\quad
Q_{12}=\frac{\nu_{12}E_2}{1-\nu_{12}\nu_{21}},\quad
Q_{66}=G_{12},\quad
\nu_{21}=\nu_{12}\frac{E_2}{E_1}.
\]
La positività richiede (E_1>0,E_2>0,G_{12}>0) e (1-\nu_{12}\nu_{21}>0). I parametri vanno misurati o calibrati: nessun valore dimostrativo deve essere presentato come proprietà del pallone reale.

Per grandi rotazioni si usa la deformazione di Green–Lagrange, costruita dal tensore di Cauchy–Green (C=F^TF):
\[
E=\frac12(C-I).
\]
Per uno shell completo si separano deformazione membranale, curvatura e accoppiamento membrana-flessione. La riduzione a CST + hinges è una scelta discreta che va confrontata con una formulazione shell continua o con elementi shell standard, soprattutto per dipendenza dalla mesh e locking.

## 4. Cuciture: legge d'interfaccia, non semplice bordo condiviso

Per una cucitura (Gamma_s) tra pannelli (+) e (-), si definiscono:
- salto di spostamento ([u]=u^+-u^-);
- salto di rotazione/pendenza ([\theta]);
- trazione (t^\pm=\sigma^\pm n^\pm);
- momento risultante (m^\pm).

Una legge elastica lineare iniziale può essere scritta come
\[
t_s=K_u[u],\qquad m_s=K_\theta[\theta],
\]
con matrici di rigidezza che possono essere anisotrope e accoppiate. Nel limite (K_u,K_\theta\to\infty) si recupera il vincolo di continuità ideale; per rigidezze finite la cucitura ammette scorrimento/apertura/rotazione secondo la legge scelta.

Le condizioni di equilibrio richiedono bilancio delle trazioni e dei momenti, includendo i contributi della cucitura. Il richiamo alle condizioni di raccordo di tipo Darmois–Israel è soltanto un'analogia metodologica sul ruolo dei salti e delle leggi d'interfaccia: qui si tratta di meccanica dei solidi, non di una condizione relativistica di giunzione.

## 5. Sottospazi tangenti, vincoli e Hessiana ridotta

Per la configurazione vincolata (X\in\mathbb R^{3N}), i vincoli sono
\[
c(X)=0,\qquad J(X)=\frac{\partial c}{\partial X}.
\]
Una perturbazione ammissibile soddisfa
\[
J(X)\,\delta X=0.
\]
Scegliendo una base ortonormale (Q) del nucleo di (J):
\[
JQ=0,\qquad Q^TQ=I,\qquad \delta X=Q\xi.
\]
Il proiettore sul sottospazio tangente è (P_T=QQ^T). Se (H) è la Hessiana dell'energia vincolata (con i termini dei moltiplicatori di Lagrange), la Hessiana ridotta è
\[
H_T=Q^THQ.
\]
Questa è la matrice che descrive la stabilità lineare rispetto alle perturbazioni compatibili con i vincoli.

**Due spazi distinti non vanno confusi.** Nel framework (O_h) a 64 punti sono stati registrati 192 gradi cartesiani, 4 vincoli indipendenti e quindi uno spazio tangente di dimensione 188, rappresentato da (Q\in\mathbb R^{192\times188}). Il modello shell a 92 nodi ha invece 276 coordinate cartesiane prima dei vincoli. Per trasferire il metodo al pallone serve costruire il Jacobiano dei vincoli shell e calcolare una nuova base (Q_{\rm shell}\in\mathbb R^{276\times(276-r)}). Non si può riutilizzare direttamente la matrice (Q) 192×188.

## 6. Triplette e quaternioni: collegamento cinematico controllato

Una rotazione infinitesima comune nello spazio è generata da
\[
G_a(X)_i=e_a\times X_i,\qquad a=1,2,3.
\]
Le tre direzioni (G_1,G_2,G_3) formano la tripletta dei modi rotazionali rigidi (quando non sono eliminate da vincoli o condizioni al bordo). Vanno separate da:
- triplette spettrali, cioè sottospazi di modi con molteplicità tre;
- irriducibili (T_{1u}) e (T_{2u}) dell'azione del gruppo cubico (O_h);
- eventuali triplette di parametri o direzioni materiali.

La rappresentazione quaternionica della rotazione è
\[
q=\cos\frac{\alpha}{2}+\hat n\sin\frac{\alpha}{2},\qquad
v' = qvq^{-1},
\]
dove (v) è identificato con un quaternione puro. Per piccole rotazioni (q\simeq1+\frac12\boldsymbol\omega). Questa rappresentazione evita singolarità parametrica e permette di comporre rotazioni finite. Non crea da sola una nuova legge costitutiva: serve a descrivere orientazioni dei pannelli, frame locali e cinematica del corpo.

Il raccordo corretto è quindi: orientazioni dei pannelli e rotazioni finite rappresentate da quaternioni; variazioni infinitesime proiettate nello spazio tangente; modi rotazionali identificati separatamente dalle deformazioni elastiche. La compatibilità tra triplette spettrali e rappresentazioni quaternioniche va verificata tramite proiettori e intertwiners, non dedotta dalla sola presenza di tre componenti.

## 7. Raccordo con il pallone e l'effetto Magnus

Il pallone è il caso applicativo per una struttura chiusa deformabile. La geometria e la costitutiva possono influenzare:
- deformazione durante il contatto piede-pallone;
- orientazione e velocità angolare dopo il distacco;
- rugosità, cuciture e distribuzione di massa;
- deformazione aerodinamica e condizioni al contorno del flusso.

L'effetto Magnus, però, nasce dall'interazione tra rotazione, flusso e circolazione aerodinamica. Una mesh strutturale da sola non lo dimostra. Per collegare il modello strutturale alla traiettoria occorre accoppiare almeno:
\[
m\dot v=mg+F_D+F_M,\qquad
I\dot\omega=\tau_{\rm aero}+\tau_{\rm contact},
\]
con (F_M) stimata o identificata da prove/CFD e non inserita come conseguenza automatica della geometria delle cuciture. La struttura può fornire parametri e condizioni al contorno per il modello aerodinamico.

## 8. Protocollo di scansione e validazione

Per rendere il dossier presentabile a un partner tecnico occorre associare a ogni scansione:
- geometria 3D a riposo e in almeno due stati di pressione/carico;
- posizione e tracciamento delle cuciture;
- orientazione locale di pannelli e trama;
- materiale, spessore, massa areale e condizioni di pressione;
- ripetibilità della scansione e incertezza strumentale;
- prova di compressione/indentazione e, se possibile, prova di trazione/taglio su provini.

La validazione confronta nuvola di punti e mesh mediante registrazione rigida, distanza signed/unsigned, errore normale, errore di curvatura e distribuzione spaziale dei residui. I parametri ortotropi e di cucitura vanno identificati su una parte dei dati e verificati su scansioni/prove tenute fuori dalla calibrazione.

## 9. Piano di lavoro proposto

1. **Geometria:** ricostruire la superficie media dal riferimento cubico/sferico; fissare pannellizzazione, orientamenti e topologia delle cuciture.
2. **Cinematica:** definire i vincoli, calcolare (J), (Q_{\rm shell}), (P_T) e separare i sei moti rigidi (tre traslazioni e tre rotazioni) quando liberi.
3. **Meccanica:** implementare shell membranale/flessionale, ortotropia e legge di cucitura; verificare energia positiva, equilibrio e convergenza di mesh.
4. **Riduzione modale:** calcolare Hessiana ridotta, modi, triplette e loro trasformazione sotto (O_h); rappresentare le rotazioni finite con quaternioni.
5. **Dati:** acquisire scansioni e prove, calibrare parametri, stimare incertezza e validare su dati indipendenti.
6. **Aerodinamica:** accoppiare solo dopo il modello strutturale validato, per testare l'ipotesi sul contributo delle cuciture alla risposta in volo e all'effetto Magnus.

## 10. Stato delle affermazioni

- **Identità geometriche:** raggio radiale cubico e differenza cubo-sfera.
- **Formulazione matematica:** vincoli, spazio tangente, proiettore, Hessiana ridotta, costitutiva ortotropa, cinematica quaternionica.
- **Implementazione preliminare registrata:** modello discreto 92 nodi / 180 CST / 270 hinges / 90 cuciture; parametri di materiale dimostrativi.
- **Da validare con dati:** parametri ortotropi reali, rigidezze di cucitura, risposta sotto pressione/carico, accuratezza rispetto alle scansioni.
- **Ipotesi da testare:** contributo specifico di pannellizzazione e cuciture alla traiettoria e all'effetto Magnus.
- **Non dichiarato:** dimostrazione sperimentale dell'effetto Magnus, identificazione di materiale reale, validazione industriale o equivalenza tra il modello a 64 punti e la shell a 92 nodi.

## 11. Deliverable tecnico

Il dossier per la discussione è composto da questa nota progettuale e dall'appendice tecnica associata. La nota definisce il problema, il piano e le verifiche richieste; l'appendice espone in dettaglio vincoli, spazi tangenti, shell, cuciture, ortotropia, triplette, quaternioni e metriche di confronto sperimentale.
