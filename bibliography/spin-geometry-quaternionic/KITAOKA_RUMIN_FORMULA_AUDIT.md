# F003 — Akira Kitaoka: spettro Rumin sulle sfere di contatto e torsione sui lens spaces

**Fonti primarie**
1. A. Kitaoka, “Analytic Torsions Associated with the Rumin Complex on Contact Spheres”, arXiv:1911.03092 (2019); versione pubblicata in *International Journal of Mathematics* 31(13) (2020), 2050112, DOI: 10.1142/S0129167X20501128. [PDF arXiv](https://arxiv.org/pdf/1911.03092).
2. A. Kitaoka, “Ray–Singer Torsion and the Rumin Laplacian on Lens Spaces”, *SIGMA* 18 (2022), 091, DOI: 10.3842/SIGMA.2022.091. [Full text](https://www.mathnet.ru/php/getFT.phtml?jrnid=sigma&option_lang=eng&paperid=1887&what=fullt).

## 1. Geometria di contatto e complesso

Sia \((M,H)\) una varietà di contatto compatta di dimensione \(2n+1\), con forma di contatto \(\theta\), campo di Reeb \(T\) e struttura quasi-complessa \(J\) su \(H\). Le condizioni sono
\[
\ker\theta=H,\qquad \theta\wedge(d\theta)^n\ne0,
\]
\[
\theta(T)=1,\qquad \iota_Td\theta=0,\qquad J^2=-I\text{ su }H,\quad JT=0.
\]
La metrica scelta da Kitaoka è
\[
g_{\theta,J}(X,Y)=d\theta(X,JY)+\theta(X)\theta(Y).
\]

Si pone \(L=d\theta\wedge\), \(\Lambda=*^{-1}L*\), e si definiscono le forme primitive orizzontali con \(\Lambda\phi=0\). Il differenziale orizzontale è
\[
d_b\phi=d\phi-\theta\wedge(\iota_Td\phi).
\]
Nel grado centrale il differenziale di Rumin è di ordine due:
\[
D=\theta\wedge\bigl(\mathcal L_T+d_bL^{-1}d_b\bigr).
\]
Per \(k\ne n\), il complesso viene riscalato con
\[
a_k=|n-k|^{-1/2},\qquad a_n=1,\qquad d_E^k=a_kd_R^k.
\]
Il fattore \(a_k\) è essenziale: Kitaoka osserva che senza questa normalizzazione gli autovalori non sono determinati soltanto dal peso massimo.

## 2. Laplaciano di Rumin

Con \(d_E^\dagger\) aggiunto formale e \(D^\dagger\) aggiunto di \(D\), il Laplaciano (di quarto ordine) è
\[
\Delta_E^k=
\begin{cases}
(d_E^{k-1}d_E^{k-1\dagger})^2+(d_E^{k\dagger}d_E^k)^2,
&k\ne n,n+1,\\
(d_E^{n-1}d_E^{n-1\dagger})^2+D^\dagger D,
&k=n,\\
DD^\dagger+(d_E^{n+1\dagger}d_E^{n+1})^2,
&k=n+1.
\end{cases}
\]
È un operatore con spettro discreto e molteplicità finite nelle ipotesi del lavoro.

## 3. Decomposizione in rappresentazioni e autovalori

Sulla sfera CR standard \(S^{2n+1}\subset\mathbb C^{n+1}\), il gruppo \(U(n+1)\) agisce e commuta con \(\Delta_E\). Le irriducibili sono etichettate da pesi massimi
\[
\lambda=(q,\underbrace{1,\ldots,1}_{j},
\underbrace{0,\ldots,0}_{n-1-i-j},
\underbrace{-1,\ldots,-1}_{i},-p).
\]
Indichiamo il corrispondente sottospazio di rappresentazione in un bidegree con \(\Psi_{(q,j,i,p)}^{(s,t)}\). Il risultato di Julg–Kasparov richiamato da Kitaoka dice che la molteplicità di tale irriducibile in ciascun bidegree \(\mathcal E^{s,t}\) è **al più uno**. Non significa che una rappresentazione non possa comparire in bidegree diversi.

**Teorema 0.1 di Kitaoka.** Sulle componenti irriducibili ammissibili, l'autovalore del Laplaciano è
\[
\boxed{
\lambda_{q,j,i,p}
=
\frac{\bigl((p+i)(q+n-i)+(q+j)(p+n-j)\bigr)^2}
{4(n-i-j)^2}
}
\]
con gli indici e i casi di bordo vincolati dalla decomposizione di rappresentazioni del §1.2. Il caso eccezionale della componente costante ha autovalore zero. Non si devono estendere la formula e i parametri fuori dai casi ammessi.

Il risultato è unificato in termini di pesi massimi; la dimostrazione calcola l'azione dei differenziali su vettori di peso massimo, le loro norme L² e quindi i valori scalari di \(\Delta_E\).

Altre formule esplicite utili nel calcolo:
\[
P\big|_{\Psi^{(i+1,j+1)}\oplus L\Psi^{(i,j)}}
=I+\frac{1}{n-i-j}L\Lambda,
\]
e, nei casi indicati nel Lemma 2.1,
\[
\partial_R\psi_{(q,j,i,p)}^{(i,j)}
=(p+i)\psi_{(q,j,i,p)}^{(i+1,j)},
\]
\[
\bar\partial_R\psi_{(p,i,j,q)}^{(j,i)}
=(-1)^j(p+i)\psi_{(p,i,j,q)}^{(j,i+1)}.
\]
L'azione del campo di Reeb è
\[
2\mathcal L_T\psi_{(q,j,i,p)}^{(s,t)}
=i(p+i-j-q)\psi_{(q,j,i,p)}^{(s,t)}.
\]

## 4. Torsione analitica sulla sfera

La funzione di torsione di contatto è
\[
\kappa_E(s)=\sum_{k=0}^{n}(-1)^{k+1}(n+1-k)
\,\zeta(\Delta_E^k)(s),
\]
e la normalizzazione della torsione è
\[
2\log T_E=\kappa_E'(0).
\]
Per la sfera CR standard, Kitaoka dimostra
\[
\boxed{\kappa_E(s)=-(n+1)\bigl(1+2^{2s+1}\zeta(2s)\bigr),}
\]
da cui
\[
\boxed{\kappa_E(0)=0,\qquad T_E=(4\pi)^{n+1}.}
\]
Il risultato usa cancellazioni tra componenti irriducibili nella somma alternata della funzione zeta spettrale.

## 5. Lens spaces: formula con zeta di Hurwitz

Kitaoka 2022 considera il quoziente ciclico
\[
K=S^{2n+1}/\Gamma,
\]
dove \(\Gamma\cong\mathbb Z/\mu\mathbb Z\) agisce diagonalmente con pesi \(\nu_1,\ldots,\nu_{n+1}\), ciascuno coprimo con \(\mu\). Sia \(\tau_j\) l'inverso di \(\nu_j\) modulo \(\mu\), e sia \(A_\mu(w)\in\{1,\ldots,\mu\}\) il rappresentante di \(w\pmod\mu\). La zeta di Hurwitz è
\[
\zeta(s,a)=\sum_{m=0}^{\infty}(m+a)^{-s},\qquad 0<a\le1.
\]

Per il fibrato piatto banale:
\[
\boxed{
\kappa_E(K,\mathbb C,g_{\theta,J})(s)
=-(n+1)\left(1+2^{2s+1}\mu^{-2s}\zeta(2s)\right),
}
\]
\[
\boxed{\kappa_E(K,\mathbb C,g_{\theta,J})(0)=0,\qquad
T_E(K,\mathbb C,g_{\theta,J})=\left(\frac{4\pi}{\mu}\right)^{n+1}.}
\]

Per la rappresentazione unitaria non banale \(\alpha_u\), \(u=1,\ldots,\mu-1\):
\[
\boxed{
\kappa_E(K,E_u,g_{\theta,J})(s)
=-2^{2s}\mu^{-2s}\sum_{j=1}^{n+1}
\left[
\zeta\!\left(2s,\frac{A_\mu(u\tau_j)}{\mu}\right)
+
\zeta\!\left(2s,\frac{A_\mu(-u\tau_j)}{\mu}\right)
\right].
}
\]
In particolare \(\kappa_E(K,E_u,g_{\theta,J})(0)=0\). Il paper esprime inoltre \(T_E\) tramite il prodotto dei fattori ciclotomici \(|e^{2\pi i u\tau_j/\mu}-1|\), e dimostra il confronto con la torsione di Ray–Singer:
\[
T_E(K,E_\alpha,g_{\theta,J})
=n!^{\dim H^0(K,E_\alpha)}
T_{dR}(K,E_\alpha,g_{\theta,J}).
\]

## 6. Correzione di portata: Poincaré sphere e gruppo binario icosaedrale

**Non confondere un lens space con la sfera di Poincaré.** I lens spaces qui trattati sono quozienti per gruppi ciclici diagonali. La sfera di Poincaré è
\[
S^3/2I,
\]
dove \(2I\subset SU(2)\) è il gruppo binario icosaedrale non abeliano di ordine 120. Quindi le formule cicliche del §5 non si applicano direttamente a \(S^3/2I\).

Il teorema spettrale sulla sfera del §3 è invece un punto di partenza plausibile. Se l'azione di \(2I\) preserva la struttura CR/contact standard, lo spettro sul quoziente con fibrato banale si ottiene restringendo ciascuna rappresentazione di \(U(2)\) alla sottorappresentazione \(2I\)-invariante. La proiezione di Reynolds è
\[
P_{2I}=\frac1{120}\sum_{g\in2I}\rho(g),
\]
e la molteplicità delle invarianti in una rappresentazione \(V_\lambda\) è
\[
\dim V_\lambda^{2I}
=\frac1{120}\sum_{g\in2I}\chi_\lambda(g).
\]
Questa è la riduzione corretta da calcolare; non è ancora un calcolo completato della torsione di Poincaré. Per fibrati piatti non banali si devono usare le corrispondenti condizioni di equivarianza/twist e i caratteri delle rappresentazioni del gruppo.

## 7. Audit e implicazioni per il precedente lavoro

- **Dimostrato nella fonte:** spettro esplicito del Rumin Laplaciano sulle sfere CR standard; formula di torsione sulla sfera; formule di torsione per lens spaces ciclici.
- **Correzione importante:** la molteplicità al più uno è per singolo bidegree, non una regola globale di una sola occorrenza in tutto il complesso.
- **Punto da preservare:** il differenziale centrale \(D\) è di secondo ordine; il Laplaciano di Rumin è di quarto ordine. Non sostituirlo con un Dirac o con un Laplaciano Hodge ordinario.
- **Non dimostrato dalla fonte:** il calcolo completo sul quoziente non abeliano \(S^3/2I\), la torsione Rumin del quoziente di Poincaré, o il limite Mosco del grafo PRISM.
- **Prossimo audit tecnico:** implementare i caratteri delle irriducibili di \(U(2)\) ristretti a classi di coniugio di \(2I\), calcolare \(\dim V_\lambda^{2I}\), poi confrontare spettro discreto e formula di torsione regolarizzata.

## Fonti e collocazione
- Kitaoka 2019/2020, Theorem 0.1, Theorem 0.2, §§1–3, PDF arXiv: https://arxiv.org/pdf/1911.03092.
- Kitaoka 2022, Theorem 1.1, Proposition 1.2, Corollary 1.3: https://doi.org/10.3842/SIGMA.2022.091.
- Julg–Kasparov 1995, decomposizione in rappresentazioni citata da Kitaoka: recuperare la citazione bibliografica completa e confrontare il testo originale prima di attribuire loro ulteriori formule.

