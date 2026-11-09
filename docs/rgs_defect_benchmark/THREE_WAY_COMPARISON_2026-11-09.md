# Confronto quantitativo Q1–cochain P1–Airy — 9 novembre 2026

**CI:** [GitHub Actions run 42656544200](https://github.com/fabianleonaressi95/theorem/actions/runs/42656544200) — success  
**Artifact riproducibile:** [rgs-cochain-defect-report](https://github.com/fabianleonaressi95/theorem/actions/runs/42656544200/artifacts/13691882405)  
**Ambito:** elasticità lineare isotropa 2D, sorgenti regolarizzate; confronto numerico, non teorema di convergenza.

## 1. Configurazione del confronto

Sono stati eseguiti tre riferimenti distinti:

1. **Q1 FEM quadrilatero:** elemento bilineare, quadratura di Gauss 2×2.
2. **Cochain P1:** differenze di spostamento su spigoli orientati, ricostruzione del gradiente su triangoli, entrambe le diagonali della cella quadrata.
3. **Airy finite-difference:** soluzione del problema biharmonico di incompatibilità, con stress ricostruito dal potenziale di Airy.

Il dominio è il quadrato unitario, il materiale è isotropo con \(\lambda=\mu=1\), e i problemi di spostamento usano condizioni naturali di trazione nulla con rimozione dei tre modi rigidi. Per Airy si impongono dati clamped equivalenti, modulo gauge affine, alla condizione di trazione nulla sui lati rettilinei.

Le sorgenti sono campionate da profili regolarizzati comuni: inclusione shear, dipolo shear, taglio di Volterra, disclinazione a cuneo e dipolo di disclinazione. Per il riferimento Airy il punto di taglio è posto a \(x_0=1/2+h/2\), cioè tra i nodi e in corrispondenza del primo centro di cella attivo a destra di \(1/2\). Questo elimina lo slittamento di mezzo passo presente nella versione precedente. Restano differenze di quadratura/interpolazione tra campionamento nodale Airy e campionamento cell-centred FEM/cochain.

Sono stati prodotti:
- 56 confronti Q1/cochain: 7 casi × 4 griglie \(n=9,17,33,65\) × 2 orientazioni;
- 20 confronti Airy/Q1/cochain: tre difetti a \(n=17,33,65\), più il dipolo a \(n=129\), entrambe le orientazioni;
- audit separato del limite dipolo–dislocazione su \(n=129\).

## 2. Q1 contro cochain P1: energia

Differenza relativa:
\[
\delta_E=\frac{|E_{\rm Q1}-E_{\rm cochain}|}
{\max(|E_{\rm Q1}|,|E_{\rm cochain}|)}.
\]

| Caso | n=9 | n=17 | n=33 | n=65 |
|---|---:|---:|---:|---:|
| Inclusione shear singola | 12,76% | 4,33% | 1,20% | 0,309% |
| Dipolo shear regolarizzato | 15,43% | 5,43% | 1,53% | 0,395% |
| Dislocazione di bordo (Volterra regolarizzata) | 20,12% | 13,31% | 7,20% | 2,41% |
| Disclinazione a cuneo | 39,37% | 31,06% | 16,80% | 5,35% |
| Dipolo di disclinazione | 58,87% | 60,64% | 51,37% | 31,23% |

I test di patch affine e sorgente nulla passano: la differenza energetica affine è dell'ordine \(10^{-14}\), mentre l'energia del caso nullo è zero. Le due orientazioni della diagonale danno gli stessi valori energetici nei casi riportati.

**Lettura:** per inclusione, dipolo shear, Volterra e disclinazione singola la differenza Q1/cochain decresce con il raffinamento. Il dipolo di disclinazione converge più lentamente: la differenza resta 31,23% a \(n=65\) e scende a 12,12% nel confronto a \(n=129\). Non è corretto dichiarare equivalenza energetica già raggiunta a griglia finita.

## 3. Confronto con Airy: campi ed energia

Le seguenti percentuali sono calcolate sul campo interno, escludendo un margine di tre celle vicino al bordo. Per l'energia Airy si integra la densità elastica ricostruita da stress e deformazione elastica mediati sulle celle. È quindi un indicatore coerente di confronto, ma non una quadratura identica a quella Q1 o P1.

### Dislocazione di bordo

| n | Q1–Airy energia | cochain–Airy energia | errore stress Q1 | errore stress cochain | errore strain Q1 | errore strain cochain |
|---|---:|---:|---:|---:|---:|---:|
| 17 | 11,70% | 23,46% | 34,51% | 37,43% | 50,39% | 61,26% |
| 33 | 23,52% | 29,03% | 28,27% | 29,14% | 37,58% | 44,36% |
| 65 | 8,30% | 10,51% | 14,44% | 14,68% | 16,96% | 19,20% |

### Disclinazione a cuneo

| n | Q1–Airy energia | cochain–Airy energia | errore stress Q1 | errore stress cochain | errore strain Q1 | errore strain cochain |
|---|---:|---:|---:|---:|---:|---:|
| 17 | 0,42% | 31,35% | 26,17% | 29,81% | 24,26% | 29,51% |
| 33 | 11,73% | 26,56% | 11,84% | 13,63% | 10,68% | 12,45% |
| 65 | 2,85% | 8,05% | 6,28% | 6,62% | 5,90% | 6,23% |

### Dipolo di disclinazione

| n | Q1–Airy energia | cochain–Airy energia | errore stress Q1 | errore stress cochain | errore strain Q1 | errore strain cochain |
|---|---:|---:|---:|---:|---:|---:|
| 17 | 79,67% | 92,00% | 40,87% | 65,93% | 40,19% | 69,83% |
| 33 | 57,43% | 79,30% | 20,33% | 28,25% | 21,00% | 28,70% |
| 65 | 24,24% | 47,90% | 10,74% | 12,37% | 10,94% | 12,49% |
| 129 | 7,28% | 18,52% | 5,67% | 5,97% | 5,70% | 5,97% |

**Lettura:** i campi stress/strain si avvicinano al riferimento Airy con il raffinamento. Il dipolo richiede la griglia più fine: a \(n=129\) gli errori di campo sono circa 5,7–6,0%, ma il divario energetico cochain–Airy è ancora 18,52%. Il confronto energetico e quello dei campi non sono intercambiabili.

## 4. Dipolo di disclinazione → dislocazione di bordo

L'audit usa \(n=129\), \(h=1/128\), \(b=0.002\), core gaussiano \(\sigma=0.025\), con cariche di Frank opposte \(\pm b/d\). Le separazioni sono commensurabili con la griglia: \(d=16h,8h,4h,2h\).

| d | d/h | errore relativo incompatibilità | errore relativo stress Airy |
|---:|---:|---:|---:|
| 0,125 | 16 | 85,28% | 32,39% |
| 0,0625 | 8 | 36,87% | 10,75% |
| 0,03125 | 4 | 8,90% | 2,38% |
| 0,015625 | 2 | \(4,96\times10^{-14}\) | \(4,29\times10^{-11}\) |

Il residuo debole Airy resta dell'ordine \(10^{-11}\).

Il valore quasi nullo a \(d=2h\) è una **identità discreta legata allo stencil centrato**: la differenza di due profili gaussiani traslati di \(\pm h\), divisa per \(2h\), coincide con la differenza centrale della gaussiana usata per il taglio di Volterra. È un controllo algebrico molto forte della compatibilità tra le sorgenti discretizzate, ma non dimostra da solo il limite continuo né l'espansione energetica singolare del teorema di Cesana–De Luca–Morandotti.

## 5. Q6: audit cinematico separato

Il report Q6 conferma:
- complesso Q6: 64 vertici, 192 spigoli, 240 quadrati;
- sottocomplesso prodotto \(C_4^3\): 192 quadrati; 48 quadrati intra-coppia mantenuti distinti;
- quoziente materiale \(C_4\times C_4\): 16 vertici, 32 spigoli, 16 facce e fibra interna di cardinalità 4;
- residui massimi esattamente nulli per \(D_1D_0\), mappe di catena e pullback cinematico.

Questa verifica è combinatoria/cinematica. Non è ancora il morfismo tra il complesso Q6 e la mesh fisica FEM/Airy.

## 6. Cosa possiamo concludere

**Verificato numericamente nel benchmark**
- patch test affine e caso sorgente nulla;
- residui dei solutori;
- convergenza energetica Q1/cochain per quattro famiglie di sorgenti;
- miglioramento degli errori stress/strain rispetto al riferimento Airy con il raffinamento;
- equivalenza discreta dipolo–edge al valore grid-aligned \(d=2h\);
- identità esatte della mappa cinematica Q6.

**Non ancora dimostrato**
- equivalenza energetica Q1/cochain/Airy nel limite \(h\to0\);
- limite singolare del core \(\varepsilon\to0\) con rinormalizzazione;
- convergenza Mosco o \(\Gamma\)-convergenza;
- riproduzione del metodo CIP-DG pubblicato: Airy qui è un riferimento finite-difference indipendente;
- mappa di catena Q6/PRISM verso la mesh fisica traction-free;
- calibrazione o validazione su campioni reali, inclusi materiali AM.

## 7. Prossimi passi tecnici

1. Separare lo studio \(h\to0\) da quello \(\varepsilon\to0\), usando griglie che risolvano progressivamente il core.
2. Allineare in modo conservativo le sorgenti cell-centred e nodali e misurare l'errore di proiezione prima di attribuirlo al solutore.
3. Aggiungere una comparazione indipendente con il CIP-DG del preprint 2026, non solo con Airy finite-difference.
4. Costruire il morfismo Q6→mesh triangolata/quadrilatera e verificare il pullback dell'energia, non soltanto della cinematica.
5. Solo dopo, introdurre variabili interne/dissipazione e procedere a cicli isteretici o dati sperimentali.

**Riferimento teorico:** Cesana, De Luca, Morandotti, *Semi-discrete modeling of systems of wedge disclinations and edge dislocations via the Airy stress function method*, SIAM J. Math. Anal. 56(1), 79–136 (2024), DOI [10.1137/22M1523443](https://doi.org/10.1137/22M1523443). Il paper stabilisce l'equivalenza energetica asintotica nel limite singolare regolarizzato; il presente audit è un benchmark numerico preliminare e non una sua riproduzione completa.
