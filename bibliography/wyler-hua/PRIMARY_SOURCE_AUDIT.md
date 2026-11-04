# Audit delle fonti primarie: Wyler–Robertson–Gilmore–Adler–Hua

## Esito sintetico

Questa verifica separa la geometria dei domini simmetrici dalla pretesa fisica sulla costante di struttura fine. Le fonti storiche non autorizzano a presentare la formula di Wyler come derivazione accettata di \(\alpha\).

## Fonti e risultati verificati

### 1. Armand Wyler (1969)

A. Wyler, “L’espace symétrique du groupe des équations de Maxwell”, *Comptes Rendus de l’Académie des Sciences de Paris*, série A-B, **269** (1969), 743–745.

- Riferimento primario identificato nei cataloghi e nelle bibliografie.
- Non è stato recuperato in questa verifica un testo integrale consultabile; non attribuiamo al breve articolo passaggi tecnici non letti direttamente.
- Link bibliografico di riscontro: https://oeis.org/A180872

### 2. Armand Wyler (1971)

A. Wyler, “Les groupes des potentiels de Coulomb et de Yukawa”, *Comptes Rendus de l’Académie des Sciences de Paris*, série A, **271** (1971), 186–188.

- Correzione importante: il volume è **271**, non 272. La variante 272 presente in alcune bibliografie è un errore di trascrizione.
- Anche qui il testo integrale non è stato verificato direttamente.

### 3. Baldwin Robertson (1971)

B. Robertson, “Wyler’s Expression for the Fine-Structure Constant α”, *Physical Review Letters* **27**(22), 1545–1547 (29 novembre 1971), DOI [10.1103/PhysRevLett.27.1545](https://doi.org/10.1103/PhysRevLett.27.1545).

- L'autore è **Baldwin Robertson**, non Bruce Robertson.
- Il suo abstract afferma che l'accordo con il valore sperimentale si ottiene soltanto scegliendo arbitrariamente il raggio delle regioni uguale a 1; la relazione con il gruppo di invarianza dell'equazione d'onda non fissa quel raggio.
- Questo è un'obiezione matematica precisa alla normalizzazione usata per ottenere il numero, non una confutazione della geometria dei domini simmetrici.

### 4. Robert Gilmore (1972)

R. Gilmore, “Scaling of Wyler’s Expression for α”, *Physical Review Letters* **28**(7), 462–464 (14 febbraio 1972), DOI [10.1103/PhysRevLett.28.462](https://doi.org/10.1103/PhysRevLett.28.462).

- Gilmore risponde all'obiezione di Robertson: nell'abstract sostiene che la scelta \(r=1\) rende tutti gli elementi del dominio limitato \(D^n\) anche rappresentanti di coset e quindi operazioni di gruppo.
- Questo è un argomento da esaminare nel testo integrale. L'abstract non basta a stabilire che la scelta sia fisicamente obbligata, né che la formula produca una derivazione universalmente accettata di \(\alpha\).

### 5. Stephen L. Adler (1972)

S. L. Adler, “Theories of the Fine Structure Constant α”, FERMILAB-PUB-72/059-T (1972), [PDF Fermilab](https://lss.fnal.gov/archive/1972/pub/Pub-72-059-T.pdf).

- Il rapporto classifica esplicitamente la formula di Wyler nella sezione “Numerological Speculations”.
- Riporta la formula numerica \(\alpha\simeq1/137.03608\), ma conclude che resta aperta la questione se l'accordo abbia una base fisica o sia fortuito.
- È una valutazione critica storica autorevole, non un teorema di impossibilità.

### 6. Loo-Keng Hua (1963)

L. K. Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains*, Translations of Mathematical Monographs 6, American Mathematical Society (1963), DOI [10.1090/mmono/006](https://doi.org/10.1090/mmono/006).

- La scheda AMS conferma la monografia e i capitoli su domini classici, integrali, coordinate matriciali e analisi armonica.
- La fonte è pertinente alla geometria e all'analisi dei domini classici; non è una fonte che dimostri la formula fisica di Wyler o un'origine Wilson della misura.
- Il risultato T002 del repository va trattato come calcolo autonomo esplicito della densità di Bergman, con convenzioni dichiarate, non come una formula da attribuire automaticamente a Hua.

## Conseguenze per i teoremi RGS–PSU–PRISM

| Oggetto | Cosa è supportato | Cosa non è supportato |
|---|---|---|
| Dominio di tipo IV / Lie ball | Letteratura matematica sui domini simmetrici e analisi di Hua | Identificazione fisica automatica con lo spazio efficace PSU |
| Densità \(N(z)^{-5}\) in T002 | Calcolo determinante della metrica di Bergman scritto nel teorema | Derivazione da Wilson, Q6 o da Wyler |
| Numero di Wyler per \(\alpha\) | Formula storica e discussione Robertson–Gilmore–Adler | Derivazione fisica indipendente e accettata della costante |
| Cutoff Hua | Può essere definito geometricamente in un problema matematico | Non può essere scelto per calibrare \(\alpha\) o far coincidere un volume |
| Ponte Wilson–Bergman | T003–T005 delimitano no-go atomico, possibilità di limite e positività della marginale | Non è dimostrata la convergenza della marginale Wilson a \(N^{-5}d^{10}z\) |

## Correzioni bibliografiche applicate

- “Bruce Robertson” corretto in **Baldwin Robertson**.
- Wyler 1971 corretto da volume **272** a volume **271**.
- Aggiunti Gilmore (1972) e Adler (1972), necessari per rappresentare la discussione storica completa.
- Il volume di Gilmore del 1974 resta distinto dall'articolo PRL del 1972.

## Prossimo test scientifico, senza duplicare i teoremi

Non serve riscrivere T002–T005. Il prossimo controllo utile è verificare nel manoscritto RGS quali passaggi usino davvero la scelta \(r=1\), la normalizzazione dei volumi e il dominio \(D_5\). Ogni uso va classificato come:
1. identità geometrica;
2. convenzione di normalizzazione;
3. ipotesi fisica aggiuntiva;
4. conseguenza dimostrata della marginale Wilson.

Finché la mappa e la convergenza Wilson non sono dimostrate, la formula di Wyler resta contesto storico e non premessa del teorema di convergenza.
