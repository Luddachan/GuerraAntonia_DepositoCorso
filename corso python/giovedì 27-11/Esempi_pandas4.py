import pandas as pd

#dati di esempio

data = {
    'Data': ['2021-01-01', '2021-01-01', '2021-01-01','2021-01-02'],
    'Città' : ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto' : ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite' : [100, 200, 150, 300, 250]

}

df = pd.DataFrame(data)

#creazione della tabella pivot
pivot_df = pd.pivot_table(df, values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print(pivot_df)


#utilizzo di groupby per aggregare i dati
grouped_df = df.groupby('Prodotto').sum()

print(grouped_df)