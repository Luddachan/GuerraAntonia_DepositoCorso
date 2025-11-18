# -------------------------------
# Classe derivata: Allenatore
# -------------------------------

from squadra import MembroSquadra
from giocatore import Giocatore

class Allenatore(MembroSquadra):
    #allenatore eredita i valori della classe base 
    #+ quelli aggiunti da noi
    def __init__(self, nome, eta, anni_esperienza):
        #costruttore della classe base
        super().__init__(nome, eta)
        #attributi solo di questa classe
        self.anni_esperienza = anni_esperienza
        
    def dirige_allenamento(self):
        print(f"{self.nome} dirige l'allenamento con {self.anni_esperienza} anni di esperienza.")
