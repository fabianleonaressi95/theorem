# T006 — Criterio quantitativo Wilson–Bergman

**Stato: criterio sufficiente dimostrato; applicazione Q6 non verificata.**

Sia K un compatto di D5 e sia nu la probabilità con densità proporzionale a N(z)^(-5) su K. Per ogni scala k, una famiglia di classi di flusso con pesi Wilson normalizzabili induce, tramite una mappa Phi_k, una probabilità mu_k su D5.

Sia P_k una partizione misurabile di K con diametro massimo delta_k tendente a zero. Indichiamo con q_kj la massa nu della cella j e con p_kj la massa di mu_k condizionata a K. Definiamo E_k = sum_j |p_kj-q_kj| e ell_k = mu_k(D5\K).

Se delta_k, E_k ed ell_k tendono tutti a zero, allora mu_k converge debolmente a nu. Più precisamente, per la distanza bounded-Lipschitz:

 d_BL(mu_k,nu) <= 2 delta_k + diam(K) E_k/2 + 2 ell_k.

La dimostrazione si ottiene sostituendo ogni cella con un rappresentante: ciascuna delle due misure cambia un integrale Lipschitz di al più delta_k; la differenza tra le due distribuzioni discrete è limitata da diam(K) E_k/2; la massa esterna contribuisce al più 2 ell_k.

## Test richiesto per Wilson-Q6

Per applicare il criterio occorrono: (1) una famiglia di raffinamenti k; (2) mappe Phi_k dai flussi alle coordinate D5; (3) pesi marginali W_k ottenuti dall'azione Wilson, non da un fit; (4) normalizzazione e controllo della coda; (5) partizioni con delta_k -> 0; (6) verifica di E_k -> 0 contro le masse integrali di N^(-5); (7) perdita ell_k -> 0.

## Limiti

T005 prova che a beta finito ogni classe Q6 ha peso positivo. Ciò esclude un cutoff duro esatto a scala finita, ma non esclude concentrazione asintotica. Il Q6 finito fissato non fornisce da solo una famiglia con delta_k -> 0. Senza una costruzione indipendente di Phi_k e della legge di scala, l'applicazione a Wilson resta aperta.

T003 esclude l'identità atomica-continuo a scala finita; T004 tratta somme di Riemann con pesi geometrici assegnati; T005 dà la marginale Wilson e la sua positività; T006 stabilisce il test quantitativo per un eventuale limite Wilson-Bergman.

**Esito:** il criterio è dimostrato, ma non è dimostrato che i pesi Wilson Q6 lo soddisfino. Un fallimento di delta_k, E_k o ell_k falsifica quella specifica identificazione e quella specifica legge di scala, non T002.

Riferimenti: Billingsley, *Convergence of Probability Measures*, 2nd ed., 1999; Villani, *Optimal Transport: Old and New*, 2009; T003–T005 nel presente repository.