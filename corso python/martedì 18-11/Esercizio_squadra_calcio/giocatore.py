# -------------------------------
# Classe derivata: Giocatore
# -------------------------------

from squadra import MembroSquadra

class Giocatore(MembroSquadra):
    #il giocatore eredita i valori della classe base 
    #+ quelli aggiunti da noi
    def __init__(self, nome, eta, ruolo, numero_maglia):
        #richiama il costruttore della classe base
        super.__init__(nome, eta)
        #attributi specifici di questa classe
        self.ruolo = ruolo 
        self.numero_maglia = numero_maglia
        
    def gioca_partita(self):
        print(f"{self.nome} ha {self.numero_maglia} come numero e gioca come {self.ruolo}.")
        