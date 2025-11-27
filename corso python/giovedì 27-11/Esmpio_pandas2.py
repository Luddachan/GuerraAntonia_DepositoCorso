import pandas as pd

#creazione di un dataframe con dati da esempio
#dizionario  di liste
data ={
    'Nome' : ['Alice', 'Bob', 'Carla'],
    'Eta' : [25, 30, 22],
    'Città' : ['Roma', 'Milano', 'Napoli']
}

df = pd.DataFrame(data)

#stampa del dataframe originale
print("DataFrame originale:")
print(df)

#selezione delle righe dove l'età è maggiore di 23
df_older= df[df['Eta'] > 23]

#stampa delle righe selezionate
print("\nRighe con età maggiore di 23:")
print(df_older)

#aggiungiamo una nuova colonna la persona maggiorenne
df['Maggiorenne'] = df['Eta'] >= 18

#stampa del dataframe aggiornato
print("\nDataFrame con colonna 'Maggiorenne':")
print(df)