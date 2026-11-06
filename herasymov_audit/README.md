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
