import os
import numpy as np
from utils import *
from funzioni import *
from Array_mono import *
import csv

# File di output
out_csv = "california_housing_data.csv"

""" # Reset file all'inizio
if os.path.exists(out_csv):
    os.remove(out_csv)
    print(f"File '{out_csv}' subisce reset.\n") """

# Caricamento CSV
nome_csv = input("Inserisci il nome del CSV di riferimento: ")
dataset = read(nome_csv)
if dataset is None:
    exit()

# Nomi colonne in ordine corretto (corrispondenti a dataset[:, index])
colonne = [
    "longitudine", "latitudine", "housing_median_age",
    "total_rooms", "total_bedrooms", "population",
    "households", "median_income", "median_house_value"
]

# ----------------------- FUNZIONI UTILITARIE -----------------------

def stampa_report(matrix, colonne):
    """Stampa media, deviazione standard, min, max per ogni colonna."""
    
    medie = media_colonne(matrix)
    deviazioni = std_colonne(matrix)
    minimi = np.min(matrix, axis=0)
    massimi = np.max(matrix, axis=0)

    print("\n=== REPORT COMPLETO DEL DATASET ===\n")
    print("=== Statistiche ===")

    for i, nome in enumerate(colonne):
        print(f"{nome}:")
        print(f"  media = {medie[i]:.2f}")
        print(f"  std   = {deviazioni[i]:.2f}")
        print(f"  min   = {minimi[i]}")
        print(f"  max   = {massimi[i]}\n")

# Funzione per scegliere colonna (per analisi 1D)
def scegli_colonna(dataset, colonne):
    print("\n--- Seleziona colonna ---")
    for i, nome in enumerate(colonne):
        print(f"{i} - {nome}")

    scelta = int(input("Inserisci indice: "))
    return dataset[:, scelta], colonne[scelta]

# ------------------------ MENU PRINCIPALE ------------------------
# Dizionari menu
funz = {
    "1": ("Somma colonne", somma_colonne),
    "2": ("Media colonne", media_colonne),
    "3": ("Somma righe", somma_righe),
    "4": ("Media righe", media_righe),
    "5": ("Norma matrice", norma),
    "6": ("Trasposta matrice", trasposta),
    "7": ("Covarianza", covarianza),
    "8": ("Report completo", None),
    "0": ("Esci", None)
}

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

    match tipo:

        # USCITA
        case "0":
            print("Uscita dal programma.")
            break

        # ----------------------- ANALISI 2D -----------------------
        case "1":
            while True:
                print("\n=== MENU 2D ===")
                for key, (nome, _) in funz.items():
                    print(f"{key} - {nome}")

                scelta2d = input("Scegli operazione: ")

                match scelta2d:

                    case "0":
                        break

                    case "8":
                        stampa_report(dataset, colonne)

                    case _:
                        if scelta2d in funz and funz[scelta2d][1] is not None:
                            nome_op, func = funz[scelta2d]
                            risultato = func(dataset)
                            print(f"\n--- Risultato {nome_op} ---")
                            print(risultato)
                            salva_csv({nome_op: risultato}, out_csv)
                            print("Risultato salvato.")

                        else:
                            print("Scelta non valida.")

        # ----------------------- ANALISI 1D -----------------------
        case "2":
            colonna, nome_col = scegli_colonna(dataset, colonne)

            while True:
                print(f"\n=== MENU 1D: Analisi colonna '{nome_col}' ===")
                for key, (nome, _) in menu_1d.items():
                    print(f"{key} - {nome}")

                scelta1d = input("Scegli operazione: ")

                match scelta1d:

                    case "0":
                        break

                    # Richiede parametro extra
                    case "8":
                        x = float(input("Valore da inserire: "))
                        risultato = menu_1d["8"][1](colonna, x)
                        print(f"\n--- Risultato {menu_1d['8'][0]} ---")
                        print(risultato)
                        salva_csv({f"{menu_1d['8'][0]} ({nome_col})": risultato}, out_csv)

                    # Tutte le altre operazioni normali
                    case _:
                        if scelta1d in menu_1d and menu_1d[scelta1d][1] is not None:
                            nome_op, func1d = menu_1d[scelta1d]
                            risultato = func1d(colonna)
                            print(f"\n--- Risultato {nome_op} ---")
                            print(risultato)
                            salva_csv({f"{nome_op} ({nome_col})": risultato}, out_csv)
                        else:
                            print("Scelta non valida.")

        # SCELTA NON VALIDA
        case _:
            print("Opzione non riconosciuta, riprova.")
