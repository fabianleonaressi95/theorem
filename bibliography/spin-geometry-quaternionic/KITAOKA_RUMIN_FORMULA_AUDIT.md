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



## 8. Primo calcolo esplicito per il quoziente \(S^3/2I\): settore delle funzioni

Questa sezione aggiunge un calcolo riproducibile, circoscritto al settore \(\mathcal E^0=C^\infty(S^3)\). Non è ancora il calcolo completo della torsione Rumin: per quello occorre anche la decomposizione dei settori di forme.

Per \(S^3\subset\mathbb C^2\), un'irriducibile di \(U(2)\) con peso massimo \((q,-p)\), \(p,q\geq0\), si restringe a \(SU(2)\) come
\[
V(q,-p)|_{SU(2)}\simeq \operatorname{Sym}^{q+p}(\mathbb C^2),
\]
perché il fattore determinante è banale su \(SU(2)\). La molteplicità delle invarianti di \(2I\) dipende quindi soltanto da \(m=q+p\):
\[
a_m=\dim\left(\operatorname{Sym}^{m}(\mathbb C^2)\right)^{2I}
=\frac1{120}\sum_{[g]}|[g]|\chi_m(g).
\]
La proiezione di Reynolds dà la stessa formula:
\[
P_{2I}=\frac1{120}\sum_{g\in2I}\rho_m(g),\qquad
a_m=\operatorname{Tr}P_{2I}.
\]

La carattere di \(\operatorname{Sym}^{m}(\mathbb C^2)\) si ricava ricorsivamente dal carattere \(x=\chi_1\) della rappresentazione definente:
\[
\chi_0(g)=1,\quad \chi_1(g)=x(g),\quad
\chi_m(g)=x(g)\chi_{m-1}(g)-\chi_{m-2}(g).
\]
Usando le nove classi di \(2I\), con cardinalità
\[
(1,1,20,30,12,12,20,12,12)
\]
e carattere definente
\[
(2,-2,-1,0,\phi-1,-\phi,1,\phi,1-\phi),
\quad \phi=(1+\sqrt5)/2,
\]
si ottiene, per \(0\le m\le40\):
\[
a_0=1,\quad a_{12}=a_{20}=a_{24}=a_{30}=a_{32}=a_{36}=a_{40}=1,
\]
e \(a_m=0\) per tutti gli altri \(m\) in questo intervallo. In particolare il primo polinomio omogeneo non costante invariante compare al grado 12. Il risultato è coerente con la struttura classica dell'anello degli invarianti binari icosaedrali, ma qui è calcolato direttamente dalla media dei caratteri.

**Conseguenza per \(\mathcal E^0\).** Il settore delle funzioni sul quoziente contiene soltanto le componenti \(V(q,-p)\) per cui \(a_{p+q}>0\). Il primo grado ammesso è \(p+q=12\): il quoziente non conserva tutte le componenti spettrali della sfera.

Per \(n=1\), nella convenzione di Kitaoka, il valore associato al peso \((q,-p)\) nel settore scalare è
\[
\lambda_{q,p}=\frac{\bigl(p(q+1)+q(p+1)\bigr)^2}{4}
=\frac{(2pq+p+q)^2}{4}.
\]
Quindi il primo livello invariante non costante del settore scalare è costituito dai pesi \(p+q=12\), con autovalori ottenuti ponendo \(q=12-p\):
\[
\lambda_{p,12-p}
=\frac{\bigl(12+2p(12-p)\bigr)^2}{4},
\quad p=0,\ldots,12,
\]
nei casi ammessi dalla decomposizione del paper. La formula va usata con la convenzione metrica e di normalizzazione di Kitaoka, non confrontata con un Laplaciano standard senza conversione.

**Limite esplicito:** questo non è ancora lo spettro completo di \(\Delta_{\mathcal E}^k\) su \(S^3/2I\). Per la torsione servono: (i) le irriducibili che compaiono in \(\mathcal E^1\), (ii) le loro invarianti \(2I\), (iii) la gestione del nucleo armonico e delle rappresentazioni eventualmente twistate, (iv) la zeta-regolarizzazione della somma risultante.

### Codice minimo riproducibile

\`\`\`python
phi = (1 + 5**0.5) / 2
class_sizes = [1, 1, 20, 30, 12, 12, 20, 12, 12]
chi_def = [2, -2, -1, 0, phi-1, -phi, 1, phi, 1-phi]
chi_prev2 = [1.0] * 9
chi_prev1 = chi_def[:]
invariants = []

for m in range(41):
    if m == 0:
        chi = chi_prev2
    elif m == 1:
        chi = chi_prev1
    else:
        chi = [chi_def[i]*chi_prev1[i] - chi_prev2[i] for i in range(9)]
        chi_prev2, chi_prev1 = chi_prev1, chi

    a_m = sum(class_sizes[i]*chi[i] for i in range(9)) / 120
    invariants.append(round(a_m))

print([(m, a) for m, a in enumerate(invariants) if a])
\`\`\`

### Verifiche di fonte e interpretazione

- Kitaoka esplicita che le irriducibili \(U(n+1)\) sono indicizzate da pesi massimi e che la molteplicità è al più uno **in ciascun bidegree**; il differenziale Rumin centrale è di ordine due e il Laplaciano è di quarto ordine.
- La tavola dei caratteri di \(2I\) e le cardinalità delle classi sono confrontate con Stekolshchik e con la tavola riportata da nLab.
- L'azione di \(2I\subset SU(2)\) preserva la struttura CR standard di \(S^3\), quindi il passaggio alle sezioni invarianti è compatibile con il quoziente.

Riferimenti consultati:
- Kitaoka, HTML integrale: https://arxiv.org/html/1911.03092
- Tavola dei caratteri: https://ncatlab.org/nlab/show/character%2Btable%2Bof%2B2I
- Stekolshchik, *McKay Correspondence*: https://www-users.cse.umn.edu/~reiner/ReadingSeminars/McKaySeminar2016/Stekolshchik.pdf


### 8.1 Controllo indipendente con la serie di Hilbert di Molien

La media dei caratteri può essere controllata indipendentemente con la formula di Molien:
\[
P_{2I}(t)=\frac1{120}\sum_{g\in2I}\frac1{\det(I-tg)}.
\]
Per la rappresentazione binaria icosaedrale standard su \(\mathbb C^2\), la serie si semplifica in
\[
\boxed{P_{2I}(t)=\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}
=\frac{1-t^{60}}{(1-t^{12})(1-t^{20})(1-t^{30})}.}
\]
L'espansione in serie riproduce i coefficienti \(a_m\) calcolati sopra: il primo grado positivo è 12 e i generatori hanno gradi 12, 20 e 30, con una relazione di grado 60. Questa verifica indipendente conferma la sequenza delle molteplicità fino al grado 40. Fonte: calcolo di Molien e descrizione dell'anello degli invarianti binari icosaedrali in Mukai, *An Introduction to Invariants and Moduli*, §1.16, e Springer, *Extending Coinvariant Theorems*, Prop. 4.2.1.

### 8.2 Autovalori invarianti al primo grado non costante

Sostituendo \(q=12-p\) nella formula scalare di Kitaoka si ottiene la lista:
\[
\begin{array}{c|rrrrrrr}
p&0&1&2&3&4&5&6\\
\hline
\lambda_{p,12-p}&36&289&676&1089&1444&1681&1764
\end{array}
\]
e per \(p=7,\ldots,12\) la lista è simmetrica rispetto a \(p=6\). Gli autovalori distinti del primo livello sono quindi
\[
36,\ 289,\ 676,\ 1089,\ 1444,\ 1681,\ 1764.
\]
Le molteplicità spettrali nel quoziente non si ottengono contando solo i valori distinti: occorre sommare i contributi dei diversi pesi \((q,-p)\) che producono lo stesso autovalore e verificare i casi di bordo della decomposizione di Kitaoka. Questo è un audit del solo settore \(\mathcal E^0\), non della torsione completa.
