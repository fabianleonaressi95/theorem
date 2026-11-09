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
