# KTHNY e \(\mathcal N=4\) Super Yang–Mills nel programma RGS–PRISM

**Data:** 12 novembre 2026  
**Ambito:** dossier Morandotti; difetti 2D, Q6, dualità e operatori di difetto  
**Stato:** quadro comparativo e programma di collegamento. Non si afferma un'equivalenza tra KTHNY e \(\mathcal N=4\) SYM.

## 1. Perché includere entrambe

Le due teorie entrano nel programma per ragioni diverse e complementari:

- **KTHNY** è il riferimento fisico-statistico diretto per la fusione in due dimensioni mediata da difetti topologici: dislocazioni e disclinazioni, loro unbinding, screening e rinormalizzazione delle costanti elastiche.
- **\(\mathcal N=4\) Super Yang–Mills (SYM)** è una teoria di gauge conforme in quattro dimensioni con supersimmetria estesa, dualità elettrico-magnetica e operatori di linea/difetto. Offre strumenti per classificare cariche e settori di difetto e per studiare trasformazioni duali.

Non sono la stessa teoria, non hanno lo stesso numero di dimensioni né gli stessi gradi di libertà. KTHNY descrive un sistema elastico/statistico bidimensionale; \(\mathcal N=4\) SYM è una teoria quantistica di gauge 3+1-dimensionale (o formulata euclideamente in quattro dimensioni). Il collegamento deve passare attraverso una costruzione efficace o una corrispondenza dimostrata, non per analogia verbale.

## 2. Livello KTHNY: gas di difetti e rinormalizzazione elastica

Nel quadro KTHNY la fusione bidimensionale può avvenire in due passaggi: unbinding delle dislocazioni dal solido alla fase esatica e successivo unbinding delle disclinazioni dalla fase esatica al liquido isotropo, nei regimi in cui la transizione è continua e lo scenario KTHNY è applicabile.

Una variabile adimensionale comunemente usata è la rigidità di Young
\[
K=\frac{Y a^2}{k_B T},
\]
dove \(Y\) è il modulo di Young, \(a\) una scala reticolare e \(T\) la temperatura. Alla soglia di unbinding delle dislocazioni, la rigidità **rinormalizzata** soddisfa il criterio universale
\[
K_R=16\pi.
\]
Il valore del modulo nudo non è universale: dipende dall'energia di core e dal modello microscopico. Le equazioni RG evolvono almeno la rigidità elastica e la fugacità delle dislocazioni; il settore delle disclinazioni governa la transizione successiva.

Per il dossier Morandotti questo fornisce un benchmark fisico concreto: energia dei difetti, interazione a lunga distanza, fugacità, screening, moduli elastici rinormalizzati e dipendenza dalla scala. Il prototipo Saint-Venant/KKT e la baseline Airy/CIP-DG possono essere confrontati con questi osservabili, ma soltanto dopo aver allineato core, condizioni al contorno, parametri e regime termodinamico.

## 3. Livello Q6: una possibile discretizzazione del settore dei difetti

Lo spazio dei 64 esagrammi \(\mathcal H=\{0,1\}^6\) e il complesso cubico Q6 forniscono un dominio discreto sul quale definire osservabili, transizioni e correnti. La specifica [Q6_HEXAGRAM_CHARGES_MOIRE_GREEN_KUBO.md](Q6_HEXAGRAM_CHARGES_MOIRE_GREEN_KUBO.md) mantiene l'informazione di carica per ciascun esagramma.

Per un confronto KTHNY non basta chiamare tali osservabili "cariche". Occorre costruire e verificare una mappa che distingua almeno:
- vettore di Burgers \(\mathbf b\) per le dislocazioni;
- carica angolare/Frank \(s\) per le disclinazioni;
- energia di core e fugacità \(y\);
- interazione tra difetti e relativa dipendenza dalla distanza;
- vincoli di neutralità e condizioni al contorno.

Una possibile forma di partizione per un gas di difetti, da derivare dal modello microscopico e non postulare, è
\[
Z=\sum_{\{n_\alpha\}}\!
\exp\!\left[-\beta\left(E_{\rm el}(\{n_\alpha\})+
\sum_\alpha E_{c,\alpha}|n_\alpha|\right)\right],
\]
con specie \(\alpha\) distinte per tipo e carica del difetto. Le fugacità sono \(y_\alpha\sim e^{-\beta E_{c,\alpha}}\), a fattori di misura e convenzioni fissati. Il compito RGS–PRISM è derivare l'energia e la mappa da Q6, non assumere che i 64 stati siano già un gas di dislocazioni.

## 4. Livello \(\mathcal N=4\) SYM: cariche, linee e dualità

La teoria \(\mathcal N=4\) SYM ha gruppo di gauge, ad esempio, \(SU(N)\), accoppiamento complesso
\[
\tau=\frac{\theta}{2\pi}+\frac{4\pi i}{g_{\rm YM}^2},
\]
e dualità elettrico-magnetica \(S\) che agisce su \(\tau\) e sullo spettro degli operatori di linea. Gli operatori di Wilson e di 't Hooft (e più in generale Wilson–'t Hooft) portano cariche elettriche e magnetiche; la loro classificazione e trasformazione sotto dualità sono un settore matematicamente ben definito.

Questo è pertinente al programma come linguaggio per:
1. classificare cariche e settori di difetto;
2. studiare operatori di linea e olonomie;
3. analizzare trasformazioni duali che scambiano dati elettrici e magnetici;
4. costruire, se giustificato, osservabili di correlazione in presenza di difetti.

Non si deve però identificare direttamente:
\[
\text{carica Wilson/'t Hooft}\ne
\text{vettore di Burgers o carica di Frank}.
\]
Le prime sono cariche di gauge definite dalla teoria e dal gruppo; le seconde sono invarianti geometrici/elasticI di difetti cristallini. Un'identificazione richiede una mappa di campi, gruppi, unità, condizioni al contorno e azione, oppure una riduzione/teoria efficace esplicita.

## 5. Il ponte matematico da cercare

Il collegamento può essere articolato in tre problemi indipendenti.

### P1 — Gas di Coulomb e settore topologico

Derivare dalla teoria elastica 2D l'energia efficace delle cariche di difetto e confrontarne la struttura con un gas di Coulomb. Separare il settore traslazionale (Burgers) da quello rotazionale (Frank). Verificare neutralità, kernel d'interazione, fugacità e flusso RG. Questo è il ponte primario KTHNY–Morandotti.

### P2 — Connessione/olonomia e operatori di linea

Definire una connessione discreta e la sua olonomia sui cicli del complesso. Confrontare la classificazione geometrica delle olonomie con la logica degli operatori di Wilson–'t Hooft: linee, cariche, dualità e dati globali del gruppo. È un confronto strutturale; non è ancora una derivazione da \(\mathcal N=4\) SYM del modello elastico.

### P3 — Riduzione o interfaccia efficace

Cercare una costruzione precisa (riduzione dimensionale, teoria di difetto, interfaccia/boundary condition o settore efficace) che produca un sistema 2D le cui variabili e cariche abbiano un'identificazione dimostrabile con i difetti KTHNY. Solo a questo livello si potrà parlare di un ponte fisico tra le due teorie. Una semplice somiglianza tra dualità elettrico-magnetica e scambio di cariche non è sufficiente.

## 6. Criteri di verifica

- Riprodurre il criterio KTHNY \(K_R=16\pi\) nel regime di unbinding delle dislocazioni e distinguere rigidità nuda e rinormalizzata.
- Calcolare energia di core e fugacità per le configurazioni di difetto del benchmark Morandotti.
- Verificare il flusso RG e la separazione tra transizione di dislocazione e di disclinazione, quando lo scenario a due transizioni è applicabile.
- Definire sul complesso Q6 le mappe di carica e i bilanci; confrontare correlazioni e statistiche con il gas efficace.
- Per il settore SYM, specificare gruppo di gauge, global form, spettro di cariche, operatori di linea, accoppiamento \(\tau\) e azione della dualità.
- Dimostrare una mappa o una riduzione che preservi le quantità dichiarate. In assenza, mantenere i due settori come modelli comparativi distinti.

## 7. Classificazione epistemica

| Affermazione | Stato |
|---|---|
| KTHNY descrive un meccanismo di fusione 2D mediato da difetti | Teoria consolidata nel proprio regime di applicabilità |
| Criterio universale \(K_R=16\pi\) per l'unbinding delle dislocazioni | Risultato KTHNY; modulo rinormalizzato |
| Il benchmark Morandotti può essere testato contro KTHNY | Programma concreto da implementare |
| Le 64 cariche Q6 rappresentano direttamente Burgers/Frank | Non dimostrato |
| \(\mathcal N=4\) SYM possiede operatori Wilson–'t Hooft e dualità S | Teoria consolidata |
| Le cariche Wilson/'t Hooft coincidono con Burgers/Frank | Falso come identificazione diretta; richiede una mappa non banale |
| Esiste una riduzione di \(\mathcal N=4\) SYM che produce il modello KTHNY/RGS | Problema aperto di ricerca |

## 8. Riferimenti essenziali

1. D. R. Nelson, B. I. Halperin, “Dislocation-mediated melting in two dimensions”, *Physical Review B* 19 (1979), 2457. DOI: [10.1103/PhysRevB.19.2457](https://doi.org/10.1103/PhysRevB.19.2457).
2. A. P. Young, “Melting and the vector Coulomb gas in two dimensions”, *Physical Review B* 19 (1979), 1855. DOI: [10.1103/PhysRevB.19.1855](https://doi.org/10.1103/PhysRevB.19.1855).
3. A. P. Young, “On the theory of the melting transition”, *Physical Review B* 19 (1979), 1855 [controllare il riferimento bibliografico preciso prima della citazione definitiva: il record 2 è il riferimento verificato per il gas di Coulomb].
4. A. Kapustin, “Wilson–’t Hooft operators in four-dimensional gauge theories and S-duality”, *Physical Review D* 74 (2006), 025005. DOI: [10.1103/PhysRevD.74.025005](https://doi.org/10.1103/PhysRevD.74.025005).
5. Y. Hatsuda, T. Okazaki, “S-duality of boundary lines in \(\mathcal N=4\) SYM theories and supersymmetric indices”, *JHEP* 08 (2025) 127. DOI: [10.1007/JHEP08(2025)127](https://doi.org/10.1007/JHEP08(2025)127).
6. P. Cesana, L. De Luca, M. Morandotti (2024), “Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method”, *SIAM Journal on Mathematical Analysis* 56(1), 79–136. DOI: [10.1137/22M1523443](https://doi.org/10.1137/22M1523443).

**Nota bibliografica:** il riferimento Young è riportato una sola volta in bibliografia definitiva; il duplicato esplicativo sopra va eliminato in una revisione editoriale successiva.
