# Morandotti D3 — limite debole del dipolo di disclinazioni verso la dislocazione

**Stato:** derivazione distribuzionale e test di sorgente discreta proposto; nessuna prova di convergenza energetica o di equivalenza completa del modello di Cesana–De Luca–Morandotti è rivendicata.

## 1. Convenzioni fissate

Nel benchmark piano si usa
\[
\zeta=\sum_j |b^j|\,\partial_{n_j}\delta_{x_j}
      -\sum_k s^k\delta_{y_k},
\qquad
n_j=\frac{(-b_2^j,b_1^j)}{|b^j|}.
\]
Per una funzione test \(\varphi\),
\[
\langle\partial_n\delta_x,\varphi\rangle
=-\partial_n\varphi(x).
\]
Quindi il carico di una dislocazione \(b\) è
\[
\langle\zeta_b,\varphi\rangle=-|b|\,\partial_n\varphi(x)
=b_2\partial_1\varphi(x)-b_1\partial_2\varphi(x).
\]

## 2. Dipolo simmetrico e momento di Burgers

Sia \(n=b^\perp/|b|\), \(d>0\), e si pongano
\[
y_+=x+\frac d2n,\qquad y_-=x-\frac d2n,
\qquad s_d=\frac{|b|}{d}.
\]
Si scelgano le cariche di Frank \(+s_d\) in \(y_+\) e \(-s_d\) in \(y_-\). Con la convenzione di sorgente precedente,
\[
\zeta_d=-s_d\delta_{y_+}+s_d\delta_{y_-}.
\]
Per ogni \(\varphi\in C^3\) in un intorno di \(x\),
\[
\begin{aligned}
\langle\zeta_d,\varphi\rangle
&=s_d\left[\varphi\left(x-\frac d2n\right)
             -\varphi\left(x+\frac d2n\right)\right]\\
&=-|b|\,\partial_n\varphi(x)+O(d^2)\\
&=\langle |b|\partial_n\delta_x,\varphi\rangle+O(d^2).
\end{aligned}
\]
Pertanto \(\zeta_d\to |b|\partial_n\delta_x\) in senso distribuzionale. La relazione di primo momento è
\[
\boxed{|b|=s_d d.}
\]
Il verso del dipolo è fissato da \(n=b^\perp/|b|\) e dall'ordine dei segni delle due cariche. Invertire una sola di queste convenzioni inverte il Burgers risultante.

## 3. Cosa dimostra e cosa non dimostra

La derivazione dimostra il limite della **sorgente** contro funzioni test regolari, con errore di differenza centrale \(O(d^2)\). Non dimostra da sola:
- convergenza delle soluzioni elastiche;
- convergenza o equivalenza delle energie;
- il trattamento dei termini divergenti/core energy;
- uniformità rispetto a un raggio di core \(\varepsilon\to0\);
- il limite dinamico di coppie di disclinazioni.

Per confrontare le energie serve la precisa normalizzazione del teorema di riferimento, inclusi core, riscalamento e termini rinormalizzati. La sequenza \(h\to0\), \(d\to0\), \(\varepsilon\to0\) va studiata separando i tre parametri; una diagonale simultanea non identifica il limite.

## 4. Test numerico implementato sul prototipo BFS

Il test aggiunto a `tests/test_morandotti_bfs_kkt.py` confronta:
1. il carico discreto di una dislocazione con Burgers fissato;
2. il carico di un dipolo di Frank simmetrico, con \(s_d=|b|/d\);
3. lo stesso raggio gaussiano di core, la stessa mesh e la stessa quadratura per i due carichi.

Per separazioni decrescenti \(d=0.24,0.12,0.06\), il test richiede che la norma della differenza fra i due vettori di carico diminuisca. Questo è un test di consistenza della **sorgente discreta** per la specifica griglia/quadratura; non è un test di convergenza energetica e non sostituisce il confronto CIP-DG.

## 5. Prossimi gate

1. Eseguire il test e registrare l'output CI, senza anticiparne l'esito.
2. Ripetere a più livelli \(h\) mantenendo prima \(\varepsilon\) fisso.
3. A mesh risolta, variare \(\varepsilon\) e poi \(d\), registrando \(h/\varepsilon\), \(d/\varepsilon\), energia, errore di stress e condizionamento.
4. Sostituire la convenzione gaussiana prototipale con il core esatto del problema di riferimento.
5. Confrontare la sequenza energetica con il risultato variazionale pubblicato e con la baseline CIP-DG 2026.

**Classificazione:** limite distribuzionale della sorgente derivato; test discreto aggiunto ma non ancora eseguito in questa sessione; equivalenza energetica e convergenza del metodo RGS–PRISM aperte.

**FLN**
