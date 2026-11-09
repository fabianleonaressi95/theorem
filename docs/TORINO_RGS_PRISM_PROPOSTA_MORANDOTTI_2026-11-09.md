

### Audit matematico del postprocessing Airy pubblicato (9 novembre 2026)

L'ispezione diretta del codice pubblico del gruppo ha chiarito una differenza apparente: i problemi locali sono assemblati con il prodotto Hessiano \(\int D^2u:D^2v\), mentre la matrice di interazione nel postprocessing usa \(\int\Delta u\Delta v\). Per i campi di cella in due dimensioni, le due forme coincidono nel continuo quando su ogni componente del bordo il dato di Dirichlet e la derivata normale sono quelli della stessa funzione affine. Infatti
\[
\Delta u\Delta v-D^2u:D^2v
=\operatorname{div}((\operatorname{cof}D^2u)\nabla v),
\]
e la condizione affine implica \(D^2u\,t=0\), quindi il flusso di bordo \((\operatorname{cof}D^2u)n\) è nullo. La differenza di codice è pertanto matematicamente compatibile con l'identità di Green, non un bug dimostrato.

Il documento tecnico in PR specifica i controlli discreti ancora necessari: differenza relativa Frobenius fra le due matrici, simmetria, spettro/condizionamento e residuo dell'identità al bordo al variare della mesh. Questo chiarimento è un audit analitico del codice sorgente; non va confuso con una riproduzione numerica già eseguita del solver DOLFINx C0-IPDG.
