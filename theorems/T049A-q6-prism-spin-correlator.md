# T049A — Correlatore microscopico di spin su Q6 e PRISM

## Stato
Audit numerico riproducibile su configurazioni microscopiche fornite. Non è una teoria dinamica dello spin e non dimostra correlazioni RGS–PSU non standard.

## Geometrie
Q6 è il cubo (Q_6=C_2^{\square 6}), con 64 vertici e 192 archi; gli shell counts per vertice sono (1,6,15,20,15,6,1). PRISM è (C_{64}\square C_6\square C_6\square C_6\square C_5), con 69120 vertici e grado 10. Si usa la distanza prodotto, somma delle distanze cicliche minime.

## Invariante
Per spin assiale vettoriale \(\mathbf s_x\) e volume fisico di coarse-graining \(V\):
\[
\bar{\mathbf J}=V^{-1}\sum_x\mathbf s_x,\quad
S_{ij}=\epsilon_{ijk}\bar J_k,\quad
s^2=\tfrac12 S_{ij}S_{ij}=|\bar{\mathbf J}|^2.
\]
La decomposizione è
\[
s^2_{\rm self}=V^{-2}\sum_x|\mathbf s_x|^2,\qquad
s^2_{\rm pair}=2V^{-2}\sum_{x<y}\mathbf s_x\cdot\mathbf s_y.
\]
Il termine pair può essere negativo. Si riporta il correlatore grezzo e connesso per shell, con conteggio delle coppie dirette.

## Dati e riproducibilità
NPZ richiesto: a_values (T,), spin_vectors (T,N,3) o (T,R,N,3) con R repliche opzionali, volumes (T,); particle_counts (T,) o (T,R) opzionale. Un vettore nullo può rappresentare un sito vuoto. Se i conteggi non sono forniti si assume un portatore per sito. Per studiare diluizione cosmologica in una cella fisica fissata, usare volume fisico coerente e conteggi/occupazioni che variano con a; non confondere volume comovente e fisico.

Comandi:
```bash
python -m pytest tests/test_q6_prism_spin_correlator.py -q
python scripts/q6_prism_spin_correlator.py --input spin.npz --geometry q6 --max-distance 6 --output q6.json
python scripts/q6_prism_spin_correlator.py --input spin_prism.npz --geometry prism --max-distance 3 --output prism.json
```

Il codice stima q=-d log(s²)/d log(a) separatamente per totale, self, pair e densità, e g_pair=s²_pair/n². I fit sono diagnostici e usano solo valori positivi.

## Limiti fisici
Il grafo determina topologia e shell metrici, non Hamiltoniana, misura d'equilibrio o legge di spin. Il contributo self classico non coincide automaticamente con il contatto locale assiale-assiale quantistico EC: occorrono ordinamento e rinormalizzazione dichiarati. Se lo spin è associato a spigoli/facce, occorre una formulazione in cochain orientate e trasporto gauge. Il repository non contiene ancora i vettori microscopici con normalizzazione, volume e prescrizione del contatto; nessun esponente RGS–PSU fisico viene pertanto dichiarato.
