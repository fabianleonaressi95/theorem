# C60 — cell problem nucleare e ottimizzazione del campo bulk

Data: 2026-11-21  
Classificazione: **teorema dimostrato nel modello intrinseco faccia-per-faccia**  
Densità interfaciale: \\(\\psi(a,\\nu)=|a|\\), indipendente dalla normale.

## 1. Problema di cella

Su una faccia piana identificata con un poligono \\(P\\subset\\mathbb R^2\\), siano
\\[
g(\\xi)=A\\xi+b,\\qquad \\widetilde G\\in\\mathbb R^{3\\times2},
\\qquad M=A-\\widetilde G.
\\]
Consideriamo successioni \\(u_h\\in SBV(P;\\mathbb R^3)\\) con
\\[
u_h\\to g\\text{ in }L^1(P),\\qquad
\\nabla u_h=\\widetilde G\\quad\\text{a.e.}
\\]
Nel problema di cella, la parte di salto genera il difetto distribuzionale
\\(M\\mathcal L^2\\). Allora
\\[
\\liminf_{h\\to0}\\int_{J_{u_h}}|[u_h]|\\,d\\mathcal H^1
\\ge |P|\\,\\|M\\|_*.
\\]
La costruzione SVD del §3 raggiunge il limite. Pertanto
\\[
\\boxed{\\mathcal C(M)=\\|M\\|_*=\\sum_j\\sigma_j(M).}
\\]

## 2. Limite inferiore

Da \\(u_h\\to g\\) in \\(L^1\\) segue \\(Du_h\\to A\\mathcal L^2\\) in distribuzioni. Poiché la parte assolutamente continua è esattamente \\(\\widetilde G\\mathcal L^2\\), la parte di salto converge distribuzionalmente a \\(M\\mathcal L^2\\). Per successioni con costo interfaciale limitato, la misura di salto ha variazione uniformemente limitata; ogni sottosuccessione che realizza il liminf ammette quindi un limite debole-* che coincide con \\(M\\mathcal L^2\\) nell'interno.

Per ogni \\(Q\\in\\mathbb R^{3\\times2}\\) con \\(\\|Q\\|_{op}\\le1\\),
\\[
Q:([u_h]\\otimes\\nu_h)
=[u_h]\\cdot(Q\\nu_h)\\le |[u_h]|.
\\]
Testando contro funzioni non negative compatte, passando al limite e poi esaurendo \\(P\\), si ottiene
\\[
|P|Q:M\\le\\liminf_h\\int_{J_{u_h}}|[u_h]|\\,d\\mathcal H^1.
\\]
La dualità
\\[
\\|M\\|_* = \\sup_{\\|Q\\|_{op}\\le1}Q:M
\\]
dà il limite inferiore nucleare.

La distinzione rispetto alla stima Frobenius è sostanziale: la TV matriciale indotta dalla norma euclidea del salto e dalla normale libera è la norma nucleare, non \\(\\|M\\|_F\\).

## 3. Recupero mediante SVD

Scriviamo
\\[
M=\\sum_{j=1}^r\\sigma_j a_j\\otimes b_j,
\\quad |a_j|=|b_j|=1,\\quad r\\le2.
\\]
Poniamo
\\[
u_h(\\xi)=\\widetilde G\\xi+b+
\\sum_{j=1}^r\\sigma_jh
\\left\\lfloor\\frac{\\xi\\cdot b_j}{h}\\right\\rfloor a_j.
\\]
Allora \\(\\|u_h-g\\|_{L^\\infty(P)}\\le h\\sum_j\\sigma_j\\to0\\) e \\(\\nabla u_h=\\widetilde G\\) a.e. Le rette della famiglia \\(j\\) hanno distanza \\(h\\), salto \\(h\\sigma_j a_j\\), e densità lineare \\(1/h\\); il loro costo tende a \\(|P|\\sigma_j\\). Sommando:
\\[
\\lim_{h\\to0}\\int_{J_{u_h}}|[u_h]|\\,d\\mathcal H^1
=|P|\\sum_j\\sigma_j=|P|\\|M\\|_*.
\\]
Le intersezioni fra famiglie di rette sono \\(\\mathcal H^1\\)-trascurabili. L'incollaggio su un numero finito di facce conserva i salti macroscopici nel limite, poiché le correzioni alle frontiere sono uniformemente \\(O(h)\\).

## 4. Corollario: difetto di rango uno

Se \\(M=\\sigma a\\otimes b\\) ha rango uno, allora
\\[
\\|M\\|_*=\\|M\\|_F=\\sigma.
\\]
La laminazione unidimensionale
\\[
u_h(\\xi)=\\widetilde G\\xi+b+
\\sigma h\\left\\lfloor\\frac{\\xi\\cdot b}{h}\\right\\rfloor a
\\]
raggiunge il costo \\(|P|\\sigma\\), uguale al lower bound. Dunque il caso rango uno è un corollario immediato del teorema generale, non un problema di cella distinto.

## 5. Ottimizzazione del campo bulk con penalità lineare

Sia \\(A\\in\\mathbb R^{3\\times2}\\) il gradiente macroscopico su una faccia. Per il bulk quadratico e il costo micro-interfaciale nucleare, consideriamo
\\[
\\min_{G\\in\\mathbb R^{3\\times2}}
\\left\{|G|_F^2+\\lambda\\|A-G\\|_*\\right\},
\\qquad \\lambda\\ge0.
\\]
Il fattore area della faccia moltiplica l'intero problema e non modifica il minimizzatore.

Sia \\(A=U\\operatorname{diag}(s_1,s_2)V^T\\) una SVD compatta, con \\(s_i\\ge0\\). Per invarianza unitaria e disuguaglianza di von Neumann, il problema si riduce alla minimizzazione sui valori singolari:
\\[
\\min_{x_i\\ge0}\\sum_i
\\left[x_i^2+\\lambda|s_i-x_i|\\right].
\\]
Ogni coordinata è minimizzata da
\\[
x_i^*=(s_i-\\lambda/2)_+.
\\]
Pertanto
\\[
\\boxed{G^*=U\\operatorname{diag}((s_i-\\lambda/2)_+)V^T,}
\\]
e il difetto ottimo è
\\[
\\boxed{M^*=A-G^*
=U\\operatorname{diag}(\\min(s_i,\\lambda/2))V^T.}
\\]
Il valore minimo per faccia, prima del fattore area, è
\\[
\\sum_i\\left[(s_i-\\lambda/2)_+^2
+\\lambda\\min(s_i,\\lambda/2)\\right].
\\]

**Precisazione sul rango.** Per \\(\\lambda>0\\), ogni valore singolare positivo di \\(A\\) produce un valore singolare positivo di \\(M^*\\). Quindi \\(\\operatorname{rank}M^*=\\operatorname{rank}A\\): non è corretto dire che il difetto ottimo diventa rango uno quando una sola singolarità supera la soglia. È invece il campo ottimo \\(G^*\\) ad avere rango pari al numero di singolarità di \\(A\\) che superano \\(\\lambda/2\\). Per \\(A\\) di rango due, il difetto ottimo resta di rango due per ogni \\(\\lambda>0\\), anche quando \\(G^*\\) ha rango uno o zero.

Per il candidato C60 con \\(A_f^TA_f=I_2\\), le due singolarità sono entrambe 1; dunque
\\[
G_f^*=(1-\\lambda/2)_+A_f,\\qquad
M_f^*=\\min(1,\\lambda/2)A_f.
\\]
Questa formula è una soluzione del problema penalizzato specificato, non un'affermazione che \\(G\\) sia libero in ogni modello cinematico DPO.

## 6. Ambito e limiti

Dimostrato:
- cell problem ottimale \\(\\mathcal C(M)=\\|M\\|_*\\) per \\(\\psi(a,\\nu)=|a|\\);
- recupero SVD e corollario di rango uno;
- minimizzatore soft-thresholding per \\( |G|_F^2+\\lambda\\|A-G\\|_*\\).

Non affermato:
- densità anisotrope o dipendenti dalla normale;
- campi bulk variabili all'interno delle facce;
- vincoli aggiuntivi di immersione, embeddedness o cinematica;
- teorema integrale CF generale su tutte le superfici poliedrali;
- soluzione del problema con bulk \\(W(G)=|G|_F\\) non quadratico.

