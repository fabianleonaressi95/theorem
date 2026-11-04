# T001 — Teorema di Liouville per il flusso hamiltoniano

**Stato: DIMOSTRATO (classico).**  
**Ruolo nel programma RGS–PSU–PRISM: lemma matematico di base; il collegamento a PSU–Anti-Twin, PRISM e alla misura di Bergman resta da dimostrare separatamente.**

## 1. Enunciato

Sia \((M,\omega)\) una varietà simplettica liscia di dimensione \(2n\), sia \(H\in C^\infty(M)\) un'Hamiltoniana autonoma e sia \(X_H\) il campo hamiltoniano definito da

\[
\iota_{X_H}\omega=-dH.
\]

Sia \(\Phi_t\) il suo flusso, definito per i tempi considerati. Allora

\[
\boxed{\Phi_t^*\omega=\omega}
\]

per ogni tale \(t\). Di conseguenza il volume simplettico

\[
\mathrm{vol}_\omega=\frac{\omega^n}{n!}
\]

è invariato:

\[
\boxed{\Phi_t^*\mathrm{vol}_\omega=\mathrm{vol}_\omega.}
\]

In coordinate canoniche \((q^1,\ldots,q^n,p_1,\ldots,p_n)\), ciò equivale alla conservazione della misura di Liouville \(d^nq\,d^np\).

## 2. Dimostrazione

Per la formula di Cartan per la derivata di Lie,

\[
\mathcal L_{X_H}\omega
=d(\iota_{X_H}\omega)+\iota_{X_H}(d\omega).
\]

Poiché \(\omega\) è simplettica, è chiusa: \(d\omega=0\). Dalla definizione di \(X_H\), \(\iota_{X_H}\omega=-dH\), e quindi

\[
\mathcal L_{X_H}\omega=d(-dH)=0.
\]

La derivata temporale del pullback lungo il flusso è

\[
\frac{d}{dt}\Phi_t^*\omega
=\Phi_t^*(\mathcal L_{X_H}\omega)=0.
\]

Pertanto \(\Phi_t^*\omega\) è costante in \(t\). A \(t=0\), \(\Phi_0\) è l'identità, per cui \(\Phi_0^*\omega=\omega\). Ne segue

\[
\Phi_t^*\omega=\omega.
\]

Il pullback commuta con il prodotto esterno, dunque

\[
\Phi_t^*\left(\frac{\omega^n}{n!}\right)
=\frac{(\Phi_t^*\omega)^n}{n!}
=\frac{\omega^n}{n!}.
\]

Questo conclude la dimostrazione. \(\square\)

## 3. Forma canonica

Con

\[
\omega=\sum_{j=1}^n dq^j\wedge dp_j,
\]

si ottiene

\[
\frac{\omega^n}{n!}
=dq^1\wedge dp_1\wedge\cdots\wedge dq^n\wedge dp_n,
\]

che, a meno della convenzione d'orientazione, è la misura \(d^nq\,d^np\). Il teorema afferma che il flusso hamiltoniano ha Jacobiano simplettico e quindi determinante unitario rispetto a tale volume.

## 4. Ipotesi e limiti

1. La chiusura \(d\omega=0\) è essenziale per la dimostrazione.
2. La non-degenerazione di \(\omega\) garantisce l'esistenza e l'unicità di \(X_H\).
3. Il flusso deve esistere nel tratto temporale considerato; completezza globale non è necessaria per la versione locale.
4. Il risultato riguarda il volume simplettico, non una densità arbitraria come una misura di Bergman.
5. Un sistema dissipativo o un'evoluzione non hamiltoniana non gode automaticamente di questa invarianza.

## 5. Conseguenza e collegamento al progetto

Per un settore efficace descritto da coordinate canoniche \((q,p)\), se la dinamica PSU–Anti-Twin è effettivamente generata da un'Hamiltoniana rispetto a una forma simplettica \(\omega_{\mathrm{eff}}\), allora il suo flusso conserva

\[
 d\mu_L=\frac{\omega_{\mathrm{eff}}^n}{n!}.
\]

Questa è una conseguenza condizionale dell'identificazione hamiltoniana: non dimostra da sola che il modello PSU possieda tale struttura, né che la misura efficace sia quella di Bergman su D5.

In particolare, per dedurre una densità di Bergman occorre una trasformazione di coordinate o una mappa di riduzione esplicita e dimostrare come il pullback della misura venga trasformato. La sola conservazione di Liouville non implica il fattore \(N(z)^{-5}\).

## 6. Riferimenti

- J.-M. Souriau, *Structure of Dynamical Systems: A Symplectic View of Physics*, Birkhäuser, 1997 (edizione inglese; testo originale francese 1969).
- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989, capitoli 8–9.
- R. Abraham e J. E. Marsden, *Foundations of Mechanics*, 2nd ed., Benjamin/Cummings, 1978.

I riferimenti sostengono il teorema classico e il formalismo simplettico; non sono presentati come prova di una specifica dinamica RGS–PSU.

## 7. Prossimo problema, non incluso in questo teorema

Dimostrare, a partire dalla struttura PSU–Anti-Twin già definita, l'esistenza di una forma simplettica globale \(\omega_{\mathrm{PSU}}\), la sua non-degenerazione e la compatibilità della dinamica proposta con un'Hamiltoniana. Solo dopo si potrà studiare rigorosamente la relazione tra misura di Liouville e misura di Bergman D5.
