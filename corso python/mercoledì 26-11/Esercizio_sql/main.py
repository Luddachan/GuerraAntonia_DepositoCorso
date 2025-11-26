import os
import numpy as np
import csv
from utils import read, salva_csv
from funzioni import *
from Array_mono import *

# File di output
out_csv = "california_housing_analysis.csv"

# Reset file all'inizio
if os.path.exists(out_csv):
    os.remove(out_csv)
    print(f"File '{out_csv}' subisce reset.\n")

# Caricamento CSV
nome_csv = input("Inserisci il nome del CSV di riferimento: ")
dataset = read(nome_csv)
if dataset is None:
    exit()

# Colonne richieste per il menù (nomi in italiano)
colonne = [
    "longitudine", "latitudine", "housing_median_age",
    "total_rooms", "total_bedrooms", "population",
    "households", "median_income", "median_house_value"
]

# Collegamento tra nomi italiani e nomi reali del CSV
mappa = {
    "longitudine": "longitude",
    "latitudine": "latitude",
    "housing_median_age": "housing_median_age",
    "total_rooms": "total_rooms",
    "total_bedrooms": "total_bedrooms",
    "population": "population",
    "households": "households",
    "median_income": "median_income",
    "median_house_value": "median_house_value"
}

# Carica il file CSV in memoria come lista di dizionari
with open(nome_csv, newline="") as f:
    reader = csv.DictReader(f)
    dati = list(reader)

def estrai_colonna(nome):
    """
    Estrae tutti i valori numerici dalla colonna richiesta.
    Non usa try, quindi verifica manualmente se il valore è convertibile.
    """
    col_csv = mappa[nome]
    valori = []

    for riga in dati:
        valore = riga[col_csv]

        # Controllo manuale: salta valori vuoti o non numerici
        if valore.replace('.', '', 1).isdigit():
            valori.append(float(valore))

    return valori

def mostra_menu():
    """Mostra il menu delle colonne selezionabili."""
    print("\n=== MENÙ DEI VALORI DISPONIBILI ===")
    for i, voce in enumerate(colonne, start=1):
        print(f"{i}. {voce}")
    print("0. Esci")

def mostra_estremi(colonna):
    """Calcola e mostra min e max della colonna scelta."""
    valori = estrai_colonna(colonna)

    print("\n=== Valori estremi rilevanti ===")
    print(f"Colonna: {colonna}")
    print(f"Min: {min(valori)}")
    print(f"Max: {max(valori)}")

# Loop principale del programma
while True:
    mostra_menu()
    scelta = input("\nSeleziona un numero: ")

    # Uscita
    if scelta == "0":
        print("Uscita dal programma.")
        break

    # Controllo che la scelta sia valida
    if scelta.isdigit() and 1 <= int(scelta) <= len(colonne):
        colonna_scelta = colonne[int(scelta) - 1]
        mostra_estremi(colonna_scelta)
    else:
        print("Scelta non valida, riprova.")


# Funzione per scegliere colonna (per analisi 1D)
def scegli_colonna(dataset, colonne):
    print("\n--- Seleziona colonna ---")
    for i, nome in enumerate(colonne):
        print(f"{i} - {nome}")
    scelta = int(input("Inserisci indice colonna: "))
    return dataset[:, scelta], colonne[scelta]

# STAMPA REPORT COMPLETO
def stampa_report(matrix, colonne):
    
    medie = media_colonne(matrix)
    deviazioni = std_colonne(matrix)
    minimi = np.min(matrix, axis=0)
    massimi = np.max(matrix, axis=0)
    print("\n=== REPORT COMPLETO DEL DATASET ===\n")
    
    print("=== Statistiche medie e deviazioni standard ===")
    for i, nome in enumerate(colonne):
        print(f"{nome.capitalize()}: media = {medie[i]:.2f}, std = {deviazioni[i]:.2f}")
    print()


    # analisi valori estremi
    # Mappa tra nomi "italiani" e colonne reali del CSV

 
    

# MENU PRINCIPALE
funz = {
    "1": ("Somma colonne", somma_colonne),
    "2": ("Media colonne", media_colonne),
    "3": ("Somma righe", somma_righe),
    "4": ("Media righe", media_righe),
    "5": ("Norma matrice", norma),
    "6": ("Trasposta matrice", trasposta),
    "7": ("Covarianza", covarianza),
    "8": ("Report proteine", None),
    "9": ("Analisi 1D su una colonna", None),
    "0": ("Esci", None)
}

# MENU 1D
menu_1d = {
    "1": ("Valore minimo", val_min),
    "2": ("Valore massimo", val_max),
    "3": ("Media", media),
    "4": ("Deviazione standard", dev_std),
    "5": ("Indice valore minimo", indice_val_min),
    "6": ("Indice valore massimo", indice_val_max),
    "7": ("Mediana", mediana),
    "8": ("Posizione ordinata inserimento", posiz_ord_inserimento),
    "0": ("Torna indietro", None)
}
while True:
    print("\n=== SCEGLI TIPO DI ANALISI ===")
    print("1 - Analisi 2D (tutta la matrice)")
    print("2 - Analisi 1D (una colonna)")
    print("0 - Esci")
    
    tipo = input("Scegli un'opzione: ")

    if tipo == "0":
        print("Uscita dal programma.")
        break

    elif tipo == "1":  # Analisi 2D
        while True:
            print("\n=== MENU 2D ===")
            for key, (nome, _) in funz.items():
                if key != "9":  # Escludiamo l'opzione 1D nel menu 2D
                    print(f"{key} - {nome}")
            
            scelta2d = input("Scegli un'operazione 2D: ")

            if scelta2d == "0":
                break

            if scelta2d == "8":  # Report completo
                stampa_report(dataset, colonne)
                continue

            if scelta2d in funz and funz[scelta2d][1] is not None:
                nome_op, func = funz[scelta2d]
                risultato = func(dataset)
                print(f"\n--- Risultato {nome_op} ---")
                print(risultato)
                salva_csv({nome_op: risultato}, out_csv)
                print("Risultato salvato.")

    elif tipo == "2":  # Analisi 1D
        colonna, nome_col = scegli_colonna(dataset, colonne)

        while True:
            print(f"\n=== MENU 1D: Analisi colonna '{nome_col}' ===")
            for key, (nome, _) in menu_1d.items():
                print(f"{key} - {nome}")

            scelta1d = input("Scegli operazione 1D: ")

            if scelta1d == "0":
                break

            nome_op, func1d = menu_1d[scelta1d]

            # Caso con parametro extra (posizione ordinata inserimento)
            if scelta1d == "8":
                x = float(input("Valore da inserire: "))
                risultato = func1d(colonna, x)
            else:
                risultato = func1d(colonna)

            print(f"\n--- Risultato {nome_op} ---")
            print(risultato)
            salva_csv({f"{nome_op} ({nome_col})": risultato}, out_csv)
            print("Risultato salvato.\n")