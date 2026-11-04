# Audit di applicabilità T008 — marginale Wilson Q6 verso Bergman

**Data:** 2026-11-04  
**Esito:** NON VERIFICATA; il modello documentato non definisce ancora una successione di misure su D5.  
**Portata:** audit delle ipotesi necessarie, non confutazione del limite in una futura famiglia di raffinamenti.

## 1. Criterio da testare

T008 è un criterio sufficiente. Per una successione di probabilità \(\mu_k\) su \(D_5\), un compatto \(K\Subset D_5\), partizioni \(P_k\) di diametro massimo \(\delta_k\), e \(\nu_K\) la probabilità Bergman normalizzata su K, richiede:

- \(\delta_k\to0\);
- errore di massa sulle celle \(E_k=\sum_j|p_{kj}-q_{kj}|\to0\);
- massa esterna \(\ell_k=\mu_k(D_5\setminus K)\to0\).

Allora \(d_{BL}(\mu_k,\nu_K)\le 2\delta_k+\operatorname{diam}(K)E_k/2+2\ell_k\to0\).

Il criterio è condizionale: non costruisce \(\mu_k\), la mappa flussi→D5, né la scala k.

## 2. Audit delle ipotesi sul Q6 documentato

| Requisito T008 | Evidenza nel modello disponibile | Esito |
|---|---|---|
| Famiglia \(\mu_k\) di probabilità su D5 | T005 definisce \(W_\beta([c])\) su classi del quoziente intero e una marginale su \(H_L\cong\mathbb T^{68}\); non definisce una famiglia di misure su D5 | **Manca** |
| Parametro di raffinamento k | Q6 è il complesso finito fisso con 64 vertici, 192 lati e 240 plaquette; non è specificata una successione di complessi/reticoli | **Manca** |
| Mappa \(\Phi_k\) dai flussi alle coordinate D5 | T005 afferma esplicitamente che il settore canonico \(q\) non è derivato dalla marginale | **Manca** |
| Partizioni con \(\delta_k\to0\) | Nessuna griglia o partizione di D5 costruita dalla legge Wilson | **Manca** |
| Errore celle \(E_k\to0\) | Non esistono masse Wilson su celle D5 confrontabili con \(\int_{cell}N(z)^{-5}d\mu_0\) | **Non calcolabile** |
| Massa esterna \(\ell_k\to0\) | T005 prova positività a ogni classe per ogni \(\beta>0\), non un limite di concentrazione uniforme su compatti D5 | **Non dimostrata** |

## 3. Cosa è già stabilito

1. Per ogni \(\beta>0\), i coefficienti di Bessel sono positivi e T005 ottiene \(W_\beta([c])>0\) per ogni classe. Quindi nessun cutoff duro esatto è prodotto a scala finita.
2. La positività non esclude concentrazione asintotica e non implica una densità limite.
3. T008 è un criterio sufficiente corretto una volta che esistano la famiglia \(\mu_k\), la mappa \(\Phi_k\), e le quantità \(\delta_k,E_k,\ell_k\).
4. T004 costruisce somme di Riemann con pesi geometrici già assegnati; non identifica quei pesi con la marginale Wilson.

## 4. Candidato di scala, non risultato

Una possibile direzione da derivare è un limite di forte accoppiamento \(\beta\to\infty\), con riscalamento dei flussi di ordine \(\sqrt{\beta}\). Per coefficienti Bessel con indice \(n=O(\sqrt{\beta})\), l'approssimazione gaussiana suggerisce una forma quadratica efficace sul quoziente di rango 5.

Questo è soltanto un candidato di analisi asintotica. Non prova:
- che il quoziente abbia la normalizzazione/covarianza richiesta;
- che esista una mappa canonica dalle cinque variabili reali a una carta \(D_5\subset\mathbb C^5\);
- che la densità risultante sia \(N(z)^{-5}\);
- che il bordo sia tight, cioè che \(\ell_k\to0\).

Non scegliere un cutoff o una mappa per adattare il risultato a Hua/Wyler: entrambi devono emergere dalla marginalizzazione e dalla legge di scala.

## 5. Verdetto

**T008: criterio matematico sufficiente, applicazione Wilson-Q6 non verificata.**

L'ostacolo immediato non è un errore numerico: è strutturale. Il Q6 fissato e la marginale T005 non forniscono ancora l'indice di raffinamento, la mappa \(\Phi_k\), né le tre successioni quantitative. Perciò oggi non è lecito dichiarare né dimostrata né falsificata la convergenza Wilson→Bergman.

## 6. Prossimo lemma minimo

Prima di nuovi workflow, occorre derivare dalla matrice intera del quoziente una famiglia esplicita di misure normalizzate sul reticolo di rango 5 e una legge di scala \(\beta_k\). Solo dopo si potrà:

1. ricavare la forma quadratica efficace e la sua normalizzazione;
2. definire una mappa geometrica \(\Phi_k\) indipendente dalla densità bersaglio;
3. stimare uniformemente la coda fuori da \(K\);
4. stimare l'errore totale delle masse sulle celle.

Se il punto 2 non produce naturalmente una carta D5, l'identificazione con Bergman non segue e va abbandonata o riformulata.

## 7. Lacuna di riproducibilità

T005 cita tre file Q6-specifici in `docs/` — `Q6_D5_INTEGER_FIBER_QUOTIENT.md`, `Q6_D5_SATURATED_KERNEL_AND_TAIL_BOUND.md`, `Q6_D5_WILSON_FIVE_TORUS_MARGINAL.md` — che non risultano presenti nel ramo `main` al momento di questo audit (risposta 404 del repository). Le formule riportate in T005 sono quindi leggibili, ma quei tre artefatti non sono riproducibili da questo repository finché non vengono ripristinati o ricollocati. Questo non cambia il verdetto di convergenza, ma impedisce un audit indipendente completo dei dati interi sottostanti.
