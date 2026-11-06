# Registro maestro — estrazione e verifica delle formule

**Scopo:** estrarre in modo sistematico formule e risultati dalla bibliografia THEROEM e dalle fonti primarie reperite online, quindi verificarli indipendentemente prima di usarli nei teoremi RGS–PSU–PRISM–Q6.

## Stati epistemici
- **TRASCRITTA:** formula riportata dalla fonte con riferimento localizzabile.
- **ATTRIBUZIONE VERIFICATA:** autore, titolo, edizione e collocazione controllati.
- **VERIFICATA ANALITICAMENTE:** derivazione o prova ricostruita indipendentemente.
- **VERIFICATA SIMBOLICAMENTE/NUMERICAMENTE:** controllo computazionale documentato; non sostituisce una prova.
- **CONDIZIONALE:** corretta solo sotto ipotesi esplicite.
- **DA VERIFICARE:** fonte o passaggio non ancora controllato.
- **CONTESTATA/ERRATA:** discrepanza dimostrata e documentata.
- **APERTO:** manca un passaggio essenziale.

## Procedura obbligatoria per ogni voce
1. Registrare citazione primaria, edizione/versione, DOI/URL e pagina/equazione.
2. Estrarre la formula senza cambiare convenzioni o normalizzazioni.
3. Definire ogni simbolo, dominio, unità, ipotesi e convenzione.
4. Ricostruire il passaggio precedente e quello successivo nella fonte.
5. Cercare una seconda fonte indipendente o il testo originale.
6. Verificare dimensioni, segni, fattori, casi limite, simmetrie e condizioni di validità.
7. Eseguire controllo simbolico/numerico riproducibile quando pertinente.
8. Solo dopo, valutare un collegamento a un teorema THEROEM. La somiglianza formale non costituisce un ponte.

## Registro di avanzamento

| ID | Fonte / autore | Famiglia di formule | Stato iniziale | Scheda |
|---|---|---|---|---|
| F001 | Wyler (1969, 1971), Robertson (1971), Gilmore (1972), Adler (1972) | Espressione proposta per la costante di struttura fine e critica di scala | Formula trascritta; fondamento fisico non stabilito | [Wyler–Hua formula audit](wyler-hua/FORMULAS_AND_VERIFICATION.md) |
| F002 | L. K. Hua (1958/1963), domini classici | Domini di Cartan, operatori di Hua, kernel di Poisson–Szegő/Bergman e integrali | Parziale; formule da confrontare con la monografia primaria | [Wyler–Hua formula audit](wyler-hua/FORMULAS_AND_VERIFICATION.md) |
| F003 | A. Kitaoka (2019/2020, 2022); Rumin–Seshadri (2012); Cheeger–Müller | Laplaciano Rumin, restrizione a 2I, zeta regolarizzata e confronto topologico | Decomposizione n=1 Julg–Kasparov (pesi U(2), bordi VI–VII), restrizione SU(2), invarianti 2I via caratteri/Reynolds e Molien; intertwiner centrale D†D derivato esattamente; zeta non twistate e combinazione torsionale ridotte a Hurwitz; T_E=2π²/15 identificata con il volume nella convenzione non aciclica. Verifiche indipendenti esatte (caratteri/Molien m≤300, D simbolico, periodicità d_n n≤600, identità Gamma) e cross-check numerico ad alta precisione. Restano aperte la fase/matrice globale di D, ζ′₀(0), ζ′₁(0) separatamente e i twist non banali. | [Audit Kitaoka](spin-geometry-quaternionic/KITAOKA_RUMIN_FORMULA_AUDIT.md); [codice caratteri](spin-geometry-quaternionic/RUMIN_2I_N1_CHARACTER_AUDIT.py) |
| F004 | Kogut (1979), Wilson/lattice gauge | Hamiltoniana, plaquette action, vincoli di Gauss | Da estrarre dalla fonte primaria | Da aprire |
| F005 | Edwards–Anderson (1975), Sherrington–Kirkpatrick (1975) | Hamiltoniane EA/SK, distribuzioni quenched, overlap e replica trick | Formule base trascritte; limiti termodinamici distinti | [Audit spin glass](spin-glasses/SPIN_GLASS_FORMULA_AUDIT.md) |
| F006 | Parisi (1979–1980), Guerra (2003), Talagrand (2006), Panchenko (2013) | Funzionale di Parisi, interpolazione Guerra, identità Ghirlanda–Guerra, ultrametricità | Talagrand (2006) e Guerra (2003) confrontati con i testi primari; covarianza SK, PDE, penalità Parisi e fattore 1/2 fissati nella convenzione; direzione del bound chiarita (pressione vs energia libera); test esatto aggiunto | [Audit spin glass](spin-glasses/SPIN_GLASS_FORMULA_AUDIT.md) |
| F007 | Atiyah–Singer (1969) e geometria spinoriale | Indice di operatori ellittici/Fredholm | Fonti presenti; formulazione precisa da estrarre | Da aprire |
| F008 | Ryu–Takayanagi (2006), Faulkner–Lewkowycz–Maldacena (2013) | Entropia olografica e correzioni quantistiche | Da estrarre | Da aprire |
| F009 | TEGR / Weitzenböck / Einstein–Cartan | Torsione, scalare torsionale, identità con Ricci scalare | Bibliografia primaria da completare | Da aprire |
| F010 | Di Pietro–Ripà (2024/2026) | Cicli Hamiltoniani in grafi distanza degli ipercubi | Enunciato registrato; prova e definizioni da estrarre | Da aprire |

\n\n**Codice di verifica F006:** [PARISI_NORMALIZATION_AUDIT.py](spin-glasses/PARISI_NORMALIZATION_AUDIT.py) — covarianza su coppie \(i<j\), conversione pressione/free energy e identità della penalità discreta.\n## Regola di priorità
Si procede per dipendenza matematica, non per notorietà dell'autore. Prima le definizioni e i teoremi che alimentano direttamente T001–T010; poi le fonti di confronto; infine le proposte non standard, sempre con ricostruzione critica e test falsificabili.

## Prima tranche
La prima scheda tratta Wyler e Hua perché il repository contiene già T002–T008 su domini di tipo IV, densità di Bergman e marginali Wilson. Il risultato numerico di Wyler va tenuto separato dalla dimostrazione matematica di Hua e dalla giustificazione fisica della costante alpha.
