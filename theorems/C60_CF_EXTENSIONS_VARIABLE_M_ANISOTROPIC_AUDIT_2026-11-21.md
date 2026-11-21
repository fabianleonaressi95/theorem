# C60 — audit matematico delle estensioni CF: M variabile, anisotropia e immersione

Data: 2026-11-21  
Riferimento: commit `992eb80c64af0afb2e227ad523042d51ef04dbc4` (branch `research/c60-cf-nuclear-norm-cell-problem`).  
Scopo: separare i risultati dimostrati dalle estensioni che richiedono ancora una prova completa.

## Esito sintetico

| Tema | Stato corretto |
|---|---|
| Lower bound per (M(x)) misurabile e (psi(a,\nu)=|a|) | **Dimostrabile** per convergenza debole-* delle misure e test interni |
| Recovery per ogni (M\in L^\infty), con gradiente a.e. fissato | **Non dimostrato nel testo del commit** |
| Formula di cella anisotropa separabile | Upper bound laminato e lower bound duale; **uguaglianza aperta** |
| Rank 2 a.e. per la staircase a (\widetilde G=cA), (c>0) | **Dimostrato** nel caso a campi costanti per faccia |
| Embeddedness globale | **Aperta** |

## 1. Campo (M(x)): lower bound e problema di recovery

Sia (f\subset\mathbb R^2) una faccia piana, (M\in L^\infty(f;\mathbb R^{3\times2})), e sia
(u_h\in SBV(f;\mathbb R^3)). Supponiamo, localmente all'interno di (f), che
[
D^s u_h\stackrel{*}{\rightharpoonup}M(x)\,\mathcal H^2
]
e che i costi di salto siano quelli isotropi (|[u_h]|\,\mathcal H^1\).

**Lower bound.** Per ogni campo test continuo (Q\in C_c(f;\mathbb R^{3\times2})) con
(\|Q(x)\|_{op}\leq1), vale
[
\int_f Q:M\,d\mathcal H^2
=\lim_h\int_f Q:dD^s u_h
\leq\liminf_h\int_{J_{u_h}}|[u_h]|\,d\mathcal H^1.
]
La disuguaglianza segue da
(Q:([u_h]\otimes\nu_h)=[u_h]\cdot Q\nu_h\leq |[u_h]|\).
Prendendo il sup sui test continui a valori nella palla unitaria della norma operatore, e usando la densità dei campi continui nella dualità con la misura assolutamente continua (M\,\mathcal H^2), si ottiene
[
\boxed{\liminf_h\int_{J_{u_h}}|[u_h]|\,d\mathcal H^1
\geq\int_f\|M(x)\|_*\,d\mathcal H^2.}
]
La scelta di un campo polare misurabile dalla SVD è lecita per identificare il sup puntuale, ma non va inserita direttamente nel passaggio al limite debole-*: tale passaggio richiede test continui (o un argomento di approssimazione esplicito).

**Recovery: lacuna nel commit.** Il testo propone di far variare le direzioni SVD e di usare
(M(x)q_h(x)). Per (M) non costante, il prodotto genera termini di derivata aggiuntivi quando (M) è regolare; per (M\in L^\infty) non è neppure disponibile una derivata classica di (M). Inoltre, l'approssimazione (L^1) di (M) da sola non dimostra che la successione costruita:
1. converga proprio al dato (g);
2. mantenga esattamente (\nabla u_h=\widetilde G) a.e.;
3. abbia costo dei salti convergente a (\int_f\|M\|_*\);
4. controlli i contributi sulle interfacce della partizione e la diagonalizzazione.

Quindi la formula di densità (\|M(x)\|_*) è provata come **lower bound localizzato**, ma l'identificazione come costo rilassato esatto per ogni campo misurabile richiede una recovery sequence completa. Fino a quella prova, l'uguaglianza e il funzionale integrale completo per (\widetilde G(x)) vanno classificati come **candidati**, non come teoremi chiusi.

Il risultato già dimostrato per (M) costante su ciascuna faccia resta invariato.

## 2. Densità anisotropa separabile

Si consideri
[
\psi(a,\nu)=\Phi(a)k(\nu),
]
con (\Phi) una norma su \(\mathbb R^3\). Per una densità di interfaccia non orientata è inoltre necessario imporre
[
k(\nu)=k(-\nu),
]
perché la rappresentazione geometrica del salto è invariata sotto
(([u],\nu)\mapsto(-[u],-\nu)). Se (k) non è pari, occorre specificare una convenzione orientata coerente; senza di essa il costo non è ben definito sulle interfacce non orientate.

Per ogni base ortonormale (\{v_1,v_2\}\) di (\mathbb R^2), due famiglie laminate con normali (v_j) e salti (hMv_j) producono
[
\sum_{j=1}^2(Mv_j)\otimes v_j
=M\sum_{j=1}^2v_j\otimes v_j=M.
]
Il costo limite della costruzione è
[
\sum_{j=1}^2 k(v_j)\Phi(Mv_j).
]
Pertanto è dimostrato l'**upper bound**
[
\mathcal C_{\Phi,k}(M)
\leq
\min_{\{v_1,v_2\}\,ONB}
\bigl[k(v_1)\Phi(Mv_1)+k(v_2)\Phi(Mv_2)\bigr].
]

Per il lower bound, definendo
[
\Lambda_{\Phi,k}
=\{Q\in\mathbb R^{3\times2}:
\Phi^\circ(Q\nu)\leq k(\nu)\ \forall\nu\in S^1\},
]
la dualità dà
[
\mathcal C_{\Phi,k}(M)\geq
\sup_{Q\in\Lambda_{\Phi,k}}Q:M.
]
Il testo del commit **non dimostra** che questo sup coincida con il minimo sulle basi ortonormali. Tale identificazione va quindi lasciata **congetturale/aperta**; non va chiamata formula di cella dimostrata.

Nel caso isotropo (\Phi(a)=|a|), (k\equiv1), il risultato già provato dà
(\mathcal C(M)=\|M\|_*\), e il minimo laminato coincide con la norma nucleare.

## 3. Immersione: formulazione precisa

Per la costruzione staircase con (M) costante sulla faccia,
[
u_h(\xi)=\widetilde G\xi+b+Mq_h(\xi),
qquad \nabla u_h=\widetilde G\quad\text{a.e.}
]
Se (A^TA=I_2) e (\widetilde G=cA) con (c>0), allora
[
\operatorname{rank}\nabla u_h=\operatorname{rank}(cA)=2
\quad\text{a.e.}
]
Questo verifica il vincolo di **rango due quasi ovunque** per tale costruzione. Non dimostra che (u_h) sia un'immersione continua nel senso differenziale classico attraverso le interfacce di salto, né che sia globalmente iniettiva. L'embeddedness resta aperta. L'estensione di questo argomento a (M(x)) variabile non è coperta dalla formula staircase costante qui sopra.

## 4. Conseguenza editoriale

Fino alla costruzione di recovery per (M(x)) misurabile:
- mantenere come teorema la cell formula nucleare per (M) costante per faccia;
- registrare il lower bound variabile come risultato dimostrato;
- registrare il recovery variabile e il funzionale integrale esatto come problema aperto;
- registrare l'upper bound anisotropo e il lower bound duale separatamente;
- non elevare a teorema l'uguaglianza anisotropa;
- mantenere il risultato di rango due a.e. nel suo ambito costante per faccia.

Nessuna conclusione qui modifica o indebolisce i risultati già dimostrati e merged per il caso isotropo con (M) costante per faccia.
