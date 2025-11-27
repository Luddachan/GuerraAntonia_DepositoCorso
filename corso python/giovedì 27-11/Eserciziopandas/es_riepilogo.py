import pandas as pd
#importo train.csv
#slide 467

df = pd.read_csv('train.csv')

#printo le prime 5 righe e le ultime 5 righe del dataframe
print("Prime 5 righe del DataFrame:")
print(df.head())
print("\nUltime 5 righe del DataFrame:")
print(df.tail())

#visualizzo il tipo di dati di ogni colonna
print("\n--- Tipi di dati in ciascuna colonna ---- ")
print(df.dtypes)

#calcolo statistiche descrittive per le colonne numeriche (media, mediana, deviazione standard)
print("\n--- Statistiche per le colonne numeriche ---")
#stampa la descrizione statistica del dataframe
print(df.describe())

#calcolo media età passeggeri
#mean serve per calcolare la media
media_eta = df['Age'].mean()
print(f"\nMedia età passeggeri: {media_eta:.2f}")
#calcolo della mediana età passeggeri
mediana_eta = df['Age'].median()
print(f"Mediana età passeggeri: {mediana_eta:.2f}")
#calcolo deviazione standard età passeggeri
std_eta = df['Age'].std()
print(f"Deviazione standard età passeggeri: {std_eta:.2f}")

#identifica e rimuove i duplicati
#drop_duplicates rimuove i duplicati
df_no_duplicati = df.drop_duplicates()

#gestire i valori mancanti sostituendoli con la mediana della colonna
df_no_duplicati['Age'].fillna(mediana_eta, inplace=True)
print("\nDataFrame dopo la rimozione dei duplicati e gestione dei valori mancanti:", df_no_duplicati)

#nuova colonna "Categoria età" classifica le persone come "Giovane", "Adulto", "Senior"
def categoria_eta(x):
    #controlla l'età e restituisce la categoria corrispondente
    if x <= 18:
        return 'Giovane'
    elif x <= 65:
        return 'Adulto'
    else:
        return 'Senior'
#operazione apply per applicare la funzione categoria_eta a ogni elemento della colonna 'Age'
df['categoria_eta'] = df['Age'].apply(categoria_eta)


#salva il dataframe modificato in un nuovo file CSV
df.to_csv('train_modificato.csv', index=False)
print("\nDataFrame modificato salvato in 'train_modificato.csv'")




 