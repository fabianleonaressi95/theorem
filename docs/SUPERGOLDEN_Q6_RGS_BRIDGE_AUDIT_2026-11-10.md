# Q6–RGS–PSU: audit del ponte verso la superaurea

**Data:** 10 novembre 2026  
**Stato:** identità algebriche esatte e risultati combinatori finiti; il ponte geometrico Q6→superaurea resta aperto.

## 1. Obiettivo

L'obiettivo non è inserire \\(\\psi\\) nel modello per definizione. È derivare un operatore di raffinamento a tre canali dalla struttura Q6/RGS/PSU e dimostrare che il suo polinomio caratteristico è
\\[
p(\\lambda)=\\lambda^3-\\lambda^2-1.
\\]
La radice reale dominante è
\\[
\\psi=1.465571231876768\\ldots,\\qquad \\psi^3=\\psi^2+1.
\\]

La derivazione richiede una mappa geometrica/intertwiner. La sola presenza di tre stati, tre direzioni o tre assi quaternionici non è sufficiente.

## 2. Quello che è già esatto

### 2.1 Trasferimento supergolden a tre stati

La matrice
\\[
A_\\psi=\\begin{pmatrix}1&0&1\\\\1&0&0\\\\0&1&0\\end{pmatrix}
\\]
ha polinomio caratteristico \\(\\lambda^3-\\lambda^2-1\\). La ricorrenza associata è
\\[
S_0=0,\\quad S_1=0,\\quad S_2=1,\\qquad
S_{n+3}=S_{n+2}+S_n.
\\]
Quindi \\(S_{n+1}/S_n\\to\\psi\\), per la dominanza della radice reale positiva.

La matrice trigrammatica già registrata,
\\[
M_T=\\begin{pmatrix}0&0&1\\\\1&0&0\\\\0&1&1\\end{pmatrix},
\\]
è esattamente coniugata ad \\(A_\\psi\\) tramite la permutazione ciclica \\(P\\):
\\[
M_T=P A_\\psi P^{-1}.
\\]
Questo risolve una differenza di ordinamento degli stati; non identifica ancora gli stati con celle geometriche Q6.

### 2.2 Raffinamento cubicale Q6 effettivamente costruito

Il teorema T055 costruisce la suddivisione ai punti medi del 2-scheletro cubicale Q6:
- celle grossolane: \\(64,192,240\\);
- celle raffinate: \\(496,1344,960\\);
- figli per cella genitore: \\(1,2,4\\) nei gradi 0,1,2;
- mappe cellulari \\(S_k\\) che rispettano esattamente il bordo:
  \\(B'_1S_1=S_0B_1\\), \\(B'_2S_2=S_1B_2\\).

Il trasferimento sulle sei direzioni coordinate è \\(D=2I_6\\). La restrizione a tre assi coordinati è dunque \\(2I_3\\), non \\(A_\\psi\\). I due operatori non hanno lo stesso polinomio caratteristico e non sono simili.

Questo è un risultato importante: la suddivisione cubicale standard è una costruzione corretta, ma **non genera da sola la superaurea**.

### 2.3 Antipodalità Q6

La mappa \\(c(x)=x\\oplus63\\) è un'involuzione senza punti fissi e produce 32 coppie antipodali. Poiché \\(6-k\\equiv k\\pmod2\\), conserva la parità di Hamming. Pertanto le 32/32 classi della bipartizione pari/dispari non coincidono con i due fogli antipodali.

Per collegare Anti-Twin alla superaurea bisogna definire l'azione sui tre canali e dimostrare che il trasferimento commuta con tale azione, oppure specificare una simmetria che la scambia.

## 3. Cosa non è ancora certificato

Il rapporto di recupero Krist-All nel repository segnala che l'archivio recuperato non contiene:
- relazione di equivalenza delle classi;
- codifica canonica dei rappresentanti;
- enumeratore deterministico e tabella completa;
- definizioni/matrici originali di \\(K\\) e \\(W_0\\).

Di conseguenza il conteggio 11.725, il residuo \\(W_0\\) e l'identità \\(K^3=K^2+I\\) restano risultati storici non certificati dal materiale recuperato. Non li uso come premessa della derivazione.

## 4. Il ponte matematico da costruire

Serve un complesso raffinato \\(C^\\bullet_{Q6}\\) e uno spazio ridotto tridimensionale \\(V_3\\), con:
- una mappa di compressione \\(J:C^k_{Q6}\\to V_3\\), o un sottospazio invariante esplicitamente definito;
- un operatore geometrico di trasferimento \\(R_{Q6}\\), ricavato dalle mappe genitore-figlio, dalle incidenze o da una struttura RGS/Krist-All recuperata;
- una relazione di intertwining
  \\[
  J R_{Q6}=A_\\psi J
  \\]
  (oppure \\(M_T\\) secondo la convenzione di ordinamento);
- verifica di rango, nucleo, indipendenza dalla base e compatibilità con l'azione antipodale;
- un'azione quaternionica sui canali, se si vuole identificare il tripletto con gli assi locali: la mappa deve essere equivarante, non solo dimensionale.

Una via alternativa è costruire una ricorrenza di conteggio/raffinamento \\(v_{n+3}=v_{n+2}+v_n\\) da una regola geometrica di sostituzione. In quel caso bisogna mostrare esplicitamente quali oggetti sono contati e perché la regola locale produce quei numeri.

## 5. Test falsificabili e criterio di successo

Il nuovo audit riproducibile controlla:
1. identità della ricorrenza e convergenza dei rapporti;
2. coniugazione esatta Phase-21/trigramma;
3. dati esatti del trasferimento Q6 T055;
4. involuzione antipodale e conservazione della parità;
5. ostacolo spettrale tra \\(2I_3\\) e \\(A_\\psi\\).

La derivazione sarà promossa da **aperta** a **dimostrata** soltanto quando verrà prodotto un \\(J\\) e un \\(R_{Q6}\\) geometricamente definiti che soddisfino l'intertwining. Una regressione numerica del polinomio caratteristico non basta se la matrice è stata inserita a mano.

## 6. Stato epistemico

| Affermazione | Stato |
|---|---|
| \\(\\psi^3=\\psi^2+1\\) e ricorrenza supergolden | **Prova algebrica** |
| Coniugazione Phase-21/trigramma | **Identità matriciale esatta** |
| Raffinamento midpoint Q6 e chain map T055 | **Teorema combinatorio finito** |
| Trasferimento direzionale midpoint \\(2I_6\\) | **Identità esatta** |
| 32 coppie antipodali; antipode conserva la parità | **Identità combinatoria** |
| Mappa geometrica Q6→operatore supergolden | **Aperta** |
| Identificazione del tripletto con gli assi quaternionici | **Aperta** |
| 11.725 classi Krist-All e \\(K^3=K^2+I\\) dal pacchetto recuperato | **Non certificata** |
| Interpretazione fisica di \\(\\psi\\) come costante universale | **Non dimostrata** |

## 7. Esecuzione

Eseguire:

```bash
python scripts/audit_supergolden_q6_bridge.py
python -m unittest tests/test_supergolden_q6_bridge.py
```

Il JSON risultante è un audit di algebra e combinatoria finita. Non certifica il ponte geometrico ancora mancante.
