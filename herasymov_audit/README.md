# Herasymov / fractogenesis — audit

Questa cartella contiene un audit matematico indipendente dei sorgenti 2D e 3D di [xcontcom/fractogenesis](https://github.com/xcontcom/fractogenesis), con particolare attenzione a:

- indicizzazione delle regole totalistiche;
- equivarianza sotto il gruppo cubico;
- padding e raffinamento;
- limiti del collegamento a quaternioni, qutrit, supergolden e RGS.

## File

- [REPORT.md](REPORT.md): ricostruzione matematica, dimostrazioni e classificazione dei risultati.
- [audit_symmetry.py](audit_symmetry.py): test riproducibile con NumPy delle 24 rotazioni cubiche proprie e del padding 3D.

## Esecuzione

```bash
python -m pip install numpy
python audit_symmetry.py
```

Lo script usa un seed fisso e stampa un riepilogo JSON. I test sono su tori periodici piccoli; la dimostrazione generale è nel rapporto.

## Nota di rigore

Il codice sorgente esaminato non implementa direttamente quaternioni, SU(2), qutrit o la ricorrenza supergolden. Questi collegamenti sono trattati come problemi di costruzione matematica successiva, non come proprietà già dimostrate del repository upstream.


## Audit Koopman

È disponibile [audit_koopman.py](audit_koopman.py), un esperimento diagnostico di chiusura lineare su tre primi momenti di Fourier. Non assume l'esistenza di una matrice supergolden: misura il residuo della migliore regressione lineare e chiarisce che non equivale a una restrizione esatta dell'operatore di Koopman.

Esecuzione:

```bash
python audit_koopman.py
```


## Test T2u e molteplicità

[\`audit_t2u_multiplicity.py\`](audit_t2u_multiplicity.py) costruisce dieci triplette covarianti T2u dagli armonici cubici e testa la chiusura del loro spazio di 30 osservabili. Il test è una regressione proiettata finito-campione, non un intertwiner numerico già costruito verso il tangente RGS 188D.

Esecuzione:

```bash
python audit_t2u_multiplicity.py --samples 500
```


## Intertwiner verso RGS 188D

- [`audit_rgs_t2u_intertwiner.py`](audit_rgs_t2u_intertwiner.py): solver Reynolds per (J\in\mathbb R^{188\times30}), richiede le 48 azioni tangenti RGS verificate.
- [`selftest_t2u_intertwiner.py`](selftest_t2u_intertwiner.py): unit test sintetico del solver; non usa dati RGS.

Il contratto NPZ del solver e la distinzione tra tripletto (188\times3) e componente isotypic di rango 30 sono documentati nel report. Il calcolo sul tangente RGS reale resta in attesa delle matrici (U_{tan}(g)) nella stessa base (Q_{tangent}).
