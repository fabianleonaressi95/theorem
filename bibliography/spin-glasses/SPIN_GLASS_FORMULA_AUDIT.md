# F005–F006 — Edwards–Anderson, Sherrington–Kirkpatrick, Parisi, Guerra, Talagrand e Panchenko

**Scopo:** estrarre le formule fondamentali dei modelli spin-glass e fissare esattamente quali risultati possono essere usati sul grafo finito Q6 e quali richiedono un limite termodinamico.

## 1. Edwards–Anderson (EA): modello a corto raggio

Su un grafo reticolare o più in generale un grafo \(G=(V,E)\), con spin Ising \(\sigma_i\in\{-1,+1\}\), la forma standard è
\[
\boxed{H_J(\sigma)=-\sum_{(i,j)\in E}J_{ij}\sigma_i\sigma_j
-h\sum_{i\in V}\sigma_i.}
\]
I couplings \(J_{ij}\) sono variabili casuali indipendenti (quenched), spesso con legge gaussiana
\[
J_{ij}\sim\mathcal N(J_0,\Delta^2)
\]
oppure bimodale
\[
\mathbb P(J_{ij}=+J)=p,\qquad
\mathbb P(J_{ij}=-J)=1-p.
\]
A couplings fissati:
\[
Z_J(\beta)=\sum_{\sigma\in\{-1,+1\}^{|V|}}e^{-\beta H_J(\sigma)},
\qquad
F_J(\beta)=-\beta^{-1}\log Z_J(\beta).
\]
La media quenched è \(\mathbb E_J[F_J]\), non \(-\beta^{-1}\log\mathbb E_J[Z_J]\). Questa distinzione è sostanziale.

## 2. Sherrington–Kirkpatrick (SK): interazione a raggio infinito

Nella convenzione originale:
\[
\boxed{H_J(\sigma)=-\frac12\sum_{i\ne j}J_{ij}\sigma_i\sigma_j,}
\]
con couplings gaussiani indipendenti per coppie e scalatura
\[
J_{ij}\sim\mathcal N\!\left(\frac{\bar J_0}{N},
\frac{\bar J^2}{N}\right).
\]
La media \(\bar J_0/N\) conserva il contributo ferromagnetico estensivo e la varianza \(\bar J^2/N\) conserva energia libera estensiva. In una convenzione moderna equivalente si scrive
\[
H_N(\sigma)=-\frac{\beta}{\sqrt N}\sum_{i<j}g_{ij}\sigma_i\sigma_j
-h\sum_i\sigma_i,
\qquad g_{ij}\stackrel{iid}{\sim}\mathcal N(0,1),
\]
ma bisogna controllare se il simbolo \(\beta\) è incluso nell'Hamiltoniana o nella misura di Gibbs: non mescolare le due convenzioni.

## 3. Overlap fra repliche

Per due configurazioni \(\sigma^a,\sigma^b\):
\[
\boxed{R_{ab}=\frac1N\sum_{i=1}^N\sigma_i^a\sigma_i^b.}
\]
L'overlap diagonale è \(R_{aa}=1\). L'array degli overlap è l'osservabile centrale per la struttura delle fasi spin-glass.

Per un grafo finito Q6, questa definizione si applica con \(N=64\), ma il singolo valore \(N=64\) non definisce un limite termodinamico.

## 4. Replica trick: identità formale e cautela

L'identità usata nel calcolo formale è
\[
\log Z=\lim_{r\to0}\frac{Z^r-1}{r}.
\]
Per la media quenched:
\[
\mathbb E\log Z
=\lim_{r\to0}\frac{\mathbb E[Z^r]-1}{r}.
\]
È un passaggio formale finché non si giustificano l'analiticità/continuazione in \(r\), l'intercambio dei limiti e le operazioni di media. Non è una dimostrazione rigorosa del metodo delle repliche.

## 5. Equazioni di Ghirlanda–Guerra

Nella forma standard, per funzioni limitate \(f\) dell'array degli overlap delle prime \(n\) repliche e funzione limitata \(\psi\):
\[
\boxed{
\mathbb E\langle f\,\psi(R_{1,n+1})\rangle
=\frac1n\mathbb E\langle f\rangle\,
\mathbb E\langle\psi(R_{12})\rangle
+\frac1n\sum_{\ell=2}^{n}
\mathbb E\langle f\,\psi(R_{1\ell})\rangle.
}
\]
Queste identità sono proprietà del limite Gibbs sotto ipotesi e perturbazioni appropriate; non sono automaticamente vere per una simulazione finita o per un campione finito di repliche.

## 6. Formula di Parisi e normalizzazione verificata sulle fonti primarie

Questa sezione fissa una convenzione precisa e non mescola il parametro d'inversa temperatura nel Hamiltoniano con quello nella misura di Gibbs. Le formule sono confrontate con Talagrand (2006), §1, equazioni (1.1)–(1.14), e Guerra (2003), §§2–4, equazioni (10)–(15), Theorems 3–5.

### 6.1 Convenzione SK di Talagrand

Talagrand definisce (Annals of Mathematics 163 (2006), p. 221, eq. (1.1))
\[
H_N(\sigma)=-\frac{\beta}{\sqrt N}\sum_{i<j}g_{ij}\sigma_i\sigma_j,
\qquad
Z_N=\sum_{\sigma\in\{-1,1\}^N}
\exp\!\left(H_N(\sigma)+h\sum_i\sigma_i\right),
\]
con \(g_{ij}\) i.i.d. standard gaussiani. Qui \(\beta\) è già dentro \(H_N\), mentre \(h\) è il campo adimensionale nella misura.

Per \(R_{12}=N^{-1}\sum_i\sigma_i^1\sigma_i^2\), ponendo \(r_i=\sigma_i^1\sigma_i^2\in\{\pm1\}\),
\[
\begin{aligned}
\mathbb E H_N(\sigma^1)H_N(\sigma^2)
&=\frac{\beta^2}{N}\sum_{i<j}r_ir_j\\
&=\frac{\beta^2}{2N}\left[\left(\sum_i r_i\right)^2-N\right]\\
&=\frac{\beta^2N}{2}R_{12}^2-\frac{\beta^2}{2}.
\end{aligned}
\]
Quindi
\[
N^{-1}\operatorname{Cov}(H_N(\sigma^1),H_N(\sigma^2))
=\underbrace{\frac{\beta^2}{2}R_{12}^2}_{\xi_{\rm cov}(R_{12})}
-\frac{\beta^2}{2N}.
\]
Il limite di covarianza è \(\xi_{\rm cov}(q)=\beta^2q^2/2\), esattamente come Talagrand eq. (1.3)–(1.4), p. 222. Il termine finito \(-\beta^2/(2N)\) è una correzione \(O(N^{-1})\), non una seconda convenzione per il coefficiente principale.

**Origine del fattore \(1/2\):** è l'identità della somma su coppie non ordinate
\[
\sum_{i<j}r_ir_j=\frac12\left[\left(\sum_i r_i\right)^2-N\right].
\]
Non va eliminato lasciando invariati \(N^{-1}\), la varianza dei couplings e la definizione di \(\beta\).

### 6.2 PDE di Parisi nella convenzione di Talagrand

Sia \(x(q)\) la funzione non decrescente (right-continuous) di ordine Parisi, con valori in \([0,1]\); non la denotiamo \(\xi(q)\), per evitare di confonderla con la funzione di covarianza \(\xi_{\rm cov}\). La PDE all'indietro è
\[
\partial_q\Phi(q,y)
=-\frac{\beta^2}{2}
\left(\partial_{yy}\Phi(q,y)
+x(q)(\partial_y\Phi(q,y))^2\right),
\qquad
\Phi(1,y)=\log(2\cosh y).
\]
La funzionale è
\[
\boxed{\mathcal P_\beta(x)
=\Phi(0,h)-\frac{\beta^2}{2}\int_0^1q\,x(q)\,dq,}
\]
e la pressione limite è \(\inf_x\mathcal P_\beta(x)\). Questa è la normalizzazione di Talagrand eq. (1.11)–(1.14), pp. 222–223, espressa nella forma PDE continua.

Il fattore è anche visibile nella versione a passi finiti. Talagrand pone
\[
\theta(q)=q\,\xi_{\rm cov}'(q)-\xi_{\rm cov}(q)=\frac{\beta^2q^2}{2}
\]
e scrive
\[
\mathcal P_k(\mathbf m,\mathbf q)
=\log2+X_0-\frac12\sum_{\ell=1}^k
m_\ell\bigl[\theta(q_{\ell+1})-\theta(q_\ell)\bigr].
\]
Il termine di penalità è quindi
\[
-\frac{\beta^2}{4}\sum_{\ell=1}^k
m_\ell(q_{\ell+1}^2-q_\ell^2)
=-\frac{\beta^2}{2}\int_0^1q\,x(q)\,dq.
\]
La PDE e la penalità contengono il \(1/2\) richiesto dalla covarianza SK di questa convenzione.

### 6.3 Confronto con Guerra (2003): campo e temperatura

Guerra (arXiv:cond-mat/0205123, §§2–3, eq. (10)–(15), pp. 3–5) usa invece
\[
H_N(\sigma,h,J)=-\frac1{\sqrt N}\sum_{i<j}J_{ij}\sigma_i\sigma_j
-h\sum_i\sigma_i,\qquad
Z_N=\sum_\sigma e^{-\beta H_N(\sigma,h,J)}.
\]
In questa convenzione \(\beta\) è fuori dal Hamiltoniano. La sua PDE è
\[
\partial_q f(q,y)+\frac12
\left(f_{yy}(q,y)+x(q)f_y(q,y)^2\right)=0,
\qquad f(1,y)=\log\cosh(\beta y),
\]
e la funzionale trial
\[
\bar\alpha(\beta,h;x)=\log2+f(0,h;x,\beta)
-\frac{\beta^2}{2}\int_0^1q\,x(q)\,dq.
\]
La conversione alla PDE di Talagrand si ottiene ponendo
\[
\Phi(q,z)=\log2+f(q,z/\beta);
\]
il campo è da convertire coerentemente: il valore iniziale è \(\Phi(0,\beta h)\) se \(h\) è il campo fisico della convenzione di Guerra.

Guerra, Theorem 3 (pp. 6–7), dimostra
\[
\alpha_N(\beta,h):=N^{-1}\mathbb E\log Z_N
\leq \inf_x\bar\alpha(\beta,h;x)
\]
uniformemente in \(N\), con una sum rule non negativa (Theorems 4–5). È un **upper bound sulla pressione**. Per l'energia libera fisica \(f_N=-\alpha_N/\beta\), la stessa disuguaglianza diventa un **lower bound**. Talagrand (2006), Theorem 1.1, dimostra l'uguaglianza nel limite termodinamico; non si devono attribuire a Guerra, da solo, l'intera uguaglianza finale.

### 6.4 Diagnosi della discrepanza “\(\beta^2\) senza \(1/2\)”

Una formula che mostra \(\beta^2\) al posto di \(\beta^2/2\) nel coefficiente della PDE o nel termine di penalità può essere corretta soltanto se la funzione di covarianza è normalizzata come \(\xi_{\rm cov}(q)=\beta^2q^2\), oppure se il parametro \(\beta\) è riscalato di \(\sqrt2\), o se sono cambiate le convenzioni sui couplings/Hamiltoniano. Non è la stessa normalizzazione dell'equazione (1.1) di Talagrand.

**Conclusione dell'audit del fattore:** per \(H_N=-\beta N^{-1/2}\sum_{i<j}g_{ij}\sigma_i\sigma_j\), con \(g_{ij}\sim N(0,1)\), overlap \(R=N^{-1}\sum_i\sigma_i^1\sigma_i^2\), e pressione \(N^{-1}\mathbb E\log Z_N\), i fattori \(\beta^2/2\) nella PDE e nella penalità sono verificati dalla fonte primaria. Il fattore \(1/2\) non è una scelta estetica; segue dalla covarianza.

## 7. Ultrametricità di Panchenko

Sotto le identità di Ghirlanda–Guerra, per una misura casuale sul ball unitario di uno spazio di Hilbert separabile, Panchenko dimostra l'ultrametricità del supporto. In termini di overlap:
\[
\boxed{R_{12}\ge\min(R_{13},R_{23})\quad\text{quasi sicuramente}.}
\]
La forma equivalente sulle distanze, quando gli overlap sono prodotti scalari di vettori sullo stesso raggio, è
\[
\|\sigma^1-\sigma^2\|
\le\max\{\|\sigma^1-\sigma^3\|,\|\sigma^2-\sigma^3\|\}.
\]
È un teorema condizionato alle Ghirlanda–Guerra identities, non un teorema universale su ogni grafo finito.

## 8. Audit delle affermazioni e limiti

- EA e SK sono modelli distinti: EA è a corto raggio su un grafo reticolare; SK è mean-field completo con varianza scalata come \(1/N\).
- La soluzione replica-simmetrica originale SK non è corretta a tutte le temperature; la rottura di simmetria delle repliche di Parisi è essenziale a bassa temperatura.
- Guerra fornisce una bound inferiore e una sum rule; Talagrand dimostra l'uguaglianza con il funzionale di Parisi per SK.
- Panchenko dimostra ultrametricità assumendo Ghirlanda–Guerra; non è lecito inferire Ghirlanda–Guerra da una distribuzione numerica che appare gerarchica.
- I risultati di ultrametricità nel modello EA tridimensionale sono oggetto di test numerici e dibattito; non vanno confusi con il teorema mean-field di Panchenko.

## 9. Trasferibilità a Q6 e al filone RGS–PRISM

Sul cubo \(Q_6\), \(|V|=64\), \(|E|=192\), il modello EA è perfettamente definibile:
\[
H_J(\sigma)=-\sum_{(i,j)\in E(Q_6)}J_{ij}\sigma_i\sigma_j.
\]
Si possono calcolare esattamente, enumerando \(2^{64}\) configurazioni solo con metodi specializzati o campionando, quantità finite quali energia, overlap tra repliche, frustrazione e correlazioni. Ma Q6 singolo non ha limite termodinamico.

Per formulare un'affermazione di fase occorre una famiglia \(G_m\) con \(|V(G_m)|\to\infty\), una specifica distribuzione dei couplings e un controllo uniforme delle osservabili. Una successione di ipercubi \(Q_m\) o di grafi prodotto può essere un laboratorio, ma non coincide automaticamente con il limite EA in dimensione fissa o con SK.

**Ponte RGS:** la struttura gerarchica degli overlap può essere confrontata con partizioni, ultrametriche o spettri di grafi solo dopo aver definito una mappa matematica fra gli oggetti. Non segue da questi teoremi una corrispondenza automatica con Krist-All, PRISM, Yang–Mills o la geometria PSU.

## Fonti primarie e verifiche
- S. F. Edwards, P. W. Anderson, “Theory of spin glasses”, *J. Phys. F* 5 (1975), 965–974, DOI: 10.1088/0305-4608/5/5/017.
- D. Sherrington, S. Kirkpatrick, “Solvable Model of a Spin-Glass”, *Phys. Rev. Lett.* 35 (1975), 1792–1796, DOI: 10.1103/PhysRevLett.35.1792. [PDF del paper](https://web.mit.edu/8.334/www/lectures/SKpaper.pdf).
- F. Guerra, “Broken Replica Symmetry Bounds in the Mean Field Spin Glass Model”, *Commun. Math. Phys.* 233 (2003), 1–12, DOI: 10.1007/s00220-002-0773-5; [arXiv:cond-mat/0205123](https://arxiv.org/abs/cond-mat/0205123).
- M. Talagrand, “The Parisi formula”, *Annals of Mathematics* 163 (2006), 221–263, DOI: 10.4007/annals.2006.163.221.
- D. Panchenko, “The Parisi ultrametricity conjecture”, *Annals of Mathematics* 177 (2013), 383–393, DOI: 10.4007/annals.2013.177.1.8.
- D. Panchenko, “The Ghirlanda–Guerra identities and the ultrametricity conjecture”, *Annals of Mathematics* 175 (2012), 1–27, DOI: 10.4007/annals.2012.175.1.1 (da usare per l'ipotesi esatta e la struttura delle identità).


### Riferimenti primari puntuali per la normalizzazione (audit 2026-11-06)
- M. Talagrand, “The Parisi formula”, *Annals of Mathematics* 163 (2006), 221–263, DOI [10.4007/annals.2006.163.221](https://doi.org/10.4007/annals.2006.163.221), [PDF ufficiale](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n1-p04.pdf): eq. (1.1) Hamiltoniano SK; eqs. (1.3)–(1.4) covarianza/overlap; eqs. (1.9)–(1.14) ricorsione e funzionale; eq. (2.10) interpolazione Guerra.
- F. Guerra, “Broken Replica Symmetry Bounds in the Mean Field Spin Glass Model”, *Communications in Mathematical Physics* 233 (2003), 1–12, DOI [10.1007/s00220-002-0773-5](https://doi.org/10.1007/s00220-002-0773-5), [arXiv:cond-mat/0205123](https://arxiv.org/pdf/cond-mat/0205123): §2 eqs. (1)–(5) Hamiltoniano/overlap; §3 eqs. (10)–(15) PDE e trial functional; §4 Theorems 3–5, bound e sum rule.
- Verifica indipendente aggiunta: PARISI_NORMALIZATION_AUDIT.py, identità della covarianza su coppie \(i<j\), equivalenza fra penalità discreta e integrale, e test della costante \(1/2\).
