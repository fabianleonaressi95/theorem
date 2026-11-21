# C60 — rilassamento banale per densità di salto superlineare: `ψ=|a|²` e generalizzazioni

Data: 2026-11-21. Dimostra l'estensione del teorema quadratico
(`C60_CF_QUADRATIC_JUMP_RELAXATION_2026-11-21.md`, che copriva solo
la coppia C60 con `M=0`) a `g∈SBV(Σ)` e `G∈L^p` generali,
`M=∇g−G` arbitrario. Include la generalizzazione a
`ψ(a,ν)=φ(|a|)` con `φ(t)/t→0` per `t→0`.

## 1. Enunciato

Sia `Σ` la superficie poliedrale (o un dominio piano — la prova è
la stessa). `g∈SBV(Σ;ℝ^m)`, `∇g∈L^p`, `∫_{J_g}|[g]|²<∞`;
`G∈L^p(Σ;Hom(TΣ,ℝ^m))`, `p=1` per `W=|·|_F`, `p=2` per
`W=|·|_F²`. Funzionale:

```
E(u) = ∫_Σ W(∇_Σu) d𝓗² + ∫_{J_u} |[u]|² d𝓗¹ .
```

**Teorema.** `I(g,G) := inf liminf E(u_n) = ∫_Σ W(G) d𝓗²`
sulle successioni determinanti (`u_n→g` in `L¹`,
`∇u_n𝓗²⇀*G𝓗²`).

**Idea**: la densità quadratica permette di micro-suddividere
*ogni* salto — quelli macroscopici di `g` e quelli della
staircase di mismatch — fino a costo nullo. Il funzionale
rilassato contiene **solo** il bulk.

## 2. Limite inferiore

`u_n→g` in `L¹`, `∇u_n𝓗²⇀*G𝓗²`, `sup_n E(u_n)<∞`.

- **Bulk**: per `W=|F|_F`, la convessità positivamente
  omogenea di grado 1 e la convergenza debole-* delle misure
  danno `liminf∫|∇u_n|≥∫|G|` (Reshetnyak). Per `W=|F|_F²`, il
  bound energetico dà `∇u_n` limitato in `L²`, quindi
  `∇u_n⇀G` debolmente in `L²` e la convessità di `|·|²` dà
  `liminf∫|∇u_n|²≥∫|G|²`.
- **Salto**: `∫_{J_{u_n}}|[u_n]|²≥0`.

Quindi `liminf E(u_n) ≥ ∫W(G)`. Nessuna ipotesi aggiuntiva.

## 3. Recovery — costruzione a tre parametri

Parametri: `j` (densità CFI di `g`), `m` (micro-splitting dei
salti), `h` (passo staircase). Scelta diagonale finale.

### 3.1 Approssimazione di `g` — `g_j`

CFI (Teorema 1.1 + Cor. 2.3) su ogni faccia: `g_j` affine per
simplesso, `g_j→g` in `L¹`, `∇g_j→∇g` in `L^p`,
`∫_{J_{g_j}}|[g_j]|²→∫_{J_g}|[g]|²` (la convergenza di salto non
serve per il risultato finale — i salti verranno distrutti — ma
non fa male). `G_j|_T=⨍_T G` sulle stesse celle (G3): `G_j→G`
in `L^p`.

### 3.2 Micro-splitting — `g_j^{(m)}`

Su ogni segmento `e` di `J_{g_j}` (interfaccia di simplessi con
salto non nullo, interno a una faccia o su uno spigolo `Γ`) il
dato di salto è `h_e(s)=[g_j](s)` (affine a tratti in `s`).
Come in §2 del documento quadratico: striscia di larghezza
`δ_m` nel lato adiacente, `m` strati paralleli, nell'`i`-esimo
`g_j^{(m)}=g_j^-+(i/m)h_e`. Risultato:

- `g_j^{(m)}→g_j` in `L¹` (modifiche in area `O(δ_m)`);
- `∇g_j^{(m)}→∇g_j` in `L^p` (gradiente modificato
  `∇g_j+(i/m)∇h_e` uniformemente limitato su area `→0`);
- **ogni salto di `g_j^{(m)}` ha ampiezza `≤C_e/m`**, dove
  `C_e=max_e|h_e|`;
- nuovo bordo: segmenti terminali di lunghezza `O(r_m)` con
  salto macroscopico residuo (scegliere `r_m→0`).

Il numero di strati `m` è finito per `(j,e)`; la partizione
resta poliedrale finita.

### 3.3 Staircase di mismatch — `u_{j,m,h}`

Su ogni cella `P` della partizione di `g_j^{(m)}` (su cui
`g_j^{(m)}` è affine e `G_j` è costante): `M_P=A_P−G_j|_P`
costante, SVD `M_P=Σ_iσ_i a_i⊗ν_i`, e

```
u_{j,m,h}|_P = G_j|_P ξ + b_P + Σ_i σ_i a_i h⌊ξ·ν_i/h⌋ .
```

Proprietà (teorema poliedrale, esteso a piecewise-affine —
G4b): `∇u=G_j` a.e., `‖u−g_j^{(m)}‖∞≤h·max_P‖M_P‖_*`,
`u_{j,m,h}→g_j^{(m)}` in `L¹` per `h→0`.

### 3.4 Stima del costo di salto — tutti i contributi

Sia `J_{j,m,h}` il jump set di `u_{j,m,h}`. Contributi:

**(a) Micro-salti del splitting** (interfacce tra strati,
`m` per segmento `e`): ampiezza `≤C_e/m`, lunghezza `≤|e|`.
Costo per `e`:

```
≤ m · |e| · (C_e/m)² = C_e²|e|/m  →0  per m→∞ (j fisso).
```

I segmenti terminali `O(r_m)` portano salto `≤C_e`:
costo `≤C_e²·O(r_m)→0`.

**(b) Salti laminato SVD** (linee `{ξ·ν_i=kh}` dentro ogni cella
`P`): ampiezza `hσ_i`, lunghezza totale `~|P|·c_i/h`. Costo:

```
Σ_P Σ_i h²σ_i² · c_i|P|/h = h·Σ_P c_i|P|‖M_P‖_*² →0 per h→0,
```

uniforme per `(j,m)` fisso perché `max_P‖M_P‖<∞` (partizione
finita).

**(c) Salti residui sulle interfacce di cella**: tracce
convergono uniformemente (`≤h‖M‖` per lato), quindi il salto
effettivo `→[g_j^{(m)}]` che ha ampiezza `≤C_e/m` sulle interfacce
di splitting e `=0` sulle interfacce continue. Costo:

```
≤ Σ_e |e|·(C_e/m + 2h max‖M‖)²  →0 per m→∞, poi h→0.
```

**(d) Contributi ai vertici**: nessuno speciale — le stime (a)–(c)
sono per cella e la partizione è finita; i 60 vertici sono
`𝓗¹`-nulli e non creano salti aggiuntivi (i bordi si contano
una volta sola, come in G4).

### 3.5 Convergenze

- `u_{j,m,h}→g` in `L¹`: `g_j^{(m)}→g` e
  `‖u−g_j^{(m)}‖∞≤h‖M‖→0` per la diagonale.
- `∇u_{j,m,h}=G_j` a.e. fuori dagli archi di splitting dove
  `∇=G_j+(i/m)∇h_e` uniformemente limitato su area `O(δ_m)`:
  `∇u𝓗²⇀*G𝓗²` perché `G_j→G` in `L^p` ⇒ in variazione totale.
- **Bulk**: `∫W(∇u)=∫W(G_j)` esatto a.e. + correzione strip
  `O(δ_m)·sup|W|` → per `W=|F|²` il gradiente negli strati è
  uniformemente limitato (`≤C_j` per `(j,m)` fisso), quindi
  l'errore bulk →0 per `δ_m→0`; per `W=|F|` idem.
  `∫W(G_j)→∫W(G)` per convergenza forte `L^p` + crescita.
- **Salto**: §§3.4(a)–(c) →0 per la diagonale
  `(j→∞, m(j)→∞, h(j,m)→0)` con `m(j)h(j)‖M‖→0` e
  `r_m,δ_m→0`.

### 3.6 Diagonale

Scelta: per ogni `j`, `m=m(j)` tale che i costi (a),(c) `<1/j`;
poi `h=h(j,m(j))` tale che (b) e la convergenza `L¹`/`⇀*`
`<1/j`. Il bound `C_j` dipende da `j` ma non serve uniformità:
`h(j,m)·C_{j,m}≤1/j` è sempre realizzabile. ∎

## 4. Generalizzazione: `ψ(a,ν)=φ(|a|)`, `φ(t)/t→0` per `t→0`

**Ipotesi su `φ`**: continua, `φ(0)=0`, `φ(t)/t→0` per `t→0`.
(Per la semicontinuità inferiore del termine salto serve solo
`φ≥0`; il bulk come sopra. La crescenza di `φ` non è richiesta
per il lower bound poiché il termine è `≥0`.)

Le stesse tre stime diventano:

- **(a)** `m` micro-salti di ampiezza `≤C_e/m`:
  `m·φ(C_e/m)·|e| = C_e|e|·φ(C_e/m)/(C_e/m) →0`,
  perché `φ(t)/t→0` per `t→0`.
- **(b)** linee laminato ampiezza `hσ_i`: per la formula di
  coarea la lunghezza totale delle linee `{ξ·ν_i=kh}` in `P` è
  `~|P|/h`; costo per cella e direzione
  `≈ φ(hσ_i)·|P|/h`. Poiché `hσ_i→0` per `h→0` (`σ_i` fissato
  per cella, `max_P‖M_P‖<∞`) e `φ(t)/t→0`:
  `φ(hσ_i)/h = σ_i·φ(hσ_i)/(hσ_i) →0`, uniformemente in `i,P`
  perché `h·max_P‖M_P‖→0`.
- **(c)** interfacce: ampiezza `≤C_e/m+O(h)`:
  `Σ|e|·φ(C_e/m+Ch)→0` per `φ` continua con `φ(0)=0` e
  `m→∞,h→0`.

Quindi `I(g,G)=∫W(G)` per ogni `φ` superlineare-in-0. ∎

**Nota**: `φ(t)=t` (il caso isotropo) darebbe `m·(C_e/m)=C_e`
=cost — il meccanismo fallisce esattamente al limite lineare,
coerente col risultato `‖M‖_*+|[g]|` non nullo.

## 5. Portata e caveat

- La prova non usa il lemma delle misure energetiche di §5.4:
  per `|a|²` il costo di salto →0 globalmente, quindi non serve
  controllo locale ai vertici — i contributi (a)–(c) sono finiti
  e globali. **G5 non è necessario per questo teorema.**
- Serve comunque la convergenza determinante: `∇u⇀*G` —
  ereditata dalla costruzione (G_j→G in variazione totale).
- Per `W=|F|²` serve `G∈L²` e il bound `∇u∈L²` uniforme:
  la costruzione dà `∇u=G_j` a.e. + strati uniformemente
  limitati per `(j,m)` fisso — ok nella diagonale.
- La generalizzazione `φ(t)/t→0` è **teorema con schema
  completo**; la verifica riga-per-riga delle stime (b)–(c)
  con costanti esplicite resta da incorporare — i conti sono
  quelli sopra, nessun nuovo ingrediente.
- Anisotropo `Φ(a)k(ν)` con `Φ^q`, `q>1`: stesso argomento con
  `Φ` al posto di `|·|` — ma richiede `k` separabile e la
  condizione `Φ(t·)/t→0`... `Φ(a)^q/t→0` in `a` — verificare.
