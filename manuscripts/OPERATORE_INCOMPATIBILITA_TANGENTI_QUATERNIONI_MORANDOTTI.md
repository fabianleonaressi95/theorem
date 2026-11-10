# Dall'architettura tangente–quaternionica all'operatore discreto di incompatibilità

**Nota di derivazione per il dossier Morandotti — RGS–PRISM**  
**Stato:** formulazione matematica proposta e specifica verificabile. L'operatore qui definito non è ancora implementato né validato su una famiglia curva RGS–PRISM. Le identità continue e le definizioni discrete vanno tenute distinte dai risultati numerici già archiviati.

## 1. La domanda precisa

Vogliamo costruire una mappa discreta che, data una deformazione simmetrica, restituisca una sorgente di incompatibilità:
\[
\operatorname{Inc}_h\epsilon_h=\zeta_h.
\]
La sorgente deve poter rappresentare separatamente:
- dislocazioni, parametrizzate dal vettore di Burgers \(b\);
- disclinazioni, parametrizzate dal vettore/angolo di Frank \(s\);
- difetti distribuiti o regolarizzati su un core finito.

La costruzione deve essere compatibile con la geometria RGS: i gradi di libertà devono rispettare i vincoli tangenti, i frame locali devono poter essere trasportati senza ambiguità di coordinate e l'energia deve essere una forma variazionale coerente.

La tesi metodologica è:

**tangente = spazio delle variazioni ammissibili; quaternioni = rappresentazione del trasporto rotazionale; triplette = settori modali; incompatibilità = operatore differenziale/discreto sulla deformazione.**

Non si deve identificare nessuno di questi quattro oggetti con gli altri.

---

## 2. Riferimento continuo: incompatibilità di Saint-Venant in piano

Sia \(\epsilon\) un campo di deformazione simmetrico in un dominio piano:
\[
\epsilon(x)=
\begin{pmatrix}
\epsilon_{11}(x)&\epsilon_{12}(x)\\
\epsilon_{12}(x)&\epsilon_{22}(x)
\end{pmatrix}.
\]
Con la convenzione adottata in questo dossier, l'operatore scalare di incompatibilità è
\[
\operatorname{inc}\epsilon
=\partial_{22}\epsilon_{11}
+\partial_{11}\epsilon_{22}
-2\partial_{12}\epsilon_{12}.
\]
Per una deformazione compatibile \(\epsilon=\operatorname{sym}\nabla u\), con \(u\) sufficientemente regolare,
\[
\operatorname{inc}(\operatorname{sym}\nabla u)=0.
\]
Questa è l'identità di Saint-Venant. In presenza di deformazione plastica/incompatibile \(\epsilon^p\), la deformazione elastica è
\[
\epsilon^e=\operatorname{sym}\nabla u-\epsilon^p,
\]
e quindi, in senso distribuzionale,
\[
\operatorname{inc}\epsilon^e=-\operatorname{inc}\epsilon^p.
\]
La sorgente di difetto è dunque la incompatibilità della parte plastica, a segno fissato dalla convenzione scelta.

Per il potenziale di Airy \(v\), la tensione equilibrata è
\[
\sigma=\operatorname{cof}(D^2v),
\]
e la relazione elastica riportata nella nota Morandotti è
\[
\frac{1-\nu^2}{E}\,\Delta^2v=\zeta.
\]
Nel modello piano di dislocazioni/disclinazioni, la sorgente può essere scritta, con la convenzione già adottata, come
\[
\zeta=
\sum_j |b^j|\,
\partial_{(b^j)^\perp/|b^j|}\delta_{x^j}
-\sum_k s^k\delta_{y^k}.
\]
Il segno della distribuzione derivata va mantenuto coerente con la definizione di \(\partial_n\delta\); in particolare
\[
\langle\partial_n\delta_x,\varphi\rangle
=-\partial_n\varphi(x).
\]
Questa formula è il bersaglio continuo del benchmark piano, non una formula già dimostrata per la shell curva.

---

## 3. Riduzione tangente: come entrano i 188 gradi di libertà

La configurazione RGS contiene 64 punti in \(\mathbb R^3\), quindi il vettore ambientale appartiene a \(\mathbb R^{192}\). I quattro vincoli A14 (tre traslazioni del centroide e un vincolo radiale) definiscono
\[
J\in\mathbb R^{4\times192},\qquad
T_X\mathcal M=\ker J.
\]
La base ortonormale recuperata è
\[
Q\in\mathbb R^{192\times188},\qquad
JQ=0,\quad Q^TQ=I_{188}.
\]
Una variazione ammissibile è
\[
\delta x=Q\xi,\qquad \xi\in\mathbb R^{188}.
\]
Il proiettore è \(P_T=QQ^T\).

Per il guscio, con 92 nodi, si usa invece una base tangente nodale
\[
T_f=\operatorname{diag}(T_1,\ldots,T_{92})
\in\mathbb R^{276\times184},\qquad
T_i=(e_{1i},e_{2i}).
\]
Le coordinate tangenti sono \(\eta\in\mathbb R^{184}\) e lo spostamento ambientale è \(u=T_f\eta\).

Questi due tangenti hanno dimensioni diverse e non vanno identificati direttamente. Il trasferimento RGS→shell è una mappa geometrica distinta, già documentata, e deve essere applicato prima di confrontare sottospazi o operatori.

**Ruolo nell'incompatibilità:** la riduzione tangente entra nel gradiente discreto. Se \(G_h\) è il gradiente cinematico ambientale, la sua versione ammessa è
\[
G_h^{T}=G_hQ
\]
nel sistema RGS, oppure \(G_h^{T}=G_hT_f\) per il guscio, con le dimensioni adattate alle variabili nodali. La deformazione discreta è ottenuta simmetrizzando il gradiente nelle basi locali:
\[
\epsilon_h(\xi)=\operatorname{sym}(G_h^T\xi).
\]
La simmetrizzazione e la metrica locale devono essere definite nella stessa convenzione di coordinate; non basta proiettare vettori e poi trattare le componenti come se fossero tutte espresse nello stesso frame.

---

## 4. Definizione debole di un operatore discreto Inc_h

Una costruzione iniziale rigorosa può essere data in forma duale. Sia \(\mathcal T_h\) una triangolazione piana, \(\epsilon_h\) un campo simmetrico a tratti e \(V_h\subset H^2(\Omega)\) uno spazio di test globalmente \(C^1\)-conforme (per esempio un elemento di tipo Argyris o Hsieh–Clough–Tocher).

Per ogni \(\varphi_h\in V_h\), definiamo
\[
\boxed{
\langle\operatorname{Inc}_h\epsilon_h,\varphi_h\rangle
=
\sum_{K\in\mathcal T_h}
\int_K
\epsilon_h:\operatorname{cof}(D^2\varphi_h)\,dx.
}
\]
In due dimensioni,
\[
\operatorname{cof}(D^2\varphi)=
\begin{pmatrix}
\partial_{22}\varphi&-\partial_{12}\varphi\\
-\partial_{12}\varphi&\partial_{11}\varphi
\end{pmatrix}.
\]
La definizione è la forma distribuzionale di \(\operatorname{inc}\epsilon\), integrata contro funzioni test. Se \(V_h\) è conforme in \(H^2\), non occorrono termini artificiali di salto per definire questa azione duale: le derivate distribuzionali sono già rappresentate dall'integrazione contro la Hessiana del test.

Scelte alternative, come CIP-DG, sono possibili ma richiedono i termini di consistenza e penalizzazione specifici del metodo non conforme. Non si deve prendere la formula conforme e aggiungere penalità senza derivazione.

Scegliendo basi \(\{\psi_a\}\) per lo spazio delle deformazioni e \(\{\varphi_i\}\) per lo spazio test, la matrice dell'operatore è
\[
(A_h)_{ia}
=
\sum_K\int_K
\psi_a:\operatorname{cof}(D^2\varphi_i)\,dx.
\]
Se \(\epsilon_h=\sum_a e_a\psi_a\), il vettore residuo di incompatibilità è
\[
z=A_he.
\]
La sorgente assegnata si discretizza con
\[
(z_h)_i=\langle\zeta,\varphi_i\rangle.
\]
Il problema discreto diventa
\[
A_he=z_h.
\]
Questa è una definizione operativa dell'operatore debole, con spazi e quadrature espliciti. La sua convergenza e la stabilità dipendono dalla scelta delle famiglie \(\mathcal T_h,V_h\) e dalle stime uniformi.

### 4.1 Test di compatibilità esatta

Per un campo nodale continuo e affine a tratti \(u_h\), definiamo
\[
\epsilon_h=\operatorname{sym}\nabla_hu_h.
\]
Il test di base è
\[
A_h\,e(\operatorname{sym}\nabla_hu_h)=0
\]
per ogni funzione test ammessa, a meno degli errori di quadratura e della corretta gestione del bordo. È il test discreto che deve precedere qualsiasi simulazione con difetti.

### 4.2 Sorgenti di Burgers e Frank

Nel benchmark piano, per una dislocazione in \(x_j\) e una disclinazione in \(y_k\), il vettore di carico debole è costruito direttamente:
\[
(z_h)_i=
\sum_j |b^j|\,
\langle\partial_{n_j}\delta_{x_j},\varphi_i\rangle
-\sum_k s^k\varphi_i(y_k),
\qquad n_j=\frac{(b^j)^\perp}{|b^j|}.
\]
Usando la definizione distribuzionale:
\[
(z_h)_i=
-\sum_j|b^j|\,\partial_{n_j}\varphi_i(x_j)
-\sum_ks^k\varphi_i(y_k).
\]
La regolarizzazione core-radius sostituisce le delta e le loro derivate con distribuzioni supportate su dischi o anelli di core, secondo la stessa scelta del modello di riferimento. La regolarizzazione non può essere introdotta cambiando solo la quadratura: deve essere parte della definizione della sorgente.

---

## 5. Quaternioni: connessione, trasporto e olonomia

### 5.1 Il ruolo corretto del frame

Il frame locale \(R_f\in SO(3)\) di una faccia o patch viene rappresentato da un quaternione unitario \(q_f\in SU(2)\):
\[
p_{global}=q_fp_{local}q_f^{-1}.
\]
Il segno \(q_f\sim-q_f\) non cambia la rotazione. Questo è già implementato per i frame della shell.

Tuttavia, **i soli quaternioni dei frame non generano una curvatura**. Se si definisce l'elemento di collegamento come
\[
U_{fg}=q_f^{-1}q_g,
\]
il prodotto lungo un ciclo chiuso telescopa (a segni irrilevanti per SO(3)) e l'olonomia è identità: è una connessione di puro gauge. Per rappresentare disclinazioni serve una connessione discreta indipendente, non ricavata banalmente dalla differenza tra frame.

### 5.2 Connessione SU(2) discreta

Per ogni arco orientato del grafo duale si introduce
\[
U_{fg}\in SU(2),\qquad U_{gf}=U_{fg}^{-1}.
\]
Sotto un cambio di gauge locale \(g_f\in SU(2)\):
\[
U_{fg}\mapsto g_f^{-1}U_{fg}g_g.
\]
Per un ciclo orientato \(\partial p=(f_0f_1,\ldots,f_{m-1}f_m)\), con \(f_m=f_0\), l'olonomia è
\[
H_p=U_{f_0f_1}U_{f_1f_2}\cdots U_{f_{m-1}f_0}.
\]
Essa si trasforma per coniugio alla base \(f_0\):
\[
H_p\mapsto g_{f_0}^{-1}H_pg_{f_0}.
\]
La traccia e l'angolo di rotazione sono quindi invarianti di gauge. Per olonomie vicine all'identità:
\[
\Omega_p=\frac{1}{A_p}\operatorname{Log}(H_p)\in\mathfrak{su}(2),
\]
dove \(A_p\) è l'area duale e il logaritmo usa il ramo locale vicino all'identità. La parte vettoriale di \(\Omega_p\) rappresenta la densità di curvatura/Frank discreta, con la normalizzazione da fissare in base alla convenzione di SU(2) rispetto a SO(3).

**Conseguenza:** il frame quaternionico implementato fornisce la base locale; il campo \(U_{fg}\) è una nuova variabile di connessione, da introdurre soltanto se si vuole modellare una curvatura/disclinazione indipendente.

### 5.3 Torsione discreta e vettore di Burgers

La connessione da sola non definisce il Burgers: occorre anche una co-base (coframe) discreta \(\vartheta_e\), cioè la misura orientata degli spostamenti/lunghezze di riferimento espressi nei frame locali. La co-base deve includere la parte elastica e, se presente, la distorsione plastica.

Trasportando i contributi di bordo di una cella duale a un frame comune con i prodotti di \(U\), si definisce la chiusura traslazionale
\[
B_p=\sum_{e\subset\partial p}
\mathcal P_{e\to f_0}\,\vartheta_e,
\]
con orientazioni coerenti e \(\mathcal P\) prodotto dei link lungo il cammino. \(B_p\) è il candidato discreto al vettore di Burgers. In assenza di difetti e per una co-base integrabile, la chiusura deve annullarsi. La definizione esatta di \(\vartheta_e\), inclusi i fattori di lunghezza e la distinzione riferimento/deformato, è parte della futura legge cinematica: non è ancora implementata nel modello quaternionico della shell.

In linguaggio di Cartan, il bersaglio continuo è
\[
T^a=d\vartheta^a+\omega^a{}_b\wedge\vartheta^b,
\qquad
\Omega^a{}_b=d\omega^a{}_b+
\omega^a{}_c\wedge\omega^c{}_b.
\]
Torsione e curvatura sono oggetti distinti: la prima è associata alla densità di dislocazione/Burgers, la seconda alla densità di disclinazione/Frank, con convenzioni e normalizzazioni da fissare nel modello scelto.

---

## 6. Come si collegano Inc_h, Burgers e Frank

Il collegamento ha due livelli e non va compresso in un'identità non dimostrata.

### Livello A — elasticità piana di Morandotti

Si costruisce direttamente \(A_h\), la discretizzazione debole di Saint-Venant, e si impone
\[
A_he=z_h(b,s).
\]
Qui la sorgente \(z_h\) è definita dalle distribuzioni di Burgers e Frank nel benchmark piano. Questo livello consente un confronto diretto con il modello Airy/CIP-DG, mantenendo identici dominio, parametri elastici, core radius, sorgenti e condizioni al contorno.

### Livello B — geometria quaternionica/Cartan

Si introducono una connessione \(U_{fg}\) e una co-base \(\vartheta_e\); si misurano:
- olonomie \(H_p\) e curvature \(\Omega_p\), candidate alla componente Frank;
- chiusure traslazionali \(B_p\), candidate alla componente Burgers.

Occorre quindi derivare una mappa di calibrazione
\[
\mathcal S_h:(B_p,\Omega_p)_{p\in\mathcal P}
\longrightarrow z_h
\]
che converta i difetti geometrici nella sorgente debole dell'operatore di incompatibilità. La mappa deve riprodurre i campi di difetto analitici e rispettare le unità fisiche. Non è lecito porre semplicemente \(z_h=B_p+\Omega_p\): Burgers ha dimensione di lunghezza, Frank è un angolo, mentre la sorgente di Airy ha la dimensione determinata dalle convenzioni elastico-distribuzionali. La conversione richiede fattori geometrici e dimensionali espliciti.

La relazione da dimostrare è quindi
\[
\boxed{
A_h e_h
=
z_h
=
\mathcal S_h(B_h,\Omega_h).
}
\]
Il primo uguale è il problema discreto di incompatibilità; il secondo è il ponte geometrico-quaternionico ancora da derivare e calibrare.

---

## 7. Dove entrano le triplette

Le triplette non sono la sorgente di incompatibilità. Entrano dopo aver definito l'azione di simmetria sullo spazio discreto.

Sia \(D_h(g)\) la rappresentazione di una simmetria geometrica sullo spazio delle deformazioni e \(R_h(g)\) la sua azione sullo spazio test. Se geometria, connessione, sorgenti e condizioni al contorno rispettano la simmetria, l'operatore deve soddisfare la covarianza
\[
A_hD_h(g)=R_h(g)A_h.
\]
Nel caso in cui spazio test e spazio deformazioni portino la stessa rappresentazione ortogonale, questa diventa la condizione di commutazione.

Un proiettore sull'irriducibile \(\rho\) del gruppo finito \(G\) è
\[
P_\rho=
\frac{d_\rho}{|G|}
\sum_{g\in G}\overline{\chi_\rho(g)}D_h(g),
\]
quando si usa il carattere centrale e la rappresentazione è unitaria. Per isolare copie multiple e basi specifiche si usano gli operatori di matrice della rappresentazione, non soltanto il proiettore centrale.

La restrizione
\[
A_{h,\rho}=R_h(g)\text{-settore}\; A_h\; D_h(g)\text{-settore}
\]
è lecita solo dopo avere verificato la covarianza. Se il materiale ortotropo, le cuciture o i difetti rompono la simmetria, i settori si accoppiano e la decomposizione in triplette non è esatta.

Quindi:
- la tripletta geometrica delle rotazioni fornisce un settore cinematico di riferimento;
- le triplette spettrali sono cluster candidati;
- \(T_{1u}\), \(T_{2u}\) o altre etichette richiedono caratteri e azione di gruppo verificati;
- la compatibilità/incompatibilità è determinata da \(A_h\), non dal nome del settore.

---

## 8. Energia variazionale e confronto con CIP-DG

Il problema piano può essere formulato come minimizzazione dell'energia elastica sotto il vincolo di incompatibilità:
\[
\min_{\epsilon_h\in\mathcal E_h}
\frac12 a_h(\epsilon_h,\epsilon_h)
\quad\text{soggetto a}\quad
A_he=z_h.
\]
In alternativa si usa un Lagrangiano con moltiplicatore \(v_h\):
\[
\mathscr L_h(e,v)
=\frac12a_h(e,e)
+\langle A_he-z_h,v_h\rangle.
\]
Le equazioni di stazionarietà sono
\[
\begin{cases}
A_h e=z_h,\\
a_h(e,\delta e)+\langle A_h\delta e,v_h\rangle=0
\quad\forall\delta e.
\end{cases}
\]
Per recuperare la formulazione di Airy, la relazione tra il moltiplicatore \(v_h\), la tensione e la funzione di Airy va derivata con la stessa convenzione di elasticità e di bordo. Il metodo CIP-DG 2026 è la baseline numerica da confrontare: RGS non può essere presentato come prima discretizzazione FEM del problema.

Il confronto deve tenere fissi:
- dominio e geometria;
- materiale \(E,\nu\) e orientazione ortotropa, se presente;
- posizione, intensità e tipo di sorgenti;
- core radius e regolarizzazione;
- condizioni al contorno;
- norma dell'errore, energia, residui e costo computazionale.

Solo un vantaggio misurabile su stabilità, accuratezza, robustezza geometrica o costo giustifica un'affermazione di superiorità.

---

## 9. Estensione alla shell curva: ciò che cambia

La formula piana di \(\operatorname{inc}\) non si trasferisce a una superficie curva sostituendo semplicemente derivate parziali con derivate covarianti. La geometria di fondo contribuisce ai commutatori delle derivate e alla linearizzazione della curvatura.

Per una superficie \((M,g)\), il modello deve partire da:
- metrica superficiale \(g\);
- connessione di Levi-Civita o connessione materiale scelta;
- deformazione di membrana come tensore simmetrico tangente;
- curvatura seconda e sua variazione, se il modello include flessione;
- condizioni di cucitura/interfaccia tra pannelli.

L'operatore superficiale \(\operatorname{Inc}_g\) deve essere derivato dalla linearizzazione della condizione di compatibilità metrica/curvatura nella geometria scelta. Per la shell calcistica, con pannelli e cuciture, va inoltre separato il difetto di membrana dal salto rotazionale lungo le cuciture. La legge locale \(m=k_\theta\eta\) resta una legge d'interfaccia; un termine longitudinale compare solo se è introdotta un'energia di gradiente della rotazione.

La connessione quaternionica può rappresentare il trasporto dei frame tra patch e l'olonomia discreta; non elimina la necessità di derivare l'operatore superficiale e i termini di curvatura.

---

## 10. Piano di implementazione e test falsificabili

### Fase 1 — benchmark piano conforme
1. Generare triangolazioni di un dominio piano con raffinamenti successivi.
2. Implementare lo spazio test \(H^2\)-conforme e la matrice \(A_h\).
3. Verificare \(\operatorname{Inc}(\operatorname{sym}\nabla u)=0\) per campi polinomiali e spostamenti FE compatibili.
4. Verificare la sorgente analitica di una dislocazione e di una disclinazione contro il pairing distribuzionale.
5. Confrontare soluzione, energia e residui con baseline CIP-DG.

### Fase 2 — sorgenti con core
1. Sostituire delta e derivate di delta con profili core regolarizzati.
2. Verificare convergenza al limite core-radius e dipendenza dalla mesh.
3. Separare errore di quadratura, errore di discretizzazione e errore di regolarizzazione.

### Fase 3 — connessione SU(2) indipendente
1. Aggiungere variabili link \(U_{fg}\), non ricavate soltanto dai frame.
2. Testare unitarietà, inversi, trasformazione di gauge e covarianza.
3. Calcolare olonomie e verificare la legge di composizione.
4. Definire co-base e chiusure traslazionali; testare un circuito senza difetto e circuiti con Burgers noto.
5. Calibrare \(\mathcal S_h(B_h,\Omega_h)\) contro le sorgenti piane note.

### Fase 4 — triplette e simmetrie
1. Costruire generatori di simmetria sui gradi di libertà effettivi.
2. Verificare le relazioni del gruppo e i commutatori/covarianza di \(A_h\).
3. Calcolare caratteri, proiettori e intertwiners.
4. Controllare se le triplette sopravvivono a raffinamento, perturbazioni ortotrope e difetti.

### Fase 5 — geometria curva e shell
1. Derivare \(\operatorname{Inc}_g\) dalla cinematica superficiale.
2. Separare membrane, flessione e interfacce.
3. Trasferire la sorgente e il frame su patch curve.
4. Confrontare con la shell CST/cerniere solo dopo avere fissato un funzionale comune.

### Test minimi che devono fallire se la costruzione è errata
- una deformazione compatibile produce incompatibilità non nulla;
- il risultato cambia sotto un semplice cambio di gauge dei frame;
- un circuito senza difetto produce olonomia non banale;
- il Burgers calcolato dipende dal punto base oltre la trasformazione di trasporto prevista;
- la sorgente discreta non converge al pairing distribuzionale analitico;
- la decomposizione in triplette viene usata quando la covarianza di gruppo è violata;
- il bilancio energetico non coincide con la formulazione variazionale di riferimento.

---

## 11. Prototipo software effettivamente aggiunto\n\nÈ stato aggiunto il modulo \\`models/discrete_incompatibility_weak.py\\` con tre funzioni: (i) assemblaggio della forma duale \\(A_h\\) da basi di deformazione e Hessiane delle funzioni test; (ii) ricostruzione della deformazione simmetrica P1 su triangoli; (iii) assemblaggio del carico debole puntuale Burgers/Frank con la convenzione distribuzionale dichiarata.\n\nIl test \\`tests/test_discrete_incompatibility_weak.py\\` verifica l'annullamento della forma debole per una deformazione compatibile P1 contro una funzione test globale in \\(H^2_0\\), la ricostruzione di un gradiente affine, la convenzione di segno delle sorgenti e il rifiuto di triangoli degeneri. Il pairing di compatibilità è stato anche controllato numericamente durante la preparazione (residuo dell'ordine di \\(10^{-17}\\) nel caso sintetico). La CI GitHub associata al commit è in corso: il test non va dichiarato superato in CI finché non si osserva il risultato del job.\n\nQuesto è un **kernel di assemblaggio debole**, non ancora un elemento finito completo: non genera uno spazio Argyris/HCT, non implementa CIP-DG, non introduce i link quaternionici indipendenti e non calibra la mappa Cartan–Airy.\n\n## 12. Stato epistemico e conclusione per Morandotti

| Passaggio | Stato |
|---|---|
| Identità continua \(\operatorname{inc}(\operatorname{sym}\nabla u)=0\) | Identità classica |
| Tangente RGS 192×188 e proiettore | Ricostruiti e validati numericamente nel report A14 |
| Tangente shell 276×184 e frame quaternionici | Implementati/testati nel modello shell |
| Operatore debole piano \(A_h\) qui definito | Formulazione proposta; non ancora implementata |
| Sorgenti deboli Burgers/Frank | Formula di benchmark definita; test numerici da implementare |
| Link SU(2) indipendenti \(U_{fg}\) | Nuove variabili proposte; non implementate |
| Curvatura/olonomia quaternionica | Definizione proposta; non implementata |
| Co-base discreta e torsione/Burgers | Definizione strutturale proposta; calibrazione aperta |
| Mappa \(\mathcal S_h\) tra difetti Cartan e sorgente Airy | Aperta |
| Decomposizione in triplette dell'operatore | Condizionata alla covarianza di gruppo |
| Operatore superficiale \(\operatorname{Inc}_g\) per shell curva | Da derivare |
| Convergenza Mosco/Γ della famiglia curva RGS–PRISM | Aperta |

**Conclusione:** il ponte rigoroso non è “quaternioni = incompatibilità” né “triplette = difetti”. È la catena
\[
\boxed{
\text{vincoli}
\to T\mathcal M
\to \epsilon_h
\xrightarrow{\operatorname{Inc}_h}
\zeta_h
}
\]
con un livello geometrico aggiuntivo
\[
\boxed{
(U_{fg},\vartheta_e)
\to (\Omega_h,B_h)
\xrightarrow{\mathcal S_h}
\zeta_h,
}
\]
e con le triplette che intervengono nella decomposizione in settori solo quando la simmetria dell'operatore è verificata.

La domanda concreta a Morandotti diventa: quale scelta di spazi conformi/discontinui, operatori di incompatibilità e mappe di identificazione consente di dimostrare consistenza, stabilità e convergenza, prima sul benchmark piano Airy e poi sulle patch curve? Questo è un programma matematico controllabile e falsificabile.
