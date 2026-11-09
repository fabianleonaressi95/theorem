# Proposta scientifica Torino — RGS–PRISM, difetti e strutture di gradiente

**Versione:** 9 novembre 2026  
**Destinatario scientifico principale:** Marco Morandotti, DISMA — Politecnico di Torino; membro IAM@PoliTo  
**Stato:** proposta di ricerca da discutere; non è una collaborazione già concordata e non presenta RGS–PRISM come modello materiale validato.

## 1. Idea e domanda scientifica

La proposta è mettere in relazione una discretizzazione geometrica a cochain (RGS–PRISM/Q6) con i modelli variazionali e semi-discreti per dislocazioni e disclinazioni sviluppati nell'area DISMA. La domanda non è se RGS–PRISM sia già migliore di FEM, ma se la sua struttura di grafo, incidenza e decomposizione Hodge possa offrire una rappresentazione discreta controllabile di:

1. cinematica elastica e incompatibilità;
2. difetti traslazionali (dislocazioni) e rotazionali (disclinazioni);
3. evoluzione dissipativa, memoria e isteresi;
4. limiti discreto-continuo verificabili mediante convergenza variazionale.

Il punto di contatto matematico è concreto: il lavoro di Cesana, De Luca e Morandotti formula sistemi planari di disclinazioni a cuneo, dipoli di disclinazione e dislocazioni di bordo mediante elasticità lineare incompatibile e funzione di Airy. Il risultato centrale comprende l'equivalenza energetica, nel limite singolare regolarizzato, tra dipoli di disclinazione e dislocazioni di bordo [1]. La linea RGS–PRISM può essere messa alla prova proprio su questa equivalenza, prima di estendersi a geometrie o dinamiche più generali.

## 2. Ponte matematico: dal continuo alle cochain

### 2.1 Problema continuo di riferimento

Sia \(\Omega\subset\mathbb R^2\) il dominio piano. Si consideri uno spostamento \(u:\Omega\to\mathbb R^2\), una distorsione plastica \(\beta^p\) e la deformazione elastica

\[
\varepsilon^e(u,\beta^p)=\operatorname{sym}(\nabla u-\beta^p).
\]

L'energia elastica di riferimento è

\[
E(u,\beta^p)=\frac12\int_\Omega
\bigl(\varepsilon^e:C:\varepsilon^e\bigr)\,dx
+E_{\rm core}(\beta^p),
\]

dove il termine di core deve essere specificato dal modello e dalla regolarizzazione scelta. L'incompatibilità della deformazione plastica è descritta, nel caso piano, dall'operatore

\[
\operatorname{inc}(\varepsilon^p)
=\partial_{yy}\varepsilon^p_{xx}
+\partial_{xx}\varepsilon^p_{yy}
-\partial_{xy}\gamma^p_{xy}.
\]

Nella formulazione di Airy, l'equilibrio si riduce a un problema del quarto ordine per la funzione di tensione. La convenzione dei segni e il coefficiente elastico vanno mantenuti identici nel confronto numerico; non si devono confrontare solutori con condizioni al contorno diverse.

### 2.2 Discretizzazione RGS–PRISM

Su un complesso discreto si introducono:
- una 0-cochain vettoriale \(u_h\) sui vertici;
- l'incidenza \(d_0:C^0\to C^1\), che produce differenze di spostamento sugli spigoli;
- una 1-cochain plastica \(\beta_h^p\) sugli spigoli;
- l'incidenza \(d_1:C^1\to C^2\), che misura la circolazione/incompatibilità sulle facce.

Una prima energia discreta candidata è

\[
E_h(u_h,\beta_h^p)=
\frac12\langle d_0u_h-\beta_h^p,
\,\mathsf C_h(d_0u_h-\beta_h^p)\rangle
+E_{\rm core,h}(\beta_h^p).
\]

La matrice \(\mathsf C_h\), i pesi geometrici e la normalizzazione devono essere derivati dalla geometria e dalla scala \(h\), non scelti per far coincidere a posteriori gli output. Il termine \(d_1\beta_h^p\) è il candidato discreto per la carica di incompatibilità. La corrispondenza tra questa quantità e i vettori di Burgers/Frank va definita e verificata con orientazioni e convenzioni esplicite.

La decomposizione Hodge delle cochain separa componenti esatte, coesatte e armoniche. È una possibile organizzazione dei modi elastici, delle sorgenti di difetto e dei cicli globali; non implica da sola che le componenti armoniche rappresentino difetti fisici.

### 2.3 Mappa cinematica Q6 già implementata come primo quoziente

Nel ramo della PR #119 è stato aggiunto lo script **scripts/q6_prism_kinematic_map.py**. La convenzione raggruppa i sei bit in tre coppie, con codici \(2b_0+b_1\), \(2b_2+b_3\), \(2b_4+b_5\), e usa l'embedding Gray per identificare il grafo Q6 con \(C_4\square C_4\square C_4\). I primi due cicli costituiscono una cella materiale periodica \(C_4\square C_4\); il terzo è una fibra interna a quattro stati.

La mappa di quoziente è \(\pi(x,y,z)=(x,y)\). Il pullback di uno spostamento \(u\) soddisfa l'identità discreta

\[
d_0^{Q6}(u\circ\pi)=P_1d_0^{\rm mat}u,
\]

con differenze nulle sugli spigoli della fibra. Le mappe \(P_0,P_1,P_2\) sono costruite con coefficienti interi e verificano le identità di catena del sottocomplesso prodotto.

**Distinzione topologica non negoziabile:** i 240 quadrati del 2-scheletro dell'ipercubo Q6 si separano in 192 facce del prodotto \(C_4^3\) e 48 quadrati generati dai due bit appartenenti alla stessa coppia. La mappa materiale usa il sottocomplesso prodotto da 192 facce; non identifica automaticamente i 48 quadrati rimanenti con facce del materiale. Il conteggio 240 resta quello dell'audit Q6 completo, mentre il quoziente periodico usa la struttura prodotto. Questa distinzione è documentata e testata nel codice.

Questa è una mappa cinematica esatta su una cella finita, non ancora la mappa verso la griglia FEM a trazione libera e non ancora una costruzione sul grafo PRISM completo \(C_{64}\square C_6^3\square C_5\). Il collegamento alla struttura PRISM completa richiede un ulteriore morfismo di complessi e una scelta motivata delle scale.

## 3. Primo benchmark: ciò che è stato fatto e ciò che manca

La PR #119 contiene un primo confronto 2D tra:
- FEM Q1 quadrilatero con integrazione di Gauss 2×2;
- P1 su cochain di spigolo, con due orientazioni della diagonale;
- sorgenti regolarizzate di dislocazione di bordo e disclinazione a cuneo;
- dipolo di disclinazione;
- riferimento indipendente a funzione di Airy risolto con differenze finite.

Il benchmark controlla l'identità \(d_1d_0=0\), patch test affine, caso senza sorgente, residui del solutore e momenti topologici imposti. Per i campi a \(n=65\), gli errori relativi \(L^2\) rispetto al riferimento Airy riportati nella PR sono:
- dislocazione di bordo: stress 14,44% (Q1) e 14,68% (cochain); strain 16,96% e 19,20%;
- disclinazione a cuneo: stress 6,28% e 6,62%; strain 5,90% e 6,23%.

Per il dipolo a \(n=129\), gli errori sono circa 5,67–5,97%; tuttavia la differenza relativa di energia Q1/cochain è ancora 12,12%. La tendenza al raffinamento è incoraggiante ma non è una prova di equivalenza energetica.

Il test dipolo→dislocazione, con cariche opposte \(\pm s\), \(s=b/d\), mostra che riducendo la separazione \(d\) da 0,1 a 0,025 la differenza relativa della sorgente di incompatibilità scende dal 70,12% al 4,74%, e quella dello stress Airy dal 23,76% all'1,26%. È un controllo numerico di sorgenti regolarizzate, non la dimostrazione del teorema di energia rinormalizzata di [1].

**Limiti attuali:** i core sono regolarizzati con larghezza finita; il riferimento Airy è una realizzazione alle differenze finite e non il metodo CIP-DG pubblicato; la cella Q6 è periodica mentre il benchmark FEM/Airy della PR usa condizioni traction-free. Prima di confrontare i numeri occorre allineare dominio, condizioni al contorno, parametri e normalizzazione.

## 4. Programma di lavoro proposto

### Fase A — confronto matematico controllato (4–6 settimane)

1. Fissare una convenzione unica per orientazioni, tensori, segni, unità e condizioni al contorno.
2. Costruire il morfismo tra la cella Q6 periodica e il complesso triangolato/quadrilatero del benchmark.
3. Implementare la stessa sorgente di Burgers/Frank in FEM, cochain e Airy.
4. Eseguire raffinamento \(h\to0\), variazione del core \(\varepsilon\to0\), rotazione della mesh e test su singolo difetto/dipolo.
5. Confrontare energia, stress, strain, momenti di incompatibilità, residui e sensibilità alla regolarizzazione.
6. Usare il risultato di equivalenza dipolo–edge di [1] come benchmark teorico, non come risultato da presumere.

**Gate A:** nessuna pretesa di vantaggio RGS. Si prosegue solo se le quantità convergono e gli errori sono spiegabili rispetto al riferimento.

### Fase B — struttura di gradiente e memoria (6–10 settimane)

Si introduce una variabile interna \(z_h\) che descriva, a seconda del livello di modello, slip plastico, posizione/segno dei difetti o stato microstrutturale. La dinamica non va ridotta al solo gradiente dell'energia: per fenomeni rate-independent e isteretici serve una dissipation potential \(\mathcal R(\dot z_h)\), ad esempio

\[
0\in\partial_{\dot z_h}\mathcal R(\dot z_h)
+\partial_{z_h}E_h(u_h,z_h),\qquad
0\in\partial_{u_h}E_h(u_h,z_h).
\]

Si confrontano cicli di carico/scarico, dissipazione, loop area, coercività e stabilità rispetto al passo temporale. Questo è il collegamento naturale con le strutture di gradiente e con i modelli evolutivi; la simulazione numerica non equivale a identificazione sperimentale dei parametri.

### Fase C — materiali AM e IAM@PoliTo (da definire con i ricercatori)

L'estensione industriale deve partire da un campione e da una misura disponibili, non da una promessa generica. IAM@PoliTo dichiara capacità lungo la catena AM, inclusi CT, caratterizzazione microstrutturale e meccanica, trattamenti termici/HIP e produzione di componenti metallici e polimerici [4].

Un primo protocollo utile richiederebbe:
- lega, polvere e lotto; macchina, strategia di scansione, orientazione, layer thickness e parametri di processo;
- CT con segmentazione di pori/cricche e incertezza;
- microstruttura, grani/fasi e orientazione;
- trattamento termico/HIP e storia termica;
- prove meccaniche con geometria, velocità, temperatura e repliche;
- tracciabilità tra dati grezzi, mesh, parametri e report.

L'obiettivo realistico iniziale è valutare se le variabili geometriche/discrete migliorino la descrizione di localizzazione dei difetti o della risposta meccanica rispetto al riferimento FEM. L'eventuale trasferimento in software industriale o startup si valuta soltanto dopo una validazione indipendente e una dimostrazione di utilità misurabile.

## 5. Collaborazione a Torino

L'interlocutore scientifico principale proposto è **Marco Morandotti**, professore associato DISMA e membro IAM@PoliTo [2]. Il suo profilo include calcolo delle variazioni, meccanica dei continui, difetti, elasticità e deformazioni strutturate; tra i progetti elencati compaiono dinamica di dislocazioni/disclinazioni e structured deformations [3].

La collaborazione potrebbe essere organizzata per competenze, senza attribuire impegni non ancora concordati:
- **Morandotti / DISMA:** formulazione variazionale, difetti, strutture di gradiente e criteri di convergenza;
- **Cesana e De Luca:** confronto con il modello Airy e con l'equivalenza dipolo–dislocazione del 2024 [1];
- **Fabbrini e coautori:** confronto con la formulazione agli elementi finiti semi-discreta presentata come lavoro sottomesso nel 2026 [5];
- **IAM@PoliTo:** disponibilità di campioni, CT, microstruttura e prove meccaniche;
- **altri gruppi DISMA/PoliTo:** da coinvolgere in funzione del materiale e della misura, dopo aver definito il primo benchmark.

La possibile startup non è il punto di partenza. È una seconda fase eventuale, legata a un algoritmo validato, a un vantaggio documentato e a un utilizzatore industriale identificato.

## 6. Risultato richiesto dal primo incontro

Si propone un incontro tecnico di 30–45 minuti con tre decisioni:
1. scegliere un benchmark teorico comune (dislocazione di bordo o dipolo di disclinazione);
2. concordare le condizioni al contorno e le quantità da confrontare;
3. valutare se esiste un campione AM e un protocollo IAM realistico per una successiva verifica.

Il deliverable successivo sarebbe un report riproducibile con codice, dati di input, test, curve di convergenza, confronto Airy/FEM/cochain e registro esplicito di risultati verificati, ipotesi e problemi aperti.

## Riferimenti

[1] P. Cesana, L. De Luca, M. Morandotti, *Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method*, SIAM J. Math. Anal. 56(1) (2024), 79–136. DOI: [10.1137/22M1523443](https://doi.org/10.1137/22M1523443). Scheda e abstract: [CVGMT](https://cvgmt.sns.it/paper/5618/).

[2] [Profilo ufficiale di Marco Morandotti — Politecnico di Torino](https://www.polito.it/personale?p=marco.morandotti).

[3] [Marco Morandotti — Research interests and ongoing projects](https://marcomorandotti.weebly.com/research.html).

[4] [IAM@PoliTo — Integrated Additive Manufacturing](https://www.polito.it/en/research/ecosystem/research-infrastructures/iam).

[5] E. Fabbrini, P. Cesana, A. A. León Baldelli, M. Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, lavoro sottomesso (2026), scheda CVGMT: [paper 7600](https://cvgmt.sns.it/paper/7600/).

[6] [DISMA — Calcolo delle variazioni e applicazioni](https://www.disma.polito.it/la_ricerca/temi/calcolo_delle_variazioni_e_applicazioni).
