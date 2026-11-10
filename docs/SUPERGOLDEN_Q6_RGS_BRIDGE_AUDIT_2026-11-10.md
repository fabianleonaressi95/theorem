# Q6–RGS–PSU: audit del ponte verso la superaurea

**Data:** 10 novembre 2026  
**Stato:** identità algebriche esatte e risultati combinatori finiti; il ponte geometrico Q6→superaurea resta aperto.

## 1. Obiettivo

L'obiettivo non è inserire \(\psi\) nel modello per definizione. È derivare un operatore di raffinamento a tre canali dalla struttura Q6/RGS/PSU e dimostrare che il suo polinomio caratteristico è
\[
p(\lambda)=\lambda^3-\lambda^2-1.
\]
La radice reale dominante è
\[
\psi=1.465571231876768\ldots,\qquad \psi^3=\psi^2+1.
\]

La derivazione richiede una mappa geometrica/intertwiner. La sola presenza di tre stati, tre direzioni o tre assi quaternionici non è sufficiente.

## 2. Quello che è già esatto

### 2.1 Trasferimento supergolden a tre stati

La matrice
\[
A_\psi=\begin{pmatrix}1&0&1\\1&0&0\\0&1&0\end{pmatrix}
\]
ha polinomio caratteristico \(\lambda^3-\lambda^2-1\). La ricorrenza associata è
\[
S_0=0,\quad S_1=0,\quad S_2=1,\qquad
S_{n+3}=S_{n+2}+S_n.
\]
Quindi \(S_{n+1}/S_n\to\psi\), per la dominanza della radice reale positiva.

La matrice trigrammatica già registrata,
\[
M_T=\begin{pmatrix}0&0&1\\1&0&0\\0&1&1\end{pmatrix},
\]
è esattamente coniugata ad \(A_\psi\) tramite la permutazione ciclica \(P\):
\[
M_T=P A_\psi P^{-1}.
\]
Questo risolve una differenza di ordinamento degli stati; non identifica ancora gli stati con celle geometriche Q6.

### 2.2 Raffinamento cubicale Q6 effettivamente costruito

Il teorema T055 costruisce la suddivisione ai punti medi del 2-scheletro cubicale Q6:
- celle grossolane: \(64,192,240\);
- celle raffinate: \(496,1344,960\);
- figli per cella genitore: \(1,2,4\) nei gradi 0,1,2;
- mappe cellulari \(S_k\) che rispettano esattamente il bordo:
  \(B'_1S_1=S_0B_1\), \(B'_2S_2=S_1B_2\).

Il trasferimento sulle sei direzioni coordinate è \(D=2I_6\). La restrizione a tre assi coordinati è dunque \(2I_3\), non \(A_\psi\). I due operatori non hanno lo stesso polinomio caratteristico e non sono simili.

Questo è un risultato importante: la suddivisione cubicale standard è una costruzione corretta, ma **non genera da sola la superaurea**.

### 2.3 Antipodalità Q6

La mappa \(c(x)=x\oplus63\) è un'involuzione senza punti fissi e produce 32 coppie antipodali. Poiché \(6-k\equiv k\pmod2\), conserva la parità di Hamming. Pertanto le 32/32 classi della bipartizione pari/dispari non coincidono con i due fogli antipodali.

Per collegare Anti-Twin alla superaurea bisogna definire l'azione sui tre canali e dimostrare che il trasferimento commuta con tale azione, oppure specificare una simmetria che la scambia.

## 3. Cosa non è ancora certificato

Il rapporto di recupero Krist-All nel repository segnala che l'archivio recuperato non contiene:
- relazione di equivalenza delle classi;
- codifica canonica dei rappresentanti;
- enumeratore deterministico e tabella completa;
- definizioni/matrici originali di \(K\) e \(W_0\).

Di conseguenza il conteggio 11.725, il residuo \(W_0\) e l'identità \(K^3=K^2+I\) restano risultati storici non certificati dal materiale recuperato. Non li uso come premessa della derivazione.

## 4. Il ponte matematico da costruire

Serve un complesso raffinato \(C^\bullet_{Q6}\) e uno spazio ridotto tridimensionale \(V_3\), con:
- una mappa di compressione \(J:C^k_{Q6}\to V_3\), o un sottospazio invariante esplicitamente definito;
- un operatore geometrico di trasferimento \(R_{Q6}\), ricavato dalle mappe genitore-figlio, dalle incidenze o da una struttura RGS/Krist-All recuperata;
- una relazione di intertwining
  \[
  J R_{Q6}=A_\psi J
  \]
  (oppure \(M_T\) secondo la convenzione di ordinamento);
- verifica di rango, nucleo, indipendenza dalla base e compatibilità con l'azione antipodale;
- un'azione quaternionica sui canali, se si vuole identificare il tripletto con gli assi locali: la mappa deve essere equivarante, non solo dimensionale.

Una via alternativa è costruire una ricorrenza di conteggio/raffinamento \(v_{n+3}=v_{n+2}+v_n\) da una regola geometrica di sostituzione. In quel caso bisogna mostrare esplicitamente quali oggetti sono contati e perché la regola locale produce quei numeri.

## 5. Test falsificabili e criterio di successo

Il nuovo audit riproducibile controlla:
1. identità della ricorrenza e convergenza dei rapporti;
2. coniugazione esatta Phase-21/trigramma;
3. dati esatti del trasferimento Q6 T055;
4. involuzione antipodale e conservazione della parità;
5. ostacolo spettrale tra \(2I_3\) e \(A_\psi\).

La derivazione sarà promossa da **aperta** a **dimostrata** soltanto quando verrà prodotto un \(J\) e un \(R_{Q6}\) geometricamente definiti che soddisfino l'intertwining. Una regressione numerica del polinomio caratteristico non basta se la matrice è stata inserita a mano.

## 6. Stato epistemico

| Affermazione | Stato |
|---|---|
| \(\psi^3=\psi^2+1\) e ricorrenza supergolden | **Prova algebrica** |
| Coniugazione Phase-21/trigramma | **Identità matriciale esatta** |
| Raffinamento midpoint Q6 e chain map T055 | **Teorema combinatorio finito** |
| Trasferimento direzionale midpoint \(2I_6\) | **Identità esatta** |
| 32 coppie antipodali; antipode conserva la parità | **Identità combinatoria** |
| Mappa geometrica Q6→operatore supergolden | **Aperta** |
| Identificazione del tripletto con gli assi quaternionici | **Aperta** |
| 11.725 classi Krist-All e \(K^3=K^2+I\) dal pacchetto recuperato | **Non certificata** |
| Interpretazione fisica di \(\psi\) come costante universale | **Non dimostrata** |

## 7. Esecuzione

Eseguire:

```bash
python scripts/audit_supergolden_q6_bridge.py
python -m unittest tests/test_supergolden_q6_bridge.py
```

Il JSON risultante è un audit di algebra e combinatoria finita. Non certifica il ponte geometrico ancora mancante.


## 8. Raffinamento dei tre canali: il vincolo di simmetria

La decomposizione canonica dei sei bit in due triple dà
\[
Q_6=Q_3^{\rm lower}\square Q_3^{\rm upper}.
\]
Per una singola tripletta, lo spazio delle funzioni sui suoi otto stati ha la base di Walsh e una componente intrinseca tridimensionale
\[
\mathcal H_1=\operatorname{span}\{\chi_1,\chi_2,\chi_3\}.
\]
Questi sono i tre canali naturali su cui comprimere un operatore geometrico \(\mathcal R\):
\[
M=E^T\mathcal R E,\qquad
\mathcal L=(I-EE^T)\mathcal R E.
\]
La chiusura dei tre canali richiede \(\mathcal L=0\). Questa è una condizione necessaria da testare, non una proprietà automatica.

L'audit indipendente del settore trigrammatico stabilisce due ostacoli:

1. Se \(\mathcal R\) commuta con tutte le otto traslazioni di \(\mathbb Z_2^3\), la compressione \(M\) è diagonale nella base di Walsh. Il target \(M_T\) non è diagonale.
2. Se \(\mathcal R\) commuta con tutte le permutazioni \(S_3\) dei tre bit, allora \(M=\alpha I+\beta(J-I)\). Anche questa forma non coincide con \(M_T\).

Dunque la superaurea non può emergere da un raffinamento che conservi integralmente le simmetrie di traslazione del trigramma e di permutazione dei tre assi. Serve un dato geometrico che selezioni un orientamento e un ordinamento dei canali.

## 9. Ruolo corretto dei quaternioni e del rapporto aureo

Un riferimento quaternionico \(q\) può trasportare una terna orientata:
\[
e_a(q)=q e_a q^{-1},\qquad a=1,2,3.
\]
Ma la sola terna ortonormale orientata non determina i coefficienti di raffinamento. Per ottenere il target non simmetrico occorre specificare anche:
- quale canale è distinto come iniziale;
- quale ordine ciclico/orientato hanno i tre canali;
- come l'Anti-Twin agisce su tale ordinamento;
- quali figli geometrici sono assegnati a ciascun genitore.

La verifica decisiva è costruire \(\mathcal R\) dalle incidenze orientate dei figli e poi misurare \(E^T\mathcal R E-M_T\) e \(\|(I-EE^T)\mathcal R E\|\). Definire direttamente \(\mathcal R=EM_TE^T+\lambda(I-EE^T)\) sarebbe circolare e non è ammesso come derivazione.

Il collegamento già presente tra \(\varphi\) e \(\psi\) nel modello Cantor–Q6 usa pesi di ramo scelti esplicitamente in funzione di \(\varphi\), ma assume già la matrice \(A_\psi\). È quindi un modello simbolico accoppiato, non una deduzione di \(\psi\) da \(\varphi\). Il ponte geometrico deve ancora mostrare come le proporzioni auree della cella o del coframe producano i conteggi/trasferimenti a tre canali.

## 10. Prossimo test geometrico discriminante

La prossima costruzione non deve partire dal polinomio. Deve partire da un oggetto geometrico orientato:
1. scegliere una cella genitore e i suoi tre tipi di direzione tangente, identificati mediante il coframe quaternionico;
2. elencare tutti i figli con orientazione e molteplicità, includendo le identificazioni sulle facce condivise;
3. assemblare la matrice di conteggio/trasferimento senza imporre coefficienti;
4. verificare la compatibilità di bordo e l'azione Anti-Twin;
5. comprimere sui tre canali di Walsh e misurare chiusura e residuo rispetto a \(M_T\).

Se il trasferimento risultasse diagonalizzabile o simmetrico per effetto delle simmetrie residue, la proposta supergolden andrebbe modificata o respinta per quella geometria. Se invece il dato orientato producesse esattamente \(M_T\), allora \(\psi\) emergerebbe come raggio spettrale del raffinamento, senza essere stata inserita a priori.
