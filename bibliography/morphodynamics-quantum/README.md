# Morfodinamica Quantistica — bibliografia critica e mappa delle dipendenze

**Aggiornato:** 13 novembre 2026  
**Scopo:** selezionare letteratura e software che aiutino a derivare, implementare e verificare un modello di dinamica geometrico-quantistica su Q6/RGS. Questa pagina non afferma che la Morfodinamica Quantistica sia già una teoria fisica convalidata.

## 1. Domande matematiche guida

1. **Accoppiamento ibrido:** quale struttura variazionale/hamiltoniana accoppia variabili geometriche classiche e stati quantistici senza perdere positività, normalizzazione e invarianti?
2. **Geometria dipendente dal tempo:** quando una famiglia di operatori quantistici su grafi/geometrie variabili genera evoluzione unitaria? Come si identifica lo spazio di Hilbert a tempi diversi?
3. **Retroazione:** quando l'approssimazione mean-field/Ehrenfest è affidabile e quando entanglement e instabilità richiedono dinamica quantistica completa o metodi stocastici?
4. **Discretizzazione strutturale:** quali complessi, proiezioni commutanti, operatori Hodge e integratori preservano le identità geometriche e gli invarianti?
5. **Limite continuo:** quali ipotesi di compattezza, consistenza, stabilità e raffinamento permettono di passare dal complesso Q6/PRISM a un operatore continuo?

## 2. Letteratura primaria verificata

### A. Accoppiamento quantistico-classico e principi variazionali

**A1. François Gay-Balmaz, Cesare Tronci (2022).** “Evolution of hybrid quantum–classical wavefunctions.” *Physica D: Nonlinear Phenomena* 440, 133450.  
DOI: https://doi.org/10.1016/j.physd.2022.133450  
Preprint: https://arxiv.org/abs/2112.12144  
**Stato:** articolo peer-reviewed; metadati e abstract verificati presso editore/archivio.  
**Perché leggerlo:** formula una dinamica ibrida gauge-invariante tramite wavefunctions classiche di Koopman, principi variazionali e fattorizzazioni; discute densità classica/quantistica, invarianti di Poincaré e casi speciali mean-field/Ehrenfest.  
**Uso per MQM:** riferimento teorico principale per verificare se il semplice sistema Ehrenfest `(q,p,ψ)` di MQM-1B sia troppo restrittivo e quali variabili di fase/spazio delle fasi vadano aggiunte.  
**Limite di trasferimento:** non è una derivazione del modello Q6, né identifica le variabili RGS con gradi di libertà quantistici.

**A2. François Gay-Balmaz, Cesare Tronci (2022).** “Koopman wavefunctions and classical states in hybrid quantum–classical dynamics.” *Journal of Geometric Mechanics* 14(4), 559–596.  
DOI: https://doi.org/10.3934/jgm.2022019  
**Stato:** articolo peer-reviewed; metadati verificati.  
**Perché leggerlo:** approfondisce la relazione fra stati classici, wavefunctions di Koopman, gauge e formulazione geometrica della dinamica ibrida.  
**Uso per MQM:** chiarire lo spazio degli stati classici e la struttura simplettica prima di scegliere un accoppiamento discreto.

### B. Grafi quantistici con geometria variabile

**B1. Uzy Smilansky, Gilad Sofer (2024).** “Time evolution and the Schrödinger equation on time dependent quantum graphs.” *Journal of Physics A: Mathematical and Theoretical* 57, 065204.  
DOI: https://doi.org/10.1088/1751-8121/ad1fb6  
Preprint: https://arxiv.org/abs/2210.14652  
**Stato:** articolo peer-reviewed open access; metadati e abstract verificati presso IOP/arXiv.  
**Perché leggerlo:** tratta grafi metrici con lunghezze degli archi dipendenti dal tempo; mostra che la buona posizione e l'unitarietà richiedono una formulazione attenta dell'operatore e delle condizioni ai vertici; studia una fase geometrica adiabatica.  
**Uso per MQM:** riferimento essenziale per distinguere (i) pesi/conduttanze variabili sul grafo combinatorio fisso, (ii) lunghezze metriche variabili e (iii) variazione dello spazio di Hilbert.  
**Limite di trasferimento:** Q6 in MQM-1 è un grafo finito pesato con Hilbert `C^64`; non è automaticamente un grafo metrico quantistico con funzioni d'onda sugli archi. Le ipotesi e le condizioni al vertice del lavoro vanno tradotte, non copiate.

### C. Retroazione semiclassica e validità dell'approssimazione

**C1. Fabio van Dissel, George Zahariade (2025).** “Semiclassical backreaction: A qualitative assessment.” *Physical Review D* 111, 065008.  
DOI: https://doi.org/10.1103/PhysRevD.111.065008  
Preprint: https://arxiv.org/abs/2411.19825  
**Stato:** articolo peer-reviewed; pubblicazione APS del 4 marzo 2025 verificata.  
**Perché leggerlo:** confronta mean-field e truncated-Wigner stocastico con il riferimento quantistico completo in un modello accoppiato; evidenzia il ruolo di entanglement e instabilità classiche nella perdita di affidabilità delle approssimazioni semiclassiche.  
**Uso per MQM:** definire un benchmark ridotto in cui confrontare MQM-1B/Ehrenfest con un modello totalmente quantistico su pochi gradi di libertà; misurare errore di retroazione, entanglement e tempi di validità.  
**Limite di trasferimento:** il modello studiato non è Q6/RGS e non fornisce una soglia universale di validità.

### D. FEEC, complessi di Hilbert e convergenza DEC/Hodge–Dirac

**D1. Douglas N. Arnold, Richard S. Falk, Ragnar Winther (2006).** “Finite element exterior calculus, homological techniques, and applications.” *Acta Numerica* 15, 1–155.  
DOI: https://doi.org/10.1017/S0962492906210018  
**Stato:** articolo di riferimento peer-reviewed; metadati verificati presso Cambridge University Press.  
**Perché leggerlo:** costruisce il quadro FEEC di sottocomplessi discreti, proiezioni commutanti, coomologia e stabilità per Hodge Laplaciano, Maxwell ed elasticità.  
**Uso per MQM:** base teorica per il programma di raffinamento; il requisito centrale non è una somiglianza spettrale, ma una famiglia di complessi e proiezioni compatibili con il differenziale.

**D2. Douglas N. Arnold, Richard S. Falk, Ragnar Winther (2010).** “Finite element exterior calculus: From Hodge theory to numerical stability.” *Bulletin of the American Mathematical Society* 47(2), 281–354.  
DOI: https://doi.org/10.1090/S0273-0979-10-01278-4  
Preprint: https://arxiv.org/abs/0906.4325  
**Stato:** articolo peer-reviewed; metadati verificati.  
**Perché leggerlo:** esposizione del quadro astratto dei complessi di Hilbert e delle condizioni di stabilità/convergenza: sottocomplesso e proiezione di cochain limitata.

**D3. Radovan Dabetić, Ralf Hiptmair (2026).** “Convergence of discrete exterior calculus for the Hodge–Dirac operator.” *Calcolo* 63, article 21.  
DOI: https://doi.org/10.1007/s10092-026-00694-z  
Codice degli esperimenti dichiarato dagli autori: https://github.com/rdabetic/2d_dec_dirac  
**Stato:** articolo open access, pubblicato il 7 maggio 2026; metadati e pagina dell'editore verificati.  
**Perché leggerlo:** fornisce una prova di convergenza DEC per Hodge–Dirac in un quadro analitico preciso e rende disponibile il codice degli esperimenti.  
**Uso per MQM:** riferimento contemporaneo per progettare un benchmark di convergenza dell'operatore discreto e per individuare le ipotesi geometriche e analitiche che devono essere verificate.  
**Limite di trasferimento:** il risultato non dimostra la convergenza della geometria Q6/RGS; mesh, ricostruzioni, spazi e ipotesi vanno confrontati uno per uno.

## 3. Repository software esterni: uso e limiti

| Repository | Capacità documentate | Impiego concreto previsto | Cautela |
|---|---|---|---|
| [PyDEC](https://github.com/hirani/pydec) | Complessi simpliciali e cubici astratti, cobordo, Hodge star DEC, matrici di massa Whitney/FEEC | Benchmark indipendente per operatori cubici, coomologia e Hodge | Progetto storico; controllare compatibilità Python e dipendenze prima di integrarlo |
| [formoniq](https://github.com/luiswirth/formoniq) | Engine FEEC Rust, geometria simpliciale intrinseca/Regge, firme pseudo-riemanniane, Hodge–Dirac, integratori simplettici | Confronto per geometria dinamica, Hodge–Dirac e integrazione conservativa | Il README dichiara codice di ricerca in sviluppo attivo; non assumere validazione indipendente o equivalenza con Q6 |
| [DDF.jl](https://github.com/eschnett/DDF.jl) | FEEC/forme differenziali in dimensione arbitraria, mesh simpliciali | Seconda implementazione di confronto concettuale | README dichiara esplicitamente funzionalità mancanti e API in evoluzione (nota del 2020) |
| [QGLAB / Quantum-Graphs](https://github.com/manroygood/Quantum-Graphs) | Grafi metrici, condizioni ai vertici, Laplaciani, metodi differenze finite/Chebyshev, PDE dipendenti dal tempo | Prototipo per confronto con grafi metrici quantistici | MATLAB e impostazione su archi continui: non sostituisce il modello discreto a 64 siti |
| [2d_dec_dirac](https://github.com/rdabetic/2d_dec_dirac) | Codice degli esperimenti dell'articolo Dabetić–Hiptmair 2026 | Riprodurre il benchmark Hodge–Dirac dell'articolo prima di adattarne le ipotesi | Il benchmark è bidimensionale e non prova direttamente il limite Q6 |

**Regola di riuso:** nessun repository esterno va copiato integralmente o trattato come validazione del nostro modello. Prima si riproduce un benchmark minimo indipendente, poi si porta nel codice Q6 soltanto l'algoritmo o la struttura matematica pertinente, mantenendo attribuzione e licenza.

## 4. Mappa delle dipendenze con i risultati interni

| Fonte interna | Oggetto già disponibile | Cosa riutilizzare | Obbligo ancora aperto |
|---|---|---|---|
| [MQM-1 / PR #259](https://github.com/fabianleonaressi95/theorem/pull/259) | Modello finito dissipativo con `H(x)=γB diag(e^x)Bᵀ` e stato `ψ∈C^64` | Convenzioni Q6, Hamiltoniana pesata, gradienti e test già implementati nella PR | Derivare i parametri e confrontare con una dinamica geometrica conservativa |
| [T113-D](../../theorems/T113D-q6-rgs-phonon-internal-mode.md) | Azione quadratica conservativa Q6–RGS; distinzione fra Q6 e simmetria puntuale indotta | Variabili geometriche, inerzia, rigidezza e settori interni | Specificare rappresentazione interna, coefficienti e mappa verso lo stato quantistico |
| [T113-F](../../theorems/T113F-q6-graph-elastic-stabilization.md) | Forma di Dirichlet Q6 e soglia di stabilizzazione del tripletto T2u | Potenziale/stiffness geometrica derivata dall'incidenza | Identificare unità fisiche e coefficienti costitutivi |
| [T113-A](../../theorems/T113A-metric-action-phonon-phason-mode-sensitivity.md) | Azione covariante materiale e identità di sensibilità spettrale | Variazione metrica e confronto dei modi | Stress-energy completo e ricostruzione spaziale/continua |
| [T102](../../theorems/T102-cubical-supersymmetry-heat-kernel-sakharov.md) | Complesso cubico, algebra Hodge-SUSY finita e supertraccia esatta | Struttura di cochain, Laplaciani per grado e benchmark spettrali | Famiglia di operatori accoppiata a metrica e limite continuo |
| [FEEC/Mosco](../../projects/README.md) | Programma di raffinamento e convergenza | Proiezioni, compattezza, stabilità armonica e convergenza degli operatori | Costruire una famiglia di raffinamenti Q6/PRISM con ipotesi dimostrate |

### Distinzioni strutturali da preservare

- **Pesi vs metrica:** cambiare le conduttanze `e^{x_e}` su un grafo combinatorio fisso non equivale a cambiare la lunghezza metrica degli archi di un quantum graph.
- **Ibrido vs quantizzato:** `(q,p,ψ)` con `q,p` classici e `ψ` quantistico è un modello ibrido, non una quantizzazione completa della geometria.
- **Conservativo vs dissipativo:** il gradiente discendente MQM-1A ha energia monotona; il modello hamiltoniano con momenti geometrici deve avere un bilancio energetico autonomo distinto. Non si devono confondere.
- **Topologia vs simmetria:** Q6 conserva il suo complesso cubico; la simmetria (O_h) della nuvola RGS non è automaticamente una simmetria del grafo Q6 (vedi T113-D).
- **Finito vs continuo:** la convergenza FEEC/DEC richiede una famiglia di spazi, mappe di interpolazione/proiezione e stime uniformi; uno spettro finito o un test numerico non bastano.

## 5. Priorità operative

1. **Alta — audit variazionale MQM-1B.** Confrontare l'ansatz Ehrenfest con il formalismo ibrido Gay-Balmaz–Tronci. Derivare equazioni da un'azione e controllare norma, energia, gauge e positività.
2. **Alta — benchmark di geometria dipendente dal tempo.** Usare Smilansky–Sofer per isolare il caso di metrica sugli archi variabile rispetto al caso di soli pesi Q6 variabili.
3. **Alta — benchmark FEEC/DEC.** Riprodurre Dabetić–Hiptmair e PyDEC su un complesso cubico di controllo prima di progettare il raffinamento Q6.
4. **Media — validità della retroazione.** Costruire un sistema ridotto con pochi siti/modi, confrontare ibrido e quantistico completo e misurare l'errore di backreaction e l'entanglement.
5. **Media — integratori simplettici.** Confrontare un integratore simplettico per ((q,p)) con propagazione unitaria per (psi); documentare l'errore sul bilancio energetico e sulla norma.

## 6. Protocollo di aggiornamento bibliografico

Per ogni nuova voce registrare: citazione completa, DOI/arXiv, pagina primaria verificata, stato peer-review/preprint, data dell'ultimo controllo, contributo matematico preciso, collegamento interno e limite di trasferibilità. Per il software registrare URL, licenza, linguaggio, ultimo aggiornamento visibile, test/CI e benchmark riproducibile. Non promuovere un risultato numerico a teorema e non promuovere un modello interno a legge fisica senza derivazione e confronto empirico.

## 7. Fonti web verificate per questa scheda

- Gay-Balmaz–Tronci, Physica D: https://www.sciencedirect.com/science/article/pii/S0167278922001804
- Gay-Balmaz–Tronci, arXiv: https://arxiv.org/abs/2112.12144
- Smilansky–Sofer, IOP: https://doi.org/10.1088/1751-8121/ad1fb6
- van Dissel–Zahariade, APS: https://doi.org/10.1103/PhysRevD.111.065008
- Dabetić–Hiptmair, Springer: https://doi.org/10.1007/s10092-026-00694-z
- Arnold–Falk–Winther, Cambridge: https://doi.org/10.1017/S0962492906210018
- PyDEC paper: https://doi.org/10.1145/2382585.2382588

