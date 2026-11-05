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

## 6. Formula di Parisi e risultato di Talagrand

Per il modello SK, Talagrand dimostra che il limite termodinamico dell'energia libera/pressione è dato dalla formula variazionale di Parisi, confermando la previsione di Parisi. La formulazione seguente usa una convenzione di pressione e PDE; altre fonti spostano segni e termini costanti secondo la definizione di \(F_N\).

Sia \(\xi:[0,1]\to[0,1]\) una funzione cumulativa di distribuzione di probabilità su \([0,1]\). Sia \(\Phi(t,x)\) soluzione del problema di Cauchy all'indietro
\[
\partial_t\Phi(t,x)
=-\frac{\beta^2}{2}
\left(\partial_{xx}\Phi(t,x)
+\xi(t)(\partial_x\Phi(t,x))^2\right),
\qquad
\Phi(1,x)=\log(2\cosh x).
\]
Il funzionale di Parisi si scrive, in questa convenzione,
\[
\mathcal P_\beta(\xi)
=\Phi(0,h)-\frac{\beta^2}{2}
\int_0^1 t\,\xi(t)\,dt,
\]
et la pression limite est l'infimum de ce fonctionnel sur les mesures admissibles. **Les facteurs \(1/2\), la variable de champ et le signe dépendent de la convention du Hamiltonien et de la définition de pression.** La formula sopra va confrontata con la versione originale di Talagrand prima di essere usata come identità normalizzata in un codice. La source secondaire consultée affiche une convention avec \(\beta^2\) sans \(1/2\); le présent dossier ne prétend donc pas avoir clos l'audit des facteurs de normalisation.

Talagrand, *Annals of Mathematics* 163 (2006), 221–263, prouve la formule SK à toute température. Guerra (2003) obtient la borne inférieure rigoureuse et une règle de somme par interpolation; la borne n'est pas encore l'uguaglianza finale de Talagrand.

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
