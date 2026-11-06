# T049C — Intertwiner QLG a Dirac: classificazione e non unicità

## Enunciato

Sia \(V=\mathbb C^2\) la fibra QLG trasformata secondo la rappresentazione fondamentale \(U\) di \(SU(2)\), e sia \(D=\mathbb C^4\) la rappresentazione di Dirac ristretta al sottogruppo delle rotazioni spaziali. Nella convenzione del repository sorgente tale restrizione è
\[
D|_{\mathrm{Spin}(3)}=U\oplus U.
\]
Allora
\[
\mathrm{Hom}_{SU(2)}(V,D)
=\left\{K_{\alpha,\beta}=
\begin{pmatrix}\alpha I_2\\ \beta I_2\end{pmatrix}:
\alpha,\beta\in\mathbb C\right\},
\]
e lo spazio degli intertwiner ha dimensione complessa 2. Le mappe isometriche sono precisamente quelle con
\[
|\alpha|^2+|\beta|^2=1.
\]

## Dimostrazione

Scriviamo \(K=(A,B)^T\), con \(A,B\in M_2(\mathbb C)\). L'equivarianza
\[
(U(g)\oplus U(g))K=KU(g)
\]
equivale a \(U(g)A=AU(g)\) e \(U(g)B=BU(g)\) per ogni \(g\in SU(2)\). La rappresentazione fondamentale complessa di \(SU(2)\) è irriducibile; per il lemma di Schur il suo commutante è \(\mathbb C I_2\). Dunque \(A=\alpha I_2\), \(B=\beta I_2\), e non vi sono altri intertwiner. Inoltre \(K^\dagger K=(|\alpha|^2+|\beta|^2)I_2\), da cui la condizione d'isometria.

Poiché \(2I\subset SU(2)\), ogni tale \(K\) è anche \(2I\)-equivariante. Il risultato non dipende da una particolare enumerazione numerica degli elementi di \(2I\).

## Conseguenza per QLG–RGS–PSU

La fibra QLG a due componenti può essere inserita nella fibra Dirac a quattro componenti in infiniti modi isometrici, parametrizzati da \((\alpha,\beta)\in S^3\subset\mathbb C^2\). A fase globale irrilevante, resta una famiglia parametrizzata da \(\mathbb{CP}^1\). Le due inclusioni pure
\[
K_L=\binom{I_2}{0},\qquad K_R=\binom{0}{I_2}
\]
sono entrambe equivarianti sotto le rotazioni spaziali; anche le combinazioni miste lo sono.

**Quindi l'equivarianza sotto \(2I\), da sola, non seleziona un embedding fisico.** Non è lecito scegliere \(K_L\), \(K_R\), o una combinazione bilanciata e poi interpretarla come derivazione del settore Dirac. La scelta richiede un dato aggiuntivo: ad esempio una simmetria chirale/parità specificata, un operatore di massa/intertwiner dinamico, una struttura reale/quaternionica compatibile, o una rappresentazione dei boost che chiuda l'azione di Spin(1,3).

## Ostacolo Lorentziano

Il dato QLG disponibile specifica la rappresentazione spaziale \(SU(2)\), non un'azione dei boost su \(V\). Perciò non definisce una rappresentazione di \(\mathrm{Spin}(1,3)\) e non consente di imporre
\[
S_D(\Lambda)K=K S_{\mathrm{QLG}}(\Lambda)
\]
per trasformazioni di Lorentz generali. Il problema non è risolto dal solo raddoppio della dimensione: occorre costruire la trasformazione dei boost e dimostrarne la compatibilità con l'operatore QLG e con le connessioni discrete.

## Test riproducibile

Il modulo scripts/q6_qlg_dirac_intertwiner.py costruisce campioni SU(2), risolve numericamente il sistema lineare degli intertwiner e verifica dimensione 2, equivarianza e isometria per più scelte \((\alpha,\beta)\). Il test numerico controlla l'implementazione; la classificazione generale segue dal lemma di Schur.

## Stato epistemico

- **Dimostrato:** classificazione di \(\mathrm{Hom}_{SU(2)}(\mathbb C^2,\mathbb C^2\oplus\mathbb C^2)\), dimensione 2 e condizione d'isometria.
- **Verificabile numericamente:** audit dei residui su campioni di \(SU(2)\), che include il sottogruppo binario icosaedrico come conseguenza teorica.
- **Non dimostrato / aperto:** quale, se esiste, embedding è selezionato dalla dinamica QLG; estensione Lorentziana; compatibilità con la struttura quaternionica e con la parità; derivazione del bilineare assiale e della normalizzazione Noether.
- **Conseguenza metodologica:** T049B può calcolare \(J_5^a\) soltanto dopo aver ricevuto spinori Dirac a quattro componenti. T049C mostra che i dati QLG a due componenti non determinano tali spinori in modo canonico. Nessun esponente cosmologico RGS–PSU viene quindi inferito da un embedding scelto ad hoc.
