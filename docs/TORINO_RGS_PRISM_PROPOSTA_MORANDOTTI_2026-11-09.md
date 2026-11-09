

### Audit matematico del postprocessing Airy pubblicato (9 novembre 2026)

L'ispezione diretta del codice pubblico del gruppo ha chiarito una differenza apparente: i problemi locali sono assemblati con il prodotto Hessiano \(\int D^2u:D^2v\), mentre la matrice di interazione nel postprocessing usa \(\int\Delta u\Delta v\). Per i campi di cella in due dimensioni, le due forme coincidono nel continuo quando su ogni componente del bordo il dato di Dirichlet e la derivata normale sono quelli della stessa funzione affine. Infatti
\[
\Delta u\Delta v-D^2u:D^2v
=\operatorname{div}((\operatorname{cof}D^2u)\nabla v),
\]
e la condizione affine implica \(D^2u\,t=0\), quindi il flusso di bordo \((\operatorname{cof}D^2u)n\) è nullo. La differenza di codice è pertanto matematicamente compatibile con l'identità di Green, non un bug dimostrato.

Il documento tecnico in PR specifica i controlli discreti ancora necessari: differenza relativa Frobenius fra le due matrici, simmetria, spettro/condizionamento e residuo dell'identità al bordo al variare della mesh. Questo chiarimento è un audit analitico del codice sorgente; non va confuso con una riproduzione numerica già eseguita del solver DOLFINx C0-IPDG.


## 7. Aggiornamento del confronto periodico — 9 novembre 2026

Il confronto è stato esteso oltre Q6/Q1/Airy con un risolutore P1 cochain periodico, due orientazioni della diagonale e matrici d'incidenza sparse. La CI completa [42659067311](https://github.com/fabianleonaressi95/theorem/actions/runs/42659067311) è passata; artifact [JSON/CSV 13693946123](https://github.com/fabianleonaressi95/theorem/actions/runs/42659067311/artifacts/13693946123).

Il report autonomo è disponibile qui:

[Confronto periodico Q6–Q1–P1–Airy](rgs_defect_benchmark/PERIODIC_Q6_Q1_P1_AIRY_2026-11-09.md).

A (n=32), le differenze relative di energia rispetto ad Airy sono:
- inclusione shear: Q1 0,0254%, P1 0,1070%;
- dipolo shear: Q1 0,0947%, P1 0,4195%.

Gli errori di stress e strain P1 scendono sotto l'1% per entrambe le sorgenti. Il complesso triangolato P1 verifica (D_1D_0=0) esattamente a tutti i livelli e il lift Q6 al livello (4\times4) conserva pullback e energia entro precisione macchina.

Il dato non va sovrainterpretato: Q1 è più accurato di P1 in questo benchmark; i raffinamenti (n=8,16,32) sono griglie FEM e non grafi Q6 più grandi. Restano aperti il limite singolare dei core, la riproduzione C0-IPDG e la mappa dal PRISM completo alla mesh fisica.


## 8. Primo confronto con il C0-IPDG P3 del gruppo Morandotti

È stato aggiunto un driver DOLFINx 0.11 per il primo problema di cella su corona circolare, con tre campi (kappa_0,kappa_1,kappa_2), elementi P3, forma C0-IPDG e penalità (alpha=10). La prima esecuzione è riuscita: [GitHub Actions run 42661115929](https://github.com/fabianleonaressi95/theorem/actions/runs/42661115929), report [artifact 13693913162](https://github.com/fabianleonaressi95/theorem/actions/runs/42661115929/artifacts/13693913162).

Su (h=0.22,0.14,0.09), gli errori relativi in seminorma (H^2) scendono:
- (kappa_0): 17,74% → 12,74% → 6,70%;
- (kappa_1): 22,66% → 16,22% → 8,12%;
- (kappa_2): 22,13% → 16,43% → 9,29%.

Le tracce di valore al core sono imposte con residui inferiori a (1,4	imes10^{-16}); i residui della derivata normale diminuiscono con il raffinamento. Le matrici Hessiana e Laplaciana sono simmetriche e positive definite. Tuttavia la loro differenza relativa è 0,114%, 0,131% e 0,158%: non è ancora monotona decrescente. Ho aggiunto (h=0.06) per discriminare comportamento pre-asintotico e problema di formulazione/assemblaggio.

Questo è un primo test P3 C0-IPDG su un singolo core, non la riproduzione completa della procedura multi-core del lavoro pubblicato. La ricostruzione con matrice (mathcal M), più core, configurazioni fuori centro e limite singolare restano obiettivi successivi. Il report metodologico aggiornato è in [MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md](rgs_defect_benchmark/MORANDOTTI_C0_IPDG_REPRODUCTION_PLAN.md).
