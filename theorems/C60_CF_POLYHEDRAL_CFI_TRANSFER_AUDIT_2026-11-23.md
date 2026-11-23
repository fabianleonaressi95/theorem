# C60 — trasferimento della geometria A alle mesh CFI poliedrali

Data: 2026-11-23

Classificazione: **trasferimento geometrico finito-stadio dimostrato sotto le ipotesi esplicite di mesh conforme e dati affine-per-cella; verifica numerica di una mesh CFI identificata non disponibile nel materiale versionato consultato.** La recovery globale C60 resta aperta per le ragioni indicate in §7.

Questo audit verifica le quattro condizioni di trasferimento elencate nella nota C60_CF_GEOMETRY_A_TERMINAL_TRACE_AND_STRIP_SEPARATION_2026-11-23.md §6. La distinzione tra una dimostrazione uniforme per ogni mesh finita ammissibile e il controllo dei dati di una specifica istanza CFI è mantenuta esplicita.

## 1. Ipotesi finite-stadio

Sia \(\Sigma\) una superficie poliedrale compatta, eventualmente con bordo, dotata di una triangolazione finita conforme \(\mathcal T_j\). Si assume:

1. ogni faccia è euclidea e ogni triangolo della mesh è contenuto in una faccia;
2. le tracce della funzione \(g_j\) sono affini su ogni triangolo (in coordinate euclidee della faccia);
3. le identificazioni sui lati comuni della triangolazione sono conformi: i lati comuni hanno la stessa suddivisione, oppure si prende prima il raffinamento comune finito;
4. \(J_{g_j}\) è contenuto nell'unione finita degli spigoli della partizione, con salto affine su ciascun lato dopo ulteriore suddivisione;
5. \(\Sigma\) è una superficie poliedrale intrinseca: ogni punto interno a uno spigolo non ha curvatura concentrata; le eventuali singolarità intrinseche sono isolate nei vertici con angolo conico diverso da \(2\pi\).

Sono le ipotesi geometriche espresse per gli stadi CFI nei documenti C60 di recovery: approssimanti piecewise affine su una partizione poliedrale finita che raffina le facce. Se uno stadio concreto non soddisfa la conformità al punto 3, il raffinamento comune è parte obbligatoria del preprocessing.

## 2. Check 1 — suddivisione esatta del jump complex

Fissato \(j\), il numero di triangoli, facce e lati è finito. Si costruisce un grafo intrinseco \(\Gamma_j\) come segue:

- si prendono tutti i lati sui quali le due tracce di \(g_j\) differiscono;
- si inseriscono vertici a ogni estremo, incrocio, T-junction, attraversamento di uno spigolo di faccia e punto in cui cambia la coppia di triangoli o la coppia di estensioni affini;
- si fondono le copie collineari sovrapposte dello stesso tratto geometrico e si assegna a ogni lato una sola coppia ordinata di tracce;
- se un lato di salto coincide con uno spigolo tra facce, lo si conserva come un singolo lato intrinseco e si usano le due tracce delle facce incidenti.

Il risultato è un grafo finito con interni relativi dei lati disgiunti. Ogni lato ha due estensioni affini locali e il loro differenziale \(h_e\) è affine nel relativo sviluppo piano.

**Conclusione check 1:** verificato sotto le ipotesi 1–4. Non serve assumere che il jump set sia già un grafo embedded senza preprocessing: la suddivisione finita lo produce.

## 3. Check 2 — sviluppo piano attraverso gli spigoli di faccia

Sia \(x\) un punto interno a uno spigolo di faccia, non un vertice della superficie. Un intorno sufficientemente piccolo di \(x\) è l'unione di due semidischi euclidei incollati lungo il diametro comune. Sviluppando rigidamente una faccia rispetto all'altra si ottiene un disco piano isometrico all'intorno intrinseco.

Le mappe \(g_j\) sulle due facce, dopo la composizione con le rispettive isometrie di sviluppo, restano affini sui triangoli incidenti. Non è richiesto che le due mappe affini coincidano: la loro eventuale differenza è proprio una delle tracce che entra nel salto e nella famiglia finita usata per \(M_P\).

Se un lato di salto attraversa uno spigolo di faccia, lo si suddivide nel punto di attraversamento. Si applica la costruzione nei due sviluppi locali e si esclude un intorno terminale del punto di giunzione. Se il salto giace lungo lo spigolo, si usa un unico sviluppo attraverso lo spigolo e si considera il lato intrinseco una sola volta.

Per ogni stadio finito si può scegliere un numero finito di tali intorni. I confini artificiali della copertura vengono inseriti come punti di suddivisione del grafo; i loro intorni terminali sono contati in \(V\), non come cappucci \(K\).

**Conclusione check 2:** verificato per gli spigoli ordinari di una superficie poliedrale. La frase «angolo \(2\pi\)» va intesa intrinsecamente: lo sviluppo è locale e non afferma che le facce siano complanari nello spazio ambiente.

## 4. Vertici conici — sostituzione del disco piano

Un vertice conico \(p\) con angolo totale \(\Theta_p>0\) non possiede, in generale, un intorno isometrico a un disco euclideo. Perciò non si applica lì il lemma planare. Si sceglie invece un disco metrico conico \(C_\rho(p)\), cioè la palla intrinseca di raggio \(\rho\), e si sospende lo splitting al suo interno.

La frontiera ha lunghezza
\[
\mathcal H^1(\partial C_\rho(p))=\Theta_p\rho.
\]
Il numero dei settori triangolari incidenti è finito. Per ogni settore si usa il suo sviluppo euclideo, e si elencano le coppie effettive \((F,G)\) di estensioni affini che forniscono le due tracce sul medesimo settore. Per ogni coppia si prende il compatto chiuso del settore dentro un intorno conico fissato. Definiamo
\[
M_p:=\max_{(F,G,\ell)}
\sup_{x\in K_{p,\ell}}|F_\ell(x)-G_\ell(x)|<\infty,
\]
dove \(\ell\) varia sui settori e \(F_\ell,G_\ell\) sono scritte nello stesso sviluppo del settore \(\ell\). Il massimo è su una famiglia finita di coppie effettive, non su mappe espresse in coordinate incompatibili di settori diversi. Le tracce sui due lati della frontiera terminale sono una traccia esterna e una combinazione convessa di due estensioni affini dello stesso settore. Quindi il salto è al più \(M_p\), e
\[
E_{\partial C_\rho(p)}\le \Theta_p\rho M_p^2.
\]
Il salto originale conservato dentro il cono ha lunghezza totale al più \(N_p\rho\), dove \(N_p\) è il numero finito dei rami incidenti, e dunque costo al più \(N_p\rho M_p^2\).

Per la separazione dei rami, si considerano le direzioni nel link circolare del cono. Sia \(\alpha_p>0\) la minima distanza angolare intrinseca tra direzioni incidenti distinte, dopo aver fuso i raggi duplicati. Per punti sui due raggi a distanze radiali \(s,t\ge r\), la distanza conica è almeno
\[
2r\sin\!\left(\frac{\min\{\alpha_p,\pi\}}2\right).
\]
Infatti, per separazione angolare non superiore a \(\pi\) vale la formula del cono sviluppato; per separazione maggiore di \(\pi\) il cammino minimo può passare per l'apice e ha lunghezza almeno \(s+t\ge2r\). Pertanto gli intorni tubolari di larghezza \(\delta\) sono disgiunti fuori da \(C_\rho(p)\) se
\[
2(c_0\rho-\delta)\sin\!\left(\frac{\min\{\alpha_p,\pi\}}2\right)>2\delta.
\]
È la versione conica della condizione angolare della geometria A.

**Conclusione vertici:** il costo terminale è \(O(\rho M_p^2)\); la separazione è controllata dal link conico, non da un angolo euclideo arbitrariamente assegnato al vertice.

## 5. Check 3 — completezza della famiglia affine \(M_P\)

Per ogni punto terminale ordinario \(P\) si fissa un intorno compatto contenuto in uno sviluppo piano. La famiglia \(\mathcal A_P\) deve contenere:

- entrambe le estensioni affini associate a ogni ramo incidente;
- le estensioni delle celle che forniscono la traccia non modificata sul lato esterno del terminale;
- le estensioni di tutte le celle che incontrano l'intorno compatto, anche se non sono direttamente incidenti al ramo di salto;
- dopo uno sviluppo attraverso uno spigolo di faccia, le estensioni delle celle di entrambe le facce.

La finitezza della mesh rende \(\mathcal A_P\) finita. La continuità delle mappe affini sul compatto dà \(M_P<\infty\). La combinazione convessa dei due valori di strato dà il controllo uniforme in \(i\) e \(m\), esattamente come in (3.2) della nota geometria A.

Al vertice conico si usa la famiglia \(\mathcal A_p\) di §4 e il compatto radiale nel cono; non si pretende un'unica coordinata euclidea attraverso l'apice.

**Conclusione check 3:** verificato a livello di struttura finita. La costante è dipendente dallo stadio \(j\), dalla mesh e dai dati affini; non è uniforme in \(j\) e non deve essere presentata come tale. Per la diagonale CFI si sceglie \(\rho_j,\delta_j,m_j\) dopo aver fissato \(j\).

## 6. Check 4 — scelta simultanea dei terminali e delle larghezze

Per uno stadio \(j\) fissato:

1. l'insieme dei vertici del grafo, dei punti di attraversamento delle giunzioni di faccia e dei punti di cambio di traccia è finito;
2. si scelgono intorni terminali disgiunti attorno a tali punti, con raggio inferiore alla distanza minima tra centri distinti;
3. si riduce il raggio affinché gli intorni ordinari siano contenuti nei rispettivi sviluppi piani e quelli conici restino nei corrispondenti intorni conici;
4. dopo la suddivisione, i lati non incidenti sono segmenti compatti disgiunti e hanno distanza minima positiva;
5. per i lati incidenti, la minima separazione angolare nel piano sviluppato o nel link conico è positiva perché il numero di raggi è finito e i raggi duplicati sono stati fusi.

Si può quindi scegliere \(\delta_j>0\) minore simultaneamente di:
- \(c_0\rho_j/2\);
- la soglia angolare di ogni vertice ordinario e conico;
- un terzo della distanza minima tra i lati non incidenti;
- la larghezza disponibile degli sviluppi piani.

Non si afferma che una sola coppia \((\rho,\delta)\) funzioni per tutti gli stadi \(j\). La diagonale sceglie prima lo stadio \(j\), poi le sue scale geometriche.

**Conclusione check 4:** esistenza dimostrata per ogni stadio finito conforme. I valori numerici di separazione e delle costanti non sono ricavabili senza i dati espliciti della mesh.

## 7. Bilancio e limiti della conclusione

Per ogni stadio \(j\) fissato, la geometria A si trasferisce alla superficie poliedrale con:
- strati e bordo esterno \(S\), stimati come nella nota planare;
- nessun termine separato \(K\) per i lati corti assorbiti nei terminali;
- terminali ordinari e conici \(V\), con costo totale
  \[
  E_V\le \rho_j\left[
  \sum_{P\ {\rm ordinario}}C_P M_P^2+
  \sum_{p\ {\rm conico}}(\Theta_p+N_p)M_p^2
  \right].
  \]
La quantità tra parentesi è finita per ogni \(j\), ma può dipendere da \(j\).

Ne segue una stima di splitting finito-stadio, scegliendo prima \(\rho_j\downarrow0\), poi \(\delta_j/\rho_j\downarrow0\) sotto tutte le soglie geometriche, e infine \(m_j\uparrow\infty\) per annullare \(S\). La diagonale deve inoltre scegliere le scale in modo che l'errore \(L^1\) dello splitting tenda a zero.

**Non segue ancora la recovery globale C60.** Restano indipendenti:
1. la localizzazione della recovery bulk in presenza dei salti macroscopici, specificata ma non dimostrata in C60_CF_LOCALIZATION_LEMMA_2026-11-21.md;
2. il controllo della misura di salto effettiva dopo la staircase sulla partizione comune, con tutte le interfacce della partizione e le tracce terminali assegnate una sola volta;
3. la convergenza determinante completa per la successione diagonale sullo stadio \(j\), inclusa l'assenza di concentrazioni spurie sui bordi delle facce.

## 8. Verifica dell'istanza concreta

Nei documenti versionati consultati, la CFI è descritta come approssimazione piecewise affine su una partizione poliedrale finita che raffina le facce. Non è però presente, tra i file effettivamente consultabili in questo audit, un identificatore di uno stadio \(j\) con la relativa lista di triangoli, vertici, incidenze e coordinate. Pertanto:

- la dimostrazione strutturale §§2–6 copre ogni stadio che soddisfi le ipotesi finite-stadio §1;
- non viene dichiarato un controllo numerico di una mesh concreta;
- per registrare tale controllo servono l'artefatto della mesh CFI (o il file che la genera) e il relativo identificatore di stadio.

**Stato finale:** trasferimento geometrico finito-stadio dimostrato sotto le ipotesi conformi §1; verifica dei dati di una specifica istanza CFI non documentata; localizzazione SBV e recovery globale C60 ancora aperte.
