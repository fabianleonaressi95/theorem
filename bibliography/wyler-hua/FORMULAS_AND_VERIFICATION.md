# F001–F002 — Wyler, Robertson, Gilmore, Adler e Hua: estrazione preliminare delle formule

**Stato complessivo:** formule selezionate trascritte da fonti reperibili; verifica indipendente solo parziale. Nessuna formula qui riportata costituisce, da sola, una derivazione fisica della costante di struttura fine o una validazione del modello RGS.

## F001 — Espressione di Wyler per la costante di struttura fine

La formula attribuita a Wyler e riportata da Stephen L. Adler è

\[
\alpha_W=\frac{9}{8\pi^4}\left(\frac{\pi^5}{2^4\,5!}\right)^{1/4}
\simeq \frac{1}{137.0360824}.
\]

La stessa espressione è riportata da MathWorld. È una formula numerica adimensionale. La sua vicinanza al valore sperimentale non dimostra che sia derivata dalla QED o da una teoria fisica fondamentale.

### Controllo storico essenziale

- **Robertson (1971):** osserva che l'accordo con l'esperimento richiede una scelta arbitraria del raggio delle regioni geometriche pari a 1; segnala che la relazione con il gruppo d'invarianza dell'equazione d'onda non dipende da quel raggio.
- **Gilmore (1972):** risponde alla questione della scelta di scala sostenendo che, per la scelta indicata, gli elementi del dominio limitato sono rappresentanti di coset e le operazioni sono operazioni di gruppo. Questo argomento va verificato nel testo integrale e non va riassunto come una derivazione della costante fisica.
- **Adler (1972):** classifica la proposta nella sezione delle speculazioni numerologiche e conclude che resta aperto se l'accordo con l'esperimento abbia una base fisica o sia fortuito.

**Conclusione provvisoria:** la formula numerica è attribuita e trascritta; il suo status fisico rimane non dimostrato. La risposta di Gilmore affronta una questione geometrico-gruppale di scala, ma non basta a stabilire un meccanismo che produca il valore osservato di alpha.

## F002 — Hua: domini classici e operatori differenziali

### Dominio di tipo I

Per matrici complesse \(Z\in\mathbb C^{p\times q}\), con \(p\le q\), la convenzione moderna usata nella fonte di confronto è

\[
D^I_{p,q}=\{Z:I_p-ZZ^*>0\},
\]

dove \(Z^*=\overline Z^{\,t}\) e \(>0\) significa definita positiva. La frontiera è contenuta in \(I_p-ZZ^*\ge0\) e soddisfa \(\det(I_p-ZZ^*)=0\).

Ponendo
\[
V(Z)=I_p-ZZ^*,\qquad
V_{jk}=\delta_{jk}-\sum_{\ell=1}^q z_{j\ell}\overline z_{k\ell},
\]
l'operatore di Hua di tipo I nella convenzione riportata è
\[
\Delta_1=\sum_{j,k=1}^p V_{jk}\Delta_1^{jk},
\]
\[
\Delta_1^{jk}=\sum_{\alpha,\beta=1}^q
\left(\delta_{\alpha\beta}-\sum_{\ell=1}^p
z_{\ell\alpha}\overline z_{\ell\beta}\right)
\frac{\partial^2}{\partial z_{j\alpha}\,\partial\overline z_{k\beta}}.
\]

### Dominio di tipo IV (Lie ball)

Per \(Z=(z_1,\ldots,z_n)\in\mathbb C^n\), si definiscono
\[
s(Z)=\sum_{j=1}^n z_j^2,\qquad
r(Z)=1-2\lVert Z\rVert^2+|s(Z)|^2.
\]
La formula dell'operatore di Hua di tipo IV riportata nella fonte moderna di confronto è
\[
\Delta_4=\sum_{j,k=1}^n
\left[
r(Z)(\delta_{jk}-2z_j\overline z_k)
+2(\overline z_j-s(\overline Z)z_j)
(z_k-s(Z)\overline z_k)
\right]
\frac{\partial^2}{\partial z_j\,\partial\overline z_k}.
\]

**Attenzione alle convenzioni:** la classificazione dei tipi II e III viene scambiata in alcune pubblicazioni. Non copiare formule fra fonti senza controllare la convenzione. Inoltre, l'espressione sopra è una trascrizione da un articolo moderno che cita Hua e Lu; prima di marcarla come verificata rispetto all'edizione AMS 1963 occorre confrontare la pagina originale della monografia.

### Formula di rappresentazione di Poisson–Szegő

Per un dominio classico \(D\), la fonte moderna riporta che, per dato al bordo \(\phi\) sulla frontiera di Shilov \(S(D)\), una funzione Bergman-armonica è rappresentata da
\[
u(z)=\int_{S(D)}P(z,w)\,\phi(w)\,d\sigma(w),
\]
dove \(P(z,w)\) è il kernel di Poisson–Szegő e \(d\sigma\) la misura di riferimento della frontiera. La versione inversa richiede le ipotesi di regolarità e continuità dichiarate nel teorema citato; non va estesa senza controlli a domini o misure diversi.

## Controlli ancora necessari

1. Reperire la scansione/edizione primaria dei due brevi articoli di Wyler e confrontare la derivazione geometrica e le normalizzazioni.
2. Leggere integralmente Robertson e Gilmore, non soltanto gli abstract, e trascrivere i passaggi sulla scala e sui rappresentanti di coset.
3. Estrarre dal rapporto originale di Adler la discussione e le equazioni circostanti (23).
4. Confrontare gli operatori di Hua sopra riportati con le pagine originali della monografia AMS 1963 e con le convenzioni di Lu.
5. Per il dominio IV in dimensione 5, ricavare esplicitamente la funzione norma generica, la metrica di Bergman, il determinante metrico e la densità di volume prima di collegarli a T002.
6. Separare il volume euclideo, il volume della metrica invariante e ogni volume regolarizzato: non sono intercambiabili.

## Fonti consultate

1. A. Wyler, “L’espace symétrique du groupe des équations de Maxwell”, *C. R. Acad. Sci. Paris* 269 (1969), 743–745.
2. A. Wyler, “Les groupes des potentiels de Coulomb et de Yukawa”, *C. R. Acad. Sci. Paris A* 271 (1971), 186–188.
3. B. Robertson, “Wyler’s Expression for the Fine-Structure Constant alpha”, *Physical Review Letters* 27 (1971), 1545–1547, DOI: 10.1103/PhysRevLett.27.1545.
4. R. Gilmore, “Scaling of Wyler’s Expression for alpha”, *Physical Review Letters* 28 (1972), 462–464, DOI: 10.1103/PhysRevLett.28.462.
5. S. L. Adler, “Theories of the Fine Structure Constant alpha”, FERMILAB-PUB-72/059-T (1972), Eq. (23).
6. L. K. Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains*, Translations of Mathematical Monographs 6, AMS (1963), DOI: 10.1090/mmono/006.
7. “Bergman-Harmonic Functions on Classical Domains”, *International Mathematics Research Notices* (2021), per la trascrizione moderna degli operatori e della rappresentazione di Poisson–Szegő. Questa è fonte secondaria per le formule attribuite a Hua.

## Relazione con THEROEM

Questa scheda prepara l'audit dei risultati T002–T008. Non modifica quei teoremi e non assume che la formula di Wyler determini il dominio, la misura o il cutoff del modello. Ogni passaggio verso la marginale Wilson Q6 dovrà essere dimostrato separatamente.
