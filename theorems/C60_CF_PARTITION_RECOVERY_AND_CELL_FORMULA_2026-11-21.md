# C60 — recovery affine e cell formula anisotropa

Data: 2026-11-21

Classificazione:
- Recovery per gradiente costante: **dimostrato**.
- Cell formula anisotropa senza dato al bordo: **dimostrata** sotto le ipotesi della sezione 2.
- Recovery per gradiente variabile in W^{1,1}: **aperto in questo documento**; il raccordo tra celle non è dimostrato.

Questo documento separa tre questioni indipendenti. La costruzione SVD risolve il caso affine. La cell formula anisotropa è trattata senza usare il lemma di raccordo. Il passaggio a un gradiente variabile richiede invece una stima di raccordo che qui non viene presentata come provata.

---

## 1. Recovery per gradiente costante — caso isotropo

Sia M in R^{m x 2}, Q un quadrato e u(x)=Mx+b. Scriviamo una SVD
$$
M=\\sum_{i=1}^{r}\\sigma_i a_i\\otimes\\nu_i,\\qquad r\\le 2,
$$
con a_i e nu_i unitari e le nu_i ortonormali. Poniamo
$$
v_h(x)=b+\\sum_{i=1}^{r}\\sigma_i a_i\\,h\\left\\lfloor\\frac{x\\cdot\\nu_i}{h}\\right\\rfloor.
$$
La funzione è costante sulle celle poligonali della disposizione delle famiglie di rette e ha gradiente nullo quasi ovunque. Inoltre
$$
\\|v_h-u\\|_{L^\\infty(Q)}\\le h\\sum_i\\sigma_i.
$$
Sulle rette della famiglia i, fuori dai punti d'intersezione con le altre famiglie, il salto ha ampiezza h sigma_i. La lunghezza totale delle rette di quella famiglia in Q, moltiplicata per h, tende a |Q|. Pertanto
$$
\\lim_{h\\downarrow0}\\int_{J_{v_h}}|[v_h]|\\,d\\mathcal H^1
=|Q|\\sum_i\\sigma_i=|Q|\\,\\|M\\|_*.
$$
Le intersezioni sono finite e hanno misura H^1 nulla. Non è imposto alcun dato al bordo; non si afferma una recovery con traccia prescritta.

**Lower bound affine.** Se v_h converge a Mx+b in L^1(Q) e i costi isotropi sono limitati, la coercività controlla le variazioni su ogni sottoquadrato compatto. La convergenza distribuzionale delle derivate e la dualità tra norma nucleare e norma operatore, prima su sottoquadrati compatti e poi per esaurimento di Q, danno
$$
\\liminf_h\\int_{J_{v_h}}|[v_h]|\\,d\\mathcal H^1
\\ge |Q|\\,\\|M\\|_*.
$$
La densità affine isotropa è quindi esattamente la norma nucleare.

## 2. Cell formula anisotropa senza vincolo al bordo

Assumiamo che psi: R^m x S^1 -> [0,infty) soddisfi
$$
c|a|\\le\\psi(a,\\nu)\\le C|a|,\\qquad
\\psi(ta,\\nu)=t\\psi(a,\\nu)\\ (t>0),\\qquad
\\psi(-a,-\\nu)=\\psi(a,\\nu).
$$
La cell formula è **senza dato al bordo**. Per un quadrato Q di area uno definiamo
$$
f_{cell}(M)=\\inf\\left\\{\\liminf_{h\\to\\infty}
\\int_{J_{w_h}\\cap Q}\\psi([w_h],\\nu_{w_h})\\,d\\mathcal H^1:
w_h\\to Mx\\text{ in }L^1(Q),\\ w_h\\text{ piecewise constant}\\right\\}.
$$
Definiamo
$$
\\Lambda_\\psi=\\{A\\in R^{m x 2}:
A:(a\\otimes\\nu)\\le\\psi(a,\\nu)\\quad\\forall a,\\nu\\}
$$
e
$$
g_\\psi(M)=\\inf\\left\\{\\sum_{i=1}^N\\psi(b_i,\\nu_i):
N<\\infty,\\ M=\\sum_{i=1}^N b_i\\otimes\\nu_i\\right\\}.
$$

**Le decomposizioni nell'infimo includono anche termini con normali parallele.** Non li fondiamo: senza subadditività di psi rispetto ad a, la fusione non è giustificata.

**Dualità convessa.** g_psi è positivamente 1-omogenea e convessa, perché le decomposizioni si possono concatenare. È finita e coerciva grazie ai limiti c|a| <= psi <= C|a|. In dimensione finita è dunque continua e coincide con il supporto del suo polare:
$$
g_\\psi(M)=\\sup_{A\\in\\Lambda_\\psi} A:M.
$$
Infatti A appartiene a Lambda_psi se e solo se A:M <= g_psi(M) per ogni M: una direzione segue testando sui tensori semplici, l'altra applicando la disuguaglianza a ogni decomposizione finita.

**Lower bound della cell formula.** Per A in Lambda_psi, la disuguaglianza sui salti dà
$$
A:Dw_h\\le\\psi([w_h],\\nu_{w_h})\\,\\mathcal H^1\\!\\llcorner J_{w_h}.
$$
La coercività controlla le variazioni. Passando al limite distribuzionale su sottoquadrati compatti e poi esaurendo Q,
$$
f_{cell}(M)\\ge\\sup_{A\\in\\Lambda_\\psi}A:M=g_\\psi(M).
$$

**Upper bound per ogni decomposizione finita.** Fissiamo una decomposizione arbitraria
$$
M=\\sum_{i=1}^N b_i\\otimes\\nu_i,
$$
senza restrizioni di non-parallelismo. Scegliamo fasi phi_i e poniamo
$$
w_h(x)=\\sum_{i=1}^N b_i h\\left\\lfloor\\frac{x\\cdot\\nu_i+\\phi_i}{h}\\right\\rfloor.
$$
La funzione è costante sulle celle poligonali della disposizione delle rette e converge uniformemente a Mx, a meno di una costante additiva. Ogni famiglia di rette contribuisce al costo per unità di area con psi(b_i,nu_i), per 1-omogeneità. Se alcune normali sono parallele, si scelgono fasi distinte per separare le rette; le intersezioni tra famiglie non parallele sono finite e non contribuiscono all'integrale su J_w. Quindi
$$
f_{cell}(M)\\le\\sum_{i=1}^N\\psi(b_i,\\nu_i).
$$
Prendendo l'infimo su tutte le decomposizioni finite,
$$
\\boxed{f_{cell}(M)=g_\\psi(M)=\\sup_{A\\in\\Lambda_\\psi}A:M.}
$$
La densità è la funzione di supporto di Lambda_psi, ossia l'inviluppo convesso positivamente 1-omogeneo generato dal costo sui tensori di rango uno. Questo risultato riguarda la cella senza dato al bordo; non dimostra la versione con traccia affine prescritta.

**Conseguenze.**
- Per psi(a,nu)=|a|, Lambda_psi è la palla unitaria della norma operatore e f_cell(M)=||M||_*.
- Per psi(a,nu)=Phi(a)k(nu), la formula ONB è in generale soltanto un upper bound.
- psi(a,nu)=|a|^2 è fuori dalle ipotesi di 1-omogeneità e va trattata separatamente.

**Evidenza numerica ONB.** Lo script colloquio_morandotti/cell_check2.py riporta, per M=[[1,0.3],[0.2,0.9],[0.1,-0.4]] e psi(a,nu)=|a|(2-|nu_1|), ONB 2.5726173 contro una decomposizione a due famiglie non ortogonali 2.5119742 (angolo circa 103.5 gradi). Questo è un controesempio numerico alla pretesa di ottimalità ONB per quei dati, non una prova dell'ottimalità globale della decomposizione non ortogonale.

## 3. Recovery per gradiente variabile — APERTO

Per c in W^{1,1}(Q;R^m), il lower bound isotropo
$$
\\liminf_h\\int_{J_{v_h}}|[v_h]|\\,d\\mathcal H^1
\\ge\\int_Q\\|\\nabla c\\|_*\\,dx
$$
segue dalla dualità e dalla convergenza distribuzionale delle derivate, con localizzazione ed esaurimento del dominio.

**Il recovery upper bound non è dimostrato qui.** La precedente costruzione cella-per-cella produce interfacce artificiali; la stima del loro costo non segue dalla sola affermazione che l'ampiezza del salto è O(delta^2+h). La proposta di una fascia di raccordo richiede un lemma autonomo che specifichi partizione, assegnazione dei valori, conteggio delle interfacce e stima dei salti. Fino alla dimostrazione di quel lemma, l'identità
$$
\\inf_{v_h\\to c\\text{ in }L^1}\\liminf_h F(v_h)
=\\int_Q\\|\\nabla c\\|_*\\,dx
$$
resta **aperta quanto al recovery upper bound** e non viene classificata come teorema.

Di conseguenza, non si dichiara dimostrata l'applicazione per G-tilde(x) misurabile ottenuta invocando un Lemma R variabile. Restano validi i risultati per gradiente costante per faccia, quando il difetto M_f è costante e si applica direttamente la costruzione affine.

## 4. Immersione — rank 2 quasi ovunque

Per u_h(xi)=c_0 A xi+b+v_h(xi), con c_0>0, A^T A=I_2 e v_h piecewise constant,
$$
\\nabla u_h=c_0A\\quad\\text{a.e.},\\qquad \\operatorname{rank}\\nabla u_h=2\\quad\\text{a.e.}
$$
Questo non implica continuità globale, iniettività o embeddedness attraverso i fronti di salto. L'embeddedness globale resta aperta.

## 5. Stato finale

| Affermazione | Stato |
|---|---|
| Recovery per gradiente costante M, caso isotropo | **Provato** |
| Cell formula anisotropa senza dato al bordo, inf su tutte le decomposizioni finite | **Provato** sotto le ipotesi dichiarate |
| Fusione di termini con normali parallele | **Non consentita in generale**; non viene usata |
| Lower bound nucleare per gradiente variabile, psi=|a| | **Provato** |
| Recovery per c in W^{1,1} | **Aperto**: raccordo non dimostrato |
| Formula ONB anisotropa | **Solo upper bound** |
| Rank 2 a.e. per gradiente c_0 A | **Provato** come proprietà del gradiente a.e. |
| Embeddedness globale | **Aperta** |
