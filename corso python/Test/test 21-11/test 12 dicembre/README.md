# Analisi e Predizione Vendite Manga

Questo progetto esegue un'analisi esplorativa dei dati (EDA) e applica algoritmi di Machine Learning su un dataset di manga best-seller per comprendere i fattori che influenzano le vendite e prevedere il successo commerciale.

## Struttura del Progetto
- `main.py`: Script Python principale contenente l'intero workflow.
- `best-selling-manga.csv`: Dataset di input (richiesto).
- `manga_analysis_dashboard.png`: Output grafico generato dallo script.
- `README.md`: Documentazione del progetto.

## Fasi del Processo

### 1. Pulizia dei Dati (Data Cleaning)
Il dataset grezzo viene processato per renderlo analizzabile:
- Conversione delle colonne `Approximate sales` e `No. of collected volumes` in formato numerico, gestendo errori e caratteri speciali.
- Estrazione dell'anno di inizio (`Start_Year`) dalla colonna testuale `Serialized` tramite espressioni regolari (Regex).
- Rimozione di valori nulli critici.

### 2. Visualizzazione (Data Visualization)
Viene generata una dashboard (`manga_analysis_dashboard.png`) con 4 grafici:
1. **Top 10 Manga**: Classifica per vendite totali.
2. **Distribuzione Demografica**: Percentuale di manga Shonen, Seinen, ecc.
3. **Scatter Plot**: Correlazione tra numero di volumi pubblicati e vendite totali.
4. **Trend Temporale**: Media delle vendite basata sull'anno di inizio della serie.

### 3. Machine Learning
L'obiettivo è predire le **Vendite Totali** (`Approximate sales`) basandosi su 4 feature:
- Numero di volumi
- Anno di inizio
- Demografia (convertita numericamente)
- Editore (convertito numericamente)

Sono stati utilizzati tre modelli a confronto:
1. **Linear Regression**: Modello base per relazioni lineari semplici.
2. **Random Forest Regressor**: Modello avanzato basato su alberi decisionali per catturare relazioni complesse.
3. **KminClustering**

## Risultati Ottenuti
L'output dello script mostrerà a video le metriche di valutazione:
- **MAE (Mean Absolute Error)**: Di quanti milioni sbaglia in media il modello.
- **R² Score**: Quanto bene il modello si adatta ai dati (1.0 è perfetto).

Generalmente il numero di volumi è il predittore più forte, ma la varianza elevata dei "fenomeni virali" (come One Piece) rende la predizione esatta complessa.
