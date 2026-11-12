# Digamma–supergolden–Q6: programma analitico e audit delle identità

**Data:** 10 novembre 2026  
**Stato:** identità speciali esatte; campionamento numerico riproducibile; derivazione geometrica PSU/Q6 ancora aperta.

## Convenzione di notazione — origine comune, funzioni distinte\n\nIn questo dossier \(s=\psi_{\\rm SA}\) è sempre la costante superaurata, radice positiva di \(s^3-s^2-1=0\). La funzione digamma è scritta \(\\digamma(x)=d\\log\\Gamma(x)/dx\), e la trigamma \(\\digamma_1(x)=\\digamma'(x)\). Questa distinzione tipografica evita di usare lo stesso simbolo per la costante e per la funzione speciale. Il collegamento non è una semplice omonimia: le identità di shift, moltiplicazione e asintotica qui sotto valutano la digamma sulle scale generate da \(\\psi_{\\rm SA}\). Il dossier modulare collegato documenta inoltre il ponte Weber–Dedekind eta al discriminante \(-31\).\n\n## 1. Scelta di impostazione

Il digamma
\[
\psi(x)=\frac{\Gamma'(x)}{\Gamma(x)}=\frac{d}{dx}\log\Gamma(x)
\]
è assunto come osservabile analitico principale. La funzione Gamma codifica prodotti e normalizzazioni; il digamma ne misura la variazione infinitesima. La trigamma \(\psi_1=\psi'\) misura la risposta successiva.

Questa scelta non implica che il digamma generi automaticamente la costante superaurea. Il compito è verificare quali identità esatte del digamma siano compatibili con la relazione algebrica e con i raffinamenti discreti già presenti nel programma RGS–PSU.

La costante superaurea è indicata qui con \(s\), per non confonderla con la funzione digamma:
\[
s^3-s^2-1=0,\qquad s=1.4655712318767680266\ldots
\]
e quindi \(s^3=s^2+1\).

## 2. Identità esatte di partenza

### 2.1 Ricorrenza traslazionale

Dalla relazione \(\Gamma(x+1)=x\Gamma(x)\), derivando il logaritmo:
\[
\boxed{\psi(x+1)=\psi(x)+\frac1x.}
\]
Poiché \(s^3=s^2+1\), segue l'identità esatta:
\[
\boxed{\psi(s^3)-\psi(s^2)=s^{-2}.}
\]
Più in generale, per ogni intero \(n\geq0\):
\[
\psi(s^{n+3})-\psi(s^{n+2}+0)
\]
non si riduce alla ricorrenza precedente: infatti \(s^{n+3}-s^{n+2}=s^n\), che non è in generale un intero. La sola identità di shift immediata è quella per \(n=0\). Non si deve estendere abusivamente la ricorrenza a traslazioni non intere.

### 2.2 Formula di moltiplicazione di Gauss

Per un intero positivo \(m\):
\[
\boxed{\sum_{k=0}^{m-1}\psi\!\left(x+\frac{k}{m}\right)
=m\psi(mx)-m\log m.}
\]
Per \(m=3\) e \(x=s^3/3\), combinando con \(s^3=s^2+1\):
\[
\sum_{k=0}^{2}\psi\!\left(\frac{s^3+k}{3}\right)
=3\psi(s^2)+\frac{3}{s^2}-3\log3.
\]
È una relazione esatta che mette in comunicazione il valore del digamma alla scala superaurea con una terna di argomenti equispaziati. Il fattore 3 è intero: non si applica la formula di Gauss sostituendo \(m=s\), che sarebbe scorretto.

### 2.3 Derivata e positività

Per \(x>0\):
\[
\psi_1(x)=\psi'(x)=\sum_{j=0}^{\infty}\frac{1}{(x+j)^2}>0.
\]
Dunque il digamma è strettamente crescente sul semiasse positivo. Per ogni \(a,b>0\):
\[
\psi(b)-\psi(a)=\int_a^b\psi_1(t)\,dt.
\]
Questa formula fornisce una rappresentazione esatta delle differenze sulle scale \(s^n\), senza attribuire loro una ricorrenza inesistente.

## 3. Campionamento sulle scale superauree

Definiamo:
\[
d_n=\psi(s^n),\qquad
\delta_n=d_{n+1}-d_n.
\]
Il campionamento è un'osservabile analitica ben definita. Non è, da solo, una legge di sostituzione Q6.

Per \(x\to+\infty\), l'espansione asintotica è:
\[
\psi(x)\sim\log x-\frac{1}{2x}
-\sum_{k\geq1}\frac{B_{2k}}{2k\,x^{2k}}.
\]
Ponendo \(x=s^n\):
\[
\delta_n\sim\log s
+\frac12(s^{-n}-s^{-(n+1)})
+\sum_{k\geq1}\frac{B_{2k}}{2k}
(s^{-2kn}-s^{-2k(n+1)}).
\]
In particolare:
\[
\boxed{\lim_{n\to\infty}\delta_n=\log s.}
\]
Questa è una connessione rigorosa tra la scala moltiplicativa superaurea e l'incremento asintotico del digamma. È un limite analitico, non una prova che \(s\) sia una costante fisica universale.

### Valori numerici di riferimento

Valori calcolati ad alta precisione con \(s\) radice positiva di \(x^3-x^2-1\):

| \(n\) | \(s^n\) | \(\psi(s^n)\) |
|---:|---:|---:|
| 0 | 1.0000000000 | −0.5772156649015329 |
| 1 | 1.4655712319 | 0.0038048907409820 |
| 2 | 2.1478990357 | 0.5139994494721574 |
| 3 | 3.1478990357 | 0.9795706813489254 |
| 4 | 4.6134702676 | 1.4167047756372670 |
| 5 | 6.7613693033 | 1.8354570143139840 |
| 6 | 9.9092683390 | 2.2421648994574500 |

Il valore \(s^3=s^2+1\) è visibile direttamente nella tabella. I valori sono controlli numerici, mentre le identità delle sezioni 2 e 3 sono esatte.

## 4. Test che distinguono una vera legge da una coincidenza

Il test ingenuo
\[
d_{n+3}=d_{n+2}+d_n
\]
**non** segue da \(s^{n+3}=s^{n+2}+s^n\): il digamma non è una funzione additiva. Non va assunto come teorema. Può essere calcolato come difetto
\[
\mathcal E_n=d_{n+3}-d_{n+2}-d_n
\]
solo per verificare quantitativamente quanto fallisca.

Il collegamento corretto alla matrice supergolden deve essere cercato in una delle seguenti forme, senza circolarità:

1. **Osservabile di scala:** verificare se la sequenza \(\delta_n\), o una trasformazione esplicitamente motivata di essa, soddisfa una relazione lineare a coefficienti costanti. I coefficienti devono essere stimati su dati indipendenti e poi verificati fuori campione.
2. **Identità di moltiplicazione/partizione:** usare la formula di Gauss con interi \(m\), e costruire una successione di partizioni intere orientate. La regola locale deve essere definita geometricamente prima di confrontarla con \(A_s\).
3. **Operatore da dati digamma:** definire un operatore da valori integrali o differenze di \(\psi\), con normalizzazione fissata a priori; calcolarne polinomio caratteristico e residui senza inserire \(A_s\) nella definizione.

Il target combinatorio resta:
\[
A_s=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad \det(\lambda I-A_s)=\lambda^3-\lambda^2-1.
\]
La comparsa dello stesso polinomio in un operatore costruito indipendentemente dal digamma sarebbe un risultato nuovo. Un semplice campionamento di \(\psi(s^n)\) non basta.

## 5. Ponte con Q6, Anti-Twin e quaternioni

La catena di lavoro proposta è:

- **Analitico:** Gamma → digamma → trigamma; identità di shift, moltiplicazione e asintotica.
- **Discreto:** partizioni intere e orientate dei tre canali Q3 dentro Q6; conteggi dei figli e matrici di incidenza.
- **Anti-Twin:** specificare l'azione dell'involuzione sui canali e verificare equivarianza o scambio dei canali.
- **Quaternionico:** usare il coframe \(e_a(q)=q e_a q^{-1}\) per trasportare la terna orientata. Il quaternione fissa l'orientazione del riferimento, non i coefficienti di raffinamento.
- **Spettrale:** comprimere l'operatore geometrico sul sottospazio tridimensionale, controllare leakage e polinomio caratteristico.

La suddivisione midpoint T055 continua a dare \(2I_3\) sulla restrizione a tre direzioni: non produce \(A_s\). Il nuovo candidato deve quindi provenire da una partizione orientata diversa e documentata, non da una reinterpretazione della suddivisione midpoint.

## 6. Stato epistemico

| Affermazione | Stato |
|---|---|
| Ricorrenza \(\psi(x+1)=\psi(x)+1/x\) | **Identità esatta** |
| \(\psi(s^3)-\psi(s^2)=s^{-2}\) | **Identità esatta** |
| Formula di moltiplicazione di Gauss per \(m=3\) | **Identità esatta** |
| Monotonia e rappresentazione integrale via trigamma | **Identità esatta** |
| \(\delta_n\to\log s\) | **Conseguenza asintotica dimostrabile** |
| Campionamento numerico riportato | **Verifica numerica** |
| Ricorrenza di ordine tre per \(d_n\) | **Non dimostrata; non segue dall'algebra di \(s\)** |
| Operatore digamma con polinomio \(x^3-x^2-1\) | **Candidato da costruire** |
| Derivazione Q6/PSU della superaurea tramite digamma | **Aperta** |
| Interpretazione fisica universale | **Non dimostrata** |

## 7. Riferimenti e riproducibilità

Le identità usate sono quelle standard della funzione Gamma e delle funzioni poligamma (ricorrenza, formula di moltiplicazione di Gauss, serie della trigamma ed espansione asintotica di Stirling). Per riprodurre i valori della tabella è sufficiente calcolare la radice positiva di \(x^3-x^2-1\) ad alta precisione e valutare \(\operatorname{digamma}(s^n)\) con una libreria di precisione arbitraria.

Questo dossier integra, ma non sostituisce, [l'audit Q6–RGS–PSU del ponte supergolden](SUPERGOLDEN_Q6_RGS_BRIDGE_AUDIT_2026-11-10.md).
