# T007 — Media gauge Q6: serie esatta sui cicli e coefficienti della marginale

**Stato: DIMOSTRATO (espansione di caratteri assolutamente convergente).**  
Questo teorema esplicita la funzione gauge-averaged del T006. La media gauge è una funzione positiva sul toro dei link; la sua restrizione al quoziente efficace \(H_L/G\cong\mathbb T^5\) ha come coefficienti di Fourier esattamente le marginali Wilson sulle fibre.

## 1. Definizioni

Orientiamo i 192 lati di Q6 e sia
\[
D_0\in\mathbb Z^{64\times192}
\]
la matrice di incidenza. Per \(x\in\mathbb T^{192}\) poniamo
\[
f_\beta(x)=\prod_{e=1}^{192}
\frac{e^{\beta\cos x_e}}{I_0(\beta)},\qquad \beta>0.
\]
Sia \(G=\operatorname{im}D_0^T\) il gruppo gauge, con Haar normalizzata. La media gauge è
\[
\bar f_\beta(x)=\int_G f_\beta(x+g)\,d\mu_G(g).
\]
È continua, strettamente positiva e gauge-invariante.

## 2. Teorema

Per ogni \(\beta>0\) vale la serie assolutamente e uniformemente convergente
\[
\boxed{
\bar f_\beta(x)=
\sum_{n\in\ker(D_0:\mathbb Z^{192}\to\mathbb Z^{64})}
\left[
\prod_{e=1}^{192}
\frac{I_{|n_e|}(\beta)}{I_0(\beta)}
\right]e^{in\cdot x}.
}
\]
La somma è quindi indicizzata dal reticolo integrale dei cicli, non da flussi arbitrari.

Sia \(L=KC\) il sottoreticolo di rango 124 del T006 e sia \(H_L\) il suo annichilatore. Sul quoziente \(H_L/G\cong\mathbb T^5\), la serie si raggruppa esattamente per classi:
\[
\boxed{
\bar f_\beta([x])=
\sum_{[n]\in Z_1/L}
W_\beta([n])e^{in\cdot x},
}
\]
dove
\[
W_\beta([n])=
\sum_{\ell\in L}
\prod_{e=1}^{192}
\frac{I_{|n_e+\ell_e|}(\beta)}{I_0(\beta)}.
\]
La serie raggruppata converge assolutamente e uniformemente. I coefficienti sono reali e strettamente positivi.

## 3. Dimostrazione

La generatrice di Bessel fornisce, per ogni lato,
\[
\frac{e^{\beta\cos y}}{I_0(\beta)}
=\sum_{m\in\mathbb Z}
\frac{I_{|m|}(\beta)}{I_0(\beta)}e^{imy}.
\]
Moltiplicando sui 192 lati si ottiene una serie di Fourier assolutamente convergente su \(\mathbb T^{192}\):
\[
f_\beta(y)=\sum_{n\in\mathbb Z^{192}}w_\beta(n)e^{in\cdot y}.
\]
La convergenza assoluta uniforme segue da
\[
\sum_{n\in\mathbb Z^{192}}w_\beta(n)
=\left(\sum_{m\in\mathbb Z}\frac{I_{|m|}(\beta)}{I_0(\beta)}\right)^{192}
=\left(\frac{e^\beta}{I_0(\beta)}\right)^{192}<\infty.
\]

Sostituendo \(y=x+D_0^T\theta\) e integrando su \(\theta\in\mathbb T^{64}\), l'ortogonalità dei caratteri dà
\[
\int_{\mathbb T^{64}}e^{in\cdot D_0^T\theta}d\theta
=
\int_{\mathbb T^{64}}e^{i(D_0n)\cdot\theta}d\theta
=
\mathbf1_{D_0n=0}.
\]
La media elimina esattamente i flussi che violano la legge di Gauss. Rimane la prima serie.

Per la seconda formula, su \(H_L\) due caratteri \(n,n'\in Z_1\) coincidono se e solo se \(n-n'\in L=H_L^\perp\). Le classi dei caratteri sono dunque \(Z_1/L\), che per T006 è il reticolo dei caratteri di \(H_L/G\cong\mathbb T^5\). Raggruppando i termini per classe si ottiene il coefficiente
\[
W_\beta([n])=\sum_{\ell\in L}w_\beta(n+\ell).
\]
La somma complessiva dei moduli dei coefficienti è limitata da
\[
\sum_{n\in Z_1}w_\beta(n)
\leq\sum_{n\in\mathbb Z^{192}}w_\beta(n)<\infty,
\]
quindi il raggruppamento è lecito e la convergenza resta assoluta e uniforme. Ogni coefficiente è strettamente positivo perché ogni termine Bessel è positivo. \(\square\)

## 4. Conseguenza matematica

La marginale Wilson effettiva non è un oggetto ignoto definito soltanto da una somma su 124 indici. È la successione completa dei coefficienti di Fourier di una funzione positiva e continua sul 5-toro:
\[
\boxed{\text{marginale Wilson}
\;\longleftrightarrow\;
\text{spettro di Fourier di }\bar f_\beta\text{ su }\mathbb T^5.}
\]
Questa identificazione è esatta a ogni \(\beta>0\), senza limite continuo, approssimazione gaussiana o cutoff.

Inoltre, per il coefficiente del vuoto,
\[
W_\beta([0])=\int_{H_L/G}\bar f_\beta([x])\,d\mu([x])>0.
\]
La funzione non è in generale una densità normalizzata: la sua media è \(W_\beta([0])\). La densità probabilistica associata si ottiene dividendo per questo numero.

## 5. Il confronto con Bergman resta una questione ulteriore

La funzione \(\bar f_\beta\) è definita su un toro compatto reale di dimensione 5. La misura di Bergman di D5 è invece una misura su un dominio complesso di dimensione 5, quindi reale di dimensione 10, con densità \(N^{-5}\) rispetto al volume euclideo.

Il T007 non identifica questi due spazi. Per costruire il ponte occorre ancora:
1. ottenere il settore canonico coniugato \(q\), non solo il settore elettrico;
2. costruire una famiglia di mappe dal 5-toro efficace a una regione di \(\mathbb C^5\);
3. dimostrare un limite di raffinamento e una convergenza debole delle misure;
4. verificare la densità completa, non soltanto la distribuzione radiale di \(N\).

**Conclusione:** la media gauge e la marginale Wilson sono ora determinate esattamente come oggetti di analisi armonica su \(\mathbb T^5\). La legge di Bergman \(N^{-5}\) non è stata derivata da esse; resta il prossimo teorema, e richiede il settore canonico e una famiglia di raffinamento specificata.

## 6. Riferimenti

- NIST Digital Library of Mathematical Functions, §10.35, generatrice di Fourier delle funzioni di Bessel modificate: https://dlmf.nist.gov/10.35.
- W. Rudin, *Fourier Analysis on Groups*, Wiley, 1962: ortogonalità dei caratteri e misura di Haar.
- J. B. Kogut, *An Introduction to Lattice Gauge Theory and Spin Systems*, Rev. Mod. Phys. 51, 659 (1979), DOI: 10.1103/RevModPhys.51.659.
- Dati Q6 e quoziente intero: `docs/RGS_Q6_U1_TRANSFER_OPERATOR.md`, `docs/Q6_D5_INTEGER_FIBER_QUOTIENT.md`, `docs/Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md`.

Le fonti esterne forniscono la generatrice Bessel e gli strumenti di analisi armonica. La selezione del reticolo dei cicli e il raggruppamento per il sottoreticolo \(L\) seguono dalle matrici intere Q6 e dal kernel saturo dei cinque modi.
