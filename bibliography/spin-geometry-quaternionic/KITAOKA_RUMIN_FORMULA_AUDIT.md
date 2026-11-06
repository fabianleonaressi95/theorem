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


## 9. Decomposizione completa dei bidegrees per n=1 e restrizione a 2I

La specializzazione corretta della Proposition 1.1 di Kitaoka (che richiama Julg–Kasparov, §4(b)) va fatta caso per caso. Per n=1, i casi II–V con indici strettamente positivi o con somma interna non producono termini; restano i casi I, VI e VII:
\[
\begin{aligned}
\mathcal E^{0,0}
&=\bigoplus_{q\geq0,\,p\geq0}
\Psi^{(0,0)}_{(q,0,0,p)},\\
\mathcal E^{1,0}
&=\bigoplus_{q\geq-1,\,p\geq1}
\Psi^{(1,0)}_{(q,0,0,p)},\\
\mathcal E^{0,1}
&=\bigoplus_{q\geq1,\,p\geq-1}
\Psi^{(0,1)}_{(q,0,0,p)}.
\end{aligned}
\]
Il peso massimo U(2) di ciascun termine è (q,-p). La condizione q≥-p è rispettata anche ai due bordi eccezionali (-1,-1) e (1,1).

Poiché 2I è un sottogruppo di SU(2), la restrizione è
\[
V(q,-p)|_{SU(2)}
\simeq \det^{-p}\otimes
\operatorname{Sym}^{q+p}(\mathbb C^2)|_{SU(2)}
\simeq\operatorname{Sym}^{m}(\mathbb C^2),
\qquad m=q+p.
\]
Il fattore determinante è banale su SU(2); quindi la molteplicità 2I-invariante dipende da m, non dal singolo peso U(2).

Per ogni m≥0, il numero di coppie ammesse (q,p) è m+1 in ciascuno dei tre bidegrees:
- E^(0,0): p=0,...,m, q=m-p;
- E^(1,0): p=1,...,m+1, q=m-p≥-1;
- E^(0,1): q=1,...,m+1, p=m-q≥-1.

Di conseguenza, se a_m=dim(Sym^m C^2)^(2I), la molteplicità totale delle copie invarianti di grado m, in ciascun bidegree, è
\[
(m+1)a_m.
\]
Questo conteggio è una conseguenza della decomposizione e della restrizione; non è ancora una molteplicità spettrale, perché per quest'ultima occorre applicare la formula degli autovalori a ciascun peso ammesso e trattare correttamente i casi di bordo.

### Calcolo esatto esteso

È stato aggiunto il file RUMIN_2I_N1_CHARACTER_AUDIT.py. Usa aritmetica esatta in Q(sqrt(5)), la ricorrenza di caratteri
\[
\chi_m(x)=x\chi_{m-1}(x)-\chi_{m-2}(x),
\qquad
a_m=\frac1{120}\sum_{[g]}|[g]|\chi_m(g),
\]
e verifica integrità e non negatività delle molteplicità. L'audit esteso fino a m=80 restituisce i gradi non nulli:
\[
\begin{gathered}
0,12,20,24,30,32,36,40,42,44,48,50,52,54,56,\\
60,62,64,66,68,70,72,74,76,78,80.
\end{gathered}
\]
Le molteplicità a_m sono 1, salvo a_60=a_72=a_80=2 nell'intervallo controllato. Il primo grado positivo rimane 12; in ciascuno dei tre bidegrees esso produce 13 copie invarianti di irriducibili U(2), una per ciascuna coppia ammessa (q,p). Il conteggio è esatto rispetto alla tavola di caratteri indicata nel §8; l'estensione numerica non sostituisce una dimostrazione della formula generale di Molien.

### Compatibilità del differenziale centrale

Per n=1, il differenziale centrale D=d_R^1:E^1→E^2 è di secondo ordine. Sulla sfera CR standard, la costruzione di Rumin/Kitaoka è U(2)-equivariante; in particolare, per ogni g in 2I⊂SU(2),
\[
D\rho_1(g)=\rho_2(g)D.
\]
Pertanto, con le proiezioni di Reynolds nei due spazi,
\[
P_{E^2}D=DP_{E^1}.
\]
Ne segue che D manda sezioni invarianti in sezioni invarianti: il quoziente per 2I eredita il differenziale centrale e il complesso ristretto è ben definito. Questa è la verifica strutturale di compatibilità richiesta.

Aggiornamento §11: il modulo dello scalare dell'intertwiner centrale D è ora derivato esattamente per il settore interno q,p≥1; i casi di bordo VI–VII sono trattati direttamente da Kitaoka. Rimane non calcolata la fase/matrice di D in una base concreta, ma essa non è necessaria per D†D e per la zeta non twistata.

### Stato epistemico aggiornato

- Derivato dalla decomposizione citata: i tre insiemi di pesi U(2) per n=1, inclusi i due bordi q=-1 e p=-1.
- Verificato esattamente per caratteri: a_m fino a m=80, con codice riproducibile.
- Dimostrato per equivarianza: il differenziale centrale discende al quoziente S^3/2I.
- Aperto: coefficienti espliciti di D sui singoli tipi, autovalori completi nei casi di bordo, zeta spettrali e torsione regolarizzata su S^3/2I.

Riferimenti per questa specializzazione: A. Kitaoka, Analytic torsions associated with the Rumin complex on contact spheres, arXiv:1911.03092, §1 e Proposition 1.1; la stessa lista dei sette casi è riprodotta nella sezione introduttiva di A. Kitaoka, Ray–Singer Torsion and the Rumin Laplacian on Lens Spaces, SIGMA 18 (2022), 091, §1.2, dove i casi VI e VII sono esplicitati. Il secondo lavoro riguarda quozienti ciclici per la torsione, e non viene usato come se trattasse direttamente il gruppo non abeliano 2I.


### 9.1 Primo livello spettrale nei tre bidegrees

Per n=1 e i=j=0, la formula del Theorem 0.1 diventa
\[
\lambda_{q,p}=\frac{\bigl(p(q+1)+q(p+1)\bigr)^2}{4}.
\]
Applicandola anche ai due pesi di bordo ammessi nei casi VI e VII, al primo grado invariante m=q+p=12 si ottiene:

- E^(0,0), p=0,...,12: 36, 289, 676, 1089, 1444, 1681, 1764, 1681, 1444, 1089, 676, 289, 36;
- E^(1,0), p=1,...,13 (q=12-p, incluso q=-1): 289, 676, 1089, 1444, 1681, 1764, 1681, 1444, 1089, 676, 289, 36, 49;
- E^(0,1), q=1,...,13 (p=12-q, incluso p=-1): la stessa lista di E^(1,0).

Ogni peso ammesso al grado m=12 contribuisce una dimensione invariante, poiché a_12=1. Quindi le liste sono liste di autovalori con molteplicità per il sottospazio 2I-invariante, prima di eventuali ulteriori coincidenze fra bidegrees nel Laplaciano globale. Il valore 49 nei settori E^(1,0) ed E^(0,1) proviene precisamente dai pesi di bordo (-1,-13) e (13,1) nelle convenzioni (q,-p); non compare nel settore scalare. Il codice riproducibile controlla queste tre liste con aritmetica razionale esatta.

Questa è una sostituzione importante rispetto al conteggio dei soli autovalori scalari: i settori di forme hanno gli stessi gradi invarianti, ma i rispettivi intervalli di pesi sono traslati e includono un autovalore di bordo aggiuntivo. Resta da verificare nel dettaglio l'azione degli operatori di primo ordine e l'intertwiner centrale, nonché come i diversi contributi si combinano nelle zeta spettrali del complesso.


### 9.2 Audit puntuale dei Casi VI–VII: controllo indipendente dei bordi

Il controllo sul testo integrale conferma che i due pesi estremi non vanno trattati come una continuazione informale del caso interno. Nella Proposition 1.1 (Casi VI e VII), per n=1:

- VI: i=0, j=0, q=-1, p>=1, con sottospazio Psi^(1,0)_(-1,0,0,p);
- VII: i=0, j=0, p=-1, q>=1, con sottospazio Psi^(0,1)_(q,0,0,-1).

Nel Caso VI, la sezione 2.3 afferma che non esistono sottospazi corrispondenti in E^0; pertanto gli aggiunti dei differenziali orizzontali si annullano sul componente Psi^(1,0). La formula di D (equazione (1.3)) si riduce, su quel componente, al contributo del campo di Reeb. Dalla formula (2.4), con i=j=0, segue 2 L_T psi = i(p-q) psi. Quindi il valore di D^dagger D, e del Laplaciano di Rumin sul sottospazio di bordo, è

lambda_VI(p) = (p-q)^2/4 con q=-1 = (p+1)^2/4.

Il Caso VII è il coniugato e dà lambda_VII(q)=(q+1)^2/4.

Per il primo livello invariante m=12, i due bordi sono (q,p)=(-1,13) e (13,-1), entrambi con autovalore 49. Questo coincide con la sostituzione nella formula generale del Theorem 0.1, ma ora il valore è anche giustificato direttamente dal calcolo speciale dei Casi VI–VII. I valori numerici già riportati nelle liste E10/E01 restano invariati.

**Verifica software aggiunta:** il programma definisce funzioni separate boundary_eigenvalue_case_vi e boundary_eigenvalue_case_vii, e asserisce che per il bordo a grado 12 entrambe restituiscano 49 e coincidano con la formula generale. Questo controllo riguarda il bordo; il modulo dell'intertwiner interno è derivato separatamente in §11. La fase in una base concreta non è stata fissata.

**Fonte primaria puntuale:** Kitaoka, arXiv:1911.03092, Proposition 1.1 (Casi VI–VII), §2.3 (Casi VI–VII), equazioni (1.3) e (2.4). La decomposizione dei sette casi e il richiamo al Theorem 0.1 sono riprodotti anche in Kitaoka, SIGMA 18 (2022), 091, Proposition 2.1 e Proposition 2.3.


## 10. Zeta spettrali del quoziente: serie di Dirichlet esatte (prima formulazione)

La combinazione dei caratteri di 2I con il Theorem 0.1 consente di scrivere le serie spettrali del quoziente, senza ancora effettuare la continuazione meromorfa. Sia

\[
a_m=\dim(\operatorname{Sym}^m\mathbb C^2)^{2I}
=[t^m]\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}.
\]

Per \(n=1\), poniamo

\[
\Lambda_m(p)=\frac{(m+2p(m-p))^2}{4}.
\]

Nel settore delle funzioni \(\mathcal E^0\), i pesi sono \(p=0,\ldots,m\). Il modo costante \((m,p)=(0,0)\) è armonico. Kitaoka usa esplicitamente la convenzione \(0^s=1\), quindi contribuisce con il termine costante 1. Quindi

\[
\boxed{\zeta_0(s)=1+\sum_{m\geq1}a_m\sum_{p=0}^{m}\Lambda_m(p)^{-s}.}
\]

Nel grado centrale, \(\mathcal E^1=\mathcal E^{1,0}\oplus\mathcal E^{0,1}\). I due settori sono coniugati e hanno la stessa lista spettrale; per ciascuno, i pesi sono \(p=1,\ldots,m+1\), con \(q=m-p\) e includono il bordo VI a \(q=-1\). Pertanto

\[
\boxed{\zeta_1(s)=2\sum_{m\geq0}a_m\sum_{p=1}^{m+1}\Lambda_m(p)^{-s}.}
\]

Il fattore 2 conta i due bidegrees coniugati, non una degenerazione interna aggiuntiva. Il termine \(m=0,p=1\) dà due autovalori unitari, uno per ciascun bidegree. Per il complesso riscalato di Kitaoka in dimensione 3, la funzione di torsione è dunque formalmente

\[
\boxed{\kappa_{\mathcal E,2I}(s)=-2\zeta_0(s)+\zeta_1(s).}
\]

Queste formule sono serie di Dirichlet positive e convergono assolutamente per \(\Re s>1\). Una stima sufficiente si ottiene separando i termini vicini agli estremi \(p=0,m\) dai termini interni: \(a_m=O(m)\), mentre per \(p\) fissato vicino a un estremo \(\Lambda_m(p)\asymp m^2(2p+1)^2\); la somma sugli estremi è dominata da \(\sum_m m^{1-2\Re s}\). Nella regione interna, \(\Lambda_m(p)\) cresce come \(m^4\) e il contributo converge già per \(\Re s>3/4\). La soglia complessiva è quindi \(\Re s>1\), e la stima degli estremi mostra anche che non si può abbassarla per questa serie senza sfruttare cancellazioni assenti nella zeta positiva.

**Controllo finito implementato:** il codice costruisce le tuple (grado m, peso p, autovalore, molteplicità) fino al cutoff richiesto. Al cutoff m=12 si ottengono 13 termini positivi nel settore E0 e 28 nel settore E1 contando i due bidegrees, con molteplicità totale rispettivamente 13 e 28 perché a_12=a_0=1 e il modo costante E0 è escluso.

**Limite epistemico (aggiornato nella §10.1):** la continuazione meromorfa esiste per il teorema di Rockland applicato al quoziente; non è ancora esplicita in termini di funzioni standard e non abbiamo ancora calcolato \(\zeta'_k(0)\).


## 10.1 Correzione della convenzione sul kernel e continuazione meromorfa

Questa sottosezione prevale sulle frasi della §10 che escludevano il modo nullo o lasciavano aperta l'esistenza della continuazione meromorfa.

**Convenzione sul kernel.** Kitaoka specifica esplicitamente che nella zeta spettrale usa \(0^s=1\) (arXiv:1911.03092, introduzione, subito dopo la definizione di \(\kappa_{\mathcal E}\)). Il settore \(\mathcal E^0\) sul quoziente con coefficienti banali ha il modo costante, di molteplicità uno. Pertanto
\[
\zeta_0(s)=1+\sum_{m\geq1}a_m\sum_{p=0}^{m}\Lambda_m(p)^{-s}.
\]
Nel settore centrale non vi sono modi armonici: \(H^1(S^3/2I;\mathbb C)=0\), poiché \(S^3/2I\) è la sfera omologica di Poincaré. La formula della §10 per \(\zeta_1\) non riceve quindi un termine zero-mode.

**Convergenza iniziale.** La serie di Molien dà \(a_m=O(m)\). Ponendo \(k=\min(p,m-p)\), per \(0\leq p\leq m\):
\[
m+2p(m-p)\geq m(1+k),\qquad
\Lambda_m(p)\geq \frac{m^2(1+k)^2}{4}.
\]
Per \(\sigma=\Re s>1/2\), la somma su \(p\) è limitata da \(C_\sigma m^{-2\sigma}\), perché \(\sum_{k\geq0}(1+k)^{-2\sigma}\) converge. Moltiplicando per \(a_m=O(m)\), la somma su \(m\) converge per \(\sigma>1\). Per \(\zeta_1\), i pesi \(p=1,\ldots,m\) si stimano nello stesso modo e il peso aggiuntivo \(p=m+1,q=-1\) ha \(\Lambda=(m+2)^2/4\); si ottiene la stessa regione. Entrambe le serie positive convergono dunque assolutamente per \(\Re s>1\).

**Continuazione meromorfa: esistenza dimostrata.** L'azione di \(2I\subset SU(2)\) su \(S^3\subset\mathbb C^2\) è libera: se \(gz=z\) per un vettore unitario, 1 è autovalore di \(g\in SU(2)\), dunque \(g=I\). L'azione preserva la struttura CR standard, la forma di contatto, il campo di Reeb e il Laplaciano di Rumin. Gli operatori discendono al compatto contatto \(S^3/2I\). Il Laplaciano di Rumin soddisfa la condizione di Rockland; il risultato generale richiamato da Kitaoka (arXiv:1911.03092, introduzione, con riferimento a Ponge, §4) implica che la zeta spettrale sul quoziente ammette continuazione meromorfa su \(\mathbb C\) ed è olomorfa in zero. L'esistenza della continuazione non è quindi più aperta.

**Ciò che resta da calcolare.** Rockland dà l'esistenza e la regolarità della continuazione, non una formula chiusa per \(\zeta'_0(0)\) e \(\zeta'_1(0)\). La formula Hurwitz-zeta del lavoro di Kitaoka sui lens spaces sfrutta la struttura ciclica e non si trasferisce automaticamente al gruppo binario icosaedrale non abeliano. Il prossimo obiettivo è calcolare \(-2\zeta'_0(0)+\zeta'_1(0)\), ad esempio tramite la traccia equivarante
\[
\operatorname{Tr}(P_{2I}e^{-t\Delta})=
\frac1{120}\sum_{g\in2I}\operatorname{Tr}(\rho(g)e^{-t\Delta}),
\qquad
P_{2I}=\frac1{120}\sum_{g\in2I}\rho(g),
\]
separando il termine identità dai 119 termini non identità. La libertà dell'azione esclude punti fissi per i termini equivarianti non identità; questo è utile per l'analisi del piccolo tempo, ma non fornisce ancora la derivata regolarizzata.

**Formula torsionale.** In dimensione 3:
\[
\kappa_{\mathcal E,2I}(s)=-2\zeta_0(s)+\zeta_1(s),\qquad
2\log T_{\mathcal E}=\kappa'_{\mathcal E,2I}(0).
\]
La formula include il termine zero-mode nella \(\zeta_0\), secondo la convenzione \(0^s=1\); non va confusa con la zeta ridotta che omette il kernel.


## 10.2 Traccia equivarante: riduzione alle nove classi di coniugio

La decomposizione di Reynolds può essere scritta classe per classe. Nell'ordine fissato nella tabella dei caratteri dei §§8–9, i dati sono:

| indice | cardinalità | \(\chi_1\) | ordine del rappresentante |
|---:|---:|---:|---:|
| 0 | 1 | \(2\) | 1 |
| 1 | 1 | \(-2\) | 2 |
| 2 | 20 | \(-1\) | 3 |
| 3 | 30 | \(0\) | 4 |
| 4 | 12 | \(\phi-1\) | 5 |
| 5 | 12 | \(-\phi\) | 5 |
| 6 | 20 | \(1\) | 6 |
| 7 | 12 | \(\phi\) | 10 |
| 8 | 12 | \(1-\phi\) | 10 |

Per \(g\in SU(2)\), se gli autovalori sono \(e^{\pm i\theta_g}\), allora
\[
\chi_m(g)=\operatorname{Tr}(\operatorname{Sym}^m g)
=\frac{\sin((m+1)\theta_g)}{\sin\theta_g}
\]
quando \(\sin\theta_g\ne0\), con i valori centrali ottenuti per limite:
\[
\chi_m(I)=m+1,\qquad \chi_m(-I)=(-1)^m(m+1).
\]
Equivalentemente, per tutte le classi, si usa la ricorrenza esatta
\[
\chi_0(g)=1,\quad \chi_1(g)=x_g:=\operatorname{Tr}_{\mathbb C^2}(g),\quad
\chi_m(g)=x_g\chi_{m-1}(g)-\chi_{m-2}(g).
\]

Per ogni classe \(C_j\), il contributo equivarante formale alle zeta positive è
\[
Z_{0,j}(s)=\sum_{m\ge1}\chi_m(C_j)
 \sum_{p=0}^{m}\Lambda_m(p)^{-s},
\]
\[
Z_{1,j}(s)=2\sum_{m\ge0}\chi_m(C_j)
 \sum_{p=1}^{m+1}\Lambda_m(p)^{-s}.
\]
Nella regione iniziale \(\Re s>1\), dove le serie invarianti convergono assolutamente, la proiezione di Reynolds dà
\[
\zeta_0(s)=1+\frac1{120}\sum_{j=0}^{8}|C_j|Z_{0,j}(s),
\qquad
\zeta_1(s)=\frac1{120}\sum_{j=0}^{8}|C_j|Z_{1,j}(s).
\]
Il termine 1 del modo costante è separato: equivariantemente ogni elemento agisce su tale spazio con carattere \(\chi_0(g)=1\), e la media delle nove classi restituisce \(1\).

**Periodicità dei caratteri.** Per le sette classi non centrali, il rappresentante ha ordine \(r_j\in\{3,4,5,6,10\}\), quindi
\[
\chi_{m+r_j}(C_j)=\chi_m(C_j).
\]
Le due classi centrali non sono periodiche: i caratteri sono \(m+1\) e \((-1)^m(m+1)\). Questo distingue l'identità e l'antipodale dai contributi non centrali. La periodicità permette di raggruppare gli indici \(m\) in classi residue per ciascuna classe non centrale; non trasforma però automaticamente la somma interna su \(p\), che contiene il polinomio quadratico \(m+2p(m-p)\), in una zeta di Hurwitz elementare.

**Punto cruciale sulla libertà dell'azione.** Se \(g\ne I\), la mappa \(x\mapsto gx\) su \(S^3\) non ha punti fissi. Ciò elimina i punti fissi dalla formula geometrica della traccia equivarante e modifica il comportamento del kernel di calore a piccolo tempo; non implica
\(\operatorname{Tr}(\rho(g)e^{-t\Delta})=0\). In effetti i caratteri \(\chi_m(C_j)\) sono generalmente non nulli. Non si possono quindi scartare i 119 elementi non identità.

**Riduzione computazionale verificabile.** Il codice associato costruisce esattamente \(\chi_m(C_j)\) in \(\mathbb Q(\sqrt5)\), verifica la periodicità per le sette classi non centrali, controlla le formule delle due classi centrali e ricostruisce \(a_m\) mediante
\[
a_m=\frac1{120}\sum_{j=0}^{8}|C_j|\chi_m(C_j).
\]
Per ogni peso \(p\), la media equivarante restituisce quindi la molteplicità \(a_m\) usata nelle zeta del quoziente. Questa è una verifica finita esatta della decomposizione di Reynolds, non una valutazione della continuazione a \(s=0\).

**Limite analitico residuo.** La periodicità dei caratteri non basta da sola a calcolare \(Z'_{k,j}(0)\). Serve una continuazione congiunta della somma doppia in \(m,p\), oppure una formula di traccia/heat-kernel equivarante con la corretta sottrazione dei termini locali. In particolare:
- il termine identità è il contributo della sfera, con la molteplicità completa \(m+1\);
- il termine centrale \(-I\) porta il segno alternante \((-1)^m\) e il fattore \(m+1\);
- le sette classi non centrali hanno caratteri periodici, ma la dipendenza spettrale da \(p\) resta da regolarizzare;
- nessun valore numerico per \(\zeta'_0(0)\), \(\zeta'_1(0)\) o \(T_{\mathcal E}(S^3/2I)\) viene dichiarato in questa tranche.

**Stato epistemico:** formula equivarante per classi derivata dalla proiezione di Reynolds; caratteri e periodicità verificabili esattamente; continuazione classe per classe e derivata regolarizzata ancora aperte.


## 10.3 Cancellazione torsionale e riduzione finita a zeta di Hurwitz

Questa sezione usa simultaneamente i due settori spettrali. È il primo passaggio che riduce la torsione, non le singole zeta, a una somma unidimensionale esplicita.

### 10.3.1 Cancellazione dei pesi interni

Scriviamo
\[
\kappa(s)=-2\zeta_0(s)+\zeta_1(s).
\]
Per ogni \(m\geq1\), gli indici \(p=1,\ldots,m\) sono identici nelle due somme e si cancellano esattamente. Rimangono soltanto:
- il bordo scalare \(p=0\), con \(\Lambda_m(0)=m^2/4\);
- il bordo centrale VI \(p=m+1,\ q=-1\), con \(\Lambda_m(m+1)=(m+2)^2/4\).

Al grado \(m=0\), il modo costante di \(\zeta_0\) contribuisce \(-2\), mentre il bordo di \(\zeta_1\) ha autovalore 1 e molteplicità 2: i due termini si cancellano. Pertanto, nella regione comune di convergenza \(\Re s>1\),
\[
\boxed{\;
\kappa(s)=2\sum_{m\geq1}a_m
\left[
\left(\frac{(m+2)^2}{4}\right)^{-s}
-\left(\frac{m^2}{4}\right)^{-s}
\right].\;}
\]
Questa identità usa il fattore 2 dei due bidegrees e la convenzione \(0^s=1\). La cancellazione avviene già nel complesso spettrale del quoziente.

### 10.3.2 Differenza dei coefficienti di Molien

Poniamo \(d_n=a_{n-2}-a_n\), per \(n\geq3\). Poiché \(a_1=a_2=0\), il cambio di indice dà
\[
\kappa(s)=2\,4^s\sum_{n\geq3}d_n n^{-2s}.
\]
La funzione generatrice della successione \(d_n\) è
\[
D(t):=\sum_{n\geq3}d_nt^n
=(t^2-1)\frac{1+t^{30}}{(1-t^{12})(1-t^{20})}
+1-t^2.
\]
La semplificazione esatta fornisce
\[
\boxed{\begin{aligned}
(1-t^{60})D(t)=P(t)
={}&t^{62}-2t^{60}+t^{58}-t^{48}+t^{46}\\
&-t^{40}+t^{38}-t^{36}+t^{34}-t^{30}\\
&+t^{26}-t^{24}+t^{22}-t^{20}+t^{14}-t^{12}.
\end{aligned}}
\]
Il numeratore \(P(t)\) ha un solo coefficiente per ciascun residuo non nullo modulo 60, e supporto negli esponenti 12–62. Dalla relazione \(D=P/(1-t^{60})\) segue esattamente
\[
d_{n+60}=d_n\qquad(n\geq3).
\]
Questa periodicità è una conseguenza algebrica della funzione di Molien, non una congettura basata su un cutoff numerico.

I soli rappresentanti \(n_r\geq3\) con \(d_{n_r}\ne0\), scelti in un periodo, sono:
\[
\begin{array}{c|rrrrrrrr}
n_r&12&14&20&22&24&26&30&34\\
d_{n_r}&-1&1&-1&1&-1&1&-1&1\\[2pt]
n_r&36&38&40&46&48&58&60&62\\
d_{n_r}&-1&1&-1&1&-1&1&-2&1
\end{array}
\]
Tutti gli altri residui hanno coefficiente zero. In particolare,
\[
\sum_r d_{n_r}=-1,\qquad
\sum_r d_{n_r}\left(\frac12-\frac{n_r}{60}\right)=0.
\]

### 10.3.3 Continuazione esplicita tramite Hurwitz

La periodicità permette di raggruppare la serie per residui modulo 60:
\[
\sum_{n\geq3}d_n n^{-2s}
=60^{-2s}\sum_r d_{n_r}
\zeta_H\!\left(2s,\frac{n_r}{60}\right).
\]
Quindi
\[
\boxed{\;
\kappa(s)=2\,4^s60^{-2s}
\sum_r d_{n_r}\,
\zeta_H\!\left(2s,\frac{n_r}{60}\right).\;}
\]
Il lato destro è una somma finita di funzioni zeta di Hurwitz. Fornisce una continuazione meromorfa esplicita della combinazione torsionale \(\kappa\), regolare in \(s=0\). Il fattore \(4^s60^{-2s}\) è mantenuto.

Questa formula non pretende di dare separatamente una formula chiusa per \(\zeta'_0(0)\) e \(\zeta'_1(0)\). È sufficiente per la combinazione che definisce la torsione.

### 10.3.4 Derivata in zero e formula Gamma

Usando
\[
\zeta_H(0,a)=\frac12-a,\qquad
\zeta_H'(0,a)=\log\Gamma(a)-\frac12\log(2\pi),
\]
e le due identità finite sui coefficienti \(d_{n_r}\), il termine derivato dal prefattore \(4^s60^{-2s}\) si annulla. Si ottiene
\[
\kappa'(0)=4\sum_r d_{n_r}
\left[\log\Gamma\!\left(\frac{n_r}{60}\right)
-\frac12\log(2\pi)\right].
\]
Poiché \(2\log T_{\mathcal E}=\kappa'(0)\),
\[
\boxed{\;
\log T_{\mathcal E}
=2\sum_r d_{n_r}\log\Gamma\!\left(\frac{n_r}{60}\right)
+\log(2\pi).\;}
\]
Equivalentemente,
\[
\boxed{\;
T_{\mathcal E}
=2\pi\prod_r
\Gamma\!\left(\frac{n_r}{60}\right)^{2d_{n_r}}.\;}
\]
La valutazione numerica della formula finita è
\[
\log T_{\mathcal E}\simeq0.2745567511565355917,
\qquad
T_{\mathcal E}\simeq1.3159472534785811492.
\]

### 10.3.5 Stato epistemico e limiti

- **Derivato esattamente:** cancellazione dei pesi interni nella combinazione \(-2\zeta_0+\zeta_1\), riduzione a \(d_n=a_{n-2}-a_n\), identità generatrice e periodicità 60.
- **Continuazione esplicita:** la combinazione torsionale \(\kappa(s)\) è espressa da una somma finita di zeta di Hurwitz e quindi continuata meromorficamente.
- **Derivata in zero:** formula finita in termini di funzioni Gamma, con valutazione numerica riportata.
- **Non rivendicato:** formule separate per \(\zeta'_0(0)\) e \(\zeta'_1(0)\); una formula per coefficienti locali o rappresentazioni non banali; confronto normalizzato con la convenzione Ray–Singer di altri complessi. La quantità qui calcolata è la torsione analitica del complesso Rumin nella normalizzazione di Kitaoka fissata in questo audit.


## 10.4 Confronto con Reidemeister–Ray–Singer: identificazione geometrica del valore

Questa sezione chiude il confronto di normalizzazione che era rimasto aperto in §10.3. Il confronto non va fatto con una torsione scalare aciclica: con coefficienti banali la sfera omologica di Poincaré ha
\[
H^0(M;\mathbb C)\simeq\mathbb C,\qquad
H^1(M;\mathbb C)=H^2(M;\mathbb C)=0,\qquad
H^3(M;\mathbb C)\simeq\mathbb C,
\quad M=S^3/2I.
\]
La quantità naturale è la metrica sulla retta determinante
\[
\det H^*(M;\mathbb C)
=\det H^0\otimes(\det H^1)^{-1}
\otimes\det H^2\otimes(\det H^3)^{-1}.
\]

### 10.4.1 Il quoziente è CR Seifert

Realizziamo \(S^3\) come gruppo \(SU(2)\). Il gruppo binario icosaedrale \(2I\) agisce per moltiplicazione a sinistra. La circonferenza di Hopf, realizzata dalla moltiplicazione scalare \(z\mapsto e^{it}z\), commuta con tale azione e discende quindi a \(S^3/2I\). L'azione circolare è localmente libera e preserva la struttura CR standard. Il quoziente è pertanto una varietà CR Seifert tridimensionale.

Rumin–Seshadri, Theorem 4.2, dimostrano che su ogni CR Seifert tridimensionale, per ogni rappresentazione unitaria, la metrica di Ray–Singer del complesso di contatto coincide con quella del complesso di de Rham. Nella loro convenzione il numero di torsione del complesso di contatto è l'inverso della torsione di Ray–Singer:
\[
T_C=(T_{RS})^{-1}.
\]
La loro convenzione è opposta a quella di Kitaoka per il numero \(T_{\mathcal E}\) usato in §10.3. In dimensione tre, con la dualità spettrale tra i gradi, si ha
\[
\kappa_{\mathrm{Kitaoka}}(s)=-\kappa_C(s),
\qquad
T_{\mathcal E}=e^{\kappa'_{\mathrm{Kitaoka}}(0)/2}
=(T_C)^{-1}=T_{RS}.
\]
Quindi il valore ottenuto dalla zeta Rumin è direttamente nella convenzione Ray–Singer, non nella convenzione inversa di Rumin–Seshadri. Riferimenti: Rumin–Seshadri, *Analytic torsions on contact manifolds*, Ann. Inst. Fourier 62 (2012), Theorem 4.2 e Remark 2.6; Kitaoka, SIGMA 18 (2022), Corollary 0.3. La prima fonte esplicita anche che la coincidenza delle metriche vale per rappresentazioni unitarie su CR Seifert tridimensionali.

### 10.4.2 La metrica di coomologia fissa il fattore di volume

Scegliamo le basi integrali canoniche \(1\in H^0(M;\mathbb Z)\) e \([M]^*\in H^3(M;\mathbb Z)\), con \(\int_M[M]^*=1\). Poiché \(M\) è una sfera omologica integrale, la norma di Reidemeister sulla retta determinante assegna norma 1 all'elemento
\[
1\otimes([M]^*)^{-1}.
\]
Sia \(V=\operatorname{Vol}(M,g_{\theta,J})\). Le norme armoniche L² delle due classi sono
\[
\|1\|_{L^2}=V^{1/2},\qquad
\|[M]^*\|_{L^2}=V^{-1/2}.
\]
Di conseguenza la norma L² dell'elemento della retta determinante è
\[
\bigl\|1\otimes([M]^*)^{-1}\bigr\|_{L^2}=V.
\]
La metrica di Ray–Singer è, nella convenzione standard,
\[
\|\cdot\|_{RS}=T_{RS}^{-1}\|\cdot\|_{L^2}.
\]
L'identità di Cheeger–Müller per la metrica sulla retta determinante dà quindi
\[
1=T_{RS}^{-1}V,
\qquad\boxed{T_{RS}=V.}
\]
Questo è il confronto non aciclico corretto: non si impone \(T=1\), ma si tiene conto delle basi integrali di \(H^0\) e \(H^3\) e della loro norma L².

### 10.4.3 Volume della metrica di Kitaoka sul quoziente

Nella normalizzazione sferica di Kitaoka, la metrica di contatto è \(g_{\theta,J}=4g_{\mathrm{std}}\), dove \(g_{\mathrm{std}}\) è la metrica rotonda sulla sfera unitaria \(S^3\). Moltiplicare la metrica in dimensione tre per 4 moltiplica il volume per \(4^{3/2}=8\). Poiché
\[
\operatorname{Vol}(S^3,g_{\mathrm{std}})=2\pi^2,
\]
si ha
\[
\operatorname{Vol}(S^3,g_{\theta,J})=16\pi^2.
\]
Il rivestimento \(S^3\to S^3/2I\) ha grado \(|2I|=120\), perciò
\[
\boxed{V=\operatorname{Vol}(S^3/2I,g_{\theta,J})
=\frac{16\pi^2}{120}=\frac{2\pi^2}{15}.}
\]

### 10.4.4 Riduzione esatta della formula Gamma

La formula di §10.3 dà
\[
T_{\mathcal E}
=2\pi\left[
\frac{
\prod_{a\in\{31,7,11,13,17,19,23,29\}}
\Gamma(a/30)}
{\prod_{b\in\{6,10,12,15,18,20,24\}}
\Gamma(b/30)}
\right]^2.
\]
La formula di riflessione \(\Gamma(x)\Gamma(1-x)=\pi/\sin(\pi x)\), insieme alla formula di moltiplicazione di Gauss, riduce il rapporto finito al quadrato a
\[
\left[
\frac{
\prod_{a\in\{31,7,11,13,17,19,23,29\}}
\Gamma(a/30)}
{\prod_{b\in\{6,10,12,15,18,20,24\}}
\Gamma(b/30)}
\right]^2=\frac{\pi}{15}.
\]
Ne segue la forma chiusa
\[
\boxed{T_{\mathcal E}=\frac{2\pi^2}{15}
=\operatorname{Vol}(S^3/2I,g_{\theta,J})
=T_{RS}.}
\]
Il valore numerico precedente \(1.3159472534785811492\) coincide con \(2\pi^2/15\). La coincidenza non è un confronto con il numero aciclico 1: è esattamente il fattore di volume richiesto dalla metrica sulla retta determinante per la coomologia banale della sfera omologica.

### 10.4.5 Stato epistemico e controlli residui

- **Dimostrato dalla fonte primaria:** su CR Seifert tridimensionali la metrica di Ray–Singer del complesso di contatto coincide con quella de Rham; le convenzioni numeriche di Rumin–Seshadri e Kitaoka sono inverse.
- **Derivato geometricamente:** la Hopf circle commuta con \(2I\), discende al quoziente ed è localmente libera; il volume della metrica indotta è \(16\pi^2/120\).
- **Confronto topologico:** con le basi integrali di \(H^0\) e \(H^3\), Cheeger–Müller richiede \(T_{RS}=V\), non \(1\).
- **Identificazione algebrica:** la formula Gamma di §10.3 si riduce a \(2\pi^2/15\) tramite riflessione e moltiplicazione di Gauss.
- **Test del repository:** lo script Python su GitHub non è stato eseguito end-to-end direttamente da questo runtime; quindi non si dichiara un PASS integrale del file remoto.
- **Riproduzione indipendente eseguita il 2026-11-06:** con SymPy, media dei caratteri/Reynolds = coefficienti di Molien fino a \(m=300\); periodicità \(d_{n+60}=d_n\) verificata fino a \(n=600\); identità simbolica del prodotto Gamma ridotta alla formula trigonometrica esatta; confronto numerico Gamma-volume a 100 cifre con residuo 0 nella precisione di output. Questi test riproducono le formule decisive, ma non sostituiscono l'esecuzione integrale dello script nel repository.

**Conclusione:** il confronto con Reidemeister–Ray–Singer non falsifica il risultato precedente; al contrario, con la corretta convenzione non aciclica e la metrica di Kitaoka, il valore calcolato coincide con il volume del quoziente. La torsione Rumin normalizzata in §10.3 è quindi identificata con la torsione di Ray–Singer nel caso banale, attraverso il teorema CR-Seifert di Rumin–Seshadri.


## 11. Verifica esplicita dell'intertwiner centrale \(D\) per \(n=1\)

Questa sezione chiude il passaggio lasciato aperto in §9: non si usa soltanto l'equivarianza astratta, ma si calcola anche \(D^\dagger D\) sulle copie irriducibili interne, controllando i bordi separatamente. La fonte è Kitaoka, arXiv:1911.03092v1, §2.3, Caso V (pp. 9–10 del PDF), Casi VI–VII (p. 10), formule (1.3) e (2.4). Il Caso V della sezione spettrale usa \(i+j=n-1=0\) per \(n=1\); non va confuso con la Case V della Proposition 1.1.

### 11.1 Settore interno \(p,q\geq1\)

Per il peso U(2) \((q,-p)\), il sottospazio centrale è
\[
W_{p,q}=\Psi^{(1,0)}_{(q,0,0,p)}\oplus
\Psi^{(0,1)}_{(q,0,0,p)}.
\]
Siano \(\psi_{10},\psi_{01}\) i vettori di peso massimo normalizzati di Kitaoka e
\[
A^2=\frac{p(q+1)}2,\qquad B^2=\frac{q(p+1)}2,\qquad
C=\frac{p-q}{2}.
\]
La componente esatta dell'immagine del differenziale di primo ordine è
\[
d_E\psi_{00}=A\psi_{10}+B\psi_{01},
\]
e il suo complemento ortogonale in \(W_{p,q}\) è generato da
\[
v_\perp=B\psi_{10}-A\psi_{01}.
\]
Per la formula di Kitaoka in §2.3, Caso V, si pone
\[
A'=C-2A^2,\qquad B'=C+2B^2,\qquad S=2pq+p+q.
\]
Sostituendo \(A^2,B^2\) si ottiene **esattamente**
\[
A'=-\frac S2,\qquad B'=\frac S2.
\]
La formula primaria per l'intertwiner dà
\[
D v_\perp=\sqrt{-1}\,\theta\wedge
\bigl(A'B\psi_{10}-B'A\psi_{01}\bigr)
=-\sqrt{-1}\,\frac S2\,\theta\wedge
\bigl(B\psi_{10}+A\psi_{01}\bigr).
\]
Il vettore d'arrivo ha la stessa norma del vettore di partenza, quindi
\[
\boxed{\left.D^\dagger D\right|_{W_{p,q}\ominus\operatorname{im}d_E^0}
=\frac{S^2}{4}
=\frac{(2pq+p+q)^2}{4}.}
\]
Questa è la verifica esplicita del modulo dell'intertwiner sul complemento. Sul sottospazio \(\operatorname{im}d_E^0\), invece, \(D d_E^0=0\) perché \((\mathcal E^\bullet,d_E^\bullet)\) è un complesso. I due sottospazi hanno la stessa eigenvalue del Laplaciano Rumin: sull'immagine di \(d_E^0\) essa proviene da \((d_E^0d_E^{0\dagger})^2\), sul complemento da \(D^\dagger D\). La coincidenza è precisamente quella del Theorem 0.1, non un'ipotesi di uguaglianza dei settori.

### 11.2 Settori con un peso nullo e bordi eccezionali

- **\(q=0,p\geq1\), Case III:** la rappresentazione in \(\mathcal E^{1,0}\) proviene da \(d_E^0\); \(D=0\) su tale copia e \(\Delta_E^1\) ha eigenvalue \(p^2/4\).
- **\(p=0,q\geq1\), Case IV:** il caso coniugato in \(\mathcal E^{0,1}\); \(D=0\) sulla copia proveniente da \(d_E^0\), eigenvalue \(q^2/4\).
- **\(q=-1,p\geq1\), Proposition 1.1 Case VI:** non esiste la copia sorgente in \(\mathcal E^0\), gli aggiunti orizzontali si annullano e \(D=\theta\wedge\mathcal L_T\). Da \(2\mathcal L_T\psi=\sqrt{-1}(p-q)\psi\) segue \(D^\dagger D=(p+1)^2/4\).
- **\(p=-1,q\geq1\), Case VII:** il coniugato, con \(D^\dagger D=(q+1)^2/4\).

I valori di bordo non sono estrapolati dal caso \(p,q\geq1\): sono ottenuti dai Casi VI–VII. Per \(m=12\), i due pesi \((q,p)=(-1,13)\) e \((13,-1)\) hanno eigenvalue \(49\).

### 11.3 Compatibilità con Reynolds e discendenza al quoziente

Per \(g\in2I\subset SU(2)\), l'azione è un automorfismo CR della sfera standard e preserva \(\theta,T,J,g_{\theta,J}\), \(d_b\), \(L\), la proiezione primitiva e quindi \(D\). Pertanto
\[
D\rho_1(g)=\rho_2(g)D,\qquad
P_{2I}^{E^2}D=DP_{2I}^{E^1},
\quad P_{2I}^{E^k}=\frac1{120}\sum_{g\in2I}\rho_k(g).
\]
Quindi \(D\) manda esattamente le sezioni invarianti nelle sezioni invarianti. Nel settore \(p,q\geq1\), la Reynolds projection restringe sia \(\operatorname{im}d_E^0\) sia il suo complemento; ciascuno ha dimensione \(a_m\), \(m=p+q\), e \(D^\dagger D=S^2/4\) sul secondo. Nei settori \(q=0\) o \(p=0\) rimane una sola copia centrale, mentre i due bordi VI–VII hanno una copia invariata \(a_m\) ciascuno. Non si moltiplica la degenerazione per una dimensione U(2) ulteriore: \(a_m\) è la dimensione del sottospazio \(2I\)-invariante dentro ciascuna irriducibile.

### 11.4 Verifiche simboliche riproducibili e stato

Il test aggiunto al programma verifica in aritmetica esatta:
\[
\frac{(A'B)^2+(B'A)^2}{A^2+B^2}
=\frac{(2pq+p+q)^2}{4},
\qquad A'=-S/2,\quad B'=S/2.
\]
Inoltre controlla la decomposizione Julg–Kasparov per ogni \(m\): in ciascun bidegree ci sono \(m+1\) pesi U(2) distinti, tutti con restrizione SU(2) \(\operatorname{Sym}^m\), e ognuno ha molteplicità invarianti \(a_m\). Il confronto tra media esatta dei caratteri e serie di Molien viene esteso fino a \(m=300\); la periodicità dei coefficienti torsionali \(d_n=a_{n-2}-a_n\) è controllata fino a \(n=600\). La riduzione Gamma esatta e il confronto ad alta precisione con \(2\pi^2/15\) sono verificati separatamente.

**Stato epistemico dopo questa tranche:**
- **Derivato dalla fonte primaria:** i tre insiemi di pesi U(2) per \(n=1\), i casi speciali VI–VII, e l'intertwiner centrale sul settore interno.
- **Verificato simbolicamente:** \(D^\dagger D=S^2/4\) sul complemento interno; bordi VI–VII; caratteri/Reynolds contro Molien; periodicità torsionale; identità Gamma.
- **Spettro non twistato:** le formule di zeta §§10.1–10.3 descrivono la molteplicità di ogni peso e i valori degli autovalori in \(\mathcal E^0,\mathcal E^1\); per dualità Hodge si ottengono gli altri gradi del complesso. La combinazione torsionale è continuata in modo finito tramite Hurwitz e la derivata in zero è stata valutata esattamente.
- **Non rivendicato:** matrice di \(D\) in una base globale concreta, derivata separata delle due zeta, o torsione per rappresentazioni piatte non banali.

**Fonti puntuali:** Kitaoka, arXiv:1911.03092v1, Proposition 1.1 (PDF pp. 5–6; Case I/VI/VII), §2.3 Case V–VII (PDF pp. 9–10); Julg–Kasparov, *J. Reine Angew. Math.* 463 (1995), 99–152, §4(b), come citato nella Proposition 1.1. Per la serie di Molien del gruppo binario icosaedrale: S. Mukai, *An Introduction to Invariants and Moduli*, Cambridge Studies in Advanced Mathematics 81, Cambridge University Press (2003), p. 19; si usa \(M(t)=(1+t^{30})/((1-t^{12})(1-t^{20}))\).
