# T049D — Selezione lorentziana della fibra QLG: decomposizione di Weyl e parità

## Convenzioni e rappresentazione

Si adottano \(\eta=\operatorname{diag}(-,+,+,+)\) e le matrici \(\gamma^\mu\) definite in \`rgs-qlg-quaternion-bridge/src/clifford_qlg.py\). In questa base:
\[
\gamma^0=i\begin{pmatrix}I&0\\0&-I\end{pmatrix},\qquad
\gamma^i=i\begin{pmatrix}0&\sigma_i\\-\sigma_i&0\end{pmatrix}.
\]
La restrizione alle rotazioni spaziali è \(U\oplus U\), ma i blocchi coordinati superiore/inferiore non sono sottorappresentazioni del gruppo di Lorentz.

Il prodotto definito dalla convenzione sorgente è
\[
\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3
=\begin{pmatrix}0&I\\I&0\end{pmatrix}.
\]
I proiettori chirali sono \(P_s=(I_4+s\gamma^5)/2\), \(s=\pm1\).

## Teorema: embedding Weyl lorentz-equivarianti

Per ogni \(s=\pm1\), definiamo
\[
K_s:\mathbb C^2\longrightarrow\mathbb C^4,\qquad
K_s\chi=\frac1{\sqrt2}\begin{pmatrix}\chi\\s\chi\end{pmatrix}.
\]
Allora \(K_s^\dagger K_s=I_2\), \(K_sK_s^\dagger=P_s\), e l'immagine di \(K_s\) è invariata sotto la rappresentazione spinoriale di \(\mathrm{Spin}^+(1,3)\). L'azione indotta sulle fibre a due componenti è la rappresentazione di Weyl: i generatori di rotazione sono \(J_i=\sigma_i/2\), mentre, nella convenzione adottata per i boost, \(K_i^{(s)}=-is\sigma_i/2\).

### Verifica

I generatori di rotazione sulla rappresentazione a quattro componenti sono
\[
\mathcal J_i=\frac12\begin{pmatrix}\sigma_i&0\\0&\sigma_i\end{pmatrix}.
\]
I generatori di boost nella base scelta sono
\[
\mathcal K_i=\frac{i}{2}\gamma^0\gamma^i
=-\frac{i}{2}\begin{pmatrix}0&\sigma_i\\\sigma_i&0\end{pmatrix}.
\]
Perciò
\[
\mathcal J_iK_s=K_s\frac{\sigma_i}{2},\qquad
\mathcal K_iK_s=K_s\left(-is\frac{\sigma_i}{2}\right).
\]
Con queste definizioni i generatori soddisfano \([J_i,J_j]=i\epsilon_{ijk}J_k\), \([J_i,K_j]=i\epsilon_{ijk}K_k\), \([K_i,K_j]=-i\epsilon_{ijk}J_k\). Le immagini di \(K_+\) e \(K_-\) sono dunque invarianti per tutti i generatori di Lorentz e, per esponenziazione, per la componente connessa del gruppo di Lorentz. Sono precisamente i due autospazi di \(\gamma^5\).

La decomposizione è irriducibile: le due rappresentazioni di Weyl hanno etichette non equivalenti \((1/2,0)\) e \((0,1/2)\). Pertanto un intertwiner non nullo da una fibra QLG irriducibile di dimensione complessa 2, una volta specificata quale rappresentazione di boost essa porta, può avere immagine in un solo settore chirale. Non è una selezione di \(s\): entrambe le estensioni Weyl sono matematicamente possibili.

## Parità

La matrice \(\gamma^0\), a fase globale irrilevante, realizza la trasformazione di parità e soddisfa
\[
\gamma^0\gamma^5\gamma^0{}^{-1}=-\gamma^5.
\]
Quindi scambia i due settori:
\[
\gamma^0\,\operatorname{im}K_s=\operatorname{im}K_{-s}.
\]
Una singola fibra Weyl non è chiusa sotto parità. Se il modello QLG richiede parità esatta, deve contenere entrambe le chiralità (o una fibra interna che le scambi); se ammette una fase chirale, una singola fibra è possibile, ma la scelta del segno richiede un orientamento o un dato dinamico aggiuntivo.

## Correzione concettuale a T049C

Gli embedding \( (I_2,0)^T\) e \((0,I_2)^T\) classificati in T049C sono equivarianti sotto rotazioni spaziali, ma non sono invarianti sotto i boost. Gli embedding lorentz-invarianti sono invece \(K_+\) e \(K_-\), combinazioni diagonali dei due blocchi coordinati. T049C rimane corretto come classificazione sotto \(SU(2)\); T049D aggiunge il vincolo lorentziano che restringe le possibilità alla scelta di una delle due chiralità, quando la rappresentazione dei boost sulla fibra sorgente è fissata.

## Conseguenza dinamica: cosa è e non è selezionato

Il gruppo di Lorentz restringe l'embedding a \(K_+\) oppure \(K_-\), ma non sceglie tra i due. La parità scambia i segni e dunque non può selezionarne uno mantenendo una singola fibra. Una dinamica che selezioni una chiralità deve introdurre un termine che distingua i due settori, per esempio un accoppiamento pseudoscalare/orientato o una condizione al bordo; la sua forma e la sua origine devono essere derivate dal modello QLG, non postulate.

Per una fibra QLG che inizialmente porta soltanto \(SU(2)\), l'estensione di Weyl equivale ad assegnare i generatori di boost \(K_i^{(s)}=-is\sigma_i/2\). Questa assegnazione è una possibile estensione coerente, non una conseguenza della sola rappresentazione \(2I\). Il test numerico verifica le identità matriciali; la classificazione delle due rappresentazioni Weyl segue dall'algebra di Lorentz e dalla decomposizione chirale.

## Conseguenze per T049B e per \(s^2\)

Una volta scelto e giustificato \(s\), il campo Dirac completo non è ancora disponibile: un singolo settore Weyl fornisce uno spinore a due componenti e il bilineare assiale deve essere ricostruito nella rappresentazione appropriata, con attenzione alla coniugazione e alla normalizzazione Noether. Una teoria parità-invariante richiede entrambe le componenti Weyl e un accoppiamento che specifichi come esse si combinano in un campo Dirac.

Non viene dedotta una legge alternativa a \(s^2\propto a^{-6}\). Rimangono aperti il termine dinamico QLG che sceglie/accoppia le chiralità, la mappa Noether verso \(S_{\mu\nu}\), il trasporto Spin lungo gli archi PRISM e la valutazione su dati fisici.

## Stato epistemico

- **Dimostrato algebricamente:** forma di \(\gamma^5\), proiettori, embedding \(K_\pm\), invariance sotto i generatori di Lorentz, azione della parità.
- **Verificabile numericamente:** residui delle identità di Clifford, rotazioni, boost, proiettori e scambio di parità.
- **Non derivato dal solo QLG esistente:** quale chiralità sia fisicamente realizzata e se la dinamica richieda una o entrambe.
- **Aperto:** derivazione variazionale della selezione chirale, ricostruzione di un campo Dirac parità-invariante, normalizzazione Noether dello spin e conseguente legge cosmologica.

Il motore riproducibile è \`scripts/q6_qlg_dirac_lorentz_chirality.py\`; i test sono in \`tests/test_q6_qlg_dirac_lorentz_chirality.py\`.
