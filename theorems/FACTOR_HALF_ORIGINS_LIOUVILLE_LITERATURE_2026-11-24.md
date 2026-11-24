# Dossier — Origini del fattore \(1/2\), legge di Liouville e ponti RGS–PSU–PRISM

**Data:** 24 novembre 2026  
**Classificazione:** sintesi bibliografica e matematica. Teoremi classici, verifiche numeriche e ponti aperti sono tenuti distinti.

## 0. Tesi

Il numero \(1/2\) compare in meccanismi matematici differenti. La coincidenza numerica non prova un'origine comune. La domanda scientifica è quali strutture del programma siano collegate da mappe, identità o intertwiner effettivi.

La catena principale è:
\[
\text{simplettica/para-Kähler}\to\text{flusso Hamiltoniano}
\to\text{conservazione di Liouville}
\]
e, separatamente,
\[
D_5\to\det(g_B)\propto N^{-5}\to\text{volume di Bergman}.
\]
La prima è classica e dimostrata sotto le sue ipotesi; la seconda è un'identità geometrica già formalizzata. La derivazione della misura di Bergman dalla marginale Wilson–Q6 resta aperta.

## 1. La legge di Liouville già trovata

### 1.1 Teorema classico

Sia \((M,\omega)\) simplettica di dimensione \(2n\), \(H\in C^\infty(M)\), e \(X_H\) definito da \(\iota_{X_H}\omega=-dH\). Per la formula di Cartan:
\[
\mathcal L_{X_H}\omega
=d(\iota_{X_H}\omega)+\iota_{X_H}d\omega
=-d^2H=0.
\]
Per il flusso \(\Phi_t\):
\[
\Phi_t^*\omega=\omega,\qquad
\boxed{\Phi_t^*(\omega^n/n!)=\omega^n/n!.}
\]
In coordinate canoniche, con \(\omega=\sum_jdq_j\wedge dp_j\), si conserva \(d\mu_L=d^nq\,d^np\), a meno dell'orientazione.

**Stato:** dimostrato, risultato classico. È il contenuto di T001, non una nuova legge fisica proposta da RGS.

### 1.2 Hamiltoniana PSU a cinque coppie

La formulazione di lavoro già usata nel programma è
\[
H_5(q,p)=\frac12\left(\beta\lambda q^Tq+\beta^{-1}p^Tp\right),
\quad q,p\in\mathbb R^5,
\]
con
\[
\Omega=\sum_{j=1}^{5}dq_j\wedge dp_j,\qquad
d\mu_L=\frac{\Omega^5}{5!}=\prod_{j=1}^{5}dq_j\,dp_j.
\]
Se l'evoluzione è generata da \(H_5\) rispetto a \(\Omega\), allora
\[
\mathcal L_{X_{H_5}}d\mu_L=0,\qquad
\partial_t\rho+\{\rho,H_5\}=0.
\]
Il mezzo in \(H_5\) è la normalizzazione della forma quadratica Hamiltoniana; **non** è il fattore del teorema di Liouville. La conservazione segue da \(d\Omega=0\), non dal coefficiente dell'Hamiltoniana.

Per un oscillatore isotropo, dopo il riscalamento canonico appropriato, il flusso è una rotazione comune di fase \(z\mapsto e^{i\theta}z\). La funzione
\[
N(z)=1-2z^\dagger z+|z^Tz|^2
\]
è invariata, perché \(z^\dagger z\) e \(|z^Tz|^2\) restano invarianti. Per questa dinamica isotropa specifica è quindi preservata anche \(N^{-5}d\mu_L\). Non estendere la conclusione a dinamiche anisotrope o a evoluzioni PSU non identificate con questo flusso.

### 1.3 Ponte para-Kähler

Se \((M,J,g,\omega)\) è para-Kähler, \(\omega(X,Y)=g(JX,Y)\), \(d\omega=0\), e \(X_H\) è Hamiltoniano, allora
\[
\Phi_t^*\omega=\omega,\qquad
\Phi_t^*(\omega^n/n!)=\omega^n/n!.
\]
È il risultato condizionale formalizzato in T010 e T011. L'involuzione \(J^2=I\), da sola, non implica integrabilità, metrica neutra compatibile, chiusura di \(\omega\) o Hamiltonianità. T010 e T011 sono duplicati sostanziali: non vanno contati come due risultati indipendenti.

## 2. Il lato D5: densità di Bergman

Per
\[
D_5=\{z\in\mathbb C^5:N(z)>0,\ |z^Tz|<1\},\quad
N(z)=1-2z^\dagger z+|z^Tz|^2,
\]
la metrica di T002 è
\[
g_{i\bar j}=-5\,\partial_i\partial_{\bar j}\log N(z).
\]
Il calcolo determinante dà
\[
\boxed{\det(g_{i\bar j})=10^5N(z)^{-5}.}
\]
Con \(dV_g=2^5\det(g)d^{10}z\):
\[
dV_g=N(z)^{-5}d\mu_0,\qquad d\mu_0=20^5d^{10}z.
\]
Per \(z=(q+ip)/\sqrt2\), \(d^{10}z=2^{-5}d\mu_L\), quindi \(d\mu_0=10^5d\mu_L\) con le convenzioni dichiarate in T002.

Il kernel di Bergman del dominio di tipo IV in dimensione complessa 5 ha esponente 5:
\[
K(z,w)=C_5[1-2z\cdot\bar w+(z\cdot z)(\bar w\cdot\bar w)]^{-5}.
\]
La costante \(C_5\) scompare nella Hessiana di \(\log K(z,z)\). Questo spiega l'esponente \(N^{-5}\).

**Distinzione:** Liouville conserva \(\Omega^5/5!\); Bergman deriva dal determinante della metrica. Per identificare le due misure serve una mappa e il suo Jacobiano. Liouville, da solo, non produce \(N^{-5}\).

## 3. Le origini distinte di \(1/2\)

### 3.1 Involuzioni e proiettori
Se \(S^2=I\),
\[
P_\pm=\frac{I\pm S}{2}.
\]
Il mezzo è imposto dalla decomposizione negli autospazi \(+1\) e \(-1\) di una rappresentazione di \(\mathbb Z_2\). Origine algebrica; collegamento naturale con Anti-Twin, biverso e decomposizioni pari/dispari.

### 3.2 Forme antisimmetriche e doppio conteggio
\[
F=\frac12F_{\mu\nu}\,dx^\mu\wedge dx^\nu.
\]
Il fattore corregge il doppio conteggio delle coppie ordinate \((\mu,\nu)\) e \((\nu,\mu)\). Se si somma solo su \(\mu<\nu\), scompare. Rilevante per curvatura, torsione, coforme e gauge.

### 3.3 Volume simplettico
\[
d\mu_L=\frac{\omega^n}{n!}.
\]
Il fattore è \(1/2\) soltanto per \(n=2\); nel settore PSU a cinque coppie è \(1/5!=1/120\). Non attribuire al D5 a cinque coppie il mezzo del caso \(n=2\).

### 3.4 Hamiltoniana quadratica
\[
H=\frac12p^TM^{-1}p+V(q),\qquad T=\frac12m\dot q^2.
\]
È la normalizzazione della forma quadratica dell'energia. Nel modello PSU compare in \(H_5\); è distinta dal mezzo dei proiettori e dal fattoriale della misura Liouville.

### 3.5 Oscillatore quantistico e punto zero
\[
\widehat H=\hbar\omega(a^\dagger a+1/2),\qquad
E_n=\hbar\omega(n+1/2).
\]
Il valore \(E_0=\hbar\omega/2\) segue da \([a,a^\dagger]=1\) e dalla non negatività di \(a^\dagger a\). Per collegarlo al minimo positivo \(1/2\) di \(K_0\) servono operatori di creazione/annichilazione e una corrispondenza degli autospazi, non la sola coincidenza numerica.

### 3.6 Correzione di Maslov
Nella quantizzazione semiclassica, caustiche e varietà lagrangiane producono fasi del tipo \(\exp(-i\pi\mu/2)\). Il mezzo entra nella fase attraverso l'indice di Maslov e le convenzioni di quantizzazione. Servono una varietà simplettica, una lagrangiana, una famiglia di curve e l'indice effettivo calcolato.

### 3.7 Olonomia spinoriale
Il doppio rivestimento \(SU(2)\to SO(3)\) dà il segno meno a una rotazione di \(2\pi\) sui vettori spinoriali; \(4\pi\) restituisce l'identità. Il segno \(-1\) non è di per sé un autovalore \(1/2\). Il mezzo può comparire nelle etichette \(j\in\frac12\mathbb Z\), nei generatori e nelle fasi di rappresentazione. Per \(2I\) occorre l'azione concreta; non identificare inversione spaziale con l'elemento centrale di \(SU(2)\) senza prova.

### 3.8 Correzione APS ed eta
La formula di indice APS contiene, nella convenzione standard, una correzione \((\eta+h)/2\):
\[
\operatorname{ind}D^+=\int_M\alpha-\frac{\eta(B)+h}{2}.
\]
Il mezzo è legato all'operatore tangenziale al bordo e all'asimmetria spettrale. Non è un termine universale per operatori senza bordo. Per collegarlo a Rumin/eta torsion occorre identificare l'operatore di bordo e calcolare \(\eta(0)\).

### 3.9 Generatore browniano
Per il moto browniano standard su una varietà riemanniana è usuale \(\mathcal L=\frac12\Delta_g\). Il coefficiente dipende dalla convenzione della covarianza del rumore e dalla formula di Itô. Un generatore \(\Delta_g\) corrisponde a una diversa scala temporale/varianza. Non confonderlo con un'evoluzione quantistica unitaria.

### 3.10 Midpoint/Crank–Nicolson
\[
\frac{u^{n+1}-u^n}{\Delta t}
=\frac12(F(u^n)+F(u^{n+1})).
\]
Il mezzo è la media trapezoidale fra gli estremi temporali. Per generatori anti-hermitiani lo schema è collegato alla trasformazione di Cayley e alla conservazione dell'unitarietà discreta. Il collegamento ai kernel a due tempi va verificato sullo schema effettivamente usato.

### 3.11 Wilson su reticolo
L'azione di Wilson usa
\[
S_W=\beta\sum_p\left(1-\frac1N\operatorname{ReTr}U_p\right).
\]
Nell'espansione continua i coefficienti quadratici dipendono dalla normalizzazione della traccia, dei generatori e dalla somma sugli indici antisimmetrici. Il confronto con Q6 va fatto a livello dell'azione e delle convenzioni.

### 3.12 TEGR e torsione
La torsione scalare teleparallela è una combinazione di invarianti quadratici con coefficienti \(1/4\), \(1/2\) e \(-1\). La combinazione è quella che, sotto le ipotesi TEGR, dà equazioni equivalenti a quelle della relatività generale. Per confrontarla con la torsione RGS occorre fissare convenzioni di torsione, contorsione, connessione e indici.

### 3.13 Quozienti e coperture
Per un'azione libera di \(\mathbb Z_2\) con metrica che scende al quoziente:
\[
\operatorname{Vol}(M/\mathbb Z_2)=\frac12\operatorname{Vol}(M).
\]
Per \(S^3/2I\), invece, il fattore è \(1/|2I|=1/120\), non \(1/2\). Antipodale e quoziente binario icosaedrale sono distinti.

### 3.14 Polarizzazione quadratica
Per una forma quadratica \(Q\) e la forma bilineare simmetrica associata:
\[
B(x,y)=\frac12[Q(x+y)-Q(x)-Q(y)].
\]
Il mezzo deriva dall'espansione di \(Q(x+y)\); è un'identità algebrica, non una costante dinamica.

## 4. Risultato RGS già verificato sul settore a mezzo

L'audit degli array originali \(K_0,P_G,Z_A,Z_S\), tutti \(188\times188\), è registrato in RGS_HALF_ORIGINAL_ARRAYS_AUDIT_2026-11-24.md. I risultati numerici riportati sono:
\[
\operatorname{rank}P_G=64,\quad \operatorname{ran}P_G\simeq\ker K_0,
\]
\[
Z_A^T=-Z_A,\quad Z_S^T=Z_S,
\]
\[
\operatorname{spec}(Z_S)=(+1/2)^{(3)},(-1/2)^{(3)},0^{(182)},
\]
e sei valori singolari non nulli di \(Z_A\), tutti \(1/2\). Inoltre:
\[
Z_A^2+Z_S^2\simeq0,\quad Z_AZ_S+Z_SZ_A\simeq0,
\]
\[
Z_S^3-\frac14Z_S\simeq0,\quad Z_A^3+\frac14Z_A\simeq0.
\]
Quindi \(Q=4Z_S^2=-4Z_A^2\) è, entro la precisione numerica, un proiettore ortogonale di rango 6. Sul supporto, \(2Z_S\) è un'involuzione simmetrica e \(2Z_A\) è una struttura complessa antisimmetrica che scambia i due sottospazi tridimensionali.

La ricostruzione spettrale dà:
\[
\operatorname{spec}(K_0|_{J_A})=(0.5,0.6,0.7),\quad
\operatorname{spec}(K_0|_{J_B})=(0.8,0.9,1.0).
\]
Il blocco storico \(\frac12\operatorname{diag}(1,1,-1)\) è recuperato tramite la gauge di canale \(J_B^\sharp=-J_BD\), \(D=\operatorname{diag}(1,1,-1)\).

**Stato:** numericamente verificato sui dati archiviati, non dimostrazione esatta per una famiglia astratta. \(Z_A,Z_S\) non sono simmetrie conservate dell'intero \(K_0\): non commutano con \(K_0\). Non è dimostrata un'interpretazione come punto zero, Maslov, spin o APS.

PR #441 è già merged (merge commit 14defdf04c391916524ad1799b57d2e0e3ebc580). Distingue quattro possibili meccanismi: energia di punto zero, Maslov, olonomia spinoriale e correzione eta APS. Aggiunge scripts/audit_half_sector_vs_k0.py per confrontare supporti, angoli principali, commutatori e restrizioni spettrali. Il PR non dichiara il risultato del calcolo né un'interpretazione fisica: prima di concludere va eseguito e letto audits/HALF_SECTOR_VS_K0_2026-11-24.json.

## 5. Wilson–Q6 e D5: catena esistente

La catena T002–T009 va letta unitariamente:
- **T002:** densità geometrica di Bergman \(N^{-5}\) su \(D_5\).
- **T003:** una marginale esatta push-forward di flussi interi a numero finito di gradi di libertà è atomica e non coincide con una misura di Bergman assolutamente continua.
- **T004:** misure atomiche su griglia con pesi campionati da \(N^{-5}\) convergono debolmente alla misura di Bergman troncata. È un teorema di approssimazione, non una derivazione Wilson.
- **T005:** la marginale Wilson Q6 sulle fibre ha formula esatta e coefficienti strettamente positivi a ogni \(\beta>0\); non seleziona un cutoff duro Hua a accoppiamento finito.
- **T006:** il quoziente del toro di annichilazione per il gruppo gauge è \(\mathbb T^5\).
- **T007:** la media gauge è positiva e continua sul toro efficace; i coefficienti di Fourier sono le marginali Wilson sulle fibre.
- **T008:** criterio per una convergenza debole Wilson→Bergman; non dimostra che la successione Wilson soddisfi il criterio.
- **T009:** forma quadratica efficace sul quoziente; il passaggio a cinque coordinate complesse, struttura simplettica, \(D_5\) e densità \(N^{-5}\) richiede ulteriori dati.
- **T001/T010:** conservazione di Liouville sotto ipotesi simplettiche/para-Kähler.

Conclusione:
\[
\text{Wilson–Q6 finito: marginale atomica esatta su }\mathbb T^5,
\]
\[
\text{D5: volume di Bergman continuo }N^{-5}d^{10}z,
\]
\[
\text{ponte aperto: limite debole + mappa canonica + Jacobiano derivato}.
\]
T003 vieta l'identità esatta a cutoff finito ma non un limite debole. T004 mostra che il tipo di limite è matematicamente possibile se i pesi locali corretti sono presenti. T005–T009 precisano cosa la marginale Wilson effettiva fa e cosa non fa.

## 6. Matrice di confronto

| Origine | Struttura generatrice | Collegamento nel programma | Stato |
|---|---|---|---|
| Proiettori \(P_\pm\) | Involuzione \(\mathbb Z_2\) | Anti-Twin/biverso | Classico; applicazione specifica da verificare |
| Forma antisimmetrica | Doppio conteggio | Coforme, torsione, gauge | Convenzione |
| Volume simplettico | \(\omega^n/n!\) | PSU a cinque coppie | Fattore \(1/120\) |
| Hamiltoniana | Forma quadratica | \(H_5\) | Formula di modello |
| Punto zero | Algebra dell'oscillatore | Primo autovalore \(K_0\) | Analogia; origine non dimostrata |
| Maslov | Caustiche/lagrangiane | Flussi e olonomie | Aperto |
| Spinoriale | \(SU(2)\to SO(3)\) | \(2I\), spin | Teoria classica; intertwiner da verificare |
| APS | Eta e operatore al bordo | Rumin/eta torsion | Richiede operatore di bordo ed eta |
| Browniano | Generatore \(\Delta/2\) | Kernel diffusivi | Dipende dal generatore |
| Midpoint | Media temporale | Kernel a due tempi/T051 | Schema da verificare |
| Wilson | Traccia e plaquette | Q6 gauge | Convenzioni da confrontare |
| TEGR | Invarianti quadratici di torsione | Vierbein RGS | Identificazione tensoriale aperta |
| Quoziente \(\mathbb Z_2\) | Copertura a due fogli | Antipodale/biverso | Se azione libera |
| Polarizzazione | Espansione quadratica | Forme energetiche | Identità algebrica |

## 7. Verifiche conclusive ordinate

1. Eseguire lo script già aggiunto da PR #441:  
   python scripts/audit_half_sector_vs_k0.py --k0 K0.npy --zs Z_S.npy --za Z_A.npy  
   Archiviare il JSON e leggere coseni principali, intersezioni, commutatori e spettro ristretto. Non formulare interpretazioni fisiche prima del report.
2. Per PSU, specificare coordinate, \(\Omega\), Hamiltoniana, campo \(X_H\), mappa \(z=\Phi(q,p)\) e Jacobiano; verificare che la mappa sia canonica/simplettica. Nel caso isotropo, dimostrare l'invarianza di \(N\) sotto il flusso preciso.
3. Tenere separate le normalizzazioni di volume: \(\Omega^5/5!\), il fattore costante \(10^5\) fra \(d\mu_0\) e \(d\mu_L\), e la densità non costante \(N^{-5}\).
4. Per Wilson→Bergman, definire mappe, scale, pesi e normalizzazioni; verificare il criterio T008 e il confronto locale T004. La positività T005 esclude un cutoff duro per annullamento dei pesi, non una concentrazione limite.
5. Per le quattro interpretazioni fisiche di \(1/2\), richiedere rispettivamente: operatori \(a,a^\dagger\); indice di Maslov; rappresentazione/olonomia \(SU(2)\); operatore di bordo e \(\eta(0)\).

## 8. Bibliografia ragionata

### Simplettica, Hamiltoniana e Liouville
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989, capp. 8–9.
- R. Abraham e J. E. Marsden, *Foundations of Mechanics*, 2nd ed., Benjamin/Cummings, 1978.
- J.-M. Souriau, *Structure of Dynamical Systems: A Symplectic View of Physics*, Birkhäuser, 1997.
- V. Cruceanu, P. Fortuny e P. M. Gadea, “A survey on paracomplex geometry,” *Rocky Mountain Journal of Mathematics* 26 (1996), 83–115.

### Domini simmetrici, Bergman e Hua
- L. K. Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains*, American Mathematical Society, 1963.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978.
- J. Faraut e A. Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994.
- R. X. Dong, S.-Y. Li e J. N. Treuer, “Sharp pointwise and uniform estimates for \(\bar\partial\),” *Analysis & PDE* 16 (2023), 407–431; https://msp.org/apde/2023/16-2/apde-v16-n2-p04-p.pdf.

### Oscillatore e quantizzazione semiclassica
- V. P. Maslov, *Théorie des perturbations et méthodes asymptotiques*, Dunod, 1972.
- L. Hörmander, “Fourier integral operators I,” *Acta Mathematica* 127 (1971), 79–183.
- J. J. Duistermaat, “Oscillatory integrals, Lagrange immersions and unfoldings of singularities,” *Communications on Pure and Applied Mathematics* 27 (1974), 207–281.

### Spin e doppio rivestimento
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction*, 2nd ed., Springer, 2015.
- J.-P. Serre, *Linear Representations of Finite Groups*, Springer.

### Indice APS ed eta
- M. F. Atiyah, V. K. Patodi e I. M. Singer, “Spectral asymmetry and Riemannian geometry I,” *Mathematical Proceedings of the Cambridge Philosophical Society* 77 (1975), 43–69, DOI https://doi.org/10.1017/S0305004100049410.
- M. F. Atiyah, V. K. Patodi e I. M. Singer, “Spectral asymmetry and Riemannian geometry II,” *Mathematical Proceedings of the Cambridge Philosophical Society* 78 (1975), 405–432, DOI https://doi.org/10.1017/S0305004100051872.
- M. F. Atiyah, V. K. Patodi e I. M. Singer, “Spectral asymmetry and Riemannian geometry III,” *Mathematical Proceedings of the Cambridge Philosophical Society* 79 (1976), 71–99, DOI https://doi.org/10.1017/S0305004100052105.

### Diffusione e discretizzazione temporale
- E. P. Hsu, *Stochastic Analysis on Manifolds*, American Mathematical Society, 2002.
- J. Crank e P. Nicolson, “A practical method for numerical evaluation of solutions of partial differential equations of the heat-conduction type,” *Mathematical Proceedings of the Cambridge Philosophical Society* 43 (1947), 50–67, DOI https://doi.org/10.1017/S0305004100023197.

### Gauge su reticolo e torsione
- K. G. Wilson, “Confinement of quarks,” *Physical Review D* 10 (1974), 2445–2459, DOI https://doi.org/10.1103/PhysRevD.10.2445.
- J. B. Kogut, “An introduction to lattice gauge theory and spin systems,” *Reviews of Modern Physics* 51 (1979), 659–713, DOI https://doi.org/10.1103/RevModPhys.51.659.
- J. W. Maluf, “The teleparallel equivalent of general relativity,” *Annalen der Physik* 525 (2013), 339–357, DOI https://doi.org/10.1002/andp.201200272.

### Misure, convergenza e Fourier
- P. Billingsley, *Convergence of Probability Measures*, 2nd ed., Wiley, 1999.
- V. I. Bogachev, *Measure Theory*, Vol. I, Springer, 2007.
- W. Rudin, *Fourier Analysis on Groups*, Wiley, 1962.
- NIST Digital Library of Mathematical Functions, §§10.25, 10.35, 10.41: https://dlmf.nist.gov/10.25, https://dlmf.nist.gov/10.35, https://dlmf.nist.gov/10.41.

## 9. Indice dei risultati già presenti

| File/risultato | Contenuto | Stato da conservare |
|---|---|---|
| T001-liouville-theorem.md | Teorema classico di Liouville | Dimostrato |
| T002-d5-bergman-volume-density.md | Determinante Bergman D5 e \(N^{-5}\) | Identità geometrica dimostrata |
| T003-wilson-atomic-marginal-no-go.md | No-go atomico a scala finita | Dimostrato sotto ipotesi |
| T004-riemann-sums-bergman-weak-limit.md | Convergenza geometrica a Bergman troncata | Dimostrato; non è un teorema Wilson |
| T005-q6-wilson-fiber-marginal-support.md | Marginale Wilson e positività | Dimostrato nel modello definito |
| T006-q6-wilson-five-torus-quotient.md | Quoziente \(\mathbb T^5\) | Dimostrato |
| T007-q6-gauge-average-fourier-marginal.md | Media gauge e coefficienti Fourier | Dimostrato |
| T008-wilson-to-bergman-weak-convergence-criterion.md | Criterio Wilson→Bergman | Criterio; applicazione aperta |
| T009-effective-wilson-fiber-quadratic-form.md | Forma quadratica efficace | Distinguere identità generali e verifica Q6 |
| T010-para-kahler-liouville-psu.md | Ponte para-Kähler–Liouville | Condizionale per PSU |
| T011-para-kahler-liouville-psu.md | Duplicato sostanziale di T010 | Non indipendente |
| RGS_HALF_SCALE_CARRIER_PROPOSITION_2026-11-24.md | Carrier 6D e triplette K0 | Verifica numerica |
| RGS_HALF_ORIGINAL_ARRAYS_AUDIT_2026-11-24.md | Audit degli array originali | Verifica numerica |
| PR #441 | Audit delle origini fisiche del mezzo | Merged; report dello script da eseguire/leggere |

## 10. Conclusione

La legge di Liouville è un risultato acquisito: un flusso Hamiltoniano conserva la forma simplettica e il volume di fase. Nel settore PSU a cinque coppie la misura è \(\Omega^5/5!\); il mezzo nell'Hamiltoniana è una normalizzazione distinta. Il volume di Bergman su \(D_5\) ha densità \(N^{-5}\), dimostrata separatamente in T002.

La marginale Wilson–Q6 è atomica ed esatta a scala finita, con quoziente efficace \(\mathbb T^5\); non coincide esattamente con la misura continua di Bergman. Il limite debole resta aperto. Nel settore RGS, \(1/2\) è un valore spettrale e una scala algebrica verificata numericamente su un supporto di dimensione sei; il suo significato fisico non è ancora selezionato.

La tesi sostenibile è: **il programma contiene realizzazioni concrete di più meccanismi indipendenti che producono \(1/2\); l'eventuale unificazione va dimostrata con mappe, identità e intertwiner, non dalla coincidenza del coefficiente.**


## 11. Addendum — square reflection, PRISM biverso and the RGS carrier

The square's diagonal reflection exchanges its two congruent triangular halves. After identifying the two \(L^2\) spaces by reflection, its action is the sheet-swap involution \(S\), and the normalized parity projectors are \((I\pm S)/2\).

The new record [T145](T145-square-reflection-prism-biverse-rgs-carrier.md) establishes the exact PRISM \(K_2\)-coupling reduction and its numerical realization on the original RGS six-dimensional carrier:
\[
K_0|_{\mathcal W}\simeq
I_2\otimes L_\Omega+0.15(I_6-S),
\qquad
\operatorname{spec}(L_\Omega)=\{0.5,0.6,0.7\}.
\]
The two parity branches are \(\{0.5,0.6,0.7\}\) and \(\{0.8,0.9,1.0\}\); their separation is \(2\kappa=0.30\). The basis map is an intertwiner for the compressed six-dimensional operator, with reported leakage \(3.1\times10^{-12}\).

This gives a concrete connection between square reflection, the PRISM biverso and the RGS carrier. It does not identify the ordinary Euclidean square Laplacian with the graph-coupled biverso operator, and it does not turn the many occurrences of \(1/2\) into one universal mechanism. The distinction between the biverso exchange involution and the original \(2Z_S\) sheet-sign involution is explicit in T145.

**Literature:** Godsil–Royle, *Algebraic Graph Theory*, GTM 207, Springer (2001), Ch. 14; Merris, “Laplacian matrices of graphs: a survey,” *Linear Algebra Appl.* 197–198 (1994), 143–176, DOI 10.1016/0024-3795(94)90486-3; Serre, *Linear Representations of Finite Groups* (1977).
