import pandas as pd
import numpy as np

# dataframe esempio inculusi valori mancanti e duplicati 

data = {
    'Nome' : ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
    'Eta' : [25, 30, 22, 30, np.nan, 25, 29],
    'Città' : ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Torino']
}

df = pd.DataFrame(data)

#stampa dataframe originale
print("DataFrame originale:")
print(df)

#rimozione duplicati
df= df.drop_duplicates()

#gestione dati mancanti
#rimozione delle righe dove almeno un elemento è mancante
df_cleaned = df.dropna()

#possiamo sostituire dati mancanti con valore specifico
df['Eta'] = df['Eta'].fillna(df['Eta'].mean(), inplace=True)

#stampa del dataframe pulito
print("\nDataFrame dopo la pulizia:")
print(df_cleaned)

#stampa del dataframe con dati mancanti sostituiti
print("\nDataFrame con dati mancanti sostituiti:")
print(df)