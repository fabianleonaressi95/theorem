# C60 — lemma di localizzazione con tracce prescritte (specifica, non prova)

Data: 2026-11-21
Classificazione: **specifica del risultato da dimostrare — APERTO**.
Questo documento formula il lemma necessario per estendere la
recovery `W^{1,1}` (`C60_CF_VARIABLE_GRADIENT_RECOVERY_PROOF_2026-11-21.md`)
alle funzioni con salti macroscopici su un numero finito di segmenti.
Non è una dimostrazione: la lacuna è resa esplicita nelle ipotesi e
nelle stime richieste.

## Contesto e motivazione

La recovery `W^{1,1}` da sola non implica la formula CF per dati con
salti: l'approssimazione deve preservare le tracce sulle superfici di
discontinuità e controllare i raccordi in modo quantitativo. La
strategia a tre scale (tubi attorno a `J`, strati di raccordo,
esclusione degli intorni degli spigoli) richiede un lemma autonomo
con stime uniformi — l'area che tende a zero non basta se il costo
per unità di area diverge.

## Formulazione verificabile

Sia `Ω ⊂ ℝ²` un dominio poligonale, `J` l'unione di un numero finito
di segmenti, e `u` una funzione il cui retratto su ciascun lato di
ogni segmento ha tracce `u^± ∈ W^{1,1}` assegnate. Sia `F_ε` il
funzionale della costruzione (densità bulk `f`, costo superficiale
`φ`, con eventuali termini aggiuntivi — vedi sotto).

Occorre costruire `u_{ε,ρ,r}` tale che:

1. `u_{ε,ρ,r} → u` in `L¹(Ω)`;
2. fuori dal tubo `N_ρ(J)`, coincida con una recovery bulk
   localizzata (quella del Lemma R applicata regione per regione);
3. sulle parti regolari di `J` (cioè `J ∖ N_r(V)`, dove `V` è
   l'insieme finito di vertici ed estremi), conservi le tracce
   `u^±` e soddisfi
   ```
   limsup_{ε→0} F_ε(u_{ε,ρ,r}; N_ρ(J)∖N_r(V))
       ≤ ∫_{J∖N_r(V)} φ([u],ν_J) d𝓗¹ + q(ρ),   q(ρ)→0 ;
   ```
4. presso `V`, la stima uniforme
   ```
   limsup_{ε→0} F_ε(u_{ε,ρ,r}; N_r(V)) ≤ ω(r),   ω(r)→0,
   ```
   **uniformemente rispetto a `ρ`**;
5. il costo bulk fuori dal tubo rispetti il limite superiore della
   recovery `W^{1,1}`, con errore che tende a zero per `ρ↓0`.

Il punto 4 è il punto critico: **non segue dalla sola misura di
`N_r(V)`**. Se nel raccordo il gradiente cresce come `1/r`, una
densità bulk quadratica può mantenere costo non nullo o divergente.

## Condizione sufficiente per il raccordo agli spigoli

Se il raccordo in `N_r(V)` ha ampiezza limitata e gradiente
`O(1/r)`, area `O(r²)`, e la densità bulk è controllata da `f`, il
contributo bulk è al più

```
r² sup_{|p| ≤ C/r} f(p) .
```

Per crescita di tipo `q`, `f(p) ≤ C(1+|p|^q)`:

```
r² sup_{|p|≤C/r} f(p) = O(r² + r^{2−q}) :
   q < 2  ⇒  → 0        (la stima sufficiente)
   q = 2  ⇒  O(1)       (la costruzione O(1/r) non basta)
   q > 2  ⇒  non garantisce nemmeno costo limitato.
```

Questo **non** dimostra che il raccordo sia impossibile per `q=2`:
mostra solo che la costruzione con gradiente `O(1/r)` non basta a
concludere; serve una costruzione migliore o un'ipotesi aggiuntiva.

**Il controllo deve comprendere tutto il funzionale.** Se `F_ε`
contiene anche termini superficiali, penalità di bordo, dipendenze
esplicite da `x,u` o interazioni non locali, la stima bulk non è
sufficiente: il punto 4 deve limitare `F_ε` **intero** su `N_r(V)`,
inclusi i contributi concentrati sulle interfacce.

## Ordine dei limiti

Una volta provate le stime uniformi, l'ordine corretto è:

```
fissare r, ρ → mandare ε→0 → poi r↓0 → infine ρ↓0
```

con una diagonale finale. Non si possono scambiare i limiti senza
uniformità nelle stime.

## Prerequisiti da estrarre dal materiale della PR

Prima di poter dimostrare o smentire il lemma servono, dal materiale
effettivo:

1. definizione completa di `F_ε`, con dominio e condizioni al bordo;
2. densità bulk `f` e densità superficiale `φ` esatte;
3. costruzione laminata e valori delle tracce sui bordi delle celle;
4. formula esatta del raccordo agli spigoli;
5. stima del gradiente e del costo del raccordo in funzione di
   `ε, ρ, r`.

Per C60 il bulk rilevante nel modello intrinseco è `f(p)=W(p)` con
`W` la densità bulk dichiarata (ad es. `|F|_F` o `|F|_F²`) e
`φ(a,ν)=|a|`: il caso `W=|F|_F²` ha `q=2` e ricade nel caso
critico sopra — la stima `O(1/r)` non basta e serve una costruzione
di raccordo con gradiente meglio controllato o una stima più fine.

## Stato e dipendenze

- **Recovery `W^{1,1}`**: prova candidata separata (documento
  precedente), non dimostra la localizzazione SBV.
- **Localizzazione su `J` finito**: aperta, oggetto di questo
  documento.
- **`J_g` generale in SBV**: richiede inoltre un teorema di
  approssimazione del salto generale (cfr. Lazzaroni–Wozniak–Zhang,
  preprint arXiv — quadro pertinente, non dimostrazione del lemma
  energetico specifico).
- **Applicazione CF su superfici con salti**: aperta; dipende da
  questo lemma e dal raccordo fra facce adiacenti.
