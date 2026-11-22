# C60 — teorema CF isotropo: identificazione poliedrale finita

Data: 2026-11-21
Classificazione: **dimostrato** nel modello intrinseco dichiarato —
complesso poliedrale finito, `g` affine per faccia, `G̃` costante per
faccia, ammissibili `SBV` senza vincoli di continuità ai lati,
`ψ(a,ν)=|a|`, `W(F)=|F|_F` o `W(F)=|F|_F²` (caso quadratico con
`G̃∈L²`). Non richiede il lemma di localizzazione né la recovery
`W^{1,1}`: la costruzione SVD è esplicita e le tracce si controllano
direttamente.

## 1. Enunciato

Sia `Σ` un complesso poliedrale compatto di facce piane finite. Su
ogni faccia `f`, `g_f(ξ)=A_fξ+b_f` e `G̃|_f=G̃_f` costante. Allora

```
I_W(g,G̃) = Σ_f |f|·W(G̃_f) + Σ_f |f|·‖A_f−G̃_f‖_*
           + ∫_{J_g} |[g]| d𝓗¹ ,
```

con `‖·‖_*` la norma nucleare (somma dei valori singolari) e `J_g`
l'insieme di salto di `g` (inclusi i bordi di faccia dove `g` è
discontinuo).

## 2. Recovery — costruzione SVD esplicita

Su ogni faccia, decomposizione SVD del difetto

```
M_f := A_f − G̃_f = Σ_{i=1}^{r_f} σ_{f,i} a_{f,i}⊗ν_{f,i},  r_f ≤ 2,
|a_{f,i}|=|ν_{f,i}|=1.
```

Definiamo, **senza fasi** (`φ=0`):

```
v_{h,f}(ξ) = G̃_f ξ + b_f
             + Σ_i σ_{f,i} a_{f,i} · h⌊ξ·ν_{f,i}/h⌋ .
```

Poiché `g_f(ξ) = G̃_fξ + b_f + Σ_i σ_{f,i}a_{f,i}(ξ·ν_{f,i})`:

```
‖v_{h,f} − g_f‖_{L^∞(f)} ≤ h Σ_i σ_{f,i} = h‖M_f‖_* ,
```

uniforme su tutta la faccia, **inclusi i lati**. Inoltre
`∇_Σv_{h,f} = G̃_f` quasi ovunque.

**Costo interno.** Le linee di salto della famiglia `i` sono
`{ξ·ν_{f,i}=kh}∩f`. Su ciascuna, salvo le intersezioni con le altre
famiglie (`𝓗¹`-nulle: le normali SVD sono ortogonali, gli incroci
sono punti isolati), il salto ha ampiezza `hσ_{f,i}`. Per la formula
di coarea e la convergenza delle somme di Riemann,

```
h Σ_k 𝓗¹(f ∩ {ξ·ν_{f,i}=kh}) → |f| ,
```

quindi

```
lim_{h↓0} ∫_{J_{v_{h,f}}∩f} |[v_{h,f}]| d𝓗¹
   = Σ_i σ_{f,i}|f| = |f|·‖M_f‖_* .
```

**Tracce sugli spigoli.** Per ogni lato `e⊂∂f` la stessa stima
uniforme dà `‖v_{h,f}−g_f‖_{L^∞(e)} ≤ h‖M_f‖_*`. Per un lato comune
`e=f⁻∩f⁺`, il salto effettivo della funzione globale è
`[v_h]|_e = v_{h,f⁻}|_e − v_{h,f⁺}|_e`, e

```
|[v_h]−[g]|_e ≤ h(‖M_{f⁻}‖_* + ‖M_{f⁺}‖_*)
   ⟹  ∫_e|[v_h]|d𝓗¹ → ∫_e|[g]|d𝓗¹ .
```

Le `v_{h,f}` si incollano in un ammissibile `SBV` su `Σ` (i salti sui
lati sono ammessi, nessun vincolo di continuità). La somma sugli
spigoli (numero finito) e il bulk esatto `Σ_f|f|W(G̃_f)` (il gradiente
coincide con `G̃_f` a.e.) danno `limsup_h E_W(v_h) ≤` formula
candidata.
# C60 — finite polyhedral affine isotropic identification

Date: 2026-11-21

Status: **proved in the intrinsic finite-face SBV model stated below**.

## 1. Setting

Let \(\Sigma\) be a compact finite polyhedral 2-complex. Each face \(f\) is a planar polygon equipped with an orthonormal tangent chart \(\xi\in P_f\subset\mathbb R^2\). The admissible class consists of maps that are \(SBV\) on each face; no continuity or matching-trace constraint is imposed across distinct faces. The global jump cost includes trace jumps on common edges.

On every face assume
\[
g_f(\xi)=A_f\xi+b_f,\qquad
\widetilde G|_f=\widetilde G_f\in\mathbb R^{3\times2}
\]
with \(\widetilde G_f\) constant. Put \(M_f=A_f-\widetilde G_f\). Define
\[
E_W(u)=\int_\Sigma W(\nabla_\Sigma u)\,d\mathcal H^2+
\int_{J_u}|[u]|\,d\mathcal H^1,
\]
and let \(I_W(g,\widetilde G)\) be the infimum of \(\liminf E_W(u_n)\) over determining sequences satisfying \(u_n\to g\) in \(L^1\) and
\[
\nabla_\Sigma u_n\,\mathcal H^2
\stackrel{*}{\rightharpoonup}\widetilde G\,\mathcal H^2.
\]
The measure convergence concerns the absolutely continuous tangential gradients, face by face. The singular derivative includes the macroscopic edge-trace jumps.

## 2. Theorem

For \(\psi(a,\nu)=|a|\) and either \(W(F)=|F|_F\) or \(W(F)=|F|_F^2\),
\[
\boxed{
I_W(g,\widetilde G)=
\sum_f |f|W(\widetilde G_f)
+\sum_f |f|\,\|M_f\|_*
+\int_{J_g}|[g]|\,d\mathcal H^1.
}
\]
Here \(\|\cdot\|_*\) is the nuclear norm of a tangential map \(\mathbb R^2\to\mathbb R^3\). The quadratic case is legitimate because \(\widetilde G\) is piecewise constant on a finite-area complex and thus belongs to \(L^2\).


## 2bis. Estensione a dati piecewise-affine con salti interni — G4b

L'enunciato e la costruzione della §2 valgono senza modifiche per una
partizione poliedrale finita P={T} della superficie, quando

- g|T(x)=A_T x+b_T su ogni cella T, senza imporre continuità
  tra celle adiacenti (i salti su ∂T fanno parte di J_g);
- G̃|T=G_T è costante su ogni cella;
- ogni cella è un poligono limitato e la collezione delle interfacce
  interne è finita.

Su ogni cella si pone M_T=A_T−G_T e si applica la decomposizione
SVD e la costruzione v_{h,T} della §2, con fase zero. Per ogni
x∈T̄, inclusi tutti i lati,

  ||v_{h,T}−g|T||_{L∞(T̄)} ≤ h ||M_T||_*.

Sia e=T⁻∩T⁺ un'interfaccia interna. Le tracce sono definite
lato per lato e non si richiede che coincidano. Pertanto

  ||[v_h]−[g]||_{L¹(e)}
  ≤ h H¹(e)(||M_{T⁻}||_*+||M_{T⁺}||_*).

Sommando sulle interfacce (ognuna contata una sola volta),

  Σ_e ||[v_h]−[g]||_{L¹(e)} ≤ h C(P,g,G̃),

dove C=Σ_e H¹(e)(||M_{T⁻}||_*+||M_{T⁺}||_*)<∞ è indipendente
da h. Ne segue la convergenza in L¹ dei salti su tutte le
interfacce, e quindi la convergenza dei relativi costi ∫_e|[v_h]|
per la continuità della norma in L¹. I salti interni della funzione
macroscopica non vengono né cancellati né contati due volte.

Il numero di celle e interfacce, e dunque C, può dipendere
fortemente dall'indice di densità j. Non si afferma una costante
uniforme in j. Nella diagonale si sceglie invece, per ogni j,
il parametro h_j abbastanza piccolo da imporre h_j C_j≤1/j,
insieme alle usuali condizioni su errore L¹, energia e test della
convergenza debole-*. Questo è sufficiente: la costante è uniforme
rispetto al parametro microscopico h a j fissato, non deve esserlo
rispetto alla raffinazione esterna.

**Conclusione G4b.** La recovery SVD e la convergenza delle tracce
valgono per ogni dato piecewise-affine su una partizione poliedrale
finita, anche con salti interni. La sola uniformità richiesta è
quella in h per ogni partizione fissata, fornita dalla stima
esplicita sopra. ∎


## 3. Lower bound

Per ogni successione determinante, il lemma di liminf del costo di
salto (`C60_CF_SBV_ISOTROPIC_THEOREM_2026-11-21.md` §3.1, provato)
dà

```
liminf_n ∫_{J_{u_n}}|[u_n]| ≥ Σ_f |f|·‖A_f−G̃_f‖_* + ∫_{J_g}|[g]| ,
```

perché `μ = D_Σg − G̃𝓗² = (⊕_f M_f)𝓗² + [g]⊗ν_g𝓗¹⌞J_g` con parti
mutuamente singolari. La semicontinuità del bulk (immediata per
`W=|F|_F`; per `|F|_F²` con `G̃∈L²` e controllo energetico)
completa il lower bound. Uguaglianza dei due limiti. ∎

## 4. Ipotesi e verifica

| Componente | Stato |
|---|---|
| Lower bound isotropo per `g∈SBV` | **Dimostrato** (lemma §3.1) |
| Recovery SVD per `M_f` costante, convergenza uniforme | **Dimostrata** (formula esplicita, `φ=0`) |
| Convergenza delle tracce sui lati | **Dimostrata** dalla stima `L^∞ ≤ h‖M‖_*` |
| Costo interno → `|f|‖M_f‖_*` | **Dimostrato** (coarea + somme di Riemann) |
| Costo sui lati → `∫_{J_g}|[g]|` | **Dimostrato** (stima uniforme finita) |
| Identificazione dell'infimo poliedrale | **Dimostrata** (lower = upper) |
| Recovery per `M(x)` variabile, `g∈SBV` generale | **Aperto** — problema distinto |
| Superfici curve | **Aperto** — richiede controllo delle carte |
| `ψ` anisotropo, `|a|²` | **Aperto** — cambiano cell formula e splitting |

**Nota sulla fase.** La versione con fasi `φ_{f,i}` richiede la
compensazione esplicita `−φ_{f,i}` dentro la parentesi quadra (o la
costante `−p_f` fuori); senza di essa resta un termine costante non
nullo. La scelta `φ=0` la evita del tutto ed è preferibile.

## 5. Cosa resta

- `M(x)` variabile su una faccia: richiede la recovery `W^{1,1}`
  (prova candidata) **più** il controllo delle tracce al bordo —
  la stima `L^∞` uniforme non è più disponibile cella per cella.
- `g ∈ SBV` generale (non affine): approssimazione energetica.
- Anisotropo: la cell formula `g_ψ` è provata senza vincolo di
  bordo, ma eredita gli stessi gap di tracce per `M` variabile.
- C60 con `M=0`: già coperto (`u_n=g`); questo teorema estende a
  `M_f≠0` costante per faccia.
Take a determining sequence with finite liminf energy and pass to a subsequence realizing that liminf. The bulk bound controls the absolutely continuous gradient measures: in the linear case by the \(L^1\) bulk bound, and in the quadratic case by the \(L^2\) bound and finite area. The jump term gives
\[
|D^s_\Sigma u_n|_*(\Sigma)
=\int_{J_{u_n}}|[u_n]\otimes\nu_{u_n}|_*\,d\mathcal H^1
=\int_{J_{u_n}}|[u_n]|\,d\mathcal H^1.
\]
Since \(u_n\to g\) in \(L^1\), the distributional derivatives converge distributionally. Subtracting the prescribed convergence of the absolutely continuous parts yields
\[
D^s_\Sigma u_n\stackrel{*}{\rightharpoonup}
D_\Sigma g-\widetilde G\,\mathcal H^2.
\]
On face interiors this limit has density \(M_f\); on the macroscopic jump set it has density \([g]\otimes\nu_g\). These components are mutually singular. Lower semicontinuity of total variation with the nuclear norm gives
\[
\liminf_n\int_{J_{u_n}}|[u_n]|\,d\mathcal H^1
\geq\sum_f|f|\,\|M_f\|_*+
\int_{J_g}|[g]|\,d\mathcal H^1.
\]
For \(W(F)=|F|_F\), weak-* lower semicontinuity of the measure norm gives the bulk lower bound. For \(W(F)=|F|_F^2\), boundedness in \(L^2\) gives a weakly convergent subsequence; its limit is \(\widetilde G\), identified by the prescribed measure convergence. Weak lower semicontinuity of the squared \(L^2\) norm gives
\[
\liminf_n\int_\Sigma W(\nabla_\Sigma u_n)\,d\mathcal H^2
\geq\sum_f|f|W(\widetilde G_f).
\]
Both estimates are applied on the same subsequence realizing the liminf of the total energy. This proves the lower bound.

## 4. Facewise SVD recovery

Fix a face \(f\). Choose a singular-value decomposition
\[
M_f=\sum_{i=1}^{r_f}\sigma_{f,i}a_{f,i}\otimes\nu_{f,i},
\qquad r_f\leq2,
\]
where \(\sigma_{f,i}>0\), \(|a_{f,i}|=|\nu_{f,i}|=1\), and the right singular vectors \(\nu_{f,i}\) are orthonormal. Define
\[
v_{h,f}(\xi)=\widetilde G_f\xi+b_f+
\sum_{i=1}^{r_f}\sigma_{f,i}a_{f,i}\,
h\left\lfloor\frac{\xi\cdot\nu_{f,i}}h\right\rfloor.
\]
Since
\[
g_f(\xi)=\widetilde G_f\xi+b_f+
\sum_i\sigma_{f,i}a_{f,i}(\xi\cdot\nu_{f,i}),
\]
we have the exact remainder identity
\[
v_{h,f}(\xi)-g_f(\xi)=
\sum_i\sigma_{f,i}a_{f,i}
\left(h\left\lfloor\frac{\xi\cdot\nu_{f,i}}h\right\rfloor
-\xi\cdot\nu_{f,i}\right),
\]
and hence
\[
\|v_{h,f}-g_f\|_{L^\infty(\overline f)}
\leq h\sum_i\sigma_{f,i}=h\|M_f\|_*.
\]
Thus convergence is uniform on the closed face and every side. Away from stripe interfaces the quantizers are locally constant, so \(\nabla_\Sigma v_{h,f}=\widetilde G_f\) almost everywhere.

For family \(i\), the jump sections are \(f\cap\{\xi\cdot\nu_{f,i}=kh\}\), and the jump amplitude is \(h\sigma_{f,i}a_{f,i}\). When \(r_f=2\), the right singular vectors are orthogonal; distinct families therefore intersect only at isolated points. Such intersections have \(\mathcal H^1\)-measure zero, so there is no positive-length overlap or double counting of jump cost. The section-length function
\[
L_{f,i}(t)=\mathcal H^1(f\cap\{\xi\cdot\nu_{f,i}=t\})
\]
is compactly supported and piecewise affine for a polygon. Its Riemann sums converge to its integral. By coarea,
\[
h\sum_{k\in\mathbb Z}L_{f,i}(kh)
\longrightarrow\int_{\mathbb R}L_{f,i}(t)\,dt=|f|.
\]
Consequently,
\[
\lim_{h\downarrow0}
\int_{J_{v_{h,f}}\cap f}|[v_{h,f}]|\,d\mathcal H^1
=|f|\sum_i\sigma_{f,i}=|f|\,\|M_f\|_*.
\]

## 5. Gluing faces and edge traces

Define \(v_h\) facewise by \(v_h|_f=v_{h,f}\). This is admissible in the stated intrinsic class; no continuity across edges is required. For every side \(e\subset\partial f\),
\[
\|v_{h,f}-g_f\|_{L^\infty(e)}\leq h\|M_f\|_*.
\]
For a common edge \(e=f^-\cap f^+\),
\[
\|[v_h]-[g]\|_{L^\infty(e)}
\leq h(\|M_{f^-}\|_*+\|M_{f^+}\|_*).
\]
Using \(\bigl||a|-|b|\bigr|\leq|a-b|\), we obtain
\[
\int_e|[v_h]|\,d\mathcal H^1
\longrightarrow\int_e|[g]|\,d\mathcal H^1.
\]
There are finitely many faces and edges, so these limits may be summed. The bulk term is exactly
\[
\int_\Sigma W(\nabla_\Sigma v_h)\,d\mathcal H^2
=\sum_f|f|W(\widetilde G_f).
\]
The construction gives \(v_h\to g\) uniformly facewise and the prescribed absolutely continuous gradient measure exactly. Combining the laminate costs in face interiors with the limiting macroscopic edge costs proves the upper bound and hence the theorem.

## 6. Scope

The result is restricted to a finite polyhedral complex, facewise affine \(g\), facewise constant \(\widetilde G\), the intrinsic facewise SBV class without edge continuity constraints, and the linear isotropic jump density \(|a|\).

It does not establish recovery for arbitrary \(g\in SBV\), variable \(M(x)\), general curved surfaces, or anisotropic/non-1-homogeneous jump densities. No boundary-strip localization lemma, continuous \(W^{1,1}\) recovery, or forced continuity across faces is used.

## Internal dependencies

- C60_CF_SBV_ISOTROPIC_THEOREM_2026-11-21.md — general isotropic lower-bound lemma.
- C60_CF_NUCLEAR_NORM_CELL_PROBLEM_2026-11-21.md — nuclear-norm cell cost and SVD laminate.
- C60_CF_NONZERO_BULK_DISARRANGEMENT_2026-11-21.md — facewise determining sequence for nonzero facewise bulk disarrangement.
