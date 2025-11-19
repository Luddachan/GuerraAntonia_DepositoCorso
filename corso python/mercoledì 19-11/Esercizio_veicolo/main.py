from auto import Auto
from furgone import Furgone
from motocicletta import Motocicletta
from gestore_parco import GestoreParcoVeicoli

# Esempio di utilizzo delle classi definite

parco = GestoreParcoVeicoli()

a1 = Auto("Fiat", "Punto", 2010, 5)
f1 = Furgone("Ford", "Transit", 2018, 1200)
m1 = Motocicletta("Yamaha", "R6", 2020, "sportiva")

# Aggiunta dei veicoli al parco
parco.aggiungi_veicolo(a1)
parco.aggiungi_veicolo(f1)
parco.aggiungi_veicolo(m1)
# Stampa delle informazioni sui veicoli
print(a1)
print(f1)
print(m1)
# Rimozione di un veicolo
parco.rimuovi_veicolo(a1)
# Lista dei veicoli nel parco
parco.lista_veicoli()