# Lemma candidate — forma quadratica efficace del quoziente Wilson Q6

**Stato: derivazione algebrica condizionale; matrice numerica non verificata.**  
**Scopo:** isolare la forma gaussiana che segue dall'asintotica Bessel e dalla marginalizzazione sulle fibre intere. Non identifica ancora il dominio D5 né la densità di Bergman.

## 1. Dati e notazione

Sia C in Z^(129x192) la matrice dei cicli usata in T005. Sia K sottoinsieme Z^129 il kernel saturo di rango 124 della mappa al quoziente di rango 5. Scegliamo una matrice di base intera R in Z^(124x129) le cui righe generano K, e poniamo A=RC in Z^(124x192).

Per una classe rappresentata da c in Z^129, la fibra è
W_beta([c]) = sum_{m in Z^124} product_e I_|((c+mR)C)_e|(beta)/I_0(beta).
La notazione è indipendente dalla scelta della base, a meno della trasformazione unimodulare.

## 2. Asintotica locale Bessel

Per beta→infinito e |n|≤M sqrt(beta), l'espansione locale dà
log(I_n(beta)/I_0(beta)) = -n^2/(2 beta) + O_M(beta^-1).
La stima è uniforme per n/sqrt(beta) in compatti; non è uniforme su tutto Z. Pertanto, su regioni di flusso scalate e limitate,
product_e I_|n_e|(beta)/I_0(beta) = exp[-||n||_2^2/(2 beta)+O_M(beta^-1)].
Per sostituire l'intera somma di fibra con una somma gaussiana occorre ancora una stima uniforme delle code fuori da ||n||≤M sqrt(beta).

## 3. Eliminazione gaussiana dei 124 modi di fibra

Sia S=row_R(A) sottoinsieme R^192, e supponiamo rank(A)=124. La proiezione ortogonale su S-perp è
P_perp = I_192 - A^T(AA^T)^-1 A.
Per x=cC, la minimizzazione continua lungo la fibra dà
min_{t in R^124} ||x+tA||^2 = x P_perp x^T.
Ne segue la forma quadratica efficace:
Q_eff = C P_perp C^T,   q_eff(c)=c Q_eff c^T.
Essa è invariante sotto c→c+k, k in K_R, perché KC è contenuto in S e P_perp A^T=0.

Se rank(Q_eff)=5, essa induce una forma definita positiva sul quoziente reale R^129/K_R. La condizione di rango 5 va verificata sulla matrice intera effettiva, non dedotta dal solo conteggio delle dimensioni.

## 4. Marginalizzazione continua e fattore di fibra

Nel modello gaussiano continuo,
integral_R124 exp[-||x+tA||^2/(2 beta)] dt
= (2 pi beta)^62 / sqrt(det(AA^T)) * exp[-q_eff(c)/(2 beta)].
La somma intera sulla fibra è una somma theta, non esattamente questo integrale. L'approssimazione integrale richiede che la scala gaussiana lungo il reticolo A^T Z^124 diventi larga rispetto ai suoi passi fondamentali; il controllo è espresso tramite la formula di Poisson e il minimo della forma duale. Il fattore di covolume dipende dalla base intera scelta, mentre il risultato fisico deve essere invariante sotto cambi di base unimodulari.

La previsione gaussiana candidata è
W_beta([c]) ≃ C_A beta^62 exp[-c Q_eff c^T/(2 beta)],
solo nel regime congiunto in cui (i) l'asintotica Bessel è uniforme sui flussi rilevanti, (ii) le code sono uniformemente trascurabili, e (iii) la somma theta è approssimata dall'integrale. Non è una formula asintotica già dimostrata per l'intera marginale T005.

## 5. Cosa segue e cosa non segue

Se Q_eff ha rango 5, la marginale ridotta ha una gaussiana ellittica su cinque coordinate reali del quoziente, con covarianza proporzionale a Q_eff^+ (pseudoinversa, una volta fissate coordinate sul quoziente).

Questo non produce automaticamente:
- cinque coordinate complesse z in C^5;
- una struttura simplettica o una polarizzazione canonica z=(q+ip)/sqrt(2);
- il dominio limitato di tipo IV D5;
- il fattore Jacobiano N(z)^-5.

Per ottenere D5 occorre una struttura aggiuntiva reale→complessa e una mappa indipendente dalla densità bersaglio. La gaussiana euclidea sul quoziente, da sola, non è una misura di Bergman.

## 6. Test numerici minimi richiesti sui dati originali

Dati C e una base intera R verificati, calcolare senza fitting:
1. rank_Q(A) e det(AA^T);
2. autovalori di Q_eff, verificando esattamente il rango 5 e il kernel coincidente con K_R;
3. invarianza di Q_eff sotto cambi unimodulari della base di K;
4. spettro della forma duale del reticolo di fibra, per quantificare l'errore somma–integrale con Poisson;
5. residui dell'espansione Bessel su intervalli |n|≤M sqrt(beta), separando l'evidenza numerica dalla stima uniforme analitica.

I tre file dati citati in T005 — Q6_D5_INTEGER_FIBER_QUOTIENT.md, Q6_D5_SATURATED_KERNEL_AND_TAIL_BOUND.md, Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md — non risultano nel ramo main controllato durante l'audit del 4 novembre 2026. Senza C, R o una loro ricostruzione verificabile non si possono riportare valori numerici autentici.

## 7. Verdetto

**Risultato condizionale:** la marginalizzazione gaussiana dei 124 modi di fibra conduce alla forma di Schur/proiezione Q_eff=C P_perp C^T.  
**Non verificato:** rango 5 della matrice effettiva sui dati Q6, limite della somma theta e uniformità delle code Bessel.  
**Non implicato:** geometria D5, struttura complessa, misura di Bergman o convergenza Wilson→Bergman.

Riferimento per le espansioni uniformi Bessel: NIST Digital Library of Mathematical Functions, §10.41, https://dlmf.nist.gov/10.41. Per la somma reticolare/integrale: formula di Poisson per reticoli euclidei, da applicare al reticolo effettivo e alla sua forma duale.
