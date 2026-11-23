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
- **Gradiente**: `∇v=∇g⁻+((m−i+1)/m)∇h_e`, quindi
  `‖∇v‖≤‖∇g⁻‖+‖∇h_e‖` uniforme in `m,δ` (la variazione avviene
  per salti, non per transizioni: non esiste gradiente `~1/δ`).
- **Salto fra strati adiacenti**: `v_{i+1}−v_i=−h_e/m` punto per
  punto, ampiezza `≤(C_e+cδ)/m` dove `c` dipende solo da
  `‖∇h_e‖` (il valore di `h_e` nella striscia differisce da
  quello su `e` di `O(δ)`).
- **Partizione**: ogni `S_i` è un rettangolo in `(s,t)`;
  intersecando con `𝒯` si ottiene una partizione poliedrale
  finita `ℛ_{m,δ}` (le celle `S_i∩T` sono poligoni). Le celle
  fuori striscia restano quelle di `𝒯`.

## 3. Stima (S): interfacce fra strati

Le interfacce interne \(t=-i\delta/m\), \(i=1,\ldots,m-1\), e il bordo esterno \(t=-\delta\) sono contate una sola volta. Su ciascuna il salto è esattamente \(h_e/m\), a meno della restrizione al tratto non rimosso dai cappucci terminali. Poiché \(|h_e|\le C_e+c\delta\) nella striscia e ogni tratto ha lunghezza al più \(|e|\), per \(\phi(t)=t^2\)
\[
E_S\le |e|\,m\left(\frac{C_e+c\delta}{m}\right)^2
=\frac{|e|(C_e+c\delta)^2}{m}.
\]
Quindi \(E_S\to0\) per \(m\to\infty\), a \(\delta\) fissato e poi lungo la scelta dei parametri.

## 4. Terminali, cappucci e vertici: geometria da specificare

### 4.1 Due geometrie possibili — non intercambiabili

La frase «striscia troncata fuori dai dischi terminali» deve essere resa operativa. Si distinguono due scelte.

**Scelta A — rimozione completa dei cappucci dentro i dischi.** Si definisce la regione modificata
\[
D_e:=S_\delta(e)\setminus\bigl(B_\rho(A)\cup B_\rho(B)\bigr)
\]
e si pone \(v=g\) fuori da \(D_e\). Se \(\delta<\rho\), i lati corti \(s=0\) e \(s=|e|\) della striscia completa sono interamente contenuti nei dischi: non esistono quindi tratti laterali residui da sommare come \(K\). La frontiera artificiale della regione modificata è invece costituita dagli archi (o dai lati di un'approssimazione poligonale) di \(\partial B_\rho(A)\cup\partial B_\rho(B)\) che intersecano \(D_e\). Questi tratti devono essere assegnati a \(V\) e stimati usando le **tracce effettive** di \(v\) e \(g\).

Per un complesso finito e dati affine-per-cella, esiste una costante locale \(M_P<\infty\), massimo delle differenze delle estensioni affini coinvolte sui compatti considerati, tale che il costo sui bordi artificiali è limitato da
\[
E_{\partial V}\le C\,\rho\,M_P^2.
\]
Il contributo del salto originale rimasto dentro i dischi soddisfa analogamente
\[
E_{J_g\cap\cup_P B_\rho(P)}
\le C\,\rho\,\max_e C_e^2,
\]
perché il jump complex è finito e ogni ramo ha lunghezza \(O(\rho)\). Le costanti dipendono dal complesso e dai dati affine-per-cella; non sono, in generale, controllate dal solo \(C_e\) del singolo lato.

**Scelta B — cappucci laterali esterni ai dischi.** Se la costruzione conserva una parte dei lati corti fuori dai dischi, quei segmenti costituiscono un termine \(K\) separato. Su un tratto del lato \(s=0\) o \(s=|e|\) nello strato \(i\), il salto va calcolato come differenza tra la traccia effettiva interna
\[
g^-_{\rm aff}+\frac{m-i+1}{m}h_e
\]
e la traccia effettiva del campo esterno \(g_{\rm ext}\). Non è lecito sostituire questa differenza con \((i/m)h_e\), né dedurre il bound \(C_e+c\delta\) senza un'ipotesi/ verifica sulla traccia \(g_{\rm ext}\). Se tale verifica dà un bound \(M_{e,i}\), il conto corretto è
\[
E_K\le 2\sum_{i=1}^m \frac{\delta}{m}M_{e,i}^2
\]
(per due lati completi; per tratti troncati si usano le loro lunghezze effettive). Nel caso particolare in cui \(g_{\rm ext}=g^-_{\rm aff}\) lungo il lato, si può porre \(M_{e,i}\le ((m-i+1)/m)(C_e+c\delta)\); solo allora segue
\[
E_K\le 2\frac{\delta}{m}(C_e+c\delta)^2
\sum_{i=1}^m\left(\frac{m-i+1}{m}\right)^2
\le 2\delta(C_e+c\delta)^2.
\]
La stima è \(O(\delta)\), ma dipende dalla compatibilità delle tracce effettive.

Le scelte A e B sono alternative. Non si può assegnare lo stesso tratto sia a \(K\) sia a \(V\), né usare la stima di \(K\) sui lati già rimossi dentro i dischi.

### 4.2 Vertici e giunzioni

Attorno a ogni vertice del jump complex si sceglie una regione terminale \(Q_\rho(P)\), preferibilmente poligonale se si vuole una partizione poligonale esatta, con
\[
B_{c\rho}(P)\subset Q_\rho(P)\subset B_{C\rho}(P).
\]
Dentro \(Q_\rho(P)\) non si applica lo splitting e si pone \(v=g\). Il salto originale sui rami contenuti in \(Q_\rho(P)\) ha costo \(O(\rho)\). Sulla frontiera \(\partial Q_\rho(P)\), dove il campo modificato incontra \(g\), si stima invece il salto artificiale effettivo; la sua ampiezza è limitata da una costante locale \(M_P\) solo dopo aver elencato le celle affini che forniscono le due tracce. Poiché \(\mathcal H^1(\partial Q_\rho(P))=O(\rho)\), il costo è \(O(\rho M_P^2)\).

### 4.3 Condizioni di disgiunzione

Prima di sommare i contributi, suddividere \(J_g\) in segmenti massimali sui quali la coppia di celle affine e il salto \(h_e\) sono fissati; includere come vertici tutti gli estremi, gli incroci e i punti di cambio della coppia di tracce. Per un complesso finito, dopo questa suddivisione si possono scegliere regioni terminali disgiunte e \(\delta/\rho\) abbastanza piccolo da rendere disgiunte le strisce dei rami incidenti fuori dalle regioni terminali. La scelta deve dipendere anche dalla minima separazione angolare positiva tra i rami incidenti, non soltanto dalle distanze tra segmenti non incidenti. Segmenti collineari sovrapposti vanno prima fusi o suddivisi in modo da non creare doppie assegnazioni.

La partizione finale deve assegnare ogni tratto di salto effettivo una sola volta:
- interfacce fra strati e bordo esterno della striscia: \(S\);
- eventuali lati corti effettivamente conservati fuori dalle regioni terminali: \(K\);
- salti originali dentro le regioni terminali e frontiere artificiali tra \(v\) e \(g\): \(V\).

Per una partizione poligonale comune, le regioni terminali circolari vanno sostituite da poligoni con diametro e perimetro \(O(\rho)\), oppure la loro frontiera curva va trattata separatamente.

## 5. Convergenza e ordine dei limiti

Per \(\phi(t)=t^2\), la sola stima già derivata senza ipotesi ulteriori è il contributo interno \(S\):
\[
E_S\le \sum_e |e|(C_e+c\delta)^2/m.
\]
Una stima complessiva del tipo
\[
E_{\rm jump}(v)\le E_{\rm outside}(g)
+\sum_e\bigl[|e|(C_e+c\delta)^2/m
+O(\delta M_e^2)+O(\rho M_P^2)\bigr]
\]
è **condizionale** alla scelta geometrica di §4, alla verifica delle tracce esterne \(M_e\), al controllo delle frontiere terminali \(M_P\) e alla disgiunzione dei supporti. Non va letta come una stima già dimostrata. I termini \(O(\delta M_e^2)\) e \(O(\rho M_P^2)\) non sono automaticamente \(O(\delta C_e^2)\) e \(O(\rho C_e^2)\).

L'ordine dei limiti compatibile con la geometria A è: fissare il grafo e le regioni terminali disgiunte, scegliere \(\rho\downarrow0\), quindi \(\delta/\rho\downarrow0\) anche rispetto alle separazioni angolari dei rami incidenti, scegliere \(m\uparrow\infty\) per \(S\), e infine scegliere \(h\downarrow0\) dopo la partizione comune staircase. L'ordine va adattato se si adotta la geometria B per i cappucci; in quel caso il controllo delle tracce esterne precede la stima \(K\).

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

**Stato: splitting locale condizionale.** La formula a strati e il conto (S) sono espliciti. Il controllo (K) vale soltanto dopo aver scelto una delle due geometrie di §4.1 e verificato le tracce esterne effettive; il controllo (V) richiede la stima dei salti artificiali sulle frontiere terminali, non soltanto del salto originale dentro i dischi. La disgiunzione richiede inoltre la suddivisione del jump complex e il controllo degli angoli tra rami incidenti (§4.3). Questi requisiti non sono tutti verificati dalla sola finitezza del grafo. Pertanto il lemma di splitting globale non è qui dichiarato dimostrato.

La proprietà del gradiente resta valida localmente: su ogni strato (v) è affine e (
abla v=
abla g^-+((m-i+1)/m)
abla h_e). Se la successiva staircase è costruita su una partizione comune finita e soddisfa le ipotesi del relativo lemma, allora (
abla u_{j,m,h}=G_j) quasi ovunque sulle celle. Questo fatto non colma eventuali lacune nella contabilizzazione dei salti di (v). Il trasferimento intrinseco a (Sigma) richiede inoltre di trattare esplicitamente le giunzioni tra facce e i vertici conici.
