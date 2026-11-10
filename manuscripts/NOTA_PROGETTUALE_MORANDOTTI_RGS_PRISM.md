# Proposta di collaborazione scientifica
## Discretizzazione geometrica e benchmark variazionale di difetti cristallini: un percorso RGS–PRISM

**Documento di presentazione e raccordo con l'appendice tecnica**  
**Interlocutore proposto:** Prof. Marco Morandotti — DISMA / Politecnico di Torino  
**Ambito:** dislocazioni, disclinazioni, incompatibilità cinematica, modelli variazionali e discretizzazioni geometriche  
**Proponente:** FLN

---

## 1. Sintesi della proposta

La proposta è avviare un confronto matematico circoscritto tra il quadro variazionale per difetti cristallini sviluppato da Cesana, De Luca e Morandotti e una discretizzazione geometrico-topologica RGS–PRISM.

Il punto di partenza non è la richiesta di riconoscere una nuova teoria dei materiali, né la sostituzione dei modelli variazionali o degli elementi finiti già disponibili. È una domanda verificabile:

> Una discretizzazione basata su complessi cellulari, operatori di bordo/cobordo e forme quadratiche geometriche può rappresentare le incompatibilità di dislocazioni e disclinazioni in modo coerente, stabile e computazionalmente competitivo rispetto a una formulazione di riferimento?

Il primo caso di studio sarebbe volutamente bidimensionale e aderente al modello pubblicato nel 2024. Si partirebbe da una configurazione finita di disclinazioni a cuneo e/o da un dipolo, per arrivare al limite di dislocazione di bordo. Solo dopo aver superato questo benchmark avrebbe senso estendere il lavoro a geometrie e microstrutture di materiali prodotti mediante manifattura additiva.

## 2. Riferimento matematico: il modello del 2024

Il riferimento naturale è:

P. Cesana, L. De Luca, M. Morandotti, *Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method*, **SIAM Journal on Mathematical Analysis**, 56(1), 79–136 (2024), DOI [10.1137/22M1523443](https://doi.org/10.1137/22M1523443).

Il lavoro tratta difetti reticolari di tipo rotazionale e traslazionale attraverso minimi di energie elastiche isotrope soggetti a incompatibilità cinematica. Nel regime di cinematica linearizzata piana, la formulazione usa la funzione di tensione di Airy. Un risultato centrale è l'equivalenza energetica, in un opportuno regime singolare, tra dipoli di disclinazioni e dislocazioni di bordo.

La proposta RGS–PRISM si innesta precisamente su questa struttura: non cambia il problema continuo di riferimento, ma studia una possibile rappresentazione discreta delle variabili, dei vincoli di incompatibilità e dell'energia.

## 2-bis. Aggiornamento bibliografico e baseline numerica 2025–2026

La proposta va letta alla luce degli sviluppi più recenti del gruppo. Oltre al lavoro Airy del 2024, sono ora disponibili:
- Cesana–Fabbrini–Morandotti (2025), *Variational Formulation of Planar Linearized Elasticity with Incompatible Kinematics*, che caratterizza variazionalmente l'equilibrio piano con incompatibilità traslazionali e rotazionali e riduce il problema Airy a formule di cella;
- Cesana–Fabbrini–León Baldelli–Morandotti (2026), *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation* (preprint arXiv:2609.29614), che implementa una formulazione FEM CIP-DG di un problema ellittico del quarto ordine, con problemi locali di cell formula e benchmark analitici;
- Cesana–Grillo–Morandotti–Pastore (2025), *Dissipative Dynamics of Volterra Disclinations*, per l'evoluzione dissipativa dei difetti rotazionali;
- Briatico–Cesana–Morandotti (2026), *Effective Dynamics of Disclination Pairs* (preprint arXiv:2608.12233), sul limite dinamico di un dipolo di disclinazioni che, dopo riscalamento temporale nel regime di annichilazione, segue la legge di una dislocazione;
- Cesana–Morandotti–Sambo (2026), *Equilibrium and Interaction Regimes in Mixed Disclination-Dislocation Systems* (preprint arXiv:2608.10930), per energia, equilibrio e dinamica di sistemi misti.

Questi lavori modificano il posizionamento della proposta: **non** si propone di introdurre una prima discretizzazione numerica del problema Airy, perché una baseline CIP-DG esiste già. La domanda RGS–PRISM è se una discretizzazione geometrico-topologica possa preservare ulteriori identità discrete, trattare in modo strutturato le sorgenti e offrire un vantaggio misurabile rispetto a quella baseline.

La matrice bibliografica ragionata dei 55 record CVGMT, con classificazione M1–M9 e priorità di lettura, è nel documento [Matrice bibliografica Morandotti–RGS–PRISM](MATRICE_BIBLIOGRAFICA_MORANDOTTI_RGS_PRISM.md).

## 3. Domanda scientifica e ipotesi di lavoro

Il primo obiettivo è costruire una discretizzazione che conservi, a livello discreto, le identità geometriche e algebriche necessarie al problema.

La catena concettuale da verificare è:

1. **Difetti e incompatibilità:** codificare le sorgenti rotazionali e traslazionali, distinguendo carica di disclinazione, dipolo e vettore di Burgers.
2. **Complesso discreto:** rappresentare potenziali, campi e sorgenti su celle di dimensione appropriata, con operatori di incidenza orientati.
3. **Compatibilità:** verificare le identità di bordo/cobordo e la corretta localizzazione delle sorgenti, senza introdurre difetti spurii.
4. **Energia:** definire una forma discreta coerente con il funzionale elastico/Airy di riferimento e con le condizioni al contorno.
5. **Confronto:** confrontare minimi, energie, campi ricostruiti e comportamento del dipolo quando la separazione tende a zero nel regime di riscalamento previsto dal modello continuo.

Le corrispondenze tra le variabili del modello di Airy e i cochain RGS–PRISM sono **oggetto del lavoro**, non un'identificazione già dimostrata. In particolare, non si assume che il complesso Q6 o l'intera struttura PRISM siano automaticamente il reticolo fisico del materiale.

## 4. Piano di lavoro proposto

### Fase A — Benchmark bidimensionale di riferimento

- Selezionare una configurazione del modello Cesana–De Luca–Morandotti: una disclinazione, un dipolo di disclinazioni e il corrispondente limite di dislocazione.
- Fissare dominio, regolarizzazione del core, parametri elastici, condizioni al contorno e convenzioni di segno.
- Riprodurre anzitutto il riferimento FEM/CIP-DG 2026 (o un caso analitico equivalente) e implementare una discretizzazione RGS–PRISM sul medesimo problema.
- Confrontare energia minima, dipendenza dal raggio del core, dipendenza dalla separazione del dipolo, campi ricostruiti, residui, condizionamento e costo computazionale rispetto alla baseline CIP-DG.

### Fase B — Verifica matematica e numerica

Per ogni livello di raffinamento si registreranno:

- identità di complesso, in particolare d_{k+1}d_k=0;
- compatibilità delle sorgenti con i vincoli discreti;
- positività e condizionamento delle matrici di massa;
- simmetria e coercività della forma energetica sullo spazio vincolato;
- errore su energia e campi rispetto al riferimento;
- stabilità rispetto a raffinamento, quadratura e regolarizzazione;
- costo computazionale e memoria.

La convergenza variazionale non verrà dedotta da una semplice sequenza di energie numeriche: sarà necessario formulare e affrontare separatamente liminf, successioni di recupero e compattezza.

### Fase C — Estensione a geometrie e materiali AM

Solo dopo il benchmark bidimensionale, si potrà valutare una geometria non piana o una microstruttura più articolata, con attenzione a:

- difetti e campi di incompatibilità osservati o ricostruiti;
- geometrie di grano e interfacce;
- anisotropia elastica e orientazione locale;
- dati di tomografia, microscopia e prove meccaniche, se disponibili;
- confronto con FEM e modelli variazionali già usati nel contesto applicativo.

L'eventuale contributo IAM@PoliTO riguarderebbe la definizione del caso materiale, l'accesso a dati o campioni e la scelta delle osservabili sperimentali. Non si presuppone che tali dati siano già disponibili.

## 5. Cosa esiste già nel programma RGS–PRISM

Il repository di lavoro contiene una base matematica e computazionale utile a costruire il benchmark, ma non ancora un modello RGS validato di dislocazioni in un materiale reale.

### 5.1 Complessi cellulari e identità esatte

Il complesso cubicale Q6 ha 64 vertici, 192 archi e 240 facce quadrate. Le matrici intere di incidenza soddisfano esattamente B₁B₂=0. Sono inoltre presenti verifiche di mappe di catena, suddivisione cubicale e compatibilità con simmetrie discrete.

Questi risultati forniscono strumenti per rappresentare vincoli e incompatibilità in modo controllabile. Non costituiscono, da soli, una legge costitutiva o una corrispondenza già provata con i difetti atomistici.

### 5.2 Benchmark de Rham / FEEC

È disponibile il progetto computazionale projects/de_rham_benchmark/, con:

- complessi cubicali in 2D e 3D;
- mappe geometriche e metriche di pullback;
- operatori di Hodge e problemi agli autovalori generalizzati;
- controllo delle masse diagonali storiche, delle masse DEC corrette e delle matrici FEEC consistenti;
- proiezioni di forme e test di commutazione;
- studi di raffinamento e diagnostiche spettrali.

Un controllo importante è già stato incorporato: il collasso spettrale inizialmente osservato era legato alla convenzione storica non standard M_d(K)=vol_g(K) per cochain integrali di grado massimo. La sostituzione con il peso DEC corretto 1/vol_g(K), insieme al controllo FEEC consistente, rimuove il collasso nei casi affini e sinusoidali testati. La vecchia interpretazione come prova di perdita di compattezza è stata ritirata.

Questo è un risultato utile per la proposta proprio perché documenta un ciclo di verifica e correzione, non una rivendicazione di superiorità del metodo.

### 5.3 Raffinamento PRISM e convergenza

La famiglia prodotto PRISM e il suo simbolo spettrale sono implementati e testati su un riferimento piatto. Il relativo record T048 esplicita le condizioni necessarie per una convergenza di Mosco su spazi variabili.

La convergenza di Mosco della sequenza curva RGS–PRISM, la compattezza uniforme e la convergenza spettrale generale restano questioni aperte. Sono temi per un confronto analitico, non risultati che questa proposta dà per acquisiti.

### 5.4 Stato delle verifiche

| Elemento | Stato da comunicare |
|---|---|
| Identità di catena del complesso Q6 | Esatta nella codifica finita dichiarata |
| Suddivisioni e mappe cellulari verificate | Identità finite e test automatici nei casi documentati |
| Benchmark de Rham / FEEC | Implementato; risultati numerici su famiglie finite di mesh |
| Correzione della massa di grado massimo | Verificata nei casi affini e sinusoidali testati |
| Convergenza di Mosco RGS–PRISM curva | Aperta |
| Mappa difetti di Airy ↔ cochain RGS–PRISM | Da costruire e dimostrare |
| Validazione su dati di materiali AM | Non ancora eseguita |
| Vantaggio rispetto a FEM o modelli esistenti | Non dimostrato; sarà oggetto del benchmark |

## 6. Ruoli e interlocuzione

La proposta individua un collegamento di lavoro tra:

- **DISMA:** formulazione variazionale, incompatibilità cinematica, analisi di esistenza, limiti singolari e convergenza;
- **RGS–PRISM:** costruzione della discretizzazione geometrico-topologica, operatori, algoritmi, test e riproducibilità;
- **IAM@PoliTO:** eventuale definizione del problema materiale, geometrie, dati, caratterizzazione e confronto sperimentale.

La prima interlocuzione richiesta a Morandotti è scientifica e metodologica: individuare insieme il caso di benchmark più adatto e stabilire quali proprietà matematiche una discretizzazione alternativa dovrebbe necessariamente preservare.

## 7. Risultati attesi e criteri di arresto

Il primo risultato atteso non è un prodotto industriale, ma un benchmark riproducibile con:

1. problema continuo di riferimento completamente specificato;
2. mappa discreta e funzionale RGS–PRISM definiti;
3. test di compatibilità e stabilità;
4. confronto quantitativo di energia e campi su più raffinamenti;
5. elenco trasparente delle proprietà dimostrate e di quelle ancora aperte.

Il progetto proseguirà verso casi più complessi solo se la discretizzazione supera i controlli matematici e mostra un vantaggio concreto — in accuratezza, robustezza, costo o rappresentazione dei difetti — rispetto al riferimento. In caso contrario, il benchmark dovrà documentare anche i limiti e le ragioni del mancato vantaggio.

## 8. Richiesta concreta

Si propone un primo incontro tecnico per:

- scegliere una configurazione del modello del 2024 come benchmark iniziale;
- concordare variabili discrete, condizioni al contorno e funzionale;
- definire una metrica comune per confrontare soluzione di riferimento e discretizzazione RGS–PRISM;
- stabilire se e in quale fase abbia senso coinvolgere competenze e dati IAM@PoliTO.

L'obiettivo è un esperimento matematico circoscritto, falsificabile e riproducibile, che possa stabilire rapidamente se esiste una linea di lavoro comune.

---

## Appendice tecnica collegata

Il presente documento è la **nota di progetto e di interlocuzione**. Non sostituisce l'appendice tecnica, che contiene definizioni, formule, riferimenti ai record del repository, risultati di audit, limiti e criteri di riproducibilità.

**Documento tecnico di accompagnamento:** [APPENDICE TECNICA PER LA PROPOSTA MORANDOTTI — RGS–PRISM](APPENDICE_TECNICA_MORANDOTTI_RGS_PRISM.md).

La lettura congiunta è quindi:

- **questo documento:** perché il problema è rilevante, quale domanda si propone e come organizzare il lavoro;
- **appendice tecnica:** quali strutture e verifiche sono già disponibili, quali risultati sono riproducibili e quali passaggi matematici restano da dimostrare.

## Riferimenti

1. P. Cesana, L. De Luca, M. Morandotti (2024), *Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method*, SIAM J. Math. Anal. 56(1), 79–136. [DOI: 10.1137/22M1523443](https://doi.org/10.1137/22M1523443).
2. Repository tecnico RGS–PRISM: [fabianleonaressi95/theorem](https://github.com/fabianleonaressi95/theorem).
3. Benchmark de Rham / FEEC: [README e risultati](../projects/de_rham_benchmark/README.md).
4. P. Cesana, E. Fabbrini, M. Morandotti (2025), *Variational Formulation of Planar Linearized Elasticity with Incompatible Kinematics*, Journal of Elasticity 157, art. 71. [DOI: 10.1007/s10659-025-10161-5](https://doi.org/10.1007/s10659-025-10161-5).
5. P. Cesana, E. Fabbrini, A. A. León Baldelli, M. Morandotti (2026), *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, preprint [arXiv:2609.29614](https://arxiv.org/abs/2609.29614).
6. P. Cesana, A. Grillo, M. Morandotti, A. Pastore (2025), *Dissipative Dynamics of Volterra Disclinations*, SIAM J. Appl. Math. 85(4), 1361–1386. [DOI: 10.1137/24M1688096](https://doi.org/10.1137/24M1688096).
7. N. Briatico, P. Cesana, M. Morandotti (2026), *Effective Dynamics of Disclination Pairs*, preprint [arXiv:2608.12233](https://arxiv.org/abs/2608.12233).
8. P. Cesana, M. Morandotti, A. Sambo (2026), *Equilibrium and Interaction Regimes in Mixed Disclination-Dislocation Systems*, preprint [arXiv:2608.10930](https://arxiv.org/abs/2608.10930).
9. Matrice bibliografica ragionata: [MATRICE_BIBLIOGRAFICA_MORANDOTTI_RGS_PRISM.md](MATRICE_BIBLIOGRAFICA_MORANDOTTI_RGS_PRISM.md).

**FLN**


## Caso applicativo collegato: il pallone da calcio

Per il raccordo fra incompatibilità dei difetti, shell poligonale, ortotropia dei pannelli, cuciture e frame quaternionici si veda il [Documento di raccordo calcistico](DOCUMENTO_RACCORDO_CALCISTICO_MORANDOTTI_RGS_PRISM.md). Il pallone è proposto come banco di prova meccanico distinto dal benchmark piano di Airy; non si identificano automaticamente cuciture e difetti cristallini.


## Capitolo metodologico: tangenti, quaternioni e triplette

Per la ricostruzione passo per passo dei vincoli, del tangente 188D, della riduzione della Hessiana, delle triplette geometriche e spettrali, dei frame quaternionici e del confronto con il tangente 184D del guscio calcistico, si veda il nuovo [Capitolo sui sottospazi tangenti, quaternioni e triplette](CAPITOLO_SOTTOSPAZI_TANGENTI_QUATERNIONI_TRIPLETTE_MORANDOTTI.md). Questo capitolo esplicita anche i limiti delle etichette T1u/T2u e distingue il doppio ricoprimento SU(2)→SO(3) dalla rappresentazione finita del gruppo 2I.


## Operatore discreto di incompatibilità: sviluppo successivo

Il raccordo costruttivo tra tangente, deformazione, incompatibilità elastica e geometria quaternionica è sviluppato nel [capitolo sull'operatore discreto di incompatibilità](OPERATORE_INCOMPATIBILITA_TANGENTI_QUATERNIONI_MORANDOTTI.md). La nota distingue la formulazione debole piana di Saint-Venant, il ponte Cartan SU(2) (connessione indipendente e co-base), il ruolo delle triplette come settori di simmetria e l'estensione superficiale ancora da derivare.


## Primo prototipo dell'operatore di incompatibilità

È stato aggiunto un kernel software per la forma debole piana di Saint-Venant e per il carico distribuzionale Burgers/Frank. La specifica, i limiti e i test regressivi sono documentati nel [capitolo dedicato](OPERATORE_INCOMPATIBILITA_TANGENTI_QUATERNIONI_MORANDOTTI.md); il test è stato incluso nel workflow GitHub, ma non ne dichiariamo l'esito prima della conclusione della CI. Questo prototipo non è ancora il modello curvo RGS–PRISM né la sua connessione quaternionica.
