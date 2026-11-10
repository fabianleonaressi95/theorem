# Confronto periodico Q6–Q1–P1–Airy — 9 novembre 2026

**CI verificata:** [run 42659067311 — success](https://github.com/fabianleonaressi95/theorem/actions/runs/42659067311)  
**Artifact JSON/CSV:** [rgs-cochain-defect-report, artifact 13693946123](https://github.com/fabianleonaressi95/theorem/actions/runs/42659067311/artifacts/13693946123)  
**Script:** scripts/rgs_periodic_q6_fem_airy.py  
**Ambito:** elasticità lineare isotropa 2D su toro periodico; sorgenti lisce; confronto numerico, non prova di convergenza.

## 1. Obiettivo e condizioni allineate

Il benchmark mette sullo stesso dominio e con le stesse condizioni al contorno quattro oggetti distinti:

1. **Q6 quotient:** il quoziente cinematico finito \(C_4\square C_4\), 16 vertici e fibra interna di cardinalità 4;
2. **Q1 FEM:** quadrilateri bilineari periodici, quadratura completa di Gauss \(2\times2\);
3. **P1 cochain:** triangolazione periodica degli stessi nodi e delle stesse celle, gradiente costante per triangolo, diagonali SW–NE e SE–NW;
4. **Airy spettrale:** soluzione indipendente in Fourier del problema biharmonico periodico, con ripristino del modo medio di tensione.

Parametri comuni:
- dominio fisico \([0,4]\times[0,4]\);
- \(\lambda=\mu=1\);
- spostamento periodico, con i due modi traslazionali rimossi fissando un vertice;
- medesima eigenstrain shear, campionata al centro delle celle;
- due casi: inclusione gaussiana shear e dipolo gaussiano shear.

Le sorgenti sono regolarizzate e lisce. Non sono nuclei singolari di Volterra, non sono disclinazioni singolari e non costituiscono calibrazione su un materiale reale.

## 2. Risultati energetici

Differenza relativa rispetto ad Airy:
\[
\delta_E=\frac{|E_{\mathrm{disc}}-E_{\mathrm{Airy}}|}
{\max(|E_{\mathrm{disc}}|,|E_{\mathrm{Airy}}|)}.
\]

| Sorgente | n | Q1–Airy energia | P1–Airy energia | Q1–P1 energia |
|---|---:|---:|---:|---:|
| Inclusione shear | 4 | 2,127% | 4,290% | 2,210% |
| Inclusione shear | 8 | 0,454% | 1,590% | 1,141% |
| Inclusione shear | 16 | 0,104% | 0,420% | 0,317% |
| Inclusione shear | 32 | 0,0254% | 0,1070% | 0,0815% |
| Dipolo shear | 4 | 13,301% | 21,939% | 9,963% |
| Dipolo shear | 8 | 1,691% | 5,970% | 4,352% |
| Dipolo shear | 16 | 0,387% | 1,633% | 1,251% |
| Dipolo shear | 32 | 0,0947% | 0,4195% | 0,3251% |

Q1 e P1 convergono entrambi verso Airy per entrambe le sorgenti. In questo benchmark Q1 è quantitativamente più vicino ad Airy a ogni livello riportato; non emerge un vantaggio numerico P1. La differenza Q1–P1 si riduce con il raffinamento.

## 3. Errori dei campi P1 rispetto ad Airy

| Sorgente | n | errore stress P1 | errore strain P1 |
|---|---:|---:|---:|
| Inclusione shear | 4 | 21,2647% | 9,9657% |
| Inclusione shear | 8 | 7,9829% | 4,1831% |
| Inclusione shear | 16 | 2,1663% | 1,1653% |
| Inclusione shear | 32 | 0,5570% | 0,3025% |
| Dipolo shear | 4 | 35,9438% | 27,8626% |
| Dipolo shear | 8 | 12,7709% | 9,5354% |
| Dipolo shear | 16 | 3,4774% | 2,6663% |
| Dipolo shear | 32 | 0,8959% | 0,6936% |

Gli errori Q1 sono riportati nello stesso report JSON/CSV. A \(n=32\), per l'inclusione shear, gli errori Q1 sono 0,1777% stress e 0,0772% strain; per il dipolo sono 0,2863% e 0,1744%.

## 4. Identità esatte e audit topologico

Per il P1 periodico il complesso triangolato è costruito con matrici di incidenza intere sparse:
- \(n=4\): 16 vertici, 48 spigoli, 32 triangoli;
- \(n=8\): 64 vertici, 192 spigoli, 128 triangoli;
- \(n=16\): 256 vertici, 768 spigoli, 512 triangoli;
- \(n=32\): 1024 vertici, 3072 spigoli, 2048 triangoli.

Per entrambe le diagonali e tutti i livelli il residuo esatto \(D_1D_0\) è zero. La differenza relativa di energia tra le due diagonali P1 è inferiore a \(6\times10^{-16}\).

Sul livello \(n=4\), che è il quoziente Q6 effettivo:
- il lift dei 16 spostamenti quoziente ai 64 stati Q6 conserva esattamente il pullback delle 192 cochain di spigolo: residuo massimo zero;
- l'energia Q6-lift coincide con Q1 entro errore relativo \(1,5\times10^{-16}\);
- l'energia P1-lift coincide con P1 entro precisione macchina (residuo relativo zero nel report).

La diagonale triangolare è una differenza derivata tra vertici già presenti: non è un nuovo spigolo nativo del grafo Q6. Il complesso P1 triangolato è quindi un'estensione per suddivisione delle celle del quoziente, non un'identificazione automatica con il suo 1-scheletro.

## 5. Residui numerici

- residui relativi dei sistemi Q1 e P1: ordine \(10^{-14}\) o inferiori;
- residuo della compatibilità spettrale Airy: ordine \(10^{-16}\);
- residui di catena P1: esattamente zero;
- residui del pullback Q6 a \(n=4\): esattamente zero.

## 6. Interpretazione: cosa è chiuso e cosa no

**Chiuso da questo confronto**
- il confronto periodico è ora allineato per dominio, materiale, sorgente e condizioni al contorno;
- il quoziente Q6 a \(4\times4\) è confrontato con Q1 e P1 sulla stessa cella;
- Airy spettrale fornisce un riferimento indipendente;
- la convergenza di Q1 e P1 verso Airy è verificata numericamente per due sorgenti lisce;
- la mappa di lift Q6 conserva la cinematica e l'energia discreta scelta.

**Non dimostrato**
- i livelli \(n=8,16,32\) sono raffinamenti delle famiglie FEM Q1/P1, non grafi Q6 più grandi;
- non è stata dimostrata una convergenza Mosco o \(\Gamma\) dal grafo Q6 o dal PRISM completo;
- non è stato eseguito il limite singolare del core \(\varepsilon\to0\) con rinormalizzazione;
- non è stata riprodotta l'implementazione C0-IPDG del preprint 2026;
- non è ancora costruita la mappa Q6/PRISM verso la mesh traction-free;
- non esistono qui dati sperimentali o calibrazione di campioni AM.

Il confronto periodico è quindi una validazione numerica di consistenza per sorgenti lisce, non una dimostrazione della teoria dei difetti singolari.

## 7. Collegamento con il riferimento Morandotti

Il riferimento teorico del 2024 studia dislocazioni di bordo e dipoli di disclinazione nel quadro dell'elasticità incompatibile e della funzione di Airy; il risultato principale è l'equivalenza energetica asintotica nel limite singolare regolarizzato. Il presente benchmark non prova quel risultato: prepara una base discreta riproducibile per costruire il test successivo su sorgenti singolari e rinormalizzazione.

Riferimenti:
- P. Cesana, L. De Luca, M. Morandotti, *Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method*, SIAM J. Math. Anal. 56 (2024), 79–136, DOI [10.1137/22M1523443](https://doi.org/10.1137/22M1523443).
- P. Cesana, E. Fabbrini, A. A. León Baldelli, M. Morandotti, *Semidiscrete Modeling of Dislocation-Disclination Systems: Finite Element Formulation*, preprint 2026, [arXiv:2609.29614](https://arxiv.org/abs/2609.29614).

