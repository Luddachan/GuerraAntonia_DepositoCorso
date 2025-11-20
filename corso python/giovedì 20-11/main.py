from Esercizio_astrazione import *

def main():
    # Creiamo alcuni impiegati per esempio
    imp1 = ImpiegatoFisso("Mario", "Rossi", 1500)
    imp2 = ImpiegatoAProvvigione("Luca", "Bianchi", 1000, vendite=5000, percentuale_bonus=0.05)
    imp3 = ImpiegatoAProvvigione("Anna", "Verdi", 1200, vendite=8000, percentuale_bonus=0.07)

    # Li mettiamo in una lista
    lista_impiegati = [imp1, imp2, imp3]

    # Stampiamo tutto
    stampa_stipendi(lista_impiegati)



# AVVIO DEL PROGRAMMA

if __name__ == "__main__":
    main()
