# Q6: cariche dei singoli esagrammi, campi di fase, moiré e correlazioni

**Data di formalizzazione:** 12 novembre 2026  
**Destinazione:** dossier Morandotti — RGS–PRISM  
**Stato:** specifica matematica e programma di verifica; non è presentata come legge fisica già validata.

## 1. Scopo e separazione dei livelli

Questo documento formalizza una possibile catena di raccordo tra (i) i 64 esagrammi, (ii) osservabili di carica assegnati ai singoli stati, (iii) due campi generati da un circuito, (iv) il campo relativo/moiré e (v) correlazioni temporali o dinamiche di tipo Green–Kubo.

La catena è una proposta di ricerca falsificabile. I conteggi combinatori e le identità del complesso sono esatti; l'assegnazione fisica delle cariche, la legge dei campi, la dinamica e l'eventuale legge di trasporto richiedono definizioni operative, dati e verifiche indipendenti.

Non si identifica in partenza l'esagramma con una particella, una carica elettrica o un difetto cristallino. La parola *carica* indica qui un osservabile vettoriale o scalare da definire sperimentalmente o derivare dal modello del circuito.

## 2. Spazio degli stati e complesso cubico

Si rappresentano i sei bit di un esagramma mediante
\[
\mathcal H=\{0,1\}^6.
\]
Due stati sono adiacenti se differiscono in esattamente un bit. Il grafo degli stati è quindi il grafo ipercubico \(Q_6\), con
\[
|V|=2^6=64,\qquad |E|=6\,2^5=192.
\]
Il numero delle facce quadrate bidimensionali del cubo è
\[
|F_2|=\binom{6}{2}2^{4}=240.
\]
Questi conteggi si riferiscono al complesso cubico standard di \(Q_6\); eventuali quozienti, identificazioni o sottocomplessi devono essere dichiarati separatamente.

Siano \(C^k(Q_6;\mathbb R)\) gli spazi delle co-catene e
\[
C^0\xrightarrow{d_0}C^1\xrightarrow{d_1}C^2.
\]
Con orientazioni coerenti, le matrici di incidenza soddisfano esattamente
\[
d_1d_0=0.
\]
La relazione dice che il cobordo di un cobordo è nullo. Non è una legge costitutiva e non afferma che una sorgente fisica di difetto sia nulla.

## 3. Cariche sui singoli esagrammi

Si definisca un osservabile
\[
q:\mathcal H\to\mathbb R^m,\qquad h\mapsto q(h),
\]
con \(m\) fissato dal numero di componenti misurate. La definizione di \(q(h)\) deve provenire da una regola esplicita: lettura dei due campi del circuito, misura, oppure mappa derivata da un modello microscopico.

Per evitare che un'aggregazione nasconda informazione, il dato primario è il vettore di 64 valori \(\{q(h)\}_{h\in\mathcal H}\). Medie per classi di simmetria o per sottografi sono quantità derivate e devono conservare la tracciabilità verso gli stati originali.

Per una transizione orientata \(e=(h\to h')\), si può definire un flusso di stato \(j(e)\). Il bilancio locale su un vertice si scrive, con la convenzione di incidenza scelta,
\[
(\partial_1 j)(h)=s(h),
\]
dove \(s(h)\) è una sorgente/pozzo misurabile o imposta dal modello. In assenza di sorgenti, il bilancio è \(\partial_1j=0\). La convenzione di segno e l'eventuale peso/probabilità delle transizioni vanno specificati nel dataset.

**Non segue** dal solo conteggio dei 64 stati che esista una carica conservata. La conservazione è un'ipotesi da testare confrontando cariche e flussi durante le transizioni.

## 4. Due campi del circuito e campo relativo

Siano \(\theta_1,\theta_2\) due campi di fase definiti sui vertici, oppure due campi misurati dal circuito con una loro mappa di fase esplicitata. Nel caso di fasi reali monodrome, il campo relativo è
\[
\Delta\theta=\theta_1-\theta_2,
\qquad
\eta=d_0\Delta\theta\in C^1(Q_6;\mathbb R).
\]
Per costruzione
\[
d_1\eta=d_1d_0\Delta\theta=0.
\]
Quindi un campo relativo ottenuto come differenza di due potenziali globali reali è esatto e chiuso: la sua circolazione su ogni ciclo chiuso è nulla. Non può, da solo, rappresentare una dislocazione con winding non nullo.

Per descrivere fasi fisiche modulo \(2\pi\), occorre invece trattare campi a valori in \(S^1\), sollevamenti locali, transizioni di gauge e possibili tagli/olonomie. In tal caso il winding lungo un ciclo \(\gamma\) è una quantità intera (quando ben definita):
\[
w(\gamma)=\frac{1}{2\pi}\sum_{e\in\gamma}\operatorname{unwrap}(\delta\theta_e).
\]
La definizione numerica di unwrap, la scelta dei rami e la stabilità rispetto al rumore devono essere specificate. Per difetti orientazionali/disclinazioni è necessario inoltre un campo di orientazione o una connessione con olonomia; una fase scalare non è sufficiente.

Il termine *moiré* è riservato al pattern osservabile generato dall'interferenza/variazione relativa dei due campi, non alla sola differenza simbolica. Va definito attraverso un osservabile (intensità, fase relativa, spettro spaziale o correlazione) e confrontato con i dati del circuito.

## 5. Separazione tra dislocazioni e disclinazioni

La componente traslazionale (Burgers) e quella rotazionale (Frank) devono restare distinte. Nel benchmark elastico piano, il difetto entra tramite una sorgente di incompatibilità della deformazione, non tramite la sola identità di complesso:
\[
\operatorname{Inc}_h\epsilon_h=\zeta_h,
\qquad
\zeta_h=\zeta_h^{\mathrm B}+\zeta_h^{\mathrm F}.
\]
Qui \(\operatorname{Inc}_h\), \(\epsilon_h\) e le due componenti della sorgente devono essere costruite in modo compatibile con il modello continuo di riferimento e con la regolarizzazione del core. La chiusura \(d_1d_0=0\) è un vincolo cinematico distinto e non produce automaticamente \(\zeta_h\).

Per il passaggio da campi di fase del circuito a Burgers/Frank occorre una mappa derivata, con unità, orientazioni, trasformazione e condizioni al contorno esplicite. Non si assume tale identificazione in assenza di una derivazione.

## 6. Dinamica degli stati e correlazioni

Sia \(P(h,h')\) una matrice di transizione stocastica su \(\mathcal H\), con distribuzione stazionaria \(\pi\). Per un osservabile centrato \(q\), cioè \(\sum_h\pi(h)q(h)=0\), si definisce la correlazione
\[
C_q(n)=\sum_{h,h'\in\mathcal H}
\pi(h)P^n(h,h')\,q(h)\otimes q(h').
\]
Per osservabili vettoriali va dichiarata la componente o la contrazione usata. Se il processo è stazionario e la serie è sommabile, una convenzione discreta simmetrizzata per la correlazione integrata è
\[
K_q=\frac12 C_q(0)+\sum_{n=1}^{\infty}
\frac{C_q(n)+C_q(n)^T}{2}.
\]
Se il passo temporale è \(\Delta t\), il coefficiente fisico richiede la moltiplicazione per \(\Delta t\) e gli eventuali fattori di volume, temperatura o normalizzazione previsti dalla grandezza fisica. Questa formula è una definizione di correlazione integrata; non è automaticamente una legge di trasporto per il materiale.

Per una corrente \(J\), la formula Green–Kubo va costruita sulla corrente centrata e con le convenzioni dell'ensemble e della risposta lineare del sistema in esame. Prima di interpretare \(K_J\) come conducibilità, diffusività o coefficiente elastico dissipativo occorre derivare la relazione di risposta e verificare stazionarietà, convergenza della correlazione e corretta normalizzazione.

## 7. Protocollo minimo di verifica

1. **Enumerazione:** generare i 64 stati, le 192 adiacenze e le 240 facce; controllare orientazioni e conteggi.
2. **Complesso:** costruire matrici intere di incidenza e verificare \(d_1d_0=0\) esattamente.
3. **Cariche:** pubblicare la tabella completa dei 64 stati con definizione, unità, incertezza e provenienza di ogni componente di \(q(h)\).
4. **Transizioni:** stimare o derivare \(P\), verificare normalizzazione, eventuale stazionarietà e bilanci locali.
5. **Campi:** archiviare \(\theta_1,\theta_2\), il campo relativo, il pattern moiré osservato e la procedura di unwrap.
6. **Difetti:** calcolare winding/olonomie e confrontarli con sorgenti Burgers/Frank indipendentemente definite.
7. **Correlazioni:** calcolare autocorrelazioni e correlazioni incrociate, stimare l'incertezza e verificare la convergenza della somma Green–Kubo rispetto alla finestra temporale.
8. **Confronto Morandotti:** soltanto dopo aver definito la mappa verso \(\zeta_h\), confrontare energia, stress e campi con Airy/CIP-DG a parità di core, materiale e condizioni al bordo.

## 8. Criteri di falsificazione e limiti

La proposta va respinta o modificata se: (a) le cariche non sono riproducibili a livello dei singoli stati; (b) il pattern relativo non è distinguibile dal rumore o da artefatti di fase; (c) i winding dipendono instabilmente dalla scelta dei rami; (d) il bilancio locale non è compatibile con le transizioni osservate; (e) le correlazioni non sono stazionarie o non sommabili nel regime dichiarato; (f) la mappa verso Burgers/Frank non riproduce i benchmark elastici.

**Classificazione finale**
- conteggi di \(Q_6\) e identità del complesso: **esatti**;
- cariche per esagramma: **osservabili da definire/misurare**;
- campo moiré dai due campi: **modello da specificare e verificare**;
- winding e sorgenti Burgers/Frank: **ponte matematico aperto**;
- Green–Kubo: **formalismo disponibile; dinamica, corrente e coefficienti fisici da validare**;
- legge costitutiva/di trasporto RGS risultante: **non dimostrata**.

## 9. Relazione con il benchmark Morandotti

Questo programma non sostituisce il benchmark piano di difetti. È un possibile livello microscopico/discreto aggiuntivo. Il confronto con il modello di Cesana–De Luca–Morandotti richiede una mappa esplicita da stati/campi a sorgenti di incompatibilità, la stessa regolarizzazione del core, lo stesso tensore elastico e condizioni al contorno allineate. Fino a quel momento il raccordo è una domanda matematica, non un'equivalenza.

## Riferimenti interni

- [Appendice tecnica Morandotti–RGS–PRISM](../manuscripts/APPENDICE_TECNICA_MORANDOTTI_RGS_PRISM.md)
- [Nota progettuale Morandotti–RGS–PRISM](../manuscripts/NOTA_PROGETTUALE_MORANDOTTI_RGS_PRISM.md)
- [Benchmark variazionale Saint-Venant/KKT](../manuscripts/MORANDOTTI_BENCHMARK_I_DISCRETE_SAINT_VENANT_KKT.md)
- [Record del quoziente cinematico Q6–PRISM già integrato nella PR #119](../docs/rgs_defect_benchmark/Q6_PRISM_KINEMATIC_MAP.md)
