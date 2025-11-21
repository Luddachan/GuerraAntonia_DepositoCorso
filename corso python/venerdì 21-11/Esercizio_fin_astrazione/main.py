# main.py
from camion import Camion
from furgone import Furgone
from motocarro import Motocarro
from gestore_flotta import GestoreFlotta

def main():
    # Creazione del gestore della flotta
    gestore = GestoreFlotta()

    # Creazione veicoli
    c1 = Camion("AB123CD", 5000, 4)
    f1 = Furgone("XY987ZT", 2000, "elettrico")
    m1 = Motocarro("MC456GH", 800, 5)

    # Aggiunta alla flotta
    gestore.aggiungi_veicolo(c1)
    gestore.aggiungi_veicolo(f1)
    gestore.aggiungi_veicolo(m1)

    # Stampa veicoli
    print("\n--- Veicoli in flotta ---")
    gestore.stampa_veicoli()

    # Calcolo manutenzione totale
    print("\nCosto totale manutenzione:", gestore.costo_totale_manutenzione(), "€")

    # Esempio di carico/scarico
    print("\n--- Prove di carico ---")
    c1.carica(1000)
    c1.carica(6000)   # errore perchè supera il peso massimo
    c1.scarica()

if __name__ == "__main__":
    main()
