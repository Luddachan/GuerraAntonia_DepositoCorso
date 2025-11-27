import pandas as pd

#percorso del file CSV
file_path = 'vendite.csv'

#percorso del file csv
df = pd.read_csv(file_path)

#le prime righe del dataframe
#df.head() mostra le prime 5 righe del dataframe
print(df.head())