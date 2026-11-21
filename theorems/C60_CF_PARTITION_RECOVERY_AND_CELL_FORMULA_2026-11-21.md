# C60 — lemma di recovery per partizioni e cell formula generale

Data: 2026-11-21
Classificazione: **(i) recovery per gradiente costante: dimostrato; (ii) cell formula anisotropa senza dato al bordo: dimostrata sotto le ipotesi indicate; (iii) recovery per gradiente variabile: aperto in questo documento**.

Questo documento separa tre questioni che non devono essere confuse. La costruzione SVD risolve il caso affine. La cell formula anisotropa è indipendente dal lemma di raccordo e ammette una dimostrazione per dualità e laminazioni a strisce. Il passaggio a un gradiente variabile richiede invece un raccordo tra celle la cui stima non è qui dimostrata.

---

## 1. Recovery per gradiente costante — caso isotropo

Sia (M\in\mathbb R^{m\times2}), (Q\subset\mathbb R^2) un quadrato e (u(x)=Mx+b). Scriviamo una SVD
[
M=\sum_{i=1}^{r}\sigma_i a_i\otimes\nu_i,\qquad r\le2,
]
con (a_i,\nu_i) unitari e le `\nu_i` ortonormali. Definiamo
[
v_h(x)=b' +\sum_{i=1}^{r}\sigma_i a_i\,h\left\lfloor\frac{x\cdot\nu_i}{h}\right\rfloor,
]
dove (b') assorbe la costante affine eventualmente prodotta dalla scelta delle fasi.

La disposizione delle famiglie finite di rette in (Q) induce una partizione poligonale finita; (v_h) è costante su ciascuna cella e (\nabla v_h=0) quasi ovunque. Inoltre
[
\|v_h-u\|_{L^\infty(Q)}\le h\sum_i\sigma_i.
]
Sulle rette della famiglia (i), fuori dai punti d'intersezione con le altre famiglie, il salto ha ampiezza (h\sigma_i), mentre la lunghezza totale delle rette di quella famiglia in (Q), moltiplicata per (h), tende a (|Q|). Ne segue
[
\lim_{h\downarrow0}\int_{J_{v_h}}|[v_h]|\,d\mathcal H^1
=|Q|\sum_i\sigma_i=|Q|\,\|M\|_*.
]
I punti d'intersezione hanno misura \(\mathcal H^1\) nulla. Non è imposto alcun dato al bordo; non si afferma una recovery con traccia prescritta.

**Lower bound affine.** Se (v_h\to Mx+b) in (L^1(Q)) e i costi isotropi sono limitati, la coercività dà un limite uniforme per (|Dv_h|(Q')) su ogni (Q'\Subset Q). La convergenza distribuzionale delle derivate e la dualità tra norma nucleare e norma operatore danno, per esaurimento di (Q),
[
\liminf_h\int_{J_{v_h}}|[v_h]|\,d\mathcal H^1\ge |Q|\,\|M\|_*.
]
Quindi la densità affine isotropa è esattamente la norma nucleare.

## 2. Cell formula anisotropa senza vincolo al bordo

Assumiamo
[
\psi:\mathbb R^m\times S^1\to[0,\infty),\quad
c|a|\le\psi(a,\nu)\le C|a|,
\quad \psi(ta,\nu)=t\psi(a,\nu)\ (t>0),
\quad\psi(-a,-\nu)=\psi(a,\nu).
]
La cell formula qui considerata è **senza dato al bordo**: per (M\in\mathbb R^{m\times2}),
[
f_{\rm cell}(M):=\inf\left\{\liminf_{h\to\infty}
\int_{J_{w_h}\cap Q}\psi([w_h],\nu_{w_h})\,d\mathcal H^1:
w_h\to Mx\text{ in }L^1(Q),\ w_h\text{ piecewise constant}\right\}.
]
La normalizzazione per area è sottintesa; si può prendere (|Q|=1).

Definiamo
[
\Lambda_\psi=\{A\in\mathbb R^{m\times2}:
A:(a\otimes\nu)\le\psi(a,\nu)\quad\forall a,\nu\}.
]
E poniamo
[
g_\psi(M)=\inf\left\{\sum_{i=1}^N\psi(b_i,\nu_i):
N<\infty,\ M=\sum_{i=1}^N b_i\otimes\nu_i\right\}.
]
**L'infimo mantiene tutte le decomposizioni finite, comprese quelle con normali parallele.** Non si fondono termini paralleli: senza subadditività di (\psi(\cdot,\nu)), tale fusione non è giustificata.

**Dualità convessa.** La funzione (g_\psi) è positivamente 1-omogenea e convessa (si concatenano decomposizioni); è finita e coerciva per le ipotesi (c|a|\le\psi\le C|a|). In dimensione finita è quindi continua e coincide con il supporto del suo polare:
[
g_\psi(M)=\sup_{A\in\Lambda_\psi}A:M.
]
Infatti (A\in\Lambda_\psi) equivale a (A:M\le g_\psi(M)) per ogni (M), verificando prima sui tensori semplici e poi sulle decomposizioni finite.

**Lower bound della cell formula.** Per ogni (A\in\Lambda_\psi), la disuguaglianza puntuale sui salti dà
[
A:Dw_h\le\psi([w_h],\nu_{w_h})\,\mathcal H^1\!\llcorner J_{w_h}.
]
La coercività controlla le variazioni. Passando al limite distribuzionale su sottoquadrati compatti e poi esaurendo (Q), si ottiene
[
f_{\rm cell}(M)\ge\sup_{A\in\Lambda_\psi}A:M=g_\psi(M).
]

**Upper bound per ogni decomposizione finita.** Fissiamo (M=\sum_{i=1}^N b_i\otimes\nu_i), senza alcuna restrizione di non-parallelismo. Scegliamo fasi (\phi_i\) e poniamo
[
w_h(x)=\sum_{i=1}^N b_i h\left\lfloor\frac{x\cdot\nu_i+\phi_i}{h}\right\rfloor.
]
È una funzione costante su una partizione poligonale finita di (Q), converge uniformemente a (Mx) a meno di una costante additiva, e ciascuna famiglia di rette contribuisce al costo, per unità di area, a (\psi(b_i,\nu_i)). Se alcune normali sono parallele, si scelgono fasi distinte per separare le rette; se rette di famiglie non parallele si intersecano, le intersezioni sono finite e non contribuiscono all'integrale su (J_{w_h}). Pertanto
[
f_{\rm cell}(M)\le\sum_{i=1}^N\psi(b_i,\nu_i).
]
Prendendo l'infimo su tutte le decomposizioni finite,
[
\boxed{\displaystyle
f_{\rm cell}(M)=g_\psi(M)=\sup_{A\in\Lambda_\psi}A:M.}
]
Questa è la funzione di supporto di (\Lambda_\psi), ossia l'inviluppo convesso positivamente 1-omogeneo generato dal costo sui tensori di rango uno. Il risultato riguarda la cella senza dato al bordo; non dimostra la versione con traccia affine prescritta.

**Conseguenze.**
- Per (\psi(a,\nu)=|a|), (\Lambda_\psi=\{A:\|A\|_{op}\le1\}) e (f_{\rm cell}(M)=\|M\|_*).
- Per (\psi(a,\nu)=\Phi(a)k(\nu)), la formula ONB è in generale soltanto un upper bound; il controesempio numerico riportato sotto documenta un candidato gap, non costituisce da solo una prova dell'ottimalità globale della decomposizione non ortogonale.
- Il caso (\psi(a,\nu)=|a|^2) è escluso dall'ipotesi di 1-omogeneità e va trattato separatamente.

**Evidenza numerica ONB.** Lo script `colloquio_morandotti/cell_check2.py` riporta, per (M=[[1,0.3],[0.2,0.9],[0.1,-0.4]]) e (\psi(a,\nu)=|a|(2-|\nu_1|)), ONB (2.5726173) contro una decomposizione a due famiglie non ortogonali (2.5119742) (angolo circa (103.5^\circ)). Questo confuta la pretesa che quella specifica formula ONB sia sempre ottimale, se i dati e la normalizzazione dello script sono quelli indicati; non sostituisce la dimostrazione analitica della cell formula appena data.

## 3. Recovery per gradiente variabile — APERTO

Per (c\in W^{1,1}(Q;\mathbb R^m)), il lower bound isotropo
[
\liminf_h\int_{J_{v_h}}|[v_h]|\,d\mathcal H^1
\ge\int_Q\|\nabla c\|_*\,dx
]
segue dalla dualità e dalla convergenza distribuzionale delle derivate, con localizzazione ed esaurimento del dominio.

**Il recovery upper bound non è dimostrato in questo documento.** La precedente costruzione cella-per-cella produce interfacce artificiali; la stima del loro costo non può essere sostituita dall'affermazione generica che l'ampiezza del salto è (O(\delta^2+h)). La proposta di una fascia di raccordo richiede un lemma autonomo che specifichi partizione, assegnazione dei valori, conteggio delle interfacce e stima dei salti. Fino alla dimostrazione di tale lemma, il risultato
[
\inf_{v_h\to c\ L^1}\liminf_h F(v_h)
=\int_Q\|\nabla c\|_*\,dx
]
è **congettura di recovery / problema aperto qui**, non un teorema chiuso.

Di conseguenza, non si dichiara dimostrata l'applicazione per (\widetilde G(x)) misurabile ottenuta invocando il Lemma R. Restano invece validi i risultati per gradiente costante per faccia, quando il difetto (M_f) è costante e si applica direttamente la costruzione affine.

---
---

## 3. Immersione (rank 2 a.e.)

Per `u_h(ξ) = c₀Aξ + b + v_h(ξ)` con `c₀>0`, `AᵀA=I₂` e `v_h`
piecewise constant (qualsiasi costruzione sopra, costante o variabile
per cella),

```
∇u_h = c₀A   a.e.   ⇒   rank ∇u_h = 2   a.e.
```

Proprietà del gradiente nelle regioni di continuità; non implica
continuità globale, iniettività o embeddedness attraverso i fronti di
salto. Per l'ammissibilità CF basta; per una classe di approssimanti
immersi serve una costruzione continua dedicata — resta aperta.

---

## 4. Stato finale

| Affermazione | Stato |
|---|---|
| Recovery per gradiente costante (M), caso isotropo | **Provato** |
| Cell formula anisotropa senza dato al bordo, con inf su tutte le decomposizioni finite | **Provato** sotto le ipotesi dichiarate |
| Fusione di termini con normali parallele | **Non consentita in generale**; non viene usata |
| Lower bound nucleare per (M(x)) misurabile, (\psi=|a|) | **Provato** |
| Recovery per gradiente variabile (c\in W^{1,1}) | **Aperto**: raccordo non dimostrato |
| Formula ONB anisotropa | **Solo upper bound**; controesempio numerico indicativo |
| Rank 2 a.e. per (\widetilde G=cA), (c>0) | **Provato** come proprietà del gradiente a.e. |
| Embeddedness globale | **Aperta** |
