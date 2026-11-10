# Digamma–supergolden–Q6: programma analitico e audit delle identità

**Data:** 10 novembre 2026  
**Stato:** identità speciali esatte; campionamento numerico riproducibile; derivazione geometrica PSU/Q6 ancora aperta.

## 1. Scelta di impostazione

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
Per gli esponenti successivi vale \\(s^{n+3}-s^{n+2}=s^n\\), ma la ricorrenza del digamma riguarda uno shift di un intero, non uno shift arbitrario. Quindi per \\(n>0\\) non si può dedurre \\(\\psi(s^{n+3})-\\psi(s^{n+2})=s^{-n}\\). La relazione algebrica tra le potenze non è una proprietà additiva del digamma.

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

## 3. La connessione diretta digamma–supergolden–\(\pi\)

La relazione che mancava nel primo audit è la formula di riflessione delle funzioni poligamma:
\[
\boxed{\psi(1-z)-\psi(z)=\pi\cot(\pi z),\qquad z\notin\mathbb Z.}
\]
Ponendo \(z=s\), con \(s\) radice di \(s^3-s^2-1=0\), si ottiene direttamente:
\[
\boxed{\psi(1-s)-\psi(s)=\pi\cot(\pi s).}
\]
Per mantenere entrambi gli argomenti del digamma positivi, poniamo invece \(z=s-1\in(0,1)\):
\[
\psi(2-s)-\psi(s-1)=\pi\cot(\pi(s-1))
=\pi\cot(\pi s).
\]
Usando anche la ricorrenza \(\psi(s)=\psi(s-1)+(s-1)^{-1}\):
\[
\boxed{\psi(2-s)-\psi(s)+\frac1{s-1}=\pi\cot(\pi s).}
\]
Questa è una connessione esatta e non una semplice sostituzione numerica: lo stesso argomento superaureo compare nella funzione trigonometrica periodica, mentre il digamma ne lega i valori riflessi. La formula contiene esplicitamente \(\pi\).

La formula di riflessione non dimostra che \(s\) determini \(\pi\), né che \(\pi\) sia algebrico: \(\pi\) entra come costante della struttura Gamma/trigonometrica. Il risultato dimostrato è una relazione trascendente esatta che valuta il digamma in argomenti legati a \(s\).

Un secondo punto di contatto è la formula di moltiplicazione di Gauss, che lega valori del digamma a \(\log m\), mentre i valori speciali della Gamma e le formule di riflessione/duplicazione coinvolgono \(\pi\) (per esempio \(\Gamma(1/2)=\sqrt\pi\)). Queste identità vanno mantenute distinte: la formula di Gauss da sola non introduce \(\pi\).

### 3.1 La sezione argentea: un secondo valore esatto del digamma

Introduciamo una notazione distinta dalla costante superaurea \(s\):
\[
\delta=1+\sqrt2,\qquad \delta^2-2\delta-1=0.
\]
\(\delta\) è il rapporto argenteo. L'identità trigonometrica esatta
\[
\boxed{\cot(\pi/8)=1+\sqrt2=\delta}
\]
segue dalla formula dell'angolo metà, oppure da \(\tan(\pi/8)=\sqrt2-1\).

Applicando la stessa formula di riflessione del digamma a \(z=1/8\):
\[
\boxed{
\psi(7/8)-\psi(1/8)
=\pi\cot(\pi/8)
=\pi(1+\sqrt2)
=\pi\delta.
}
\]
Quindi il rapporto argenteo non è soltanto un valore geometrico della cotangente: è esattamente il coefficiente della differenza fra due valori razionali del digamma. La relazione contiene \(\pi\) in modo esplicito ed è un'identità analitica esatta.

Le due connessioni vanno tenute affiancate ma non confuse:
\[
\begin{aligned}
\psi(7/8)-\psi(1/8)&=\pi\delta,
&&\delta=1+\sqrt2,\\
\psi(2-s)-\psi(s)+(s-1)^{-1}&=\pi\cot(\pi s),
&&s^3-s^2-1=0.
\end{aligned}
\]
La prima seleziona l'angolo razionale \(\pi/8\) e il rapporto argenteo; la seconda valuta la riflessione al parametro superaureo. Non è ancora dimostrata un'identità algebrica che trasformi \(\cot(\pi s)\) in \(\delta\), né una derivazione comune dei due numeri dalla geometria Q6/PSU. La loro presenza nella medesima formula di riflessione è il ponte analitico rigoroso; il ponte geometrico resta una domanda di ricerca.

**Nota di notazione:** in tutto il dossier \(s\) indica esclusivamente la costante superaurea; \(\delta\) indica esclusivamente il rapporto argenteo. Non usare \(s\) per entrambe.

### 3.2 La sezione aurea: un terzo valore razionale

La costante aurea
\[
\varphi=\frac{1+\sqrt5}{2}=2\cos(\pi/5)
\]
è legata all'angolo di 36 gradi. Dalla relazione
\[
\cot^2(\pi/5)=\frac{1+\cos(2\pi/5)}{1-\cos(2\pi/5)}
=1+\frac{2}{\sqrt5},
\]
e dal fatto che \(\cot(\pi/5)>0\), segue
\[
\cot(\pi/5)=\sqrt{1+\frac{2}{\sqrt5}}.
\]
La riflessione del digamma in \(z=1/5\) dà pertanto
\[
\boxed{
\psi(4/5)-\psi(1/5)
=\pi\cot(\pi/5)
=\pi\sqrt{1+\frac{2}{\sqrt5}}.
}
\]
Questa è una relazione esatta nel campo algebrico generato da \(\sqrt5\); la sua connessione con \(\varphi\) passa dall'angolo caratteristico del pentagono regolare. Non si deve però sostituire il coefficiente con \(\varphi\): infatti \(\cot(\pi/5)\ne\varphi\).

Il quadro dei tre casi è quindi:
\[
\begin{aligned}
\psi(7/8)-\psi(1/8)&=\pi(1+\sqrt2),\\
\psi(4/5)-\psi(1/5)&=\pi\sqrt{1+2/\sqrt5},\\
\psi(2-s)-\psi(s)+(s-1)^{-1}&=\pi\cot(\pi s).
\end{aligned}
\]
I primi due sono valori razionali dell'argomento del digamma, associati rispettivamente alle geometrie dell'ottagono e del pentagono; il terzo usa l'argomento algebrico irrazionale \(s\). È un unico meccanismo analitico (riflessione), ma non ancora una legge geometrica unificante.


### 3.3 Duplicazione angolare: il test esatto della sezione argentea

Per separare una vera legge di moltiplicazione angolare da una coincidenza, definiamo
\[
C_n(t)=\cot(n\theta)\quad\text{quando }t=\cot\theta.
\]
Dalla formula di addizione della cotangente:
\[
C_1(t)=t,\qquad
\boxed{C_{n+1}(t)=\frac{tC_n(t)-1}{t+C_n(t)}}
\]
quando il denominatore è diverso da zero. In particolare,
\[
C_2(t)=\frac{t^2-1}{2t}.
\]
Per il rapporto argenteo, la relazione minima
\[
\delta^2-2\delta-1=0
\]
implica esattamente
\[
C_2(\delta)=\frac{\delta^2-1}{2\delta}=1.
\]
Poiché \(\delta=\cot(\pi/8)\), questo è precisamente
\[
\boxed{\cot(\pi/4)=1.}
\]
La stessa affermazione, riscritta con la riflessione del digamma, è
\[
\boxed{
\psi(7/8)-\psi(1/8)=\pi\delta,
\qquad
\psi(3/4)-\psi(1/4)=\pi.
}
\]
Quindi la relazione quadratica dell'argentea è compatibile con la duplicazione dell'angolo; non è una semplice analogia numerica.

### 3.4 Test di moltiplicazione angolare per la supergolden

Per \(\theta=\pi s\), la stessa ricorrenza definisce esattamente
\[
C_n(\cot(\pi s))=\cot(n\pi s).
\]
La relazione cubica \(s^3-s^2-1=0\) è una relazione fra il parametro \(s\) e le sue potenze; non è una relazione fra \(\cot(\pi s)\) e le sue potenze. Pertanto non autorizza a sostituire \(t=s\) nella ricorrenza delle cotangenti, né produce automaticamente un'equazione cubica per \(t=\cot(\pi s)\).

Un controllo numerico esplorativo, con la radice positiva di \(s^3-s^2-1=0\), dà:
| \(n\) | \(\cot(n\pi s)\) |
|---:|---:|
| 1 | 0.10858493479947186 |
| 2 | −4.550397869463016 |
| 3 | 0.3363727104100731 |
| 4 | −2.165318433214175 |

Questi numeri sono soltanto controlli della ricorrenza trigonometrica; non sono autovalori RGS e non dimostrano una legge di raffinamento.

C'è inoltre una distinzione aritmetica utile. Poiché \(s\) è algebrico irrazionale, il teorema di Gelfond–Schneider implica che \(e^{\pi i s}\), valore di \((-1)^s\) ottenuto con il logaritmo principale, è trascendente. Ne segue che \(\cot(\pi s)\) è trascendente: se fosse algebrico, dalla relazione
\[
e^{2\pi i s}=\frac{\cot(\pi s)+i}{\cot(\pi s)-i}
\]
risulterebbe algebrico anche \(e^{2\pi i s}\), in contraddizione. Dunque il coefficiente trigonometrico della riflessione al parametro supergolden non può essere identificato con il rapporto argenteo, che è algebrico.

**Esito del test:** l'argentea chiude esattamente sotto la duplicazione angolare; per la supergolden è definita una dinamica di moltiplicazione angolare, ma la cubica di \(s\) non ne è il polinomio caratteristico. Un eventuale ponte RGS deve derivare da dati geometrici indipendenti.

## 4. Campionamento sulle scale superauree

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

## 5. Test che distinguono una vera legge da una coincidenza

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

## 6. Ponte con Q6, Anti-Twin e quaternioni

La catena di lavoro proposta è:

- **Analitico:** Gamma → digamma → trigamma; identità di shift, moltiplicazione e asintotica.
- **Discreto:** partizioni intere e orientate dei tre canali Q3 dentro Q6; conteggi dei figli e matrici di incidenza.
- **Anti-Twin:** specificare l'azione dell'involuzione sui canali e verificare equivarianza o scambio dei canali.
- **Quaternionico:** usare il coframe \(e_a(q)=q e_a q^{-1}\) per trasportare la terna orientata. Il quaternione fissa l'orientazione del riferimento, non i coefficienti di raffinamento.
- **Spettrale:** comprimere l'operatore geometrico sul sottospazio tridimensionale, controllare leakage e polinomio caratteristico.

La suddivisione midpoint T055 continua a dare \(2I_3\) sulla restrizione a tre direzioni: non produce \(A_s\). Il nuovo candidato deve quindi provenire da una partizione orientata diversa e documentata, non da una reinterpretazione della suddivisione midpoint.

## 7. Stato epistemico

| Affermazione | Stato |
|---|---|
| Ricorrenza \(\psi(x+1)=\psi(x)+1/x\) | **Identità esatta** |
| \(\psi(s^3)-\psi(s^2)=s^{-2}\) | **Identità esatta** |
| Formula di moltiplicazione di Gauss per \(m=3\) | **Identità esatta** |
| Monotonia e rappresentazione integrale via trigamma | **Identità esatta** |
| \(\psi(7/8)-\psi(1/8)=\pi(1+\sqrt2)\) | **Identità esatta: sezione argentea** |
| \(\psi(4/5)-\psi(1/5)=\pi\sqrt{1+2/\sqrt5}\) | **Identità esatta: angolo aureo** |
| \(\delta_n\to\log s\) | **Conseguenza asintotica dimostrabile** |
| Duplicazione \(C_2(\delta)=1\) dalla relazione \(\delta^2=2\delta+1\) | **Identità esatta** |
| Trascendenza di \(\cot(\pi s)\) (Gelfond–Schneider) | **Conseguenza teorica esatta** |
| Ricorrenza \(C_{n+1}=(tC_n-1)/(t+C_n)\) | **Identità trigonometrica esatta** |
| Campionamento numerico riportato | **Verifica numerica** |
| Ricorrenza di ordine tre per \(d_n\) | **Non dimostrata; non segue dall'algebra di \(s\)** |
| Operatore digamma con polinomio \(x^3-x^2-1\) | **Candidato da costruire** |
| Derivazione Q6/PSU della superaurea tramite digamma | **Aperta** |
| Interpretazione fisica universale | **Non dimostrata** |

## 8. Riferimenti e riproducibilità

Le identità usate sono quelle standard della funzione Gamma e delle funzioni poligamma (ricorrenza, formula di moltiplicazione di Gauss, serie della trigamma ed espansione asintotica di Stirling). Per riprodurre i valori della tabella è sufficiente calcolare la radice positiva di \(x^3-x^2-1\) ad alta precisione e valutare \(\operatorname{digamma}(s^n)\) con una libreria di precisione arbitraria.

Questo dossier integra, ma non sostituisce, [l'audit Q6–RGS–PSU del ponte supergolden](SUPERGOLDEN_Q6_RGS_BRIDGE_AUDIT_2026-11-10.md).

## Teorema formalizzato

La classificazione aritmetica della riflessione del digamma è stata isolata in un enunciato autonomo, con dimostrazione:

- [Teorema — legge di riflessione del digamma e dicotomia razionale/irrazionale](../theorems/DIGAMMA_REFLECTION_CYCLOTOMIC_LAW.md) — **dimostrato**.

Il teorema prova che per un parametro algebrico razionale il coefficiente cotangente è algebrico, mentre per un parametro algebrico irrazionale è trascendente. La derivazione di un unico operatore geometrico Q6/PSU resta aperta.


## Teorema di crescita e incremento digamma

Il collegamento fra una sostituzione orientata astratta a tre canali e il digamma è ora formalizzato nel [teorema di crescita supergolden a tre canali](../theorems/ORIENTED_THREE_CHANNEL_SUPERGOLDEN_GROWTH_LAW.md). Il risultato dimostrato è
\[
N_{n+3}=N_{n+2}+N_n,\qquad
\frac{N_{n+1}}{N_n}\longrightarrow s,\qquad
\psi(N_{n+1})-\psi(N_n)\longrightarrow\log s.
\]
La derivazione geometrica della sostituzione dai dati Q6/PSU resta esplicitamente aperta.

## Legge angolare derivata dalla similarità quadrata Kathara

La trasformazione quadrata registrata nel programma Kathara è
\[
T=\begin{pmatrix}1&1\\-1&1\end{pmatrix}
=\sqrt2R(-\pi/4).
\]
Il suo angolo di rotazione è \(\alpha=\pi/4\), e quindi la cotangente del semiangolo è il rapporto argenteo. La derivazione completa, con la riflessione del digamma, è ora un teorema autonomo:
[Legge angolare Kathara–argentea–digamma](../theorems/KATHARA_SILVER_DIGAMMA_ANGLE_LAW.md).

Questo è un ponte geometrico-analitico dimostrato per la branca argentea. Non va confuso con una derivazione spettrale della superaurea.
