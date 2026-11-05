# T049 — Dalla corrente microscopica di spin all'invariante quadratico

## Obiettivo

Derivare il contenuto microscopico di
\[
s^2=\frac12\langle S_{\mu\nu}S^{\mu\nu}\rangle
\]
e isolare l'ipotesi statistica che conduce alla legge Weyssenhoff standard
\(s^2\propto n^2\propto a^{-6}\). Il risultato deve permettere di testare, senza imporla, un'eventuale legge di correlazione RGS–PSU differente.

Questo documento costruisce il ponte e un audit parametrico. **Non afferma ancora che RGS–PSU possieda una correlazione non standard**: per deciderlo occorre calcolare o misurare il correlatore microscopico nel settore RGS–PSU.

## 1. Corrente microscopica

Per un campo di Dirac minimamente accoppiato, una convenzione comune per la corrente canonica di spin è
\[
\tau^{\lambda\mu\nu}
=\frac14\bar\psi\{\gamma^\lambda,\sigma^{\mu\nu}\}\psi,
\qquad
\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu].
\]
In quattro dimensioni questa corrente è totalmente antisimmetrica e, a fattori dipendenti dalle convenzioni, è duale alla corrente assiale
\[
A^\rho=\bar\psi\gamma^\rho\gamma^5\psi,
\qquad
\tau^{\lambda\mu\nu}\propto
\epsilon^{\lambda\mu\nu}{}_{\rho}A^\rho.
\]
La torsione EC minimale è algebrica: eliminandola dall'azione si ottiene un'interazione locale quadratica nella corrente di spin, equivalentemente una struttura assiale-assiale. Il coefficiente e il segno dipendono dalle convenzioni per l'azione, \(\kappa\), \(\epsilon^{0123}\) e la normalizzazione della corrente.

Per il limite di fluido, nel sistema di riposo si usa il tensore spaziale di spin \(S_{ij}\) con condizione di Frenkel
\[
S_{\mu\nu}u^\nu=0,
\qquad
s^2=\frac12\langle S_{ij}S_{ij}\rangle
\]
(in firma spaziale positiva). La corrispondenza con il bilineare di Dirac deve essere effettuata prima di fissare il coefficiente numerico.

## 2. Coarse-graining e correlatore

Sia \(W_\ell(x)\) un kernel di coarse-graining normalizzato,
\(\int d^3x\,W_\ell(x)=1\). Definiamo
\[
S_{ij}^{(\ell)}(x)=
\int d^3y\,W_\ell(x-y)\widehat{\mathcal S}_{ij}(y).
\]
L'invariante misurato alla scala \(\ell\) è
\[
s_\ell^2(x)=\frac12
\int d^3y\,d^3z\,
W_\ell(x-y)W_\ell(x-z)
\langle\widehat{\mathcal S}_{ij}(y)
\widehat{\mathcal S}_{ij}(z)\rangle.
\]
La decomposizione media + connessa è
\[
\langle JJ\rangle=\langle J\rangle\langle J\rangle+
\langle JJ\rangle_c.
\]
Quindi \(\langle J\rangle=0\) in un mezzo non polarizzato non implica \(\langle JJ\rangle=0\).

In una rappresentazione a particelle localizzate,
\[
\widehat{\mathcal S}_{ij}(x)=
\sum_a s^{(a)}_{ij}\,\delta^{(3)}(x-x_a),
\]
il quadrato coarse-grained si separa in:
- **auto-correlazione** \(a=b\): singola particella / shot noise;
- **correlazione di coppia** \(a\ne b\): correlazioni orientazionali e spaziali tra particelle.

In forma vettoriale tridimensionale (spin assiale \(\mathbf s_a\)) e con pesi \(w_a\), l'identità esatta è
\[
\left|\sum_a w_a\mathbf s_a\right|^2
=\underbrace{\sum_a w_a^2|\mathbf s_a|^2}_{\text{self}}
+\underbrace{2\sum_{a<b}w_aw_b\mathbf s_a\cdot\mathbf s_b}_{\text{pair}}.
\]
La routine Python T049 implementa e verifica questa identità, senza confondere il quadrato della somma con la somma dei quadrati.

**Attenzione al contatto quantistico:** nell'interazione EC efficace compare un operatore locale a quattro fermioni. Il suo valore medio richiede una prescrizione di ordinamento/renormalizzazione del prodotto di operatori. Il termine classico di auto-correlazione (shot noise) non può essere aggiunto o sottratto automaticamente: il confronto corretto deve usare la stessa prescrizione del termine assiale-assiale derivato dall'azione.

## 3. Dalla correlazione alla legge cosmologica

La conservazione del numero dà
\[
n(a)=n_0a^{-3}.
\]
Per isolare le due possibili origini statistiche dell'invariante, adottiamo l'ansatz di audit
\[
s^2(a)=
C_{\rm self}\,n(a)
+C_{\rm pair}\,n(a)^2\,g_s(a),
\qquad
g_s(a)=a^{-\gamma}.
\]
I coefficienti includono spin per particella, kernel e normalizzazione; non sono fissati da questo solo ansatz. Ne segue
\[
s^2(a)=
C_{\rm self}n_0a^{-3}
+C_{\rm pair}n_0^2a^{-(6+\gamma)}.
\]

Casi da distinguere:

| Regime | Legge | Interpretazione |
|---|---|---|
| Coppie standard, \(\gamma=0\), termine pair dominante | \(s^2\sim a^{-6}\) | chiusura Weyssenhoff usuale |
| Auto-correlazione dominante | \(s^2\sim a^{-3}\) | shot noise a volume di coarse-graining fissato; verificare prescrizione del contatto |
| Coppie con \(\gamma=-3\) | \(s^2_{\rm pair}\sim a^{-3}\) | correlazione efficace che cresce come \(a^3\) |
| \(\gamma\) generico | \(s^2_{\rm pair}\sim a^{-(6+\gamma)}\) | legge da determinare dal correlatore |

L'ipotesi \(g_s(a)\propto a^3\) non è una previsione: è la condizione necessaria, nel termine pair puro di questo ansatz, per convertire \(n^2\) in una legge \(a^{-3}\).

## 4. Equazione di stato indotta

Se il contributo EC efficace è separatamente conservato e ha
\(\rho_{\rm spin}=-A s^2\), allora
\[
\dot\rho_{\rm spin}+3H(\rho_{\rm spin}+p_{\rm spin})=0.
\]
Per un singolo termine \(s^2\propto a^{-q}\),
\[
w_{\rm spin}=\frac{p_{\rm spin}}{\rho_{\rm spin}}
=\frac q3-1.
\]
Dunque:
- \(q=6\Rightarrow w=1\): correzione stiff standard;
- \(q=3\Rightarrow w=0\): comportamento dust-like;
- se sono presenti entrambi i contributi, \(w(a)\) è dipendente da \(a\), e non è lecito assegnare a priori \(w=0\) o \(w=1\).

Questa conclusione usa la conservazione separata. Se RGS–PSU scambia spin/energia con altri gradi di libertà, va aggiunto un termine di sorgente alla continuità e la formula per \(w\) cambia.

## 5. Criterio sperimentale/computazionale per RGS–PSU

Per decidere se occorre una legge diversa, il calcolo deve restituire, a più scale \(\ell\) e densità:

1. la corrente microscopica \(\widehat{\mathcal S}_{ij}\) (o il bilineare assiale Dirac corrispondente);
2. \(\langle J\rangle\), correlatore connesso \(C_{ij,kl}(r)\) e correlatore integrato;
3. contributi self e pair separati, con prescrizione del contatto dichiarata;
4. dipendenza da \(n\), \(a\), \(\ell\) e dalla struttura geometrica RGS–PSU;
5. stabilità dell'esponente al variare di \(\ell\) e del volume, prima di interpretarlo come legge cosmologica.

Fit diagnostico: \(q_{\rm eff}(a)=-d\log s^2/d\log a\). Per una componente pair isolata si ricava \(\gamma=q_{\rm pair}-6\). Non si deve stimare \(q\) da un solo reticolo finito o da un singolo valore di densità.

### Stato delle affermazioni

| Affermazione | Stato |
|---|---|
| Corrente di spin Dirac duale alla corrente assiale in 4D | struttura standard, convenzioni da fissare |
| EC minimale produce un'interazione quadratica locale in spin/assiale | derivato dalla teoria minimale |
| \(\langle J\rangle=0\) non implica \(\langle JJ\rangle=0\) | identità statistica |
| \(s^2\propto n^2\) | chiusura standard sotto ipotesi di media Weyssenhoff |
| contributo self lineare in \(n\) | presente nel modello particellare coarse-grained; trattamento del contatto da fissare nel modello quantistico |
| \(g_s\propto a^3\) in RGS–PSU | ipotesi di test, non risultato |
| RGS–PSU richiede un esponente diverso da 6 | aperto: serve il correlatore microscopico |

## 6. Riferimenti

1. N. J. Popławski, “Cosmology with torsion: An alternative to cosmic inflation,” *Phys. Lett. B* 694 (2010), 181–185, [arXiv:1007.0587](https://arxiv.org/abs/1007.0587), [DOI](https://doi.org/10.1016/j.physletb.2010.09.056).
2. “Collapse and dispersal of a homogeneous spin fluid in Einstein–Cartan theory,” *Eur. Phys. J. C* 75 (2015), [DOI](https://doi.org/10.1140/epjc/s10052-015-3276-1).
3. “Einstein–Cartan gravitational collapse of a homogeneous Weyssenhoff fluid,” *Eur. Phys. J. C* (2014), [DOI](https://doi.org/10.1140/epjc/s10052-014-3154-2).

La bibliografia supporta il ponte EC–Weyssenhoff e la legge standard; non costituisce evidenza di una correlazione RGS–PSU non standard.
