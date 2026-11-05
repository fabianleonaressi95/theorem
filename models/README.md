# Modelli matematici e fisici

Qui si registrano i modelli con definizioni, variabili, simmetrie, parametri e limiti. I codici eseguibili restano nei repository implementativi e vengono linkati, non duplicati.

Sezioni previste: Q6 spin glass; Q6 U(1)/Wilson; SU(3)/QCD; PRISM–Krist-All; RGS–PSU tetradi/teleparallelismo; QAT luce topologica; PSU–Anti-Twin.

## Modello torsione–Lambda

- [Chiusura FLRW torsionale dust-like](TORSION_LAMBDA_DUST_CLOSURE.md): modello fenomenologico con \(\rho_T\propto a^{-3}\), conservazione separata \(p_T=0\), chiusura piatta corretta e limite \(\lambda=0\).
- Implementazione di riferimento: [scripts/torsion_lambda_dust_closure.py](../scripts/torsion_lambda_dust_closure.py).
- Test: [tests/test_torsion_lambda_dust_closure.py](../tests/test_torsion_lambda_dust_closure.py).

Il modello non è presentato come derivazione della torsione algebrica Einstein–Cartan: il ponte con una sorgente di spin e la relativa legge di scala resta aperto.
