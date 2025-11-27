import numpy as np
import pandas as pd

# -----------------------------------------------------------
# 1. GENERAZIONE DEI DATI CASUALI
# -----------------------------------------------------------

# Generiamo un intervallo di date per un mese (es. 30 giorni)
date = pd.date_range(start="2025-01-01", end="2025-01-30")

#tre città e tre prodotti
citta = ['Roma', 'Milano', 'Napoli']
prodotti = ['Mouse', 'Tastiera', 'Monitor']

#creiamo un dataframe combinando i dati
df = pd.DataFrame({
    #repeat per ripetere ogni data 3 volte (una per ogni città/prodotto)
    'Data': np.repeat(date, 3),
    "Città": np.random.choice(citta, 30),  # 30 valori casuali
    #random.choice per selezionare casualmente dagli elenchi
    "Prodotto": np.random.choice(prodotti, 30),
    #random.randint per generare numeri casuali interi
    "Vendite": np.random.randint(10, 200, 30)  # numeri casuali 10–200
})

print ("===Dataframe originale===")
print(df)

#tabella pivot (media vendite)
#funzione vista nell'esempio precedente
pivot= df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print("\n===Tabella Pivot ===")
print(pivot)

#groupby (vendite totali per prodotto)

totali = df.groupby('Prodotto')["Vendite"].sum()
print("\n===Vendite totali per prodotto===")
print(totali)