# T049B — Corrente assiale lorentziana su Q6 e PRISM

## Convenzione EC–Dirac

Il repository sorgente rgs-qlg-quaternion-bridge fissa la corrente reale contravariante \(J_5^a\), la firma \(\eta=(-,+,+,+)\) e la sorgente di Cartan
\[
\Sigma_{abc}=-\frac12\epsilon_{abcd}J_5^d,\qquad T_{abc}=\kappa\Sigma_{abc}.
\]
Nella stessa convenzione:
\[
T_{abc}T^{abc}=-\frac32\kappa^2J_{5a}J_5^a,\qquad
\mathcal L_{4f}=\frac{3\kappa}{16}J_{5a}J_5^a.
\]
Il modulo sorgente src/rgs_ec_spin_ensemble.py calcola già media, covarianza, secondo momento lorentziano e contributo di fluttuazione al contatto. T049B aggiunge la risoluzione spaziale Q6/PRISM e il calcolo diretto del bilineare dagli spinori.

## Corrente microscopica da spinori

Per spinori nel frame ortonormale locale:
\[
J_5^a=i\bar\psi\gamma^5\gamma^a\psi,\qquad
\bar\psi=i\psi^\dagger\gamma^0.
\]
Il codice implementa le matrici gamma e gamma5 della convenzione EC sorgente, controlla la realtà del bilineare e usa \(J_5^a\) per i momenti e i correlatori. Non genera né seleziona uno stato quantistico: lo spinore deve essere fornito.

## Due invarianti da non confondere

Il secondo momento locale è
\[
M^{ab}=\langle J_5^a(x)J_5^b(x)\rangle,\qquad
C^{ab}=M^{ab}-\langle J_5^a\rangle\langle J_5^b\rangle.
\]
Il contatto lorentziano è \(\eta_{ab}M^{ab}\), che può essere negativo o nullo per cancellazione. Una media nulla della corrente non implica un contatto nullo.

L'invariante di Weyssenhoff, invece, è definito nel sistema di riposo del fluido e sotto la condizione di Frenkel. Se viene fornita una 4-velocità unitaria timelike \(u^a\), il codice calcola
\[
J_\perp^a=h^a{}_bJ_5^b,\qquad
h^a{}_b=\delta^a_b+u^au_b,\qquad
s^2_{\mathrm{axial,rest}}=\eta_{ab}J_\perp^aJ_\perp^b.
\]
Questo è un **candidato proiettato** per il ponte con \(s^2=\frac12S_{ij}S_{ij}\), non ancora un'identificazione normalizzata: il coefficiente che lega il bilineare assiale al tensore di spin canonico deve essere derivato dalla variazione di Noether e dalla convenzione per \(S_{\mu\nu}\). Il codice riporta separatamente contatto lorentziano e invariante proiettato, e stima l'esponente del secondo solo se è fornita \(u^a\).

## Correlatore spaziale Q6–PRISM

Il correlatore tensoriale connesso per shell è
\[
C^{ab}(r)=\langle\delta J_5^a(x)\delta J_5^b(y)\rangle_{d_G(x,y)=r},
\qquad C_L(r)=\eta_{ab}C^{ab}(r).
\]
Il programma calcola inoltre l'invariante della corrente integrata nella cella e separa i contributi self e pair. Quest'ultimo non va identificato automaticamente con il contatto locale \(\eta_{ab}M^{ab}\).

Il confronto tra nodi è effettuato in una trivializzazione/frame comune fornita dall'utente. Il trasporto SU(2)/Spin lungo cammini non è ancora applicato: per un correlatore pienamente gauge-covariante occorre includere le olonomie orientate e gestire la dipendenza dal cammino nei cicli con curvatura.

## Input e riproducibilità

NPZ richiesto:
- scale_factors: (T,)
- uno tra spinors: (T,N,4) o (T,R,N,4), oppure axial_currents: (T,N,4) o (T,R,N,4)
- volumes: (T,), opzionale
- fluid_velocity: (T,4), opzionale, con \(\eta_{ab}u^au^b=-1\)

Per Q6, \(N=64\); per PRISM, \(N=69120\). Se si forniscono spinori, il codice calcola direttamente \(J_5^a\). Ogni valore al nodo è interpretato come contributo microscopico integrato alla corrente della cella; unità e normalizzazione vanno dichiarate. Il parametro --kappa aggiunge \(T^2\) e \(\mathcal L_{4f}\).

\`\`\`bash
python -m pytest tests/test_q6_prism_axial_current_correlator.py -q
python scripts/q6_prism_axial_current_correlator.py --input axial_q6.npz --geometry q6 --max-distance 6 --kappa KAPPA
python scripts/q6_prism_axial_current_correlator.py --input axial_prism.npz --geometry prism --max-distance 3 --kappa KAPPA
\`\`\`

## Stato epistemico

- **Derivato nella convenzione EC–Dirac sorgente:** relazione di Cartan, invariante \(T^2\) e coefficiente del contatto minimale.
- **Implementato e testato:** bilineare spinore→\(J_5^a\), momenti lorentziani, proiezione nel frame di riposo, correlatori tensoriali Q6/PRISM, contatto EC e decomposizione self/pair.
- **Non dimostrato:** che un campo di spinori fornito rappresenti lo stato quantistico fisico RGS–PSU/QLG; il programma non costruisce lo stato fisico. Il correlatore tra nodi resta in un frame comune, non ancora gauge-covariante.
- **Dato mancante:** non è presente un dataset validato di spinori o correnti \(J_5^a(x)\) su Q6/PRISM con unità, normalizzazione e prescrizione del contatto. Nessun esponente cosmologico fisico RGS–PSU viene quindi dichiarato.
- **Aperto:** normalizzazione Noether \(J_5\leftrightarrow S_{\mu\nu}\), ordinamento/renormalizzazione dell'operatore locale, convergenza in volume e scala di coarse-graining, trasporto gauge-covariante e variazione tetradica per ricavare l'equazione di stato.
