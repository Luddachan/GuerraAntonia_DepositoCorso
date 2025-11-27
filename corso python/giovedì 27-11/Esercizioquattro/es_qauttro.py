import pandas as pd
import numpy as np

# -------------------------------------------------------------------
# 1. CARICAMENTO E ESPLORAZIONE INIZIALE
# -------------------------------------------------------------------

# Caricamento del dataset da file CSV
df = pd.read_csv("clienti_random.csv")

# Visualizzo le prime righe del dataset
print("Prime 5 righe del dataset:")
print(df.head(), "\n")

# Informazioni generali: tipi di dati e valori mancanti
print("Info dataset:")
print(df.info(), "\n")

# Statistiche descrittive per le colonne numeriche
print("Statistiche descrittive:")
print(df.describe(), "\n")

# Distribuzione dei valori della colonna Churn
print("Distribuzione Churn:")
#dropna=False per includere i NaN nel conteggio
print(df["Churn"].value_counts(dropna=False), "\n")

# Gestione valori mancanti:
# - per le numeriche: sostituisco con mediana
# - per le categoriche: sostituisco con moda

num_cols = df.select_dtypes(include=[np.number]).columns
cat_cols = df.select_dtypes(exclude=[np.number]).columns

for col in num_cols:
    mediana = df[col].median()
    #df[col] ci permette di accedere alla colonna
    #fillna sostituisce i NaN con la mediana calcolata
    df[col] = df[col].fillna(mediana)
    
for col in cat_cols:
    moda = df[col].mode()[0]  
    # moda() restituisce una Serie, prendo il primo elemento
    df[col] = df[col].fillna(moda)







#analisi esplorativa
#creo una nuova colonna costo per GB
df['Costo_per_GB'] = df['Costo'] / df['GB_Consumati']
print("Prime 5 righe con nuova colonna Costo_per_GB:")
print(df.head(), "\n")

#analisi correlazione tra variabili numeriche
print ("Correlazione tra le variabili numeriche:")
#corr calcola la matrice di correlazione
print(df.corr(), "\n")

#groupby come cambiano i valori a seconda del churn
print("Statistiche per Churn:")
print(df.groupby('Churn').mean(), "\n")

