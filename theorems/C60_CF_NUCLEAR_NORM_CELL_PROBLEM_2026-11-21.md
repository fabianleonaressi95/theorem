# C60 — cell problem ottimale per il disarrangiamento bulk lineare

Data: 2026-11-21  
Classificazione: **teorema dimostrato nel modello intrinseco faccia-per-faccia**  
Densità interfaciale: \u03c8(a,\u03bd)=|a|, con norma euclidea nel target e normale unitaria.

## 1. Enunciato

Sia \(f\) una faccia piana del complesso C60, identificata con un poligono limitato \(P\subset\mathbb R^2\). Siano
\[
g(\xi)=A\xi+b,\qquad \widetilde G\in\mathbb R^{3\times2},\qquad M=A-\widetilde G.
\]
Si considerino successioni \(u_h\in SBV(P;\mathbb R^3)\) tali che
\[
u_h\to g\quad\text{in }L^1(P),\qquad
\nabla u_h=\widetilde G\quad\text{a.e. in }P.
\]
Per ogni tale successione, se la parte di salto è quella che realizza il difetto distribuzionale \(M\,\mathcal L^2\), il costo interfaciale soddisfa
\[
\liminf_{h\to0}\int_{J_{u_h}}|[u_h]|\,d\mathcal H^1
\;\ge\; |P|\,\|M\|_*.
\]
Esiste inoltre una successione esplicita per cui vale l'uguaglianza nel limite. Pertanto il costo di cella per unità di area è
\[
\boxed{\mathcal C(M)=\|M\|_*=\sigma_1(M)+\sigma_2(M).}
\]
La norma \(\|\cdot\|_*\) è la norma nucleare; per matrici \(3\times2\) vi sono al più due valori singolari non nulli.

## 2. Limite inferiore: dualità della norma nucleare

La convergenza \(u_h\to g\) in \(L^1\) implica la convergenza distribuzionale
\[
Du_h\rightharpoonup^* A\,\mathcal L^2.
\]
Poiché la parte assolutamente continua è esattamente \(\widetilde G\,\mathcal L^2\), segue
\[
D^j u_h\rightharpoonup^* M\,\mathcal L^2
\]
nel senso delle misure matriciali (sul dominio interno; eventuali contributi macroscopici di bordo sono trattati separatamente).

Sia \(Q\in\mathbb R^{3\times2}\) una matrice costante con norma operatore \(\|Q\|_{op}\le1\). Per ogni salto, con \(|\nu_u|=1\),
\[
Q:([u_h]\otimes\nu_u)
= [u_h]\cdot(Q\nu_u)
\le |[u_h]|\,\|Q\|_{op}
\le |[u_h]|.
\]
Integrando contro una funzione test non negativa compatta e passando al limite si ottiene, per ogni tale \(Q\),
\[
|P|\,Q:M
\le \liminf_{h\to0}\int_{J_{u_h}}|[u_h]|\,d\mathcal H^1.
\]
Prendendo il supremo su \(\|Q\|_{op}\le1\), si usa la dualità esatta
\[
\|M\|_* = \sup_{\|Q\|_{op}\le1} Q:M,
\]
e quindi si conclude il limite inferiore.

Questa stima non è la norma di Frobenius: il costo elementare è assegnato a matrici di rango uno \(a\otimes\nu\), con costo \(|a|\); la convessificazione con normale libera è precisamente la norma nucleare.

## 3. Recupero ottimale mediante SVD

Sia una decomposizione ai valori singolari
\[
M=\sum_{j=1}^{r}\sigma_j u_j\otimes v_j,
\qquad r=\operatorname{rank}M\le2,
\]
con \(\sigma_j>0\), \(|u_j|=|v_j|=1\). Definiamo
\[
u_h(\xi)=\widetilde G\xi+b+
\sum_{j=1}^{r}\sigma_j h
\left\lfloor\frac{\xi\cdot v_j}{h}\right\rfloor u_j.
\]
La correzione rispetto a \(g\) è
\[
u_h(\xi)-g(\xi)
=\sum_{j=1}^{r}\sigma_j
\left(h\left\lfloor\frac{\xi\cdot v_j}{h}\right\rfloor
-\xi\cdot v_j\right)u_j,
\]
da cui
\[
\|u_h-g\|_{L^\infty(P)}
\le h\sum_{j=1}^{r}\sigma_j
\longrightarrow0.
\]
Fuori dalle rette di salto, ogni termine quantizzato è localmente costante; pertanto
\[
\nabla u_h=\widetilde G\quad\text{a.e.}
\]
Le rette della famiglia \(j\) hanno normale \(v_j\), distanza reciproca \(h\), salto \(h\sigma_j u_j\). La loro lunghezza totale in un poligono fissato, moltiplicata per \(h\), converge all'area del poligono:
\[
h\sum_{k\in\mathbb Z}
\mathcal H^1\big(P\cap\{\xi\cdot v_j=kh\}\big)
\longrightarrow |P|.
\]
Di conseguenza il costo della famiglia \(j\) converge a
\[
\sigma_j |P|.
\]
Le intersezioni tra famiglie di rette hanno misura \(\mathcal H^1\) nulla e non producono un termine aggiuntivo. Sommando le famiglie,
\[
\lim_{h\to0}\int_{J_{u_h}}|[u_h]|\,d\mathcal H^1
=|P|\sum_{j=1}^{r}\sigma_j
=|P|\,\|M\|_*.
\]
La successione è SBV e ha variazione totale uniformemente limitata. Le correzioni sulle frontiere delle facce sono \(O(h)\), quindi l'incollaggio sul complesso finito C60 conserva i salti macroscopici nel limite.

## 4. Conseguenza per il funzionale C60

Per il costo lineare isotropo, il valore della costruzione ottimale sul complesso è
\[
\mathcal E_{\mathrm{micro}}(M)
=\sum_{f\in\mathcal F(C60)}
|f|\,\|M_f\|_*.
\]
Il contributo dei salti macroscopici lungo gli spigoli va aggiunto separatamente:
\[
\int_{J_g}\!|[g]|\,d\mathcal H^1.
\]
Questa formula identifica il costo minimo per il difetto bulk costante faccia per faccia, nella classe e con le condizioni di convergenza enunciate. Non identifica automaticamente il rilassamento per densità anisotrope \(\psi(a,\nu)\), campi \(\widetilde G\) variabili all'interno delle facce, vincoli di immersione, o classi cinematiche più ristrette.

## 5. Distinzione per potenze diverse

Per \(\psi(a,\nu)=|a|^p\), la stessa costruzione SVD ha costo di ordine \(h^{p-1}\):
- \(p=1\): limite finito e ottimale come sopra;
- \(p>1\): costo microscopico tende a zero;
- \(0<p<1\): questa costruzione non dà un costo uniformemente limitato.

La conclusione di ottimalità tramite norma nucleare riguarda esclusivamente \(p=1\) e la densità isotropa indipendente dalla normale.

## 5bis. Corollario: difetto di rango uno

Se \(\operatorname{rank}M\le1\), la SVD ha un solo valore singolare e
\[
\|M\|_*=\sigma_1(M)=\|M\|_F.
\]
In questo caso il lower bound nucleare coincide con la variazione totale
della misura matriciale \(M\,\mathcal L^2\) (densità di Frobenius), e una
sola famiglia di linee laminate orientata lungo \(v_1\) realizza il minimo.
Il caso rango uno non è un problema a parte: è il caso particolare
\(\sigma_2=0\) del teorema generale.

## 6. Stato logico

- **Dimostrato:** limite inferiore nucleare per ogni successione SBV con convergenza distribuzionale del difetto bulk e costo \(\int|[u_h]|\).
- **Dimostrato:** recupero SVD che satura il limite inferiore su ogni faccia piana.
- **Dimostrato:** formula additiva sul complesso finito C60 per campi bulk costanti faccia per faccia.
- **Non affermato:** formula per densità anisotrope, campi bulk non costanti o teorema integrale CF generale su superfici poliedrali.
