import pandas as pd
#slide 467

#caricare i dati in un dataframe

df = pd.read_csv('vendite_prodotti.csv')

#aggiungere una colonna totale vendite (prodotto tra quantità e prezzo unitario)
df['Totale_Vendite'] = df['Quantità'] * df['Prezzo_Unitario']

#raggruppare i dati per prodotto e calcolare il totale delle vendite per ciascun prodotto
#sum serve per sommare i valori della colonna Totale_Vendite
#reset_index serve per resettare l'indice del dataframe
totale_per_prodotto = df.groupby('Prodotto')['Totale_Vendite'].sum().reset_index()

#trovare il prodotto più venduto in termini di quantià
#idxmax restituisce l'indice del valore massimo nella serie
prodotto_piu_venduto = df.groupby('Prodotto')['Quantità'].sum().idxmax() 