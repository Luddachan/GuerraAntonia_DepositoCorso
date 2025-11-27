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


#esempio: colonna "date" in stringhe-> datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
#oppure per creare un indice
df.index = pd.to_datetime(df['date'])

#dataframe resample
#partendo da un dataframe con indice datetime
df_daily = df.resample('D').mean() #media giornaliera
df_monthly = df.resample('M').sum() #somma mensile

#aggiunge una colonna con il valore del giorno precedente
df['prev_day'] = df['value'].shift(1)
#tasso variazione giornaliero
df['daily_return'] = df['value'].pct_change()
#equivale a shift + calcolo %

#finestra mobile di 7 giorni: media e deviazione standard 
df['rolling_mean7'] = df['value'].rolling(window=7).mean()
df['rolling_std7'] = df['value'].rolling(window=7).std()


