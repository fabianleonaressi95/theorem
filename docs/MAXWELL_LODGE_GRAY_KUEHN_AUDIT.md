# Audit: Gray–Kühn Maxwell–Lodge, elettrodinamica di Weber, olonomia e ponte RGS–QLG

**Scope:** valutazione critica dei lavori di Robert W. Gray e Steffen Kühn sulla crittica a Maxwell, del problema Maxwell–Lodge, dell'elettrodinamica di Weber, dell'EED di Hively–Loebl e del possibile collegamento con olonomia quaternionica (RGS–QLG).
**Status:** audit documentale e matematico; nessuna delle tesi alternative è assunta come dimostrata.

## 1. Il risultato centrale: la dimostrazione Gray–Kühn (2019) è stata ritirata nella sua forma originaria
**Scope:** valutazione critica dei lavori di Robert W. Gray e Steffen Kühn sulla critica alle equazioni di Maxwell, del problema Maxwell–Lodge, dell'elettrodinamica di Weber, dell'EED di Hively–Loebl e del possibile collegamento con olonomia quaternionica (RGS–QLG).
**Status:** audit documentale e matematico; nessuna delle tesi alternative è assunta come dimostrata.

## 1. Il risultato centrale: la dimostrazione Gray–Kühn (2019) non regge nella forma originaria

Gray e Kühn, *Proof of the Inconsistency of the Full Set of Maxwell's Equations with the Maxwell-Lodge Experiment* (2019), argomentavano che un solenoide con `∇×A = 0`, `∂A/∂t ≠ 0`, `∇Φ = 0` e `B = 0` esterno produrrebbe `∂E/∂t ≠ 0` in contrasto con Ampère–Maxwell.

**Dove fallisce:** l'ipotesi `B_out = 0` esatto deriva dalla soluzione *semplificata* che trascura la corrente di spostamento; la contraddizione viene dedotta usando Ampère–Maxwell *completa*. Gli autori stessi hanno pubblicato la rettifica: la scomparsa del campo magnetico esterno non è compatibile con le equazioni complete quando `E_φ` varia nel tempo.

**Formulazione corretta:** per un solenoide assialsimmetrico con `E_φ(r,t)`,

```
(∇×B)_φ = −∂B_z/∂r = μ₀ε₀ ∂E_φ/∂t
```

Se `E_φ` varia, `B_z` deve avere una struttura radiale compatibile. Piccolo ≠ identicamente nullo. La soluzione esatta per un solenoide infinito con sorgente arbitraria `I(t)` è nota (Rivera–Villarroel 2002 e lavori successivi).

**Verdetto:** la dimostrazione del 2019 non stabilisce l'inconsistenza di Maxwell. La rettifica degli autori riconosce che le ipotesi usate nella dimostrazione non sono simultaneamente compatibili; non va descritta come ritiro formale dell'intero articolo.

## 2. Maxwell–Lodge: configurazione coerente con Maxwell

Rousseaux–Kofman–Minazzoli (2008, EPJD 49, 249–256) studiano una bobina intorno a un solenoide alimentato in AC: EMF indotta con campo magnetico esterno molto piccolo.

Per il solenoide **infinito ideale**, fuori dal solenoide:

```
B = 0 localmente,   A_φ = Φ_B(t)/(2πr),   ∮_C A·dl = Φ_B ≠ 0
∇×A = 0 localmente (domain esterno)
```

La circonferenza `C` che avvolge il solenoide **non** delimita una superficie interamente nel dominio esterno: il dominio è moltiplemente connesso. La classe di `[A]` in `H¹_dR(domain)` è non banale — 1-forma chiusa non esatta. La circolazione `∮ A·dl` è gauge-invariante per gauge regolari e monovalori (`∮∇χ·dl = 0`); l'oggetto fisico globale è l'**olonomia**, non `A` locale.

La legge integrale di Faraday `∮E·dl = −dΦ_B/dt` è già contenuta in Maxwell: l'effetto non richiede potenziali come entità extra-field. L'interpretazione "solo i potenziali sono fisici" è una tesi interpretativa degli autori, non una dimostrazione.

### 2.1 Faraday integrale vs Kirchhoff concentrato

La forma `v_term = Ri + L di/dt` è valida solo nel modello a parametri concentrati (dimensioni ≪ scala elettromagnetica, campi quasi-statici). Con flusso magnetico variabile concatenato la forma fondamentale è la legge integrale

```
∮_C E·dl = −dΦ_B/dt = −d(NΦ_B)/dt = −L di/dt     (λ = Li, L costante)
```

che è un'EMF con circolazione non nulla: `E_indotto` non è globalmente `−∇φ`. La distinzione fra somma di cadute di potenziale (KVL circuitale) e circolazione di campo (Faraday) è esattamente il punto topologico della §2: nel dominio esterno moltiplemente connesso la circolazione sopravvive anche quando `∇×E = 0` localmente.

**Distinzione operativa obbligatoria:** solenoide infinito ideale ≠ solenoide finito sperimentale (B esterno non nullo vicino alle estremità, condizioni al contorno reali). Non trasferire proprietà topologiche ideali al dispositivo reale senza verifica.

## 3. La tesi sperimentale generale di Gray

In *Experimental Disproof of Maxwell* (2019) Gray sostiene che un potenziale vettore oscillante e localmente irrotazionale confuti Maxwell. **Non valido in generale:**

Se `∇×A = 0` in regione semplicemente connessa, `A = ∇χ`, e con la gauge `A' = A − ∇χ = 0`, `Φ' = Φ + ∂χ/∂t`, si ottiene `E = −∇Φ'` — lo stesso campo. Un `A` oscillante irrotazionale è una rappresentazione gauge, non una confutazione. Nel dominio non semplicemente connesso resta la componente chiusa-non-esatta (circolazione), compatibile con Maxwell.

Per valutare la tesi servirebbero: campo E misurato, procedura di determinazione di A, gauge operativo, condizioni al contorno, sensibilità della misura di B.

## 4. Elettrodinamica di Weber e Extended Electrodynamics

**Weber:** legge di forza carica-carica

```
F_W = (q_s q_d / 4πε₀) (r̂/r²) (1 − ṙ²/2c² + r r̈/c²)
```

non è una riscrittura di Maxwell–Lorentz: cambia la legge di forza e l'impostazione dinamica. La correzione Gray–Kühn non confuta Weber; e la capacità di Weber di descrivere l'induzione non confuta Maxwell.

**Hively–Loebl EED (2019, Physics Essays 32, 112–126):** propone `C = ∇·A + c⁻²∂Φ/∂t` come variabile fisica invece che vincolo di gauge Lorenz, con onde longitudinali scalari (SLW). L'argomento "8 equazioni per 6 componenti ⇒ sovradeterminazione" è errato: `∇·B=0` e `∇·E=ρ/ε₀` sono vincoli su dati iniziali/sorgenti la cui compatibilità temporale è garantita da `∂ρ/∂t + ∇·J = 0`. L'erratum del 2019 corregge refusi, non la tesi. Le previsioni SLW richiedono verifica indipendente.

**Stato sperimentale:** nessuna replica indipendente conclusiva del Maxwell–Lodge; test specifici di predizioni Weber hanno dato risultati misti (un risultato positivo interpretato come Weber 2021, DOI 10.2478/jee-2021-0052; risultati nulli Canadian J. Phys. 2017 e PIER M 2021). Qingsong Li (2025, preprint non peer-reviewed) confronta previsioni numeriche Weber per solenoidi lungo/corto.
**Stato sperimentale — perimetro della ricerca svolta:** i lavori esaminati comprendono un risultato del 2021 interpretato dagli autori come favorevole a una previsione Weber/Ampère (DOI 10.2478/jee-2021-0052) e risultati nulli su altre previsioni specifiche, relative alla massa inerziale degli elettroni (Canadian J. Phys. 2017; PIER M 2021). Questi esperimenti riguardano osservabili e modelli di apparato differenti: non sono repliche dello stesso test e non possono essere aggregati in un unico verdetto sulla legge di Weber. Il lavoro di Kühn riporta una dipendenza quantitativa del segnale dalla frequenza e un accordo con la stima Weber proposta dagli autori; sulla base delle fonti qui esaminate, però, non è disponibile un confronto pubblicato e indipendente con la previsione Maxwell–Lorentz completa per lo stesso apparato, la stessa procedura di misura e le medesime condizioni al contorno. Questo è un limite del dossier esaminato, non la dimostrazione che tale confronto non esista. Il preprint di Qingsong Li (2025, non peer-reviewed) presenta ulteriori calcoli Weber per solenoidi lunghi e corti, ma non costituisce da solo una verifica sperimentale indipendente.

## 5. Ponte verso RGS–QLG: olonomia come oggetto comune

Tre livelli distinti, non da identificare:

| Livello | Oggetto | Formula |
|---|---|---|
| Classico | circolazione di A | `∮_C A·dl = Φ_B` |
| Quantistico | fase Aharonov–Bohm | `Δθ = (q/ħ)∮_C A·dl = qΦ_B/ħ` |
| Geometrico | olonomia di connessione | `Hol_γ(∇) = P exp(−∫_γ ω)` |

Per un ponte RGS–QLG rigoroso servono: fibrato, gruppo di struttura, rappresentazione della carica, mappa connessione-quaternionica ↔ potenziale EM, e recupero di U(1) come caso particolare. **Una connessione quaternionica non è automaticamente una connessione elettromagnetica**: il confronto naturale parte da U(1) e dai suoi sollevamenti.

## 6. Protocollo sperimentale discriminante (se si volesse procedere)

Solenoide finito con geometria e `I(t)` misurati; acquisizione sincronizzata di `I, dI/dt`, EMF in bobina nota, `E_φ` tangenziale e `B` esterno; sweep in raggio/lunghezza/frequenza. Confronto diretto `ℰ_misurata − ℰ_maxwell` vs `ℰ_weber` **senza** calibrazione separata per punto. Un esperimento discrimina solo se le previsioni differiscono oltre le incertezze.
Solenoide finito con geometria, distribuzione di corrente e `I(t)` misurati; acquisizione sincronizzata di `I, dI/dt`, EMF nella bobina ricevente, e mappe di `E` e `B` con sensibilità e incertezze documentate; sweep in raggio, lunghezza e frequenza. Per ciascun modello si deve calcolare il segnale effettivamente restituito dalla medesima catena di misura, includendo condizioni iniziali e al contorno, risposta del ricevitore, accoppiamenti parassiti e incertezze. Il confronto è tra `ℰ_misurata` e le due previsioni indipendenti, `ℰ_Maxwell–Lorentz` e `ℰ_Weber`, non tra il residuo di un modello e una previsione dell'altro. Parametri e procedure di calibrazione devono essere fissati prima del confronto e non riadattati separatamente per ciascun punto. L'esperimento discrimina solo se le previsioni divergono più dell'incertezza combinata.

## 7. Registro dei verdetti

| Affermazione | Stato |
|---|---|
| Gray–Kühn 2019: inconsistenza di Maxwell | **Non valida nella forma originaria** (rettifica degli autori) |
| Maxwell–Lodge richiede potenziali "extra-field" | **Non dimostrato** — coerente con Faraday + topologia |
| `A` oscillante irrotazionale confuta Maxwell | **Non valido** — gauge-equivalente a `E=−∇Φ'` |
| Weber vs Maxwell–Lorentz | **Aperto** — confronto quantitativo mancante |
| Weber vs Maxwell–Lorentz | **Aperto nel dossier esaminato** — manca qui un confronto quantitativo omogeneo e indipendente |
| EED / onde scalari Hively–Loebl | **Non verificato** — previsioni da testare |
| Olonomia ↔ olonomia quaternionica QLG | **Ipotesi** — serve formulazione bundle/gauge esplicita |

**Formula da conservare:** la dimostrazione Gray–Kühn non stabilisce l'inconsistenza del sistema completo di Maxwell perché combina una soluzione che trascura la corrente di spostamento con Ampère–Maxwell completa. Maxwell–Lodge resta un esempio di circolazione non banale in dominio moltiplemente connesso, compatibile con Maxwell e rilevante per l'olonomia.

## 8. Prossimi passi

1. Audit integrale di *Experimental Disproof of Maxwell* (tesi sperimentale generale, distinta da Maxwell–Lodge).
2. Se si costruisce il ponte QLG: fissare fibrato, gruppo di gauge e mappa `A_μ ↔ ω_quaternionic` prima di qualsiasi calcolo.
3. Monitoraggio letteratura: repliche indipendenti Maxwell–Lodge, test quantitativi Weber, stato EED. Verifica *una tantum* su richiesta, non continua.
3. Aggiornamento bibliografico *una tantum*, su richiesta: repliche Maxwell–Lodge, test quantitativi Weber e stato EED. Il presente audit non pretende di dimostrare l'inesistenza di altri confronti o repliche.
