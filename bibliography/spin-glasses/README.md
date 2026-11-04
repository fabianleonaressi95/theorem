# Vetri di spin — bibliografia e collegamenti Q6

## Fonti identificate

| Autori | Titolo | Anno / sede | Stato |
|---|---|---|---|
| S. F. Edwards, P. W. Anderson | “Theory of spin glasses” | 1975, *J. Phys. F* 5, 965–974; DOI 10.1088/0305-4608/5/5/017 | **VERIFICATA** |
| D. Sherrington, S. Kirkpatrick | “Solvable Model of a Spin-Glass” | 1975, *Phys. Rev. Lett.* 35, 1792–1796; DOI 10.1103/PhysRevLett.35.1792 | **VERIFICATA** |
| D. Sherrington, S. Kirkpatrick | “Infinite-ranged models of spin-glasses” | 1978 | **IDENTIFICATA**; sede/DOI da completare |
| G. Parisi | “Infinite Number of Order Parameters for Spin-Glasses” | 1979, *Phys. Rev. Lett.* 43, 1754–1757; DOI 10.1103/PhysRevLett.43.1754 | **VERIFICATA** |
| J. R. L. de Almeida, D. J. Thouless | instabilità AT / linea de Almeida–Thouless | 1978 | **IDENTIFICATA**; titolo e metadati completi da controllare |
| P. W. Anderson | “The concept of frustration in spin glasses” | 1978 | **IDENTIFICATA**; sede/DOI da completare |
| K. Binder, A. P. Young | “Spin glasses: Experimental facts, theoretical concepts, and open questions” | 1986, *Rev. Mod. Phys.* 58, 801–976; DOI 10.1103/RevModPhys.58.801 | **VERIFICATA** |
| M. Mézard | “Spin glass theory and its new challenge: structured disorder” | 2024, *Indian J. Phys.*; DOI 10.1007/s12648-023-03029-8 | **VERIFICATA** |
| F. Altieri, G. Baity-Jesi | “An Introduction to the Theory of Spin Glasses” | 2023 | **IDENTIFICATA**; sede/DOI da completare |
| D. Sherrington, S. Kirkpatrick | “50 years of spin glass theory” | 2025 | **DA DISAMBIGUARE**; verificare titolo e autori |
| N. Read | “Short-range Ising spin glasses: The metastate interpretation of replica symmetry breaking” | 2014 | **IDENTIFICATA**; sede/DOI da completare |
| Autori da recuperare | “Current research on spin glasses” | 2025 | **DA DISAMBIGUARE**; sembra titolo descrittivo, non necessariamente titolo editoriale |

## Collegamento interno già presente

- Repository: [rgs-qlg-quaternion-bridge](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge)
- PR #96, **merged**: [Add Edwards–Anderson spin glass model on Q6](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/pull/96)
- Branch: `feat/q6-spin-glass-edwards-anderson`
- Commit sorgente: `3969a574061e5a5630e9df95d74dbe048b48b702`
- Merge commit: `39324b9b625e2bc37149961189fb261135ec5a71`
- Documento tecnico: [Q6_EDWARDS_ANDERSON_SPIN_GLASS.md](https://github.com/fabianleonaressi95/rgs-qlg-quaternion-bridge/blob/main/docs/Q6_EDWARDS_ANDERSON_SPIN_GLASS.md)

Il modello implementato usa variabili Ising su 64 vertici e accoppiamenti quenched Gaussiani o bimodali sui 192 lati; studia frustrazione sulle 240 facce, gauge Z2, overlap tra repliche, suscettività spin-glass e cumulante di Binder. È un modello su grafo finito.

## Limiti da mantenere

Non sono dimostrati: limite termodinamico, fase spin-glass, replica-symmetry breaking, equivalenza con vetri di spin tridimensionali, né derivazione dal settore SU(2)/PSU. Le fonti classiche fondano il linguaggio e i test, non convalidano automaticamente queste identificazioni.

## Ordine di lettura / funzione nel progetto

1. Edwards–Anderson: modello a disordine quenched a corto raggio.
2. Sherrington–Kirkpatrick: modello mean-field risolvibile.
3. de Almeida–Thouless e Parisi: instabilità e struttura degli stati/parametri d'ordine.
4. Binder–Young: quadro sperimentale e teorico, limiti delle evidenze.
5. Read: metastate e interpretazione RSB nei modelli a corto raggio.
6. Mézard; Altieri–Baity-Jesi: disordine strutturato e sintesi contemporanea.

La priorità di collegamento Q6 è confrontare EA su grafo, gauge Z2, frustrazione plaquette e struttura del disordine; non assumere che il modello Ising Z2 sia già la teoria di gauge SU(2) del progetto.
