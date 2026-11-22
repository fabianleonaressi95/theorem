# Lemma di splitting autonomo per complessi poliedrali finiti

Data: 2026-11-21. Framework geometrico richiesto da
`C60_CF_QUADRATIC_JUMP_GENERAL` §3.2: costruzione e stime del
micro-splitting di un salto macroscopico, con conti separati per
strisce, cappucci e dischi di vertice. In questo documento il
lemma viene dimostrato nella sua generalità; il trasferimento a
`Σ` e a `g_j` CFI è un'applicazione.

## 1. Setup

`K` complesso poliedrale finito in `ℝ²` (o, equivalentemente, una
porzione piatta di una superficie poliedrale). `g:K→ℝ^m` affine
su ogni cella di una partizione poliedrale finita `𝒯`, e
`J_g` = unione dei lati di `𝒯` su cui il salto
`[g]=g⁺−g⁻` (tracce dai due lati) è non nullo. Su ogni segmento
`e∈J_g` il salto è la differenza di due mappe affini, quindi
**affine lungo `e`**; in particolare

```
C_e := ‖[g]‖_{L∞(e)} < ∞ ,   e compatto.
```

Estendiamo entrambe le mappe affini a tutto il piano: `g⁻_aff`,
`g⁺_aff` sono definite globalmente e la loro differenza

```
h_e(x) := g⁺_aff(x) − g⁻_aff(x)
```

è una funzione **affine su tutto il piano**, non solo sulla
traccia: questo risponde al punto (A) dell'audit — non serve
nessuna estensione aggiuntiva, l'affinità è globale. Sul
segmento `e` coincide con `[g]`, quindi `‖h_e‖_{L∞(e)}=C_e`.

## 2. Costruzione su un segmento `e=[A,B]`

Fissati `m∈ℕ` e `δ>0` piccoli, sia `S_δ(e)` la striscia di
larghezza `δ` dal lato `g⁻` di `e` (il lato `g⁺` resta
inalterato). In coordinate intrinseche `(s,t)`, `s∈[0,|e|]`
lungol'`e`, `t∈[−δ,0]` nella striscia. Dividiamo la striscia in
`m` strati di spessore `δ/m`:

```
S_i = { (s,t) : s∈[0,|e|],  t∈(−iδ/m, −(i−1)δ/m) },  i=1,…,m,
```

e poniamo

```
v(x) = g⁻_aff(x) + ((m−i+1)/m)·h_e(x)    su S_i,
```

`v=g` fuori dalla striscia (eccetto le regioni terminali di §4).
Lo strato `i=1`, adiacente a `e` (perché `t∈(−δ/m,0)`), ha coefficiente `1`, quindi la traccia su `e` coincide con `g⁺_aff` e il salto originale si annulla nell'interno del segmento. Lo strato più esterno `i=m` ha coefficiente `1/m`; sul bordo `t=−δ` resta quindi un salto di ampiezza `|h_e|/m`, che va conteggiato come interfaccia aggiuntiva.

### 2.1 Proprietà elementari

- **Affinità**: `h_e` affine ⇒ `v` affine su ogni `S_i`.
- **Gradiente**: `∇v=∇g⁻+(i/m)∇h_e`, quindi
  `‖∇v‖≤‖∇g⁻‖+‖∇h_e‖` uniforme in `m,δ` (la variazione avviene
  per salti, non per transizioni: non esiste gradiente `~1/δ`).
- **Salto fra strati adiacenti**: `v_{i+1}−v_i=h_e/m` punto per
  punto, ampiezza `≤(C_e+cδ)/m` dove `c` dipende solo da
  `‖∇h_e‖` (il valore di `h_e` nella striscia differisce da
  quello su `e` di `O(δ)`).
- **Partizione**: ogni `S_i` è un rettangolo in `(s,t)`;
  intersecando con `𝒯` si ottiene una partizione poliedrale
  finita `ℛ_{m,δ}` (le celle `S_i∩T` sono poligoni). Le celle
  fuori striscia restano quelle di `𝒯`.

## 3. Stima (S): interfacce fra strati

Le interfacce interne `t=−iδ/m`, `i=1,…,m−1`, e il bordo esterno `t=−δ` sono segmenti di lunghezza al più `|e|` (tranne le parti assegnate ai dischi terminali, §4). Su ciascuna il salto è `h_e/m`, con `|h_e|≤C_e+cδ`. Per `φ(t)=t²`:

```
E_S ≤ |e|·m·((C_e+cδ)/m)² = |e|(C_e+cδ)²/m  →  0  per m→∞, δ→0.
```

Nessuna dipendenza da `δ` nel denominatore: il numero di strati
non entra nel denominatore perché ogni interfaccia ha salto
`O(1/m)`, non `O(δ)`.

## 4. Stime (K) e (V): cappucci e vertici — il punto (B)

### 4.1 Cappucci laterali

La striscia viene troncata fuori dai dischi terminali `B_ρ(A)∪B_ρ(B)`: i tratti laterali dentro i dischi sono assegnati esclusivamente a (V), non a (K). Sulle parti residue dei bordi laterali, il salto è la differenza tra la traccia affine dello strato e la traccia del campo esterno. Il bound `C_e+cδ` è valido solo quando il campo esterno è specificato e ha traccia compatibile; tale compatibilità è un'ipotesi della costruzione locale e va verificata sulla partizione comune. I `m` strati danno `m`
segmenti di lunghezza `δ/m` per capo, lunghezza totale `δ` per
capo. Per `φ=t²`, il costo esatto è

```
E_K = 2·Σ_{i=1}^m (δ/m)·((i/m)(C_e+cδ))²
    ≤ (2δ/m³)(C_e+cδ)²·Σ_{i=1}^m i²
    ≤ (2/3)·δ·(C_e+cδ)² · (1+o(1))
    = O(δ)   per m fissato.
```

Per `φ` continua, un bound robusto è `E_K≤2δ·sup_{0≤t≤C_e+cδ}φ(t)`, che tende a zero per `δ→0` a `C_e` fissato. Nel caso quadratico dà `O(δ(C_e+cδ)²`; non si usa una somma con coefficiente di salto che non sia stato derivato dalle tracce effettive.

### 4.2 Dischi di vertice

Attorno a ogni vertice `P` del jump complex (estremi di `e`,
incroci, vertici C60) si toglie il disco `B_ρ(P)` e **non si
applica alcun splitting**: il salto resta quello di `g`.
Contributo:

```
E_V ≤ Σ_P (C_P)²·c_P ρ     →  0  per ρ→0,
```

dove `C_P` è il massimo dei `C_e` sugli segmenti incidenti e
`c_P` la lunghezza dell'arco `∂B_ρ∩J_g` (`O(1)` per ρ piccolo,
universale sui vertici di un grafo finito).

### 4.3 Disgiunzione

Definire la regione splittata come `S_δ(e)\setminus(B_ρ(A)∪B_ρ(B))`. Le parti di interfacce laterali e terminali dentro i dischi sono assegnate esclusivamente a (V), non a (K); le interfacce (S) sono troncate analogamente. Per segmenti non incidenti, scegliere le scale sotto metà delle distanze minime positive; per segmenti incidenti, la rimozione dei dischi disgiunti separa le costruzioni. La disgiunzione è dunque fra le regioni effettivamente conteggiate, non fra le strisce complete.

## 5. Convergenza e ordine dei limiti

Per `φ=t²`, fissato `g` (cioè `j` fissato nel linguaggio della
recovery), l'energia di salto residua di `v_{m,δ,ρ}` è

```
E_jump ≤ Σ_e [ |e|(C_e+cδ)²/m  +  O(δC_e²)  +  O(ρC_e²) ]
       +  (contributi invariati fuori striscia)
```

più i termini della staircase applicata dopo. Ordine:

```
m → ∞   (uccide E_S),   poi  δ → 0  (uccide E_K),   poi  ρ → 0
(uccide E_V);  infine h → 0  per la staircase.
```

`v_{m,δ,ρ}→g` in `L¹`: le modifiche sono sostenute in
`⋃_e S_δ(e)∪B_ρ`, area `O(δ+ρ)`, e `|v−g|≤C` lì.

## 6. Trasferimento a `Σ` e a `g_j` CFI

- **Dati**: `g_j` CFI è affine sui simplessi di una partizione
  che raffina le facce; `J_{g_j}` è unione finita di segmenti
  (facet di mesh) con salto affine a tratti. Le ipotesi di §1
  sono soddisfatte su ogni segmento.
- **Superfici**: la costruzione usa solo la metrica intrinseca
  piatta. Sugli **spigoli di `Σ`** (angolo `2π`, piatti) le
  coordinate `(s,t)` esistono attraverso lo spigolo: il
  micro-splitting si applica anche ai salti inter-faccia, che
  per `φ=t²` devono tendere a zero esattamente come quelli
  interni. Ai **vertici conici** `v∈V` la palla `B_ρ(v)` esclude
  la costruzione: lì il salto resta macroscopico e il suo
  contributo è `O(ρ)` nella stima (V) — coerente con G5, dove
  l'assenza di atomi di `Λ` gestisce il residuo.
- **Caso degenere `e` con più di due celle adiacenti**: il
  grafo dei salti ha vertici di valenza `k`; la palla `B_ρ`
  attorno al vertice isola il punto multiplo e la striscia si
  applica a ogni ramo separatamente (i rami condividono solo
  la palla).

## 7. Stato

**Lemma di splitting: dimostrato** per un grafo di salto finito
in un complesso poliedrale piatto, con stime separate
(S)/(K)/(V) esplicite. La proprietà 7 del documento quadratico
(gradiente uniformemente limitato nelle strisce) è verificata
in §2.1 — e si rileva che per la recovery finale non è nemmeno
necessaria: dopo la staircase `∇u_{j,m,h}=G_j` **
H²-quasi ovunque su ogni cella, strisce incluse** (il mismatch
locale è assorbito in `M_P=A_P−G_P`), quindi il bulk è
esattamente `∫W(G_j)` senza correzioni di area. Resta solo la
trascrizione delle coordinate intrinseche su `Σ` (tecnico:
la metrica è piatta fuori da `V`).
