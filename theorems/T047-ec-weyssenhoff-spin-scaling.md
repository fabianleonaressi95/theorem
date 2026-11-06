# T047 — Scaling cosmologico della torsione algebrica in un fluido di Weyssenhoff

## Enunciato e risultato principale

Nel modello Einstein–Cartan (EC) minimale con fluido di Weyssenhoff, condizione di Frenkel, spin intrinseco per particella conservato e media isotropa non polarizzata, il contributo quadratico di spin alla sorgente cosmologica scala come

\[
s^2(a)\propto a^{-6}.
\]

Dopo l'eliminazione algebrica della torsione, il corrispondente termine efficace ha equazione di stato stiff,

\[
\rho_{\rm spin}^{\rm eff}\propto -a^{-6},
\qquad
p_{\rm spin}^{\rm eff}=\rho_{\rm spin}^{\rm eff},
\qquad w_{\rm spin}=1,
\]

nel convenzionale ramo EC in cui il termine quadratico di spin entra con segno negativo. Il coefficiente numerico dipende dalle convenzioni per \(\kappa\), la normalizzazione di \(s^2\) e la definizione del tensore di spin; l'esponente e il rapporto \(p/\rho\) non dipendono da tale normalizzazione.

**Conseguenza:** in queste ipotesi il termine EC di spin-torsione non può essere identificato con il settore dust-like \(\rho_T\propto a^{-3}, p_T=0\) introdotto nel modello fenomenologico Torsion–Lambda. Il termine \(a^{-3}\) è la densità di massa a riposo del fluido, non la correzione quadratica EC di spin.

## 1. Ipotesi

Consideriamo:
1. una geometria FLRW spazialmente piatta con fattore di scala \(a(t)>0\);
2. un fluido di Weyssenhoff con quadrivelocità \(u^\mu\) e densità numerica fisica (propria) \(n\);
3. condizione di Frenkel \(S_{\mu\nu}u^\nu=0\);
4. spin intrinseco per particella conservato lungo il flusso;
5. conservazione del numero di particelle \(\nabla_\mu(nu^\mu)=0\);
6. media statistica isotropa, con correlazioni locali tali che l'invariante quadratico medio sia proporzionale a \(n^2\);
7. teoria EC minimale, senza termini cinetici indipendenti per la torsione e senza accoppiamenti non minimali aggiuntivi.

Poniamo \(s^2=\tfrac12\langle S_{\mu\nu}S^{\mu\nu}\rangle\), a meno di una costante di normalizzazione positiva.

## 2. Legge di scala del numero e dello spin

In FLRW, la conservazione del numero dà

\[
\dot n+3Hn=0,
\qquad H=\dot a/a,
\]

e quindi

\[
n(a)=n_0a^{-3}
\]

con la convenzione \(a_0=1\).

Scrivendo il tensore di spin come densità numerica per spin medio per particella, \(S_{\mu\nu}=n\,\sigma_{\mu\nu}\), l'ipotesi di spin intrinseco conservato implica che la norma quadratica media di \(\sigma_{\mu\nu}\) è costante. Pertanto

\[
s^2(a)=s_0^2\left(\frac{n(a)}{n_0}\right)^2
      =s_0^2a^{-6}.
\]

L'isotropia annulla la polarizzazione media vettoriale, ma non annulla in generale l'invariante quadratico medio: \(\langle S_{\mu\nu}\rangle=0\) non implica \(\langle S_{\mu\nu}S^{\mu\nu}\rangle=0\).

## 3. Eliminazione algebrica della torsione

Nella teoria EC minimale, l'equazione della connessione è algebrica: la torsione è determinata localmente dalla corrente di spin. Non è un campo indipendente con una propria equazione d'onda.

Eliminando la torsione dalla connessione (equivalentemente, sostituendo la soluzione algebrica nell'azione), si ottiene un'interazione efficace quadratica nella corrente di spin. Per la convenzione cosmologica standard del fluido di Weyssenhoff si può scrivere il contributo isotropizzato come

\[
\rho_{\rm eff}=\rho_{\rm pf}-A s^2,
\qquad
p_{\rm eff}=p_{\rm pf}-A s^2,
\qquad A>0.
\]

Il valore di \(A\) è convenzione-dipendente; nel frequente schema \(s^2=\tfrac12 S_{\mu\nu}S^{\mu\nu}\) è proporzionale a \(\kappa\). Il punto strutturale è che lo stesso invariante quadratico compare in densità e pressione con lo stesso coefficiente: il settore efficace ha \(p_{\rm spin}=\rho_{\rm spin}\).

Definendo \(\rho_{\rm spin,0}=A s_0^2>0\), il contributo firmato è

\[
\rho_{\rm spin}^{\rm eff}(a)=-\rho_{\rm spin,0}a^{-6},
\qquad
p_{\rm spin}^{\rm eff}(a)=-\rho_{\rm spin,0}a^{-6}.
\]

Il segno negativo è quello del ramo EC standard qui adottato; non va confuso con la positività di \(s^2\).

## 4. Verifica della continuità

Per un fluido efficace separatamente conservato,

\[
\dot\rho_{\rm spin}+3H(\rho_{\rm spin}+p_{\rm spin})=0.
\]

Con \(\rho_{\rm spin}=p_{\rm spin}=-\rho_{\rm spin,0}a^{-6}\),

\[
\dot\rho_{\rm spin}=-6H\rho_{\rm spin},
\qquad
3H(\rho_{\rm spin}+p_{\rm spin})=6H\rho_{\rm spin},
\]

e la somma è identicamente zero. Quindi \(w=1\), anche se densità e pressione firmate sono negative.

## 5. Confronto con la chiusura dust-like Torsion–Lambda

Il modello fenomenologico precedente assume

\[
\rho_T^{\rm dust}=\beta\rho_{m0}a^{-3},
\qquad p_T^{\rm dust}=0.
\]

Il modello EC di spin appena derivato dà invece

\[
\rho_{\rm spin}^{\rm EC}=-\rho_{\rm spin,0}a^{-6},
\qquad p_{\rm spin}^{\rm EC}=\rho_{\rm spin}^{\rm EC}.
\]

Gli esponenti sono distinti: \(-3\ne-6\). Inoltre le equazioni di stato sono distinte: \(0\ne1\). Dunque non esiste un'identificazione con coefficiente costante non nullo valida su un intervallo di fattore di scala.

Il background minimale corrispondente assume schematicamente la forma

\[
H^2=\frac{\kappa}{3}
\left(\rho_{m0}a^{-3}+\rho_{r0}a^{-4}
+\rho_\Lambda-\rho_{\rm spin,0}a^{-6}\right),
\]

a convenzioni e normalizzazioni fissate. La correzione di spin può diventare importante ad alta densità e produrre, in modelli appropriati, un rimbalzo; ciò non la trasforma in materia dust-like.

## 6. Quando può cambiare l'esponente?

L'esponente \(-6\) dipende dalle ipotesi 4–6. Può cambiare se:
- lo spin per particella non è conservato;
- esistono correlazioni di spin a lungo raggio o una lunghezza di correlazione dinamica;
- il fluido scambia spin o energia con altri settori;
- sono presenti accoppiamenti non minimali o gradi di libertà torsionali propaganti;
- la media statistica non è quella di un fluido isotropo non polarizzato.

In tali casi serve specificare l'equazione di trasporto dello spin e la legge di correlazione; non è lecito scegliere \(a^{-3}\) per adattamento. Per ottenere un termine efficace \(a^{-3}\) con continuità separata occorrerebbe una nuova dinamica che produca simultaneamente \(p_T=0\). Non segue dalla teoria EC minimale di Weyssenhoff.

## 7. Registro delle evidenze

| Affermazione | Stato |
|---|---|
| \(n\propto a^{-3}\) da conservazione del numero in FLRW | Derivato |
| \(s^2\propto n^2\propto a^{-6}\) con spin per particella e correlazioni locali conservati | Derivato sotto ipotesi esplicite |
| Termine quadratico EC algebrico, non propagante nel modello minimale | Struttura della teoria |
| \(p_{\rm spin}=\rho_{\rm spin}\) per la chiusura Weyssenhoff isotropizzata adottata | Risultato del modello |
| Identificazione del termine EC con \(\beta a^{-3}\) dust-like | Esclusa sotto le ipotesi del teorema |
| Correlazioni non locali o dinamica modificata che producano un'altra scala | Aperto |
| Derivazione microscopica della media di spin per il sistema RGS–PSU specifico | Aperto |

## 8. Riproducibilità

La legge di scala è implementata in `scripts/ec_spin_fluid_scaling.py`; i controlli algebrici sono in `tests/test_ec_spin_fluid_scaling.py`.

Il teorema non assegna un valore osservativo a \(\rho_{\rm spin,0}\), non stima \(\beta\), e non afferma che il modello Weyssenhoff descriva tutta la materia cosmologica.


## 9. Bibliografia di riferimento

1. N. J. Popławski, “Cosmology with torsion: An alternative to cosmic inflation,” *Physics Letters B* **694** (2010), 181–185, DOI: [10.1016/j.physletb.2010.09.056](https://doi.org/10.1016/j.physletb.2010.09.056), arXiv:[1007.0587](https://arxiv.org/abs/1007.0587). In particolare, le equazioni (8)–(12) riportano il tensore efficace Weyssenhoff, la correzione \(-\kappa s^2/4\) in densità e pressione e la conservazione che implica \(\dot{s^2}+6Hs^2=0\).
2. “Collapse and dispersal of a homogeneous spin fluid in Einstein–Cartan theory,” *European Physical Journal C* **75** (2015), DOI: [10.1140/epjc/s10052-015-3276-1](https://doi.org/10.1140/epjc/s10052-015-3276-1). Riporta esplicitamente \(\dot{S^2}=-6HS^2\) e la conseguente legge \(S^2\propto a^{-6}\).
3. “Kinematics of Einstein-Cartan universes,” Cambridge repository manuscript. Discute il fluido di Weyssenhoff, la condizione di Frenkel e i limiti della sua isotropizzazione macroscopica.

La bibliografia supporta il modello standard di fluido di spin usato qui; non sostituisce la derivazione microscopica specifica per il sistema RGS–PSU.
