# Mappa cinematica esatta Q6 → cella materiale 2D → PRISM

**Stato:** identità combinatorie e di cochain finite-dimensionali; interpretazione come modello materiale ancora candidata.  
**Ambito:** estensione del benchmark difetti della PR #119, senza sostituire il confronto Q1/cochain/Airy già presente.

## 1. Convenzioni Q6

Si rappresentano i 64 stati come parole binarie (b=(b_0,ldots,b_5)), con (b_0) bit più significativo. Il codice intero dei tre blocchi è

[
q_x=2b_0+b_1,qquad q_y=2b_2+b_3,qquad q_z=2b_4+b_5.
]

Per dare una realizzazione geometrica del ciclo a quattro stati, si usa l'embedding Gray

[
00mapsto0,quad 01mapsto1,quad 11mapsto2,quad 10mapsto3.
]

Ogni flip di un bit è allora un passo orientato lungo uno dei tre cicli (C_4). A livello di grafo,

[
Q_6 cong C_4^{(x)}square C_4^{(y)}square C_4^{(z)},
]

con 64 vertici e 192 spigoli. Questa è un'identificazione combinatoria esatta, non un'ipotesi fisica.

## 2. Proiezione sulla cella materiale e fibra interna

Si scelgono i primi due cicli come coordinate spaziali e il terzo come fibra interna:

[
pi:C_4^3longrightarrow C_4^2,qquad (x,y,z)longmapsto(x,y).
]

La cella materiale quoziente è il toro discreto periodico (C_4	imes C_4): 16 vertici, 32 spigoli orientati e 16 facce quadrate. Ogni vertice della cella ha esattamente quattro preimmagini, una per ciascun valore della coordinata (z).

Una deformazione discreta sul quoziente è una 0-cochain vettoriale
(u:V(C_4^2)	omathbb R^2). La sua estensione a Q6 è il pullback

[
widetilde u=ucircpi.
]

Le differenze sugli spigoli sono (d_0u). Gli spigoli della fibra (z) hanno differenza nulla; gli spigoli spaziali riproducono esattamente le differenze della cella quoziente, con il segno determinato dall'orientazione.

## 3. Identità di catena verificata

Il codice costruisce matrici intere di incidenza (D_0^{Q6}), (D_1^{Q6}), (D_0^{m mat}), (D_1^{m mat}), e le mappe intere (P_0,P_1,P_2). Per il sottocomplesso prodotto (C_4^3) verifica esattamente

[
D_0^{Q6}P_0=P_1D_0^{m mat},qquad
D_1^{Q6,m prod}P_1=P_2D_1^{m mat},
]

oltre alle identità (D_1D_0=0) su entrambi i complessi. Non si usa un rango floating-point per queste identità: sono moltiplicazioni di matrici a coefficienti interi.

### Distinzione importante: 240 quadrati Q6

Il grafo Q6 come 1-scheletro dell'ipercubo a sei dimensioni possiede

[
inom 62,2^4=240
]

facce quadrate. La struttura prodotto (C_4^3) usa 192 quadrati che coinvolgono bit appartenenti a due coppie diverse (12 coppie di direzioni, 16 facce per coppia). I restanti 48 quadrati sono i tre gruppi di facce generate dai due bit della stessa coppia (16 per gruppo). Questi 48 non vengono identificati con facce della cella materiale: riempirebbero i cicli (C_4) e cambierebbero la topologia del quoziente. Il codice conserva entrambi i conteggi e verifica separatamente (D_1D_0=0) per la matrice completa da 240 facce e per il sottocomplesso prodotto da 192 facce.

Questa distinzione evita di identificare senza prova la struttura delle 240 plaquette dell'audit Q6 con le 192 facce del complesso cubico prodotto usato per il quoziente materiale.

## 4. Cinematica ed energia sul quoziente

Su ogni quadrilatero periodico si interpola lo spostamento con funzioni bilineari Q1. L'energia elastica viene integrata in tutti e quattro i punti di Gauss della quadratura 2×2, invece di essere valutata soltanto sul gradiente medio al centro della cella. La distinzione è essenziale sul toro pari 4×4: la media delle differenze sui lati opposti annulla i modi checkerboard/Nyquist e introdurrebbe deformazioni spurie a energia zero. Il gradiente al centro resta disponibile come diagnostica, ma non viene usato per calcolare l'energia.

Si pone

[
\varepsilon=\tfrac12(F+F^T),\qquad
W(\varepsilon)=\tfrac{\lambda}{2}(\operatorname{tr}\varepsilon)^2+
\mu\,\varepsilon:\varepsilon,
]

e si sommano i quattro contributi di Gauss (con Jacobiano 1/4 della cella unitaria) sulle 16 celle. È una discretizzazione periodica Q1 di riferimento, con \(\lambda\ge0\), \(\mu>0\); non è ancora l'energia FEM a trazione libera della PR #119.

## 5. Cosa è dimostrato e cosa resta da fare

**Verificabile esattamente nel codice**
- bijezione tra i 64 stati e (C_4^3);
- conteggi 64/192/240 e separazione 192+48;
- identità di bordo del bordo;
- mappe di catena (P_0,P_1,P_2);
- identità di pullback (D_0^{Q6}widetilde u=P_1D_0^{m mat}u);
- annullamento delle differenze sugli spigoli della fibra.

**Ancora da validare**
- confronto quantitativo della cella periodica con FEM/Airy a condizioni al contorno periodiche allineate;
- convergenza al raffinamento della cella, non deducibile dalla singola taglia 4×4;
- identificazione del quoziente con una sottostruttura fisica del grafo PRISM completo (C_{64}square C_6^3square C_5);
- inserimento di variabili interne e dissipazione per dislocazioni mobili e isteresi;
- dati sperimentali di provini AM (CT/microstruttura, orientazione di stampa, porosità, curve meccaniche e protocollo termico).

Non si rivendicano una dimostrazione di Mosco/(Gamma)-convergenza, una previsione di proprietà di materiale o una superiorità rispetto a FEM.

## 6. Riproduzione

```bash
python scripts/q6_prism_kinematic_map.py
python -m unittest discover -s tests -p 'test_q6_prism_kinematic_map.py' -v
```

Il workflow della PR #119 esegue entrambi i comandi e conserva il JSON dell'audit come artifact.
