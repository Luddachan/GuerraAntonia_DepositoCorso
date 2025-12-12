import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# 1. Carichiamo il modello

rf_caricato = joblib.load('C:\\Users\\compu\\Documents\\GitHub\\GuerraAntonia_DepositoCorso\\corso python\\Test\\test 21-11\\test 12 dicembre\\modello_manga.pkl')
print("Modello caricato! Pronto a fare previsioni.")

# 2. Carichiamo il dataset per 'insegnare' agli encoder i nomi di Generi ed Editori
df = pd.read_csv('C:\\Users\\compu\\Documents\\GitHub\\GuerraAntonia_DepositoCorso\\corso python\\Test\\test 21-11\\test 12 dicembre\\cleaned_manga_dataset.csv')


df['Demographic'] = df['Demographic'].astype(str)
df['Publisher'] = df['Publisher'].astype(str)

le_demo = LabelEncoder()
le_demo.fit(df['Demographic']) # L'encoder impara: "Shonen" = 1, "Seinen" = 2, ecc.

le_pub = LabelEncoder()
le_pub.fit(df['Publisher'])    # L'encoder impara i nomi degli editori

print("Encoders inizializzati correttamente.")

def predict_new_manga(volumes, start_year, demographic, publisher):
    """
    Funzione per predire le vendite di un nuovo manga ipotetico.
    """
    # 1. Encoding dei dati (Testo -> Numero)
    
    # Gestione DEMOGRAFICA
    try:
        # Trasformiamo l'input in lista perché transform vuole una lista
        demo_code = le_demo.transform([str(demographic)])[0]
    except ValueError:
        print(f"Attenzione: Demografia '{demographic}' mai vista prima. Uso un valore medio/default (0).")
        demo_code = 0 
        
    # Gestione EDITORE
    try:
        pub_code = le_pub.transform([str(publisher)])[0]
    except ValueError:
        print(f"Attenzione: Editore '{publisher}' mai visto prima. Uso un valore medio/default (0).")
        pub_code = 0 

    # 2. Creazione del vettore input
    
    input_data = [[volumes, start_year, demo_code, pub_code]]
    
    # 3. Predizione
    # --- CORREZIONE: Usiamo 'rf_caricato', non 'rf' ---
    prediction = rf_caricato.predict(input_data)[0]
    
    print(f"\n--- PREDIZIONE ---")
    print(f"Scenario: Manga {demographic} di {publisher} ({start_year}, {volumes} volumi)")
    print(f"Vendite Stimate: {prediction:.2f} Milioni di copie")
    return prediction

# --- ESEMPIO DI UTILIZZO ---

predict_new_manga(volumes=45, start_year=2010, demographic='Shōnen', publisher='Shueisha')