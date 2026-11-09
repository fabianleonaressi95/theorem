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

Il workflow GitHub Actions [42655229679](https://github.com/fabianleonaressi95/theorem/actions/runs/42655229679) ha eseguito sei test dedicati e l'audit JSON: tutti i residui esatti di catena e di pullback sono zero. Il test e il report sono quindi riproducibili sul ramo della PR.

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

Il test dipolo→dislocazione, con cariche opposte \(\pm s\), \(s=b/d\), mostra che riducendo la separazione \(d\) da 0,1 a 0,025 la differenza relativa della sorgente di incompatibilità scende dal 70,12% al 4,74%, e quella dello stress Airy dal 23,76% all'1,26%. È un controllo numerico di sorgenti regolarizzate, non la dimostrazione del teorema di energia rinormalizzata di [1]. Nel report riproducibile la scansione usa (n=129), (h=1/128) e (d=0.1,0.075,0.05,0.0375,0.025), quindi (d/h=12.8,9.6,6.4,4.8,3.2): è stata esclusa la separazione allineata (d=2h), che produce una coincidenza artificiale dello stencil discreto. Anche la scansione corretta resta a griglia fissa e non dimostra da sola il limite continuo.

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

### Fase B — struttura di gradiente, dinamica dei difetti e memoria (6–10 settimane)

Questa fase ha un collegamento diretto con lavori specifici di Morandotti e coautori, non soltanto con una generica analogia fra gradienti:

1. **Dinamica di dislocazioni e minimizing movements.** Bonaschi, van Meurs e Morandotti (2017) studiano una struttura di gradient flow per dislocazioni a vite. Con un numero finito di direzioni di scorrimento e un criterio di massima dissipazione, l'evoluzione è una inclusione differenziale; il modello continuo è ottenuto come limite di schemi temporali che vincolano ogni passo a una direzione di glide. È il riferimento metodologico per costruire una dinamica discreta RGS senza sostituire arbitrariamente la dissipazione con una metrica quadratica [7].

2. **Dinamica dissipativa delle disclinazioni di Volterra.** Cesana, Grillo, Morandotti e Pastore (2025) trattano sistemi finiti di disclinazioni a cuneo, con moti isotropi oppure vincolati a direzioni preferenziali di un materiale cristallino [8]. Questo fornisce il riferimento per introdurre orientazioni di glide, mobilità e leggi di dissipazione nel modello discreto.

3. **Equivalenza dinamica dipolo–dislocazione.** Briatico, Cesana e Morandotti (2026, preprint) individuano per una coppia di disclinazioni a cuneo opposte due regimi — divergenza delle disclinazioni e annichilazione del dipolo — e mostrano che, nel regime di annichilazione e dopo una riscalatura temporale, la legge del dipolo coincide con quella di una dislocazione di bordo [9]. Questo è un benchmark dinamico particolarmente adatto al nostro audit statico già esistente: non basta riprodurre la convergenza delle sorgenti e dei campi, occorre confrontare anche traiettorie, punti stazionari, stabilità e tempi caratteristici.

La proposta RGS è quindi introdurre uno stato discreto (z_h) che registri posizione, segno e orientazione dei difetti, insieme a una variabile interna separata per lo slip/memoria plastica. L'energia (E_h) deve derivare dal problema elastico già confrontato con Airy; la dissipazione (mathcal R_h) deve invece essere derivata dalla regola di glide scelta e dalle eventuali direzioni ammissibili. La forma astratta da verificare è

\[
0\in\partial_{\dot z_h}\mathcal R_h(\dot z_h)
+\partial_{z_h}E_h(u_h,z_h),\qquad
0\in\partial_{u_h}E_h(u_h,z_h).
\]

Non si assume a priori che (mathcal R_h) sia quadratica, isotropa o metrica: il confronto con i modelli di massima dissipazione serve proprio a determinare la struttura corretta. Il primo test dinamico dovrebbe riprodurre i due regimi della coppia di disclinazioni e verificare la legge dipolo→dislocazione dopo la riscalatura temporale. Solo dopo si introducono cicli di carico/scarico, dissipazione, area dei loop, memoria e confronto con prove meccaniche. Una simulazione non equivale a identificazione sperimentale dei parametri.

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

Il primo fascicolo integrativo è stato preparato il 9 novembre 2026; entro il 18 novembre il deliverable successivo proposto è un report di confronto con codice, dati di input, test, curve di convergenza, confronto Airy/FEM/cochain e registro esplicito di risultati verificati, ipotesi e problemi aperti.

## Riferimenti

[1] P. Cesana, L. De Luca, M. Morandotti, *Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method*, SIAM J. Math. Anal. 56(1) (2024), 79–136. DOI: [10.1137/22M1523443](https://doi.org/10.1137/22M1523443). Scheda e abstract: [CVGMT](https://cvgmt.sns.it/paper/5618/).

[2] [Profilo ufficiale di Marco Morandotti — Politecnico di Torino](https://www.polito.it/personale?p=marco.morandotti).

[3] [Marco Morandotti — Research interests and ongoing projects](https://marcomorandotti.weebly.com/research.html).

[4] [IAM@PoliTo — Integrated Additive Manufacturing](https://www.polito.it/en/research/ecosystem/research-infrastructures/iam).

[5] E. Fabbrini, P. Cesana, A. A. León Baldelli, M. Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, lavoro sottomesso (2026), scheda CVGMT: [paper 7600](https://cvgmt.sns.it/paper/7600/).

[6] [DISMA — Calcolo delle variazioni e applicazioni](https://www.disma.polito.it/la_ricerca/temi/calcolo_delle_variazioni_e_applicazioni).

[7] G. A. Bonaschi, P. van Meurs, M. Morandotti, *Dynamics of screw dislocations: A generalised minimising-movements scheme approach*, European Journal of Applied Mathematics 28(4) (2017), 636–655. DOI: [10.1017/S0956792516000462](https://doi.org/10.1017/S0956792516000462).

[8] P. Cesana, A. Grillo, M. Morandotti, A. Pastore, *Dissipative Dynamics of Volterra Disclinations*, SIAM Journal on Applied Mathematics 85(4) (2025), 1361–1386. DOI: [10.1137/24M1688096](https://doi.org/10.1137/24M1688096).

[9] N. Briatico, P. Cesana, M. Morandotti, *Effective Dynamics of Disclination Pairs*, preprint (2026), [arXiv:2608.12233](https://arxiv.org/abs/2608.12233), [CVGMT](https://cvgmt.sns.it/paper/7926/).


### Aggiornamento quantitativo del confronto (9 novembre 2026)

Il confronto Q1–cochain P1–Airy è stato esteso e superato in CI: [run 42656544200](https://github.com/fabianleonaressi95/theorem/actions/runs/42656544200), con [artifact JSON/CSV](https://github.com/fabianleonaressi95/theorem/actions/runs/42656544200/artifacts/13691882405). Sono stati prodotti 56 confronti Q1/cochain e 20 confronti Airy/Q1/cochain, con patch test, caso nullo, residui e doppia orientazione della diagonale.

Per il dipolo di disclinazione, la differenza energetica Q1/cochain scende dal 60,64% a n=17 al 12,12% a n=129; gli errori di stress rispetto ad Airy a n=129 sono 5,67% (Q1) e 5,97% (cochain). Il divario energetico cochain–Airy resta però 18,52%, quindi il confronto non è ancora chiuso sul piano energetico.

**Correzione dell'audit grid-aligned:** la precedente sequenza includeva separazioni commensurate con lo stencil centrato; il valore quasi nullo a d=2h era una coincidenza discreta e non evidenza di limite continuo. Quella sequenza è superata e non va usata come risultato scientifico. Nel run #69 è stata sostituita da separazioni non bloccate sulla griglia, d=(0.1, 0.075, 0.05, 0.0375, 0.025), con d/h=(12.8, 9.6, 6.4, 4.8, 3.2). L'errore relativo della sorgente scende dal 70,12% al 4,74% e quello dello stress Airy dal 23,76% all'1,26%. È una tendenza numerica a griglia fissa con sorgenti regolarizzate, non una prova del limite continuo o del teorema energetico.

Il report completo, con tabelle, definizioni degli errori e limiti, è disponibile in [THREE_WAY_COMPARISON_2026-11-09.md](rgs_defect_benchmark/THREE_WAY_COMPARISON_2026-11-09.md). Restano aperti il limite del core, la convergenza Mosco/Γ, la riproduzione CIP-DG e la mappa Q6/PRISM verso la mesh fisica.


### Regressione aggiornata e confronto diretto CIP-DG

La regressione [run #69](https://github.com/fabianleonaressi95/theorem/actions/runs/42657016309) è conclusa con successo: 9 test Airy e 7 test del quoziente Q6, oltre ai test del benchmark difetti e ai confronti Q1/P1. Artifact: [rgs-cochain-defect-report](https://github.com/fabianleonaressi95/theorem/actions/runs/42657016309/artifacts/13693051779).

A n=129 per il wedge dipole, la differenza energetica Q1/cochain è ancora 12,12%; la differenza Q1/Airy è 7,28% e cochain/Airy 18,52%. Non si dichiara quindi validazione energetica.

È stato preparato il piano per riprodurre direttamente il metodo pubblicato nel 2026: [MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md](rgs_defect_benchmark/MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md). Il metodo usa 3N problemi locali Airy in P3 C0-IPDG su domini perforati, una matrice finita di ricostruzione e parametri di core espliciti. Il nostro Airy a differenze finite resta un riferimento indipendente, non l'implementazione CIP-DG del gruppo.


### Confronto periodico Q6–FEM–Airy

È stato completato anche un audit separato per le condizioni periodiche, evitando di confrontare direttamente il quoziente toroidale Q6 con il benchmark a trazione libera. Sul toro ([0,4]^2), la cella Q6 (C_4\times C_4) è stata confrontata con Q1 FEM periodico e Airy spettrale di Fourier, per inclusione shear e dipolo shear lisci.

L'energia del campo Q1 periodico (4\times4), dopo il pullback sulla fibra Q6, coincide con l'energia FEM entro (1,5\times10^{-16}); il residuo cinematico di pullback è zero. Raffinando il FEM periodico da (n=4) a (n=32), lo scarto energetico rispetto ad Airy scende dal 2,127% allo 0,0254% per l'inclusione e dal 13,301% allo 0,0947% per il dipolo. Gli errori di stress a (n=32) sono rispettivamente 0,178% e 0,286%.

CI: [run 42657822468](https://github.com/fabianleonaressi95/theorem/actions/runs/42657822468); artifact [JSON/CSV](https://github.com/fabianleonaressi95/theorem/actions/runs/42657822468/artifacts/13691798892). Il confronto usa sorgenti periodiche lisce: non dimostra ancora il trasferimento di difetti singolari o disclinazioni sulla fibra Q6, né il morfismo verso la mesh fisica o la convergenza Mosco/Γ.
