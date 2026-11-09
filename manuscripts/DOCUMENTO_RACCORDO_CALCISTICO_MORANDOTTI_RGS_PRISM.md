# Documento di raccordo — dal problema del pallone alla meccanica dei difetti
## Ponte tra il caso calcistico RGS–PRISM e la proposta variazionale per Morandotti

**Ruolo nel dossier:** terzo documento autonomo, da leggere dopo la Nota progettuale e prima/dopo l'Appendice tecnica come caso applicativo che rende concreto il programma matematico.  
**Destinatario:** Prof. Marco Morandotti — DISMA / Politecnico di Torino  
**Proponente:** FLN

---

## 1. Perché serve questo documento

La Nota progettuale propone un confronto tra la formulazione variazionale dei difetti cristallini e una possibile discretizzazione geometrico-topologica RGS–PRISM. L'Appendice tecnica documenta gli strumenti discreti, i controlli e i limiti già registrati.

Il lavoro sul pallone da calcio fornisce il terzo elemento: **un problema meccanico concreto, geometricamente non banale e computazionalmente già impostato**, sul quale mettere alla prova la connessione fra geometria, incompatibilità, anisotropia, cuciture e risposta elastica.

Il pallone non viene presentato come un cristallo e le sue cuciture non vengono identificate automaticamente con dislocazioni o disclinazioni. È un sistema ingegneristico con guscio poligonale, pannelli, giunzioni e tessuto/composito: proprio per questo permette di separare e misurare contributi geometrici e costitutivi che nel problema dei difetti compaiono in forma più astratta.

La domanda comune è:

> Come si rappresentano, in una struttura discreta, le incompatibilità geometriche e costitutive che impediscono a una configurazione locale di essere realizzata come deformazione globale compatibile, e come si riflettono tali incompatibilità nell'energia e nei campi di tensione?

---

## 2. Il problema calcistico già costruito

Il modello RGS–PRISM del pallone usa la geometria del icosaedro troncato:

| Oggetto | Quantità |
|---|---:|
| Vertici geometrici originali | 60 |
| Pannelli pentagonali | 12 |
| Pannelli esagonali | 20 |
| Cuciture fisiche tra pannelli | 90 |
| Nodi della mesh, inclusi i centri pannello | 92 |
| Elementi triangolari CST | 180 |
| Cerniere diedrali | 270 |

Ogni pannello viene suddiviso in triangoli con un nodo centrale. La mesh è chiusa e conforme: ogni lato triangolare appartiene a due triangoli. Le 90 cuciture fisiche sono distinte dagli spigoli interni introdotti dalla triangolazione.

Il modello meccanico implementato combina:

1. membrane triangolari CST in tensione piana;
2. ortotropia locale dei pannelli, con parametri indipendenti (E_1,E_2,G_{12},\nu_{12}), spessore e angolo materiale;
3. flessione linearizzata mediante cerniere diedrali;
4. rigidezza di cucitura distinta, tramite moltiplicatore flessionale e termine opzionale di rinforzo assiale;
5. pressione applicata alle facce di riferimento e vincoli di gauge per rimuovere i modi rigidi.

La matrice di rigidezza è assemblata come somma dei contributi membranali, flessionali e di cucitura. Il problema risolto è, nella versione attuale, un equilibrio lineare vincolato.

**Stato:** implementazione e test numerici del modello discreto; non è ancora una simulazione non lineare completa di gonfiaggio, contatto, pieghe, danno o scorrimento adesivo.

I valori dei materiali presenti negli esempi sono parametri dimostrativi, non misure del pallone. Non è ancora disponibile nel repository una scansione sperimentale del pallone né una caratterizzazione indipendente dei provini.

---

## 3. La connessione con i difetti: tre livelli da non confondere

### 3.1 Incompatibilità cinematica

Nel modello di difetti cristallini, la cinematica elastica è vincolata da sorgenti incompatibili. Nel quadro piano linearizzato, la funzione di Airy consente di rappresentare il campo di tensione associato all'incompatibilità.

Nel pallone, una struttura chiusa composta da pannelli con orientazioni materiali locali e giunzioni non equivalenti può produrre una risposta che non è descritta da un'unica membrana isotropa omogenea. La compatibilità globale dipende dall'accoppiamento fra:
- geometria dei pannelli;
- orientazioni locali del materiale;
- rigidezze delle cuciture;
- curvatura e chiusura del guscio;
- condizioni di carico e vincolo.

Questa è una **analogia meccanica utile**, non ancora un'identificazione matematica fra sorgente di disclinazione e cucitura.

### 3.2 Curvatura e carica topologica

L'icosaedro troncato presenta 12 facce pentagonali e 20 esagonali. La distinzione pentagono/esagono è geometricamente essenziale: i pentagoni concentrano la curvatura angolare del poliedro, mentre gli esagoni completano la struttura.

La relazione di Eulero per il poliedro chiuso,
[
V-E+F=2,
]
impone un vincolo topologico globale. Per un reticolo esagonale ideale su una superficie chiusa, la necessità di difetti di coordinazione è un fatto topologico generale; nel pallone, tuttavia, la geometria dei pannelli e la topologia del reticolo dei materiali non sono la stessa cosa.

Perciò i 12 pentagoni possono essere trattati come **sedi geometriche candidate** per studiare concentrazione di curvatura e risposta locale. Non si afferma che siano 12 disclinazioni cristalline del materiale: per sostenerlo servirebbe definire e misurare un campo di orientazione microscopico e la sua olonomia.

### 3.3 Anisotropia costitutiva e cuciture

Il modello separa deliberatamente:
- anisotropia geometrica cubo–sfera;
- armonica cubica (H_4);
- contrasto pentagono/esagono;
- ortotropia del materiale;
- rigidezza delle cuciture.

Questi contributi non devono essere fusi in un unico coefficiente di “anisotropia”. Una variazione osservata nella forma o nella tensione può avere origini diverse; il modello consente di attivarle separatamente e confrontarne gli effetti.

Questa separazione è direttamente utile alla ricerca sui difetti: prima di attribuire una concentrazione di tensione a un difetto geometrico, bisogna escludere che sia spiegata da una variazione costitutiva, da una giunzione o dalla sola curvatura.

---

## 4. Dal modello di Airy alla shell: il ponte matematico da costruire

Il modello di Cesana–De Luca–Morandotti è un riferimento piano/semi-discreto basato sulla funzione di Airy. Il pallone è invece un guscio chiuso, curvo e composto da pannelli. Non è corretto trasferire direttamente l'equazione piana senza derivare i termini di curvatura e le condizioni di giunzione.

Il raccordo proposto ha quattro passaggi.

### Passaggio A — patch planare di riferimento

Selezionare una regione locale del guscio e costruire un benchmark piano con:
- cinematica linearizzata;
- parametri elastici fissati;
- una sorgente di incompatibilità prescritta;
- condizioni al contorno esplicite.

Riprodurre prima il caso Airy di riferimento. Questo verifica che la discretizzazione riproduca il problema noto senza invocare la geometria del pallone.

### Passaggio B — patch discreta con giunzione

Sostituire progressivamente la patch piana con una patch triangolata della shell, mantenendo controllati geometria, materiale e carico. Introdurre una cucitura come interfaccia con legge meccanica esplicita.

Confrontare:
- energia minima;
- risultanti e campi di tensione;
- salto di rotazione/diagonale attraverso la giunzione;
- localizzazione delle concentrazioni;
- sensibilità alla rigidezza della cucitura.

Il salto di rotazione della cerniera è una variabile cinematica del modello di shell; non è, da solo, una carica di disclinazione.

### Passaggio C — connessione discreta e sorgenti

Definire su un complesso adatto:
- gradi di libertà cinematici;
- operatori di compatibilità;
- sorgenti rotazionali e traslazionali;
- operatori di bordo/cobordo;
- forma energetica e condizioni al contorno.

Solo dopo questa definizione si potrà formulare una mappa candidata fra incompatibilità di Airy e cochain RGS–PRISM. La condizione (d_{k+1}d_k=0) assicura la coerenza algebrica del complesso, ma non determina da sola la legge costitutiva né la mappa fisica delle sorgenti.

### Passaggio D — chiusura globale del pallone

Estendere il benchmark alle 32 facce e alle 90 cuciture, studiando la distribuzione di energia e tensione sotto pressione. Confrontare separatamente:
1. shell isotropa senza rinforzo di cucitura;
2. shell ortotropa senza rinforzo;
3. shell ortotropa con rigidezza di cucitura;
4. perturbazioni geometriche cubo–sfera/(H_4);
5. eventuali campi di orientazione locale misurati.

La geometria globale serve a verificare se gli effetti locali si accumulano o si compensano sulla superficie chiusa.

---

## 5. Il livello quaternionico: orientazione locale e trasporto

Il lavoro già sviluppato introduce un riferimento locale tangente in ogni nodo della shell. Per il pallone:
[
N=92,qquad 3N=276,qquad 2N=184.
]
La matrice (Tin\mathbb R^{276\times184}) incorpora due direzioni tangenti ortonormali per nodo e soddisfa (T^TT=I). La rigidezza ridotta è
[
K_{\mathrm{tan}}=T^TKT.
]

I riferimenti locali possono essere codificati mediante quaternioni unitari (q_i\in SU(2)). L'azione sui quaternioni puramente immaginari,
[
p\mapsto q_i p q_i^{-1},
]
induce una rotazione in (SO(3)). La doppia copertura (q_i\sim -q_i) è un'identità algebrica, non un nuovo grado di libertà materiale.

Questo livello permette di formulare in modo naturale:
- trasporto di orientazioni fra pannelli;
- confronto fra frame locali;
- olonomia lungo circuiti della mesh;
- discontinuità di orientazione attraverso cuciture;
- possibili sorgenti rotazionali, una volta definite le variabili fisiche che le rappresentano.

Per passare da una semplice scelta di frame a un campo materiale quaternionico occorrono misure o una legge costitutiva che assegni significato fisico all'orientazione. Non si assume che i quaternioni descrivano già la microstruttura del tessuto.

### 5.1 Trasferimento RGS–shell

La geometria RGS di partenza contiene 64 punti e 192 componenti ambienti; la shell contiene 92 nodi e 276 componenti ambienti, con 184 gradi di libertà tangenti. È quindi necessario un trasferimento esplicito, non una corrispondenza per semplice conteggio.

È stato costruito un interpolatore geometrico direzionale (W\in\mathbb R^{276\times192}), basato sulle direzioni radiali dei 64 punti RGS e dei 92 nodi della shell, con vincoli locali di riproduzione affine. La proiezione tangenziale elimina poi la componente normale alla superficie.

Questa mappa è una scelta geometrica riproducibile. Non preserva automaticamente energia, rigidezza, azione di gruppo o spettro. Gli angoli principali e gli intertwiner possono essere interpretati solo dopo aver specificato i sottospazi e le azioni di simmetria da confrontare.

Il tripletto delle rotazioni globali, se usato come benchmark cinematico, non va confuso con il sottospazio (T_{2u}) RGS: quest'ultimo richiede la sua base numerica corretta e una verifica separata.

---



---

## 5-bis. Giunzioni geometriche e condizioni di Darmois–Israel

Il formalismo di Darmois–Israel fornisce un linguaggio geometrico particolarmente utile per descrivere un'interfaccia \\(\\Sigma\\) che separa due regioni. In relatività generale le due regioni possono essere due domini di spazio-tempo; nel problema del pallone, per analogia strutturale, possono essere due patch di pannello che si incontrano lungo una cucitura.

Sia \\(h_{ab}^{\\pm}\\) la prima forma fondamentale indotta sui due lati dell'interfaccia e sia \\(K_{ab}^{\\pm}\\) la rispettiva seconda forma fondamentale, calcolata con normali coerentemente orientate. Si definiscono i salti
\\[
[h_{ab}]=h_{ab}^{+}-h_{ab}^{-},\\qquad
[K_{ab}]=K_{ab}^{+}-K_{ab}^{-}.
\\]

### a) Condizione di Darmois

Per una giunzione priva di strato singolare, la geometria indotta deve essere continua e, nella formulazione classica, anche la curvatura estrinseca:
\\[
[h_{ab}]=0,\\qquad [K_{ab}]=0.
\\]
La prima condizione impedisce un'apertura o una discontinuità della metrica intrinseca dell'interfaccia; la seconda esclude un salto della curvatura estrinseca che richiederebbe una sorgente superficiale singolare nelle equazioni di Einstein.

### b) Condizione di Israel

Se la metrica indotta è continua ma la curvatura estrinseca presenta un salto, \\([K_{ab}]\\ne0\\), le equazioni di Einstein ammettono uno strato sottile con tensore energia-impulso superficiale
\\[
S_{ab}=-\\frac{1}{8\\pi G}
\\left([K_{ab}]-h_{ab}[K]\\right),
\\qquad [K]=h^{ab}[K_{ab}],
\\]
per la convenzione di segno qui adottata. Il segno complessivo cambia se si cambia convenzione per la normale o per la seconda forma fondamentale; nella comparazione occorre quindi fissare una convenzione unica.

### c) Traduzione controllata nel modello del pallone

Nel guscio poligonale, l'interfaccia è una cucitura fra due pannelli. Il corrispettivo cinematico da imporre è la compatibilità della geometria di bordo: i due lati devono condividere la stessa curva fisica e una parametrizzazione coerente. In una shell perfettamente incollata, gli spostamenti di bordo sono compatibili; la rotazione normale può invece presentare un salto, misurato dal diedro fra le patch.

Il salto di curvatura estrinseca è quindi un descrittore geometrico candidato della piega/rotazione relativa lungo la cucitura. Per una shell elastica, però, la relazione fra tale salto e la forza o il momento di linea deriva dal funzionale costitutivo della shell e dalla legge della giunzione, non dall'equazione di Israel. In particolare:
- la continuità della prima forma fondamentale corrisponde a un'interfaccia senza apertura o scorrimento incompatibile;
- il salto della seconda forma fondamentale descrive una discontinuità di curvatura/rotazione;
- la risultante e il momento trasmessi dalla cucitura si ricavano dalla variazione del funzionale elastico e dalle condizioni di equilibrio all'interfaccia;
- una cucitura cedevole o con scorrimento richiede condizioni cinematiche più generali e una legge di interfaccia esplicita.

Non si deve dunque porre (S_{ab}) di Israel uguale alla tensione meccanica della cucitura: hanno dimensioni, significato fisico ed equazioni costitutive differenti. Il formalismo relativistico è un **modello guida per la struttura dei salti geometrici**, mentre la shell calcistica richiede una propria legge elastica di linea.

### d) Ponte verso RGS–PRISM e teleparallelismo

La formulazione discreta può registrare, su ogni interfaccia, almeno:
1. la metrica indotta sui due lati;
2. il frame tangente e la normale di ciascun pannello;
3. la rotazione relativa, eventualmente rappresentata da un quaternione;
4. il salto di curvatura estrinseca discreto;
5. le forze e i momenti di linea ottenuti dalla variazione dell'energia.

Questo fornisce un luogo matematico naturale per confrontare operatori di compatibilità, cochain e olonomie. In una formulazione teleparallela, inoltre, si può descrivere la geometria tramite tetradi e connessione di spin; l'eventuale torsione concentrata sull'interfaccia deve però essere derivata dalla scelta di connessione e dalle condizioni di raccordo, non identificata automaticamente con il salto di (K_{ab}).

### e) Benchmark proposto

Per una singola cucitura fra due patch:
- verificare la continuità della curva di bordo e della metrica indotta;
- calcolare le normali e le seconde forme fondamentali sui due lati;
- misurare il salto \\([K_{ab}]\\) e il diedro discreto;
- derivare dalla shell energy le trazioni e i momenti di linea;
- confrontare il limite di cucitura molto rigida con il raccordo cinematicamente continuo;
- confrontare il limite di rigidezza flessionale nulla con una cerniera ideale.

Il risultato atteso non è una “Israel equation” per il pallone, ma una **legge di giunzione elastica discreta** che usa la stessa organizzazione geometrica: dati indotti continui, salti di curvatura e sorgenti superficiali/lineari definite da un funzionale.

Questa estensione rende più preciso il collegamento fra il problema calcistico, le interfacce dei materiali e il programma geometrico RGS–PRISM, mantenendo separati il formalismo di relatività generale e la meccanica dei gusci.




---

## 5-ter. Derivazione variazionale della legge elastica di giunzione

### Cinematica

Siano X⁺(s), X⁻(s) le curve di bordo delle due patch, parametrizzate dalla stessa ascissa curvilinea. Una giunzione chiusa senza scorrimento soddisfa
\[
X^+(s)=X^-(s),\qquad [h_{ab}]=0.
\]
Con t tangente unitaria orientata e n⁺, n⁻ normali alle patch, il diedro firmato è
\[
\theta=\operatorname{atan2}\left(t\cdot(n^-\times n^+),n^-\cdot n^+\right).
\]
La configurazione di riferimento ha diedro θ₀; poniamo η=θ−θ₀. Se i frame locali sono codificati da quaternioni unitari q₋,q₊, la rotazione relativa è q_rel=q₊q₋⁻¹ (rotazione relativa espressa nel frame ambientale); il vettore rotazione è ω=Log_SO(3)(q_rel) e il salto firmato è η=t·ω−η₀. Si usa il ramo principale, con continuità del ramo durante l'evoluzione.

### Riduzione dell'energia di shell

In una fascia di raccordo di larghezza w, il salto angolare η corrisponde, al primo ordine, a una curvatura concentrata b≈η/w. Per una shell isotropa l'energia flessionale per unità di area è ½D_b b², con D_b=Et³/[12(1−ν²)]. Integrando sulla fascia:
\[
\mathcal E_\Gamma=\frac12\int_\Gamma D_b(\eta/w)^2w\,ds
=\frac12\int_\Gamma\frac{D_b}{w}\eta^2\,ds.
\]
Dunque la densità lineare è ψ_Γ=½k_θ η², con k_θ=D_b/w, e la variazione dà il momento per unità di lunghezza:
\[
\boxed{m_\Gamma=\frac{\partial\psi_\Gamma}{\partial\eta}
=\frac{D_b}{w}(\theta-\theta_0).}
\]
La tangente costitutiva è D_b/w. Il segno dipende dalla convenzione coerente per normale e diedro; l'energia è invariata se si invertono entrambe.

Per una shell ortotropa si usa la matrice flessionale D_b e la direzione di curvatura c: D_eff=cᵀD_b c. Quindi ψ_Γ=½(D_eff/w)η². Se le due fasce hanno rigidezze D₊,D₋ e larghezze w₊,w₋, minimizzando ½w₊D₊b₊²+½w₋D₋b₋² sotto il vincolo w₊b₊+w₋b₋=η si ottiene
\[
k_\theta=\left(\frac{w_+}{D_+}+\frac{w_-}{D_-}\right)^{-1},
\qquad \psi_\Gamma=\frac12k_\theta\eta^2.
\]
Questa è la rigidezza equivalente in serie; non va confusa con una media aritmetica dei moduli.

### Legge discreta, momento e forze nodali

Per una cucitura discreta di lunghezza ℓ_e, larghezza duale w_e e moltiplicatore α_e:
\[
E_e=\frac12\alpha_eD_{eff}\frac{\ell_e}{w_e}
(\theta_e-\theta_{0,e})^2.
\]
Derivando:
\[
M_e=\frac{\partial E_e}{\partial\theta_e}
=\alpha_eD_{eff}\frac{\ell_e}{w_e}(\theta_e-\theta_{0,e}),
\quad
k_e=\frac{\partial^2E_e}{\partial\theta_e^2}
=\alpha_eD_{eff}\frac{\ell_e}{w_e}.
\]
Con g_e=∇_u θ_e, il residuo interno è r_e=M_e g_e e la parte materiale della tangente è K_e^mat=k_e g_e g_eᵀ. In una formulazione geometricamente non lineare completa si aggiunge K_e^geo=M_e∇²_u θ_e. Il solver attuale usa la linearizzazione del diedro e non assembla quest'ultimo termine.

### Apertura e scorrimento: legge coesiva opzionale

Se la cucitura può aprirsi o scorrere, si introduce il salto traslazionale δ=[u]. Una legge lineare passiva è
\[
\psi_c=\frac12\delta^T K_\Gamma\delta,
\qquad t_\Gamma=K_\Gamma\delta,
\quad K_\Gamma=K_\Gamma^T\succeq0.
\]
Per un edge, E_e^coh=½ℓ_e δ_eᵀK_Γδ_e. La continuità perfetta e la legge coesiva sono modelli alternativi: non si deve imporre contemporaneamente [u]=0 e interpretare una trazione coesiva non nulla come grado di libertà indipendente.

### Rapporto con Darmois–Israel

La legge elastica usa il salto di rotazione/curvatura per ottenere un momento di linea dal funzionale della shell. Israel usa il salto della seconda forma fondamentale per determinare un tensore energia-impulso superficiale nelle equazioni di Einstein. Il parallelismo è geometrico-variazionale, non un'identità fra coefficienti o grandezze fisiche. Il limite k_θ→∞ impone θ→θ₀ (giunzione rotazionalmente rigida); k_θ→0 dà una cerniera flessionale libera. La compatibilità traslazionale è una condizione distinta.

### Implementazione e stato

La legge è implementata in models/football_seam_law.py; i test dedicati sono in tests/test_football_seam_law.py. Il modulo restituisce energia, momento di edge, tangente materiale, risultanti coesive e rotazione relativa quaternionica.

**Stato:** derivazione variazionale e implementazione isolata con test unitari aggiunti. La legge non è ancora integrata nel solver globale né validata con prove sperimentali di cucitura. D_eff, w_e, α_e e K_Γ richiedono identificazione da dati indipendenti.


## 6. Programma sperimentale: cosa misurare

Il caso calcistico rende possibile un protocollo industriale concreto. Per rendere identificabili i parametri servono misure indipendenti:

| Misura | Parametri/effetti identificabili |
|---|---|
| Scansione 3D della superficie a pressione nota | forma, deformazione globale, residuo geometrico |
| Prove coupon nelle due direzioni del materiale | (E_1,E_2,G_{12},\nu_{12}) |
| Prove di trazione/taglio della cucitura | rigidezza assiale e risposta di giunzione |
| Pressione–volume e deformata a più pressioni | rigidezza globale e non linearità |
| DIC o correlazione d'immagine | campi di spostamento e deformazione |
| Misure ripetute dopo cicli di gonfiaggio | memoria, assestamento e possibile isteresi |
| Orientazione dei filati/fibre per pannello | frame materiale e trasporto di orientazione |

La scansione da sola non identifica univocamente tutte le costanti. La calibrazione deve separare dati di identificazione e dati di validazione, con almeno un caso tenuto fuori dal fit.

L'isteresi, se osservata, va distinta fra risposta del materiale, cucitura, attrito/contatto e procedura di misura. Una simulazione non costituisce una validazione industriale.

---

## 7. Benchmark comuni e criteri di riuscita

Il programma congiunto può essere valutato attraverso una matrice di benchmark:

| Livello | Riferimento | Output | Criterio |
|---|---|---|---|
| 1. Piano | soluzione Airy/semi-discreta | energia e campi | riproduzione del riferimento |
| 2. Patch shell | modello CST + cerniere | spostamenti e tensioni | convergenza rispetto al raffinamento |
| 3. Giunzione | legge di cucitura misurata | salti e concentrazioni | identificabilità e bilancio energetico |
| 4. Guscio chiuso | pallone completo | forma e risposta alla pressione | confronto con scansione/DIC |
| 5. RGS–PRISM | complesso e forma discreta | sorgenti, cochain, energia | compatibilità, stabilità, confronto con FEM |
| 6. Quaternioni | frame/trasporto SU(2) | olonomia e sottospazi | covarianza e residui di intertwining |

Il progetto supera il benchmark solo se:
- il riferimento piano è riprodotto entro tolleranze dichiarate;
- la discretizzazione mantiene compatibilità e stabilità al raffinamento;
- le costanti costitutive sono identificate da prove indipendenti;
- la shell riproduce misure non usate nella calibrazione;
- l'eventuale vantaggio RGS–PRISM è quantificato rispetto a FEM e al modello shell standard.

---

## 8. Cosa è già disponibile e cosa resta da fare

### Già implementato o documentato
- mesh chiusa dell'icosaedro troncato, 92 nodi, 180 triangoli e 270 cerniere;
- membrane CST ortotrope;
- flessione linearizzata a cerniere diedrali;
- rigidezza di cucitura separata;
- carico di pressione e vincoli di gauge;
- campi cubo–sfera e armonica (H_4) come parametri geometrici indipendenti;
- registrazione ICP rigida e metriche di confronto con scansioni;
- frame tangenti locali, lift quaternionico e rigidezza ridotta;
- trasferimento geometrico direzionale RGS–shell.

### Ancora aperto
- dati di scansione reali e prove coupon/giunzione;
- legge non lineare di gonfiaggio e contatto;
- identificazione sperimentale delle costanti;
- formulazione Airy su patch curva e termini di curvatura;
- definizione fisica delle sorgenti discrete;
- mappa dimostrata fra sorgenti di difetto e cochain;
- preservazione energetica/spettrale del trasferimento RGS–shell;
- confronto quantitativo con FEM su dati condivisi;
- prova di convergenza di Mosco per la sequenza curva.

---

## 9. Proposta concreta a Morandotti

Si propone di usare il caso del pallone come **secondo banco di prova applicativo**, non come sostituto del benchmark teorico sui difetti.

La collaborazione potrebbe iniziare con due attività coordinate:

1. **DISMA:** selezione del problema Airy di riferimento e definizione rigorosa delle variabili di incompatibilità, delle sorgenti e del funzionale.
2. **RGS–PRISM / shell:** trasferimento della stessa struttura di compatibilità a una patch triangolata con giunzione, verificando energia, campi e stabilità.

In una fase successiva, l'eventuale coinvolgimento IAM@PoliTO permetterebbe di scegliere un pallone/campione, ottenere scansioni e prove meccaniche, identificare le leggi di pannello e cucitura e confrontare le previsioni con dati reali.

La richiesta a Morandotti non è di validare il modello del pallone né di accettare un'identificazione fra cuciture e difetti cristallini. È di discutere se il ponte matematico fra incompatibilità, complessi discreti e forme energetiche possa essere formulato in modo rigoroso, usando prima un benchmark piano noto e poi il guscio calcistico come problema applicativo controllato.

---

## 10. Collocazione nel dossier

I tre documenti hanno funzioni distinte e complementari:

1. **Nota progettuale:** perché proporre la collaborazione e quale problema teorico affrontare.
2. **Documento di raccordo calcistico (questo testo):** quale problema meccanico concreto collega geometria, anisotropia, cuciture, frame quaternionici e incompatibilità.
3. **Appendice tecnica:** quali strutture, implementazioni, test e risultati RGS–PRISM sono già disponibili e quali restano aperti.

Il pallone fornisce così un ponte applicativo verificabile tra il problema astratto dei difetti e una struttura ingegneristica reale, senza confondere analogia, modello numerico e validazione sperimentale.
