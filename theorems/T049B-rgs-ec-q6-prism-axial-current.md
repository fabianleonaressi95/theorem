# T049B — Corrente assiale lorentziana su Q6 e PRISM

## Collegamento con l'implementazione EC–Dirac RGS–PSU

Il repository sorgente `rgs-qlg-quaternion-bridge` definisce la corrente reale contravariante (J_5^a), firma (eta=(-,+,+,+)), sorgente di Cartan
[
\Sigma_{abc}=-\frac12\epsilon_{abcd}J_5^d,qquad T_{abc}=\kappa\Sigma_{abc},
]
e identità
[
T_{abc}T^{abc}=-\frac32\kappa^2J_{5a}J_5^a.
]
Nella stessa convenzione l'azione efficace minimale contiene
[
\mathcal L_{4f}=\frac{3\kappa}{16}J_{5a}J_5^a.
]
Il codice sorgente `src/rgs_ec_spin_ensemble.py` calcola già media, covarianza, secondo momento lorentziano e contributo di fluttuazione al contatto. T049B aggiunge la risoluzione spaziale su Q6/PRISM senza sostituire questa convenzione con un prodotto euclideo.

## Due correlatori, da non confondere

Per i campioni di corrente assiale sui vertici, il momento locale è
[
M^{ab}=\langle J_5^a(x)J_5^b(x)\rangle_{x,\mathrm{ensemble}},quad
C^{ab}=M^{ab}-\langle J_5^a\rangle\langle J_5^b\rangle.
]
Il contatto lorentziano è (eta_{ab}M^{ab}), che può essere negativo o nullo per cancellazione. La media nulla della corrente non implica un contatto nullo.

Il correlatore geometrico connesso per shell è
[
C^{ab}(r)=\langle\delta J_5^a(x)\delta J_5^b(y)\rangle_{d_G(x,y)=r},
quad C_L(r)=\eta_{ab}C^{ab}(r).
]
In aggiunta il codice calcola l'invariante della corrente integrata nella cella e ne separa esattamente i contributi self e pair. Questo invariante di cella non va identificato automaticamente con il contatto locale (eta_{ab}M^{ab}).

## Input e output

NPZ: `scale_factors (T,)`, e uno tra `spinors (T,N,4)` / `(T,R,N,4)` oppure `axial_currents (T,N,4)` / `(T,R,N,4)`, più facoltativamente `volumes (T,)`. Se si forniscono spinori, il codice calcola direttamente `J5^a=i bar(psi) gamma5 gamma^a psi` con le matrici e l'aggiunto di Dirac del modulo sorgente EC–Dirac. Gli spinori devono essere espressi nel frame ortonormale locale dichiarato. Ogni corrente al nodo è interpretata come contributo microscopico integrato alla corrente della cella; unità e normalizzazione vanno dichiarate dall'utente. `--kappa` aggiunge gli invarianti di torsione e il termine locale a quattro fermioni nelle convenzioni indicate.

Comandi:
```bash
python -m pytest tests/test_q6_prism_axial_current_correlator.py -q
python scripts/q6_prism_axial_current_correlator.py --input axial_q6.npz --geometry q6 --max-distance 6 --kappa KAPPA
python scripts/q6_prism_axial_current_correlator.py --input axial_prism.npz --geometry prism --max-distance 3 --kappa KAPPA
```

Il confronto tra componenti di nodi distinti è effettuato in una trivializzazione/frame comune fornita dall'utente. Non applica ancora trasporto parallelo SU(2)/Spin lungo cammini: per una correlazione pienamente gauge-covariante occorre includere le olonomie orientate lungo i cammini, tenendo conto della dipendenza dal cammino nei cicli con curvatura.\n\n## Stato epistemico

- **Derivato nella convenzione EC–Dirac sorgente:** relazione di Cartan e coefficienti (T^2), (mathcal L_{4f}).
- **Implementato e testato qui:** bilineare Dirac spinore→J5^a nella convenzione sorgente, momenti lorentziani, decomposizione media/fluttuazione, shell tensor correlators Q6/PRISM, contatto EC e decomposizione self/pair della cella.
- **Non dimostrato:** che un eventuale campo di spinori fornito rappresenti lo stato quantistico fisico RGS–PSU/QLG. Il codice calcola il bilineare, ma non genera né seleziona lo stato fisico. Il confronto tra nodi resta in una trivializzazione comune, non ancora gauge-covariante.
- **Dato mancante:** il repository sorgente contiene il motore di ensemble e gli operatori Dirac discreti, ma non un dataset validato di spinori o correnti (J_5^a(x)) su Q6/PRISM con unità, normalizzazione e prescrizione del contatto. Quindi non si dichiara un esponente cosmologico RGS–PSU.
- **Aperto:** rinormalizzazione/ordinamento dell'operatore locale, convergenza in volume e scala di coarse-graining, derivazione dell'equazione di stato dalla variazione tetradica dell'azione efficace.

