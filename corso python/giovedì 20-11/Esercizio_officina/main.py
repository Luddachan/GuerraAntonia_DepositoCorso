from elettrodomestico import Elettrodomestico
from classiderivate import *

def menu():
    elenco = []  # lista di elettrodomestici

    while True:
        print("\n=== MENU OFFICINA ===")
        print("1. Inserisci Lavatrice")
        print("2. Inserisci Frigorifero")
        print("3. Inserisci Forno")
        print("4. Mostra elettrodomestici registrati")
        print("5. Esci")

        scelta = input("> Scegli un'opzione: ")

        # --------------------------------------------------------
        # 1. Inserisci Lavatrice
        # --------------------------------------------------------
        if scelta == "1":
            print("\n--- Nuova Lavatrice ---")
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno acquisto: "))
            guasto = input("Guasto: ")
            kg = float(input("Capacità (kg): "))
            giri = int(input("Giri centrifuga: "))

            # Creazione dell’oggetto Lavatrice
            lav = Lavatrice(marca, modello, anno, guasto, kg, giri)
            #aggiunto alla lista
            elenco.append(lav)
            print("Lavatrice aggiunta!")

        # --------------------------------------------------------
        # 2. Inserisci Frigorifero
        # --------------------------------------------------------
        elif scelta == "2":
            print("\n--- Nuovo Frigorifero ---")
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno acquisto: "))
            guasto = input("Guasto: ")
            litri = int(input("Litri: "))
            freezer = input("Ha freezer? (s/n): ").lower() == "s"

            #creazione oggetto frigo e aggiunta alla lista
            frigo = Frigorifero(marca, modello, anno, guasto, litri, freezer)
            elenco.append(frigo)
            print("Frigorifero aggiunto!")

        # --------------------------------------------------------
        # 3. Inserisci Forno
        # --------------------------------------------------------
        elif scelta == "3":
            print("\n--- Nuovo Forno ---")
            marca = input("Marca: ")
            modello = input("Modello: ")
            anno = int(input("Anno acquisto: "))
            guasto = input("Guasto: ")
            tipo = input("Tipo alimentazione (elettrico/gas): ")
            ventilato = input("Ventilato? (s/n): ").lower() == "s"

            forno = Forno(marca, modello, anno, guasto, tipo, ventilato)
            elenco.append(forno)
            print("Forno aggiunto!")

        # --------------------------------------------------------
        # 4. Mostra elettrodomestici registrati (SEMPLIFICATO)
        # --------------------------------------------------------
        elif scelta == "4":
            print("\n=== ELETTRODOMESTICI REGISTRATI ===")

            if len(elenco) == 0:
                print("Nessun elettrodomestico inserito.")
            else:
                for elettro in elenco:
                    print(elettro.descrizione())
                    print("Costo stimato:", elettro.stima_costo_base(), "€")
                    print()

        # --------------------------------------------------------
        # 5. Esci
        # --------------------------------------------------------
        elif scelta == "5":
            print("\nUscita dal programma. Arrivederci!")
            break

        else:
            print("Scelta non valida, riprova.")
            
            
# Avvio del programma
if __name__ == "__main__":
    menu()
