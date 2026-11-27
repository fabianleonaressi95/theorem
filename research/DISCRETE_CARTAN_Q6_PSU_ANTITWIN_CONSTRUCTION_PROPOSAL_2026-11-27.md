# Proposta di costruzione discreta di Cartan su complessi cellulari
## RGS / Q6 / PSU / Anti-Twin — 27 novembre 2026

**Stato:** proposta matematica falsificabile; non è un teorema dimostrato e non certifica ancora un limite fisico continuo.

**Scopo.** Definire sullo stesso supporto cellulare (i) olonomia di curvatura, (ii) difetto di chiusura del coframe come torsione discreta, (iii) leggi di trasformazione locali di Lorentz, (iv) identità di Bianchi da verificare, mantenendo indipendenti coframe e connessione. La costruzione deve poter contenere il settore PSU–Anti-Twin senza identificare lo scambio dei fogli con la torsione.

## 1. Supporto combinatorio: requisito 4D

Sia \(K_h\) un complesso simpliciale orientato di dimensione 4, localmente finito, con insiemi \(K_h^{(k)}\) di k-simplessi. La scelta simpliciale è una proposta minimale perché ogni 2-faccia e 3-cella ha una struttura di bordo esplicita; la costruzione può essere trascritta a complessi cellulari regolari dopo averne fissato le mappe di attacco.

Si fissano:
- un orientamento per ogni spigolo e ogni faccia;
- mappe di bordo \(\partial_k:C_k(K_h)\to C_{k-1}(K_h)\), con \(\partial_{k-1}\partial_k=0\);
- un ordinamento dei vertici di ogni simplesso, usato solo per fissare i cammini e i segni;
- un frame di Lorentz in ogni vertice \(v\), con fibra \(V_v\simeq\mathbb R^{1,3}\) e metrica \(\eta=\mathrm{diag}(+1,-1,-1,-1)\).

**Gate dimensionale:** il grafo Q6 e il cubo combinatorio a sei coordinate non sono questo \(K_h^{(4)}\). Q6 può essere un carrier o un settore interno del modello; per ottenere una discretizzazione dello spaziotempo occorre fornire una successione di complessi 4D, mappe di confronto e una regola geometrica che selezioni la segnatura lorentziana. Lo split golden 6D \(3+3\) non seleziona da solo una coordinata temporale.

## 2. Variabili indipendenti e convenzioni

Per ogni spigolo orientato \(e=(v,w)\), si introducono:

1. **Link lorentziano**
   \[
   L_{vw}:V_w\longrightarrow V_v,\qquad L_{vw}\in SO^+(1,3).
   \]
   Il link trasporta componenti dal frame in \(w\) al frame in \(v\).

2. **Coframe edge**
   \[
   E_{vw}\in V_v.
   \]
   È il vettore di spostamento discreto dell'estremo \(w\), espresso nel frame di \(v\). Per l'orientazione inversa si impone
   \[
   L_{wv}=L_{vw}^{-1},\qquad E_{wv}=-L_{vw}^{-1}E_{vw}.
   \]
   Questa è una convenzione di discretizzazione da testare contro la geometria scelta; non discende dal solo grafo.

3. **Campi interni**: link di gauge \(U_{vw}\in G\), variabili PSU sui due fogli, e campi di materia \(\Psi_v\) in rappresentazioni specificate. I link lorentziani \(L\) e i link interni \(U\) sono fattori distinti del gruppo di struttura.

Il coframe \(E\) e la connessione \(L\) sono variabili indipendenti. Non si impone \(L\) come funzione di una metrica discreta tramite una connessione di Levi-Civita.

## 3. Gauge locale di Lorentz

A ogni vertice si assegna \(h_v\in SO^+(1,3)\). Le trasformazioni sono
\[
E_{vw}\mapsto E'_{vw}=h_vE_{vw},\qquad
L_{vw}\mapsto L'_{vw}=h_vL_{vw}h_w^{-1}.
\]
Le relazioni per lo spigolo inverso sono preservate:
\[
L'_{wv}=(L'_{vw})^{-1},\qquad
E'_{wv}=-L'_{vw}{}^{-1}E'_{vw}=h_wE_{wv}.
\]
Quindi i campi edge sono covarianti nel frame scelto all'origine dello spigolo. Una verifica automatica deve controllare queste identità per matrici casuali in \(SO^+(1,3)\), entro la tolleranza numerica dichiarata, oltre a un test simbolico/algebrico quando possibile.

## 4. Trasporto lungo cammini e olonomia di faccia

Per un cammino orientato \(p=(v_0,v_1,\ldots,v_m)\), il trasporto da \(v_m\) a \(v_0\) è
\[
P_p=L_{v_0v_1}L_{v_1v_2}\cdots L_{v_{m-1}v_m}:V_{v_m}\to V_{v_0}.
\]
Sotto gauge locale,
\[
P_p\mapsto h_{v_0}P_ph_{v_m}^{-1}.
\]

Per una faccia orientata \(f=(v_0,v_1,v_2)\), si sceglie esplicitamente il vertice base \(v_0\) e il bordo positivo \(v_0\to v_1\to v_2\to v_0\). L'olonomia è
\[
H_f=L_{v_0v_1}L_{v_1v_2}L_{v_2v_0}.
\]
Essa trasforma per coniugio:
\[
H_f\mapsto h_{v_0}H_fh_{v_0}^{-1}.
\]
Pertanto funzioni di classe come \(\operatorname{tr}(H_f)\), o invarianti costruiti da \(H_f\), sono gauge-invarianti. La curvatura discreta non è \(H_f\) stesso in ogni regime: in un regime di facce piccole e connessione regolare si può definire un logaritmo locale
\[
\mathcal R_f=\log H_f
\]
solo quando \(H_f\) appartiene a un intorno in cui il ramo del logaritmo è fissato. Il flusso di curvatura continuo è recuperabile soltanto con una stima di consistenza rispetto all'area orientata della faccia e al raffinamento.

**Controllo di orientazione:** invertire l'orientazione di \(f\) deve dare \(H_{\bar f}=H_f^{-1}\), con punto base coerentemente trasportato. Un cambio di punto base deve produrre olonomie coniugate tramite il trasporto sul cammino scelto.

## 5. Torsione discreta come chiusura covariante del coframe

Per ogni faccia \(f\) con punto base \(v_0\), si trasporta ogni edge-vector del bordo nel frame \(V_{v_0}\). Per il bordo triangolare positivo:
\[
\mathcal T_f=
E_{v_0v_1}
+L_{v_0v_1}E_{v_1v_2}
+L_{v_0v_1}L_{v_1v_2}E_{v_2v_0}
\in V_{v_0}.
\]
In forma indipendente dalla triangolazione, dato un bordo ordinato \(e_i=(v_i,v_{i+1})\) e il cammino \(p_i\) dal punto base \(v_0\) a \(v_i\),
\[
\mathcal T_f=\sum_i P_{p_i}E_{v_iv_{i+1}}.
\]
Con le trasformazioni della sezione 3, ogni termine e quindi la somma trasformano come
\[
\mathcal T_f\mapsto h_{v_0}\mathcal T_f.
\]
La norma lorentziana \(\eta(\mathcal T_f,\mathcal T_f)\) è quindi gauge-invariante, ma può essere nulla anche per un vettore non nullo: non va usata da sola come diagnostica. Vanno registrate le quattro componenti nel frame, invarianti quadratici appropriati e la dipendenza dalla scala della faccia.

Questa è una **definizione discreta candidata** di torsione integrata sulla faccia. La corrispondenza con l'integrale di \(T^a=de^a+\omega^a{}_b\wedge e^b\) richiede una stima di consistenza. Non è lecito chiamare torsione un generico residuo di chiusura prima di aver fissato coframe, trasporto, base, orientazione e trasformazione di gauge.

### 5.1 Test limite elementare

Nel caso piatto \(L_{vw}=I\), la formula si riduce alla somma orientata dei vettori edge:
\[
\mathcal T_f=\sum_{e\subset\partial f}E_e.
\]
Per un coframe esatto derivato da coordinate \(x_v\in\mathbb R^{1,3}\), \(E_{vw}=x_w-x_v\), la somma telescopica è zero. Questo test è necessario ma non sufficiente: non prova la convergenza al tensore di torsione su mesh curve.

### 5.2 Separazione tra curvatura e torsione

I due osservabili sono indipendenti:
- \(H_f\) misura la rotazione/boost accumulata dalla connessione;
- \(\mathcal T_f\) misura il difetto di chiusura del coframe dopo il trasporto.

I test sintetici devono includere almeno quattro casi:
1. \(H_f=I,\ \mathcal T_f=0\): settore piatto e senza torsione;
2. \(H_f\ne I,\ \mathcal T_f=0\): curvatura senza torsione;
3. \(H_f=I,\ \mathcal T_f\ne0\): torsione senza curvatura (settore teleparallelo locale);
4. \(H_f\ne I,\ \mathcal T_f\ne0\): settore Riemann–Cartan generico.

La realizzabilità dei quattro casi su un dato complesso e con vincoli globali è un problema separato da verificare, non una conseguenza automatica delle formule locali.

## 6. Identità di Bianchi: bersaglio e forma discreta da dimostrare

Nel continuo, con convenzioni Cartan,
\[
T^a=De^a,\qquad R^a{}_b=D\omega^a{}_b,
\]
e valgono
\[
DT^a=R^a{}_b\wedge e^b,\qquad DR^a{}_b=0.
\]
La prima è la seconda identità di Bianchi con torsione; la seconda è la prima identità di Bianchi.

Nel discreto, la versione corretta deve essere costruita con trasporti e ordinamenti non abeliani. Per ogni 3-cella \(c\), occorre:
- scegliere un vertice base;
- scegliere cammini di collegamento dai vertici base delle facce al base di \(c\);
- trasportare tutte le olonomie di faccia allo stesso frame;
- ordinare i fattori in modo compatibile con la decomposizione del bordo;
- dimostrare che il prodotto orientato e trasportato delle olonomie sulla superficie chiusa è l'identità (identità di Bianchi discreta, con le ipotesi e le convenzioni specificate).

Per la torsione occorre una relazione di bordo covariante che confronti la somma dei difetti di faccia con l'azione della curvatura sul coframe. Non si deve scrivere semplicemente \(\sum_{f\subset\partial c}\mathcal T_f=0\): in presenza di curvatura i frame non coincidono e tale somma non è covariante. La relazione candidata deve essere derivata dal trasporto e poi confrontata con \(DT=R\wedge e\) nel limite di raffinamento.

**Stato:** le identità continue sono teoremi standard; la loro discretizzazione per questa specifica scelta di variabili e cammini è aperta finché non viene fornita una dimostrazione indipendente dalle scelte ausiliarie o una regola canonica per esse.

## 7. Spin lift e materia

Il passaggio da \(SO^+(1,3)\) a \(\mathrm{Spin}^+(1,3)\simeq SL(2,\mathbb C)\) richiede:
- una struttura spin sul complesso o un criterio equivalente di sollevamento coerente;
- link \(\widetilde L_{vw}\) che proiettino su \(L_{vw}\);
- compatibilità dei prodotti sui cammini e controllo dei segni \(\mathbb Z_2\) sui cicli;
- una rappresentazione di materia dichiarata e una discretizzazione dell'operatore di Dirac.

Non basta avere una rappresentazione di Spin(6), né un operatore finito sul grafo Q6. Il risultato negativo già registrato in T149 (spettro a due valori per l'operatore considerato) resta un vincolo: non dimostra un fermione continuo massless. Sono necessari test di località, doubling/specie, spectral flow, anomalie e convergenza spettrale.

## 8. Inserimento PSU–Anti-Twin senza confusione categoriale

Si mantengono due fattori distinti:
\[
\mathcal H=\mathcal H_{\rm geom}\otimes\mathbb C^2_{\rm sheet}
\otimes\mathcal H_{\rm matter}.
\]
L'involuzione di foglio \(J_{\rm AT}=I\otimes\tau_1\) e il generatore \(Q=q_0\tau_3\) soddisfano
\[
J_{\rm AT}^2=I,\qquad J_{\rm AT}QJ_{\rm AT}^{-1}=-Q.
\]
Per link U(1) coniugati sui fogli, \(U^{(-)}_e=(U^{(+)}_e)^*\), il cambio di foglio scambia le rappresentazioni coniugate. Questo è un settore interno/discreto.

La torsione, invece, è \(\mathcal T_f\) costruita da coframe e connessione lorentziana. Non si identifica:
- scambio PSU dei fogli con torsione;
- curvatura interna U(1)/SU(2) con curvatura lorentziana;
- parità Q6 con orientazione dello spaziotempo;
- antipodalità del cut-and-project con inversione temporale.

Il collegamento fisico fra sheet-difference \(s_{\rm AT}\), variabili fluide e componenti del coframe deve emergere da un'azione o da una mappa costitutiva verificabile.

## 9. Azione discreta e variazione indipendente

Una volta definite le variabili, la forma generale è
\[
S_h[E,L,U,\Psi,\Phi]=S_{\rm grav,h}[E,L]
+S_{\rm gauge,h}[U]+S_{\rm matter,h}[E,L,U,\Psi]
+S_{\rm fluid,h}[E,\Phi]+S_{\rm int,h}.
\]
Non si fissano coefficienti per far coincidere a posteriori uno spettro o una costante. Ogni termine deve essere:
- locale o quasi-locale con raggio dichiarato;
- gauge-invariante;
- dimensionalmente coerente;
- consistente con un'azione continua bersaglio;
- variazionalmente ben definito.

Le equazioni discrete si ottengono variando \(E\) e \(L\) indipendentemente, oltre ai campi interni e di materia. In tal modo le equazioni del coframe e della connessione sono distinte e la sorgente di torsione può essere identificata senza imporre a priori \(T=0\).

## 10. Rami geometrici da non confondere

| Ramo | Vincolo | Curvatura | Torsione |
|---|---|---:|---:|
| Riemann–Cartan | \(E,L\) indipendenti | ammessa | ammessa |
| Teleparallelo | olonomia di curvatura trivializzata/localmente piatta | \(R=0\) | ammessa |
| Torsione-libero | vincolo \(T=0\) | ammessa | \(T=0\) |
| Levi-Civita derivato | connessione determinata dalla metrica/coframe con \(T=0\) | ammessa | \(T=0\) |

La formulazione RGS che intende unificare curvatura e torsione deve partire dal primo ramo. Il teleparallelismo è un settore distinto, non sinonimo di geometria di Cartan generale.

## 11. Piano di audit computazionale

Il primo audit non deve usare parametri fisici calibrati. Deve essere un test geometrico sintetico su un piccolo 4-simplex e su una triangolazione di un 4-cubo.

| Test | Costruzione | Criterio di accettazione |
|---|---|---|
| C1 | orientazioni e bordi | \(\partial^2=0\) esatto |
| C2 | gauge casuale \(h_v\) | leggi di trasformazione di \(E,L\) rispettate entro tolleranza |
| C3 | olonomia faccia | trasformazione per coniugio; inversione \(H_{\bar f}=H_f^{-1}\) |
| C4 | coframe esatto, link identità | \(\mathcal T_f=0\) entro errore macchina |
| C5 | connessione piatta non banale per gauge | olonomie identità sui contratti; covarianza della torsione |
| C6 | configurazione con curvatura e torsione | i due osservabili non collassano in un unico scalare |
| C7 | Bianchi su 3-cella | identità ordinata e trasportata dimostrata e verificata |
| C8 | raffinamento geometrico | convergenza di \(H_f\), \(\mathcal T_f\) ai flussi continui previsti |
| C9 | Anti-Twin | \(J^2=I,\ JQJ^{-1}=-Q\), senza contaminare \(T_f\) |
| C10 | spin lift | coerenza dei segni sui cicli e convergenza dell'operatore di materia |

C7 e C8 sono gate matematici, non semplici test numerici. Il loro superamento richiede una dimostrazione e stime uniformi, non soltanto output di uno script.

## 12. Relazione con le dieci famiglie

- **Q6:** fornisce il carrier combinatorio finito; non sostituisce \(K_h^{(4)}\).
- **GOLDEN:** può fornire coordinate/proiezioni e dati metrici candidati; non seleziona la segnatura lorentziana.
- **IVM:** fornisce direzioni e simmetrie spaziali; serve una mappa compatibile con il complesso 4D.
- **CELL:** fornisce orientazioni, catene e mappe di bordo; deve essere esteso al supporto 4D.
- **REP:** fornisce fibre e rappresentazioni; il lift Spin(1,3) resta da costruire.
- **SPACETIME:** ospita \(E,L,H_f,\mathcal T_f\) e l'azione di Cartan.
- **ANALYSIS:** deve fornire stabilità FEEC/Mosco e convergenza degli operatori.
- **DYNAMICS:** accoppia link, flussi, MHD e QLG solo dopo la derivazione dell'azione/evoluzione.
- **ARITH:** fornisce coefficienti algebrici solo se compaiono nella geometria o nell'azione derivata.
- **MORPH:** interpreta variazioni del coframe come deformazioni solo dopo aver definito una legge costitutiva.

Le dieci famiglie sono quindi raccordate dalla medesima struttura \(K_h,\partial,d_h,M_h,E,L,U,\Psi\), ma i collegamenti sono di natura diversa: alcuni sono identità algebriche, altri interfacce architetturali, altri ancora ipotesi fisiche.

## 13. Letteratura di confronto

1. T. Regge, “General Relativity Without Coordinates”, *Nuovo Cimento* 19 (1961), 558–571. DOI: 10.1007/BF02733251.
2. A. N. Hirani, *Discrete Exterior Calculus*, PhD thesis, Caltech (2003). DOI: 10.7907/ZHY8-V329.
3. D. N. Arnold, R. S. Falk, R. Winther, “Finite element exterior calculus, homological techniques, and applications”, *Acta Numerica* 15 (2006), 1–155. DOI: 10.1017/S0962492906210018.
5. Y. Xue, “Quantum Regge calculus of Einstein-Cartan theory”, *Physics Letters B* 682 (2009),  ఉత్త. DOI: 10.1016/j.physletb.2009.10.082.
6. Y. Cho, “Gauge theory of Poincaré symmetry”, *Physical Review D* 14 (1976), 3335. DOI: 10.1103/PhysRevD.14.3335.
7. D. Braune, A. Gillespie, M. B. Tong, P. Desbrun, “Discrete Torsion of Connection Forms on Simplicial Meshes”, *ACM Transactions on Graphics* 44(4), Article 67 (2025). DOI: 10.1145/3731197.
8. S. Christiansen, “On the definition of curvature in Regge calculus”, *IMA Journal of Numerical Analysis* 44 (2024). DOI: 10.1093/imanum/drad095.
9. J. M. Lee, *Introduction to Riemannian Manifolds*, per le convenzioni geometriche continue; la segnatura lorentziana richiede la formulazione pseudo-riemanniana corrispondente.
10. Yan et al., “Dynamics of Regge calculus with torsion”, arXiv:2610.00593 (2026), **preprint non peer-reviewed**; da usare soltanto come confronto esplorativo.

**Nota bibliografica:** il riferimento Xue è stato verificato sul record editoriale: *Physics Letters B* 682(3), 300–304 (7 dicembre 2009). La sua formulazione euclidea e torsione-libera va tenuta distinta dal programma Riemann–Cartan qui proposto. Il seguito di Xue, *Physical Review D* 82, 064039 (2010), DOI 10.1103/PhysRevD.82.064039, costituisce un ulteriore confronto su complessi simpliciali 4D, tetradi e connessioni, non una validazione indipendente del nostro schema.

## 14. Classificazione conclusiva

| Enunciato | Stato |
|---|---|
| Trasformazione gauge di \(E,L\) e coniugio dell'olonomia | [E] conseguenza algebrica delle definizioni |
| Covarianza di \(\mathcal T_f\) | [E] conseguenza algebrica, date le convenzioni |
| \(d_h^2=0\) | [P] proprietà del complesso scelto |
| Corrispondenza \(\mathcal T_f\to\int_f T\) | [O] richiede consistenza e raffinamento |
| Bianchi discreta torsionale per la costruzione | [O] da derivare |
| Complesso 4D lorentziano ottenuto da Q6/golden/IVM | [O] non costruito |
| Lift Spin⁺(1,3) e limite Dirac | [O] non dimostrato |
| Azione RGS/PSU–Anti-Twin di Einstein–Cartan | [H/O] da derivare e variare |
| Identificazione dello scambio Anti-Twin con torsione | **esclusa** |

**Criterio di promozione:** questa proposta può diventare un teorema soltanto dopo aver fissato un complesso 4D effettivo, dimostrato la covarianza e le identità discrete, costruito una successione di raffinamenti e provato le stime di consistenza/convergenza. Fino ad allora resta un programma di costruzione controllato e falsificabile.
