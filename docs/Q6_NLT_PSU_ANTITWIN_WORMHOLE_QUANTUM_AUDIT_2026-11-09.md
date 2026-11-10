# Q6–NLT / PSU–Anti-Twin / wormhole: audit variazionale e programma quantistico

**Stato:** derivazione strutturale; nessuna identificazione fisica o soluzione accoppiata è ancora dimostrata.  
**Scopo:** stabilire quali passaggi matematici sono leciti prima di accoppiare la dinamica di fase Q6 al wormhole EMS.

## 1. Convenzioni

Siano (B_1\in\mathbb R^{64\times192}) e (B_2\in\mathbb R^{192\times240}) le matrici di bordo del complesso Q6, con (B_1B_2=0). Le fasi sono
\[
\theta\in\mathbb T^{64},\qquad \phi\in\mathbb T^{192}.
\]
Poniamo
\[
A(\theta)=B_1\sin(B_1^T\theta),\quad
C(\phi)=B_1^T\sin(B_1\phi),\quad
D(\phi)=B_2\sin(B_2^T\phi).
\]
I seni sono componente per componente. Indichiamo gli ordini con
(r_0(\theta),r_d(\phi),r_u(\phi)), corrispondenti a (R_0,R_{1,down},R_{1,up}).

Nel sistema rotante, se le frequenze naturali sono uniformi e quindi rimovibili, i campi di fase diventano:

**NL**
\[
F_\theta=-\sigma r_d(\phi)A(\theta),\qquad
F_\phi=-\sigma r_0(\theta)C(\phi)-\sigma D(\phi).
\]

**NLT**
\[
F_\theta=-\sigma r_d(\phi)A(\theta),\qquad
F_\phi=-\sigma r_0(\theta)r_u(\phi)C(\phi)
         -\sigma r_d(\phi)D(\phi).
\]

Se le frequenze \(\omega,\widetilde\omega\) sono eterogenee, un unico sistema rotante non le elimina: i termini di drift vanno mantenuti e costituiscono un'ulteriore sorgente di non-equilibrio.

## 2. Test necessario per l'esistenza di un potenziale

Se il campo fosse un gradiente euclideo (F=-\nabla U), le derivate miste dovrebbero coincidere:
\[
\frac{\partial F_{\theta_i}}{\partial\phi_e}
=
\frac{\partial F_{\phi_e}}{\partial\theta_i}.
\]

Per NL si ottiene la condizione necessaria
\[
\boxed{
\frac{\partial r_d}{\partial\phi_e}A_i(\theta)
=
\frac{\partial r_0}{\partial\theta_i}C_e(\phi)
\quad\text{per ogni }i,e.}
\tag{NL-IC}
\]

Per NLT:
\[
\boxed{
\frac{\partial r_d}{\partial\phi_e}A_i(\theta)
=
\frac{\partial r_0}{\partial\theta_i}r_u(\phi)C_e(\phi)
\quad\text{per ogni }i,e.}
\tag{NLT-IC}
\]

La seconda condizione è indipendente dal termine (D\) perché quel termine non dipende da \(\theta\). Le condizioni sono uguaglianze fra prodotti esterni di vettori: non sono identità topologiche conseguenti a (B_1B_2=0). In generale non valgono per ordini d'ordine non costanti. Quindi **non è lecito assegnare automaticamente un potenziale scalare né interpretare il gap numerico come barriera energetica**.

Più in generale, per una mobilità positiva (M(X)), la condizione è che (M^{-1}F) sia un campo chiuso (e, sul dominio considerato, esatto). Una mobilità non diagonale può cambiare il test; va specificata e verificata, non scelta a posteriori per forzare il risultato.

## 3. Cosa si può chiamare energia congelata

Se si congelano i coefficienti d'ordine (r_0,r_d,r_u), i singoli termini sinusoidali hanno primitive formali. Ad esempio, con coefficienti costanti:
\[
U_{\rm frozen}^{NL}
=-\sigma r_d\sum_{v=1}^{64}\cos((B_1^T\theta)_v)
 -\sigma r_0\sum_{e=1}^{192}\cos((B_1\phi)_e)
 -\sigma\sum_{p=1}^{240}\cos((B_2^T\phi)_p).
\]
Per NLT i coefficienti dei due blocchi di \(\phi\) diventano rispettivamente \(r_0r_u\) e \(r_d\). Questa è un'energia a coefficienti congelati, non il potenziale della dinamica completa: quando gli ordini dipendono dalle fasi, la derivata di (U_{frozen}) omette i termini di derivazione dei coefficienti. È utile solo come approssimazione adiabatica da sottoporre a verifica.

## 4. Conseguenza per il collegamento al wormhole

L'azione euclidea conservativa
\[
S_E[X]=\int d\tau\left[
\frac12G_{AB}(X)\dot X^A\dot X^B+V(X)
\right]
\]
è utilizzabile per un istantone solo se è stata derivata una dinamica conservativa efficace con metrica cinetica (G) e potenziale (V), e se i due stati collegati sono punti stazionari appropriati di (V).

La dinamica NL/NLT fornita è invece dissipativa/non-equilibrio in generale. Se il test di integrabilità fallisce, la via corretta non è inventare (U_{Q6}), ma formulare un problema stocastico di transizione. Per una dinamica ridotta
\[
\dot q=b(q;\sigma)+\sqrt{2\varepsilon}\,\eta(\tau),
\]
con rumore bianco normalizzato e matrice di diffusione identità, l'azione di Freidlin–Wentzell è
\[
I[q]=\frac14\int
\|\dot q-b(q;\sigma)\|^2\,d\tau.
\]
Con diffusione (D(q)), il costo diventa
\[
I[q]=\frac14\int
(\dot q-b)^TD^{-1}(\dot q-b)\,d\tau.
\]
Il minimizzatore fra bacini fornisce un quasi-potenziale e un esponente di transizione nel limite di rumore debole. Questo è distinto dall'azione euclidea gravitazionale del wormhole.

Il ponte fisicamente consistente può quindi avere due livelli:
1. il settore wormhole EMS conserva la propria azione euclidea gravitazionale/scalare;
2. il settore Q6/NLT fornisce una dinamica ridotta e, se necessario, un costo di transizione non-equilibrio;
3. un accoppiamento (gW(R_{th})\,\mathcal C(q_+,q_-)) è ammesso solo dopo aver definito \(\mathcal C\), la simmetria Anti-Twin e la provenienza di (W) dalle equazioni ridotte o da un principio variazionale esplicito.

Non si deve sommare direttamente (I[q]) e (S_E^{WH}) come se fossero la stessa azione: hanno origini e significati diversi. Per combinarli serve una teoria stocastica-gravitazionale o una derivazione microscopica che specifichi rumore, dissipazione e backreaction.

## 5. Riduzione collettiva minima da testare

Una scelta controllabile di coordinate d'ordine è
\[
q=(r_0,r_d,r_u),\qquad
q_+=(r_0^+,r_d^+,r_u^+),\quad
q_-=(r_0^-,r_d^-,r_u^-).
\]
Le coordinate sono soggette ai vincoli del loro dominio (in particolare non si deve supporre che i tre ordini siano indipendenti). Si deve prima calcolare il Jacobiano completo del sistema di fase e identificare:
- punti fissi nel frame appropriato;
- autovalori e autovettori della linearizzazione;
- eventuali biforcazioni al variare di \(\sigma\);
- dipendenza dai seed e dalla dimensione della finestra di scansione;
- persistenza o scomparsa del gap quando la velocità di scansione tende a zero.

Un gap finito in quattro velocità di scansione e con deviazioni standard ampie non prova due attrattori: può derivare da transitori, campionamento, rumore, mancata convergenza o isteresi dinamica.

## 6. Accoppiamento Anti-Twin e wormhole: ansatz da verificare

La quantità di disaccordo tra i fogli può essere definita senza assegnarle ancora un significato energetico:
\[
\mathcal C(q_+,q_-)
=\frac12(q_+-q_-)^T\Lambda(q_+-q_-),
\qquad \Lambda\succeq0.
\]
È invariante sotto lo scambio (q_+\leftrightarrow q_-). Un ansatz di interazione è
\[
V_{int}=gW(R_{th})\mathcal C(q_+,q_-).
\]
Questo termine è un **ansatz fenomenologico**, non una conseguenza già dimostrata di NLT o delle equazioni EMS. Per derivarlo occorre:
1. definire quali gradi di libertà Q6 vivono sui due fogli;
2. specificare la regola di identificazione al collo;
3. ridurre l'azione EMS con tali condizioni al contorno;
4. verificare la simmetria Anti-Twin e la positività/stabilità del termine;
5. evitare doppio conteggio fra energia Q6 e energia gravitazionale.

Solo dopo questi passaggi si può calcolare l'Hessiano accoppiato e cercare un istantone del sistema conservativo risultante. In alternativa, nel caso non-equilibrio, si calcola un costo di transizione stocastico accoppiato alla geometria, senza chiamarlo istantone euclideo.

## 7. Test falsificabili e ordine di esecuzione

**Test A — integrabilità.** Valutare numericamente il rotore incrociato NL-IC e NLT-IC su configurazioni casuali e lungo le traiettorie; usare differenze finite verificate con più passi. Un residuo non nullo stabile falsifica un potenziale euclideo ordinario per il campo completo.

**Test B — stabilità.** Calcolare gli autovalori del Jacobiano completo delle fasi in corrispondenza dei punti fissi. Distinguere stabilità lineare, cicli limite e transitori.

**Test C — quasi-staticità.** Ripetere scansioni con velocità progressivamente ridotte e più seed, intervalli di confidenza e criteri di arresto; il gap va estrapolato, non semplicemente letto all'ultima velocità.

**Test D — riduzione.** Verificare che le tre coordinate d'ordine chiudano una dinamica autonoma o quantificare i termini di memoria/non-Markoviani. Senza chiusura, non sono coordinate collettive sufficienti.

**Test E — wormhole.** Solo dopo A–D, introdurre l'accoppiamento ai gradi di libertà EMS, ricalcolare le equazioni del collo, il sistema di fluttuazioni e gli autovalori dell'Hessiano. Il precedente audit EMS (azione euclidea riportata (0.68223), autovalori Hessiani (-1.03758,1.51486,3.82636)) è un benchmark separato, non il risultato del sistema accoppiato.

## 8. Criterio di successo

Il collegamento sarà considerato dimostrato a livello matematico solo se si ottengono, nell'ordine:
- una definizione riproducibile degli ordini (r_0,r_d,r_u);
- il test d'integrabilità e la classificazione equilibrata/non-equilibrata;
- una riduzione collettiva con errore controllato;
- una derivazione dell'accoppiamento al collo dalle equazioni/azione EMS, oppure una dichiarazione esplicita del suo carattere fenomenologico;
- una soluzione numerica convergente del problema di transizione pertinente;
- confronto NL/NLT con controlli su seed, scansione e rumore.

**Conclusione attuale:** il collegamento NL/NLT–wormhole è una linea di ricerca coerente, ma il passaggio corretto è prima un audit di non-equilibrio. NLT può suggerire metastabilità; non dimostra da sola una doppia buca, una barriera energetica o tunnelling. Il wormhole può fornire il settore geometrico del collo; non trasforma automaticamente una dinamica dissipativa in un'azione euclidea.
