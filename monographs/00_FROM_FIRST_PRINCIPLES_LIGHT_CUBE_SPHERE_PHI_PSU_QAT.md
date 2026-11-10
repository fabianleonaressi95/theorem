# Ricostruzione dalle fondamenta — luce, cubo-sfera, π→φ, 2I e PSU–Anti-Twin

**Stato:** documento di apertura della ricostruzione integrale  
**Data:** 10 novembre 2026  
**Scopo:** ripartire dalle motivazioni e dalle unità fondamentali, prima dei grafi Q6, di PRISM, dei benchmark FEEC e delle implementazioni. Questo testo non sostituisce le derivazioni originarie: le ordina, identifica ciò che è già esatto e indica ciò che va recuperato dai quaderni e dai file storici.

> **Vincolo editoriale:** QLG non è assunto come filone fondativo né come asse della ricostruzione. Il percorso da ricostruire è luce/unità fondamentali → geometria cubo-sfera → derivazione π→φ e struttura aurea → quaternioni/2I e geometria sferica → PSU–Anti-Twin → Q-ball/QAT → interfacce con stringhe e Calabi–Yau. Q6 e PRISM entrano dopo, come discretizzazioni e laboratori matematici, non come punto di partenza.

## 0. La domanda originaria

La domanda non è inizialmente «quale grafo usare?» o «quale Laplaciano converge?». È: **quale struttura geometrica minima può organizzare luce, causalità, unità fondamentali e doppio foglio spazio-temporale senza introdurre parametri arbitrari?**

Il primo schema storico da recuperare integralmente è la catena ZPE–vuoto–cutoff–scala geometrica–massa/potenziale. Nei quaderni precedenti è stata registrata nella forma
\[
\mathrm{ZPE}\to\rho_{\rm vac}\to\ell\to\rho_p\to(\eta,R)\to m,\,F,\,V.
\]
Le formule annotate erano \(\rho_{\rm vac}=6\hbar c/(\pi\ell^4)\), \(\ell=\sqrt{\hbar G/c^3}=\ell_P\), \(\rho_p=3\hbar c/(\pi r_p^4)\), \(r_p=4\lambda_p\) e \(m_p=\sqrt{\alpha_g}\,m_\ell\). Queste espressioni sono **formule storiche del modello da sottoporre a audit dimensionale e fisico**, non vengono qui promosse a identità standard né a risultati verificati. Il recupero deve chiarire definizioni di \(\rho_p,r_p,\lambda_p,\eta,R,\alpha_g,m_\ell\), unità, normalizzazioni e derivazione di ogni fattore numerico.

Il punto di partenza è il ruolo della luce e delle costanti che fissano le scale:
\[
c,\qquad \hbar,\qquad G,\qquad
\ell_P=\sqrt{\frac{\hbar G}{c^3}},\qquad
t_P=\sqrt{\frac{\hbar G}{c^5}},\qquad
E_P=\sqrt{\frac{\hbar c^5}{G}}.
\]
Queste definizioni sono standard. Il progetto deve spiegare se e come la geometria proposta produce relazioni fra tali scale; non può ridefinirle per adattare uno spettro numerico.

Tre livelli vanno tenuti distinti:
1. **unità dimensionali standard**: definizioni di \(\ell_P,t_P,E_P\);
2. **costruzione geometrica**: cubo, sfera, direzioni, raggi e fogli;
3. **interpretazione fisica**: identificazione della costruzione con fotone, evento, tempo o struttura dello spazio. Quest'ultimo livello richiede equazioni del moto e confronto con Maxwell e relatività.

## 1. Cubo e sfera: geometria radiale prima della discretizzazione

Sia il cubo centrato nell'origine
\[
C_a=[-a,a]^3.
\]
Per una direzione unitaria \(n=(n_1,n_2,n_3)\in S^2\), il raggio fino alla superficie del cubo è
\[
r_C(n)=\frac{a}{\|n\|_\infty},
\qquad
\|n\|_\infty=\max_i|n_i|.
\]
La sfera inscritta di raggio \(a\) ha raggio radiale costante
\[
r_S(n)=a.
\]
La differenza radiale è quindi
\[
\Delta r(n)=a\left(\frac{1}{\|n\|_\infty}-1\right).
\]
Questa è un'identità geometrica esatta, non una legge fisica. Quantifica l'anisotropia radiale del cubo rispetto alla sfera e fornisce una prima funzione geometrica senza pesi scelti a mano.

Per una rotazione \(R\), la stessa costruzione nel riferimento ruotato diventa
\[
r_{C,R}(n)=\frac{a}{\|R^{-1}n\|_\infty}.
\]
Il Jacobiano della mappa radiale tridimensionale associata, quando la mappa è definita come \(x\mapsto a q_R(\hat x)x\) con \(q_R(n)=1/\|R^{-1}n\|_\infty\), va derivato includendo la dipendenza angolare; non va sostituito automaticamente con il solo fattore radiale. La formula \(a^3q_R^3\) vale per il volume di una trasformazione omotetica a direzione fissata, non è da sola il Jacobiano completo di una mappa angolarmente variabile.

**Conseguenza:** il cubo-sfera definisce un campo di anisotropia geometrica. Non dimostra ancora che un fotone sia una sfera inscritta in un cubo, né che l'anisotropia sia osservabile fisicamente. Questo è il primo oggetto da portare da geometria a dinamica.

## 2. Il passaggio π→φ: origine pentagonale della struttura aurea

Il rapporto aureo non va introdotto come costante scelta per fitting. La sua origine geometrica elementare è la simmetria pentagonale. Per un pentagono regolare, l'angolo al centro associato a un lato è
\[
\frac{2\pi}{5}.
\]
La metà è \(\pi/5\). La geometria della diagonale e del lato, insieme alla relazione corda-raggio, porta a
\[
\ell=2R\sin\left(\frac{\pi}{5}\right),\qquad
 d=2R\sin\left(\frac{2\pi}{5}\right),\qquad
\frac d\ell=\frac{\sin(2\pi/5)}{\sin(\pi/5)}
=2\cos\left(\frac{\pi}{5}\right)=\varphi.
\]
La diagonale \(d\) e il lato \(\ell\) del pentagono regolare hanno quindi rapporto aureo. Dalla geometria delle corde si ottiene l'equazione
\[
\varphi^2-\varphi-1=0,
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]
La stessa relazione si può ricavare dalla somma delle radici quinte dell'unità, scegliendo la radice reale positiva pertinente. Questa è la relazione esatta che connette l'angolo razionale in \(\pi\) alla radice quadratica aurea.

La catena da documentare nel suo ordine originario è:
\[
\pi\;\longrightarrow\;\frac{\pi}{5}
\;\longrightarrow\;2\cos(\pi/5)
\;\longrightarrow\;\varphi
\;\longrightarrow\;\mathbb Q(\sqrt5).
\]
Non basta citare la formula finale: nella ricostruzione completa vanno riportati il disegno, il rapporto diagonale/lato, l'equazione quadratica e il punto in cui la simmetria a cinque pieghe entra nella geometria tridimensionale.

**Precisazione epistemica:** l'identità pentagonale è matematica esatta. Il fatto che essa sia il seme necessario della geometria RGS–PSU è una scelta architetturale del programma; l'identificazione con una costante fisica richiede una derivazione ulteriore.

## 3. Dalla struttura aurea all'icosaedro, ai quaternioni e a 2I

L'icosaedro regolare porta la simmetria a cinque pieghe in tre dimensioni. Le coordinate canoniche dei suoi vertici si esprimono tramite permutazioni cicliche di
\[
(0,\pm1,\pm\varphi),
\]
con la normalizzazione da dichiarare esplicitamente. Il gruppo delle rotazioni dell'icosaedro è isomorfo ad \(A_5\), di ordine 60. Il suo doppio rivestimento in \(SU(2)\) è il gruppo binario icosaedrale
\[
2I\subset SU(2),\qquad |2I|=120.
\]
Il gruppo \(2I\) è realizzato da quaternioni unitari e contiene le due preimmagini \(q,-q\) delle rotazioni di \(SO(3)\).

Il ponte quaternioni–rotazioni non è un'analogia: è l'omomorfismo
\[
q:\ v\mapsto qvq^{-1},
\qquad
SU(2)\simeq S^3\longrightarrow SO(3),
\]
con kernel \(\{\pm1\}\). La convenzione algebrica e matriciale è fissata nel record T063. La geometria icosaedrale deve poi essere espressa con rappresentazioni, classi di coniugio, proiettori e intertwiners, non soltanto con immagini.

Il quoziente
\[
S^3/2I
\]
è lo spazio sferico di Poincaré. Esso fornisce un benchmark naturale per operatori spinoriali e spettrali su una varietà a curvatura positiva. Il passaggio da questo benchmark alla geometria PSU o alla struttura del vuoto non è automatico: richiede una metrica, una struttura spin, un operatore e condizioni di equivarianza dichiarate.

## 4. φ, ψ e raffinamento

Oltre a \(\varphi\), il programma usa la costante superaurea \(\psi\), definita come radice reale positiva di
\[
x^3-x^2-1=0,
\qquad
\psi\approx1.465571231876768.
\]
\(\varphi\) e \(\psi\) non sono intercambiabili:
- \(\varphi\) nasce dalla simmetria pentagonale e dal campo \(\mathbb Q(\sqrt5)\);
- \(\psi\) nasce da una relazione cubica e compare nelle strutture di raffinamento/Krist-All registrate nel programma.

Il ponte tra queste due costanti deve essere una relazione algebrica o spettrale dimostrata, non una somiglianza numerica. Le connessioni con funzioni eta di Dedekind, funzioni zeta e zeta spettrali devono specificare campo, carattere, prodotto o identità funzionale utilizzata. La relazione standard
\[
\zeta_{\mathbb Q(\sqrt5)}(s)
=\zeta(s)L(s,\chi_5)
\]
è una fattorizzazione della zeta di Dedekind del campo quadratico, ma non dimostra da sola una formula per lo spettro RGS.

## 5. PSU–Anti-Twin: doppio foglio e recupero della simmetria

Il settore PSU–Anti-Twin è il nucleo geometrico del modello a due fogli. La sua formulazione deve partire da:
- due copie/fogli con una mappa di identificazione dichiarata;
- involuzione Anti-Twin e suo insieme dei punti fissi;
- orientazione e struttura causale;
- metrica e coframe su ciascun foglio;
- legge di raccordo e regolarità al bordo/interfaccia;
- osservabili invarianti sotto l'involuzione.

Il recupero della simmetria Lorentz non si può postulare dal disegno dei due fogli: va mostrato a partire dalla metrica o dall'azione. Le costruzioni già registrate per l'involuzione cellulare di Q6 sono un modello discreto finito e non costituiscono da sole la dimostrazione della simmetria Lorentz del biverso continuo.

La terminologia PSU va mantenuta nella forma canonica stabilita dall'autore; le sue diverse espansioni storiche non vanno fuse o ridefinite senza controllare i documenti originari.

## 6. Q-ball: sintesi geometrica PSU–Anti-Twin

Nel lessico del progetto, la Q-ball è la configurazione/sintesi geometrica che integra PSU e Anti-Twin. Non va ridotta a una semplice palla materiale né confusa con la Q-ball standard della teoria dei campi senza una corrispondenza di campi, carica conservata, potenziale e soluzione localizzata.

La costruzione da formalizzare è:
1. geometria di base e coordinate;
2. due fogli e involuzione;
3. superficie/volume di raccordo e condizioni di regolarità;
4. campi o densità che vivono sulla configurazione;
5. carica conservata e condizioni di stabilità;
6. limite sferico e deformazione/ovalizzazione;
7. osservabili che distinguono la Q-ball proposta da una sfera ordinaria o da un solitone standard.

La parola «sintesi» è qui un'affermazione strutturale del programma; il suo contenuto fisico va stabilito dalle equazioni, non dal nome.

## 7. QAT e luce: dalla figura alla teoria testabile

QAT collega la geometria cubo-sfera, l'evento centrale, i coni nulli, i due fogli e la riconnessione/ovalizzazione. La luce deve essere il primo test fisico, perché fornisce un vincolo esterno preciso: propagazione causale a velocità \(c\), polarizzazione, modi, energia-impulso e compatibilità con Maxwell.

Per rendere QAT una teoria matematica verificabile occorre fissare:
- variabili di campo e loro dominio;
- metrica e convenzione di segnatura;
- coframe/vierbein;
- connessione e distinzione tra Levi-Civita e Weitzenböck;
- equazioni di campo o principio variazionale;
- condizioni iniziali/al contorno;
- previsione quantitativa diversa o equivalente a Maxwell in un regime dichiarato.

La lettura «il tempo è la velocità di riconnessione dei due coni» è una proposta interpretativa da tradurre in una variabile e in un'equazione misurabile. Non è ancora una definizione fisica accettata.

## 8. Interfaccia con teoria delle stringhe e Calabi–Yau

Il programma include il confronto con teoria delle stringhe e varietà di Calabi–Yau. Questo confronto deve essere collocato dopo la definizione geometrica di base, non usato come scorciatoia per giustificarla.

L'interfaccia standard da verificare è:
- varietà interna compatta di dimensione reale sei (nel caso Calabi–Yau tridimensionale);
- metrica Kähler e forma olomorfa parallela;
- olonomia contenuta in \(SU(3)\) nel caso di olonomia esatta;
- spinori covariantemente costanti e conseguenze supersimmetriche secondo il contesto;
- gruppi di simmetria, coomologia e dati topologici;
- eventuale ruolo di \(2I\), del campo \(\mathbb Q(\sqrt5)\) e delle strutture auree come simmetrie o dati di costruzione.

Non si può chiamare una geometria «Calabi–Yau» solo perché è a sei dimensioni, quaternionica, aurea o compatta. Servono le condizioni differenziali e metriche pertinenti. Analogamente, una compatibilità con una costruzione di stringa è un'interfaccia da derivare, non una conferma retroattiva del modello PSU.

## 9. Solo dopo: discretizzazioni Q6 e PRISM

Q6 e PRISM entrano come strumenti di realizzazione discreta:
- Q6: laboratorio finito per incidenza, catene, involuzioni, simmetrie, Fourier e gauge;
- PRISM: famiglia di grafi prodotto, classi, operatori e raffinamenti;
- FEEC/Mosco: strumenti per studiare il passaggio dal discreto al continuo.

Essi devono approssimare strutture geometriche già definite, oppure fornire una costruzione discreta autonoma con una mappa esplicita verso la geometria. Non possono essere retroattivamente assunti come origine del programma.

## 10. Registro delle prove e dei passaggi ancora da recuperare

| Passaggio | Stato da assegnare nella ricostruzione |
|---|---|
| Definizione Planck di \(\ell_P,t_P,E_P\) | [E] |
| Raggio cubo e sfera, \(r_C(n)=a/\|n\|_\infty\) | [P] identità geometrica |
| Derivazione originaria completa \(\pi\to\varphi\) | [O] recuperare il documento/disegno originale; la formula pentagonale è [E/P] |
| Coordinate auree dell'icosaedro | [E/P] |
| Realizzazione quaternionica di \(SU(2)\to SO(3)\) | [P], record T063 |
| Gruppo binario icosaedrale \(2I\) e \(S^3/2I\) | [E/P] per la struttura standard; applicazione PSU da dimostrare |
| Ponte \(\varphi\), \(\psi\), eta di Dedekind e zeta spettrale | [O/C], identità da specificare una per una |
| Geometria PSU–Anti-Twin continua | [H/O] finché non sono fissati varietà, involuzione, metrica e azione |
| Q-ball come sintesi PSU–Anti-Twin | [H/M] da tradurre in campi, cariche e stabilità |
| QAT e luce | [H/O] fino a equazioni e confronto Maxwell |
| Interfaccia stringhe/Calabi–Yau | [C/O] finché non sono verificate le condizioni geometriche |
| Q6/PRISM come discretizzazione | [M/N/P] per ciascun oggetto specifico, con mappe esplicite |

## 11. Regola di ricostruzione

L'ordine di lavoro da questo punto è rigoroso:

1. recuperare la prima formulazione originale della luce e delle unità fondamentali;
2. ricostruire la geometria cubo-sfera e la funzione radiale senza pesi arbitrari;
3. riportare integralmente la derivazione originaria \(\pi\to\varphi\), poi collegarla a icosaedro, quaternioni e \(2I\);
4. ricostruire PSU–Anti-Twin e il suo recupero Lorentziano;
5. definire la Q-ball come sintesi PSU–Anti-Twin con equazioni e osservabili;
6. formalizzare QAT e confrontarlo con Maxwell;
7. sviluppare il confronto con stringhe/Calabi–Yau;
8. solo dopo ricostruire Q6, PRISM, gauge, operatori e limiti continui come realizzazioni matematiche.

Ogni passaggio deve contenere: definizione, derivazione, unità, ipotesi, risultato, verifica indipendente, non-conclusioni e dipendenza dal passaggio precedente. Nessun filone può essere dichiarato «unificato» se il ponte che lo collega al precedente non è scritto.
