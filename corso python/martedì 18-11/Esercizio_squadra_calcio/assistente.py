# -------------------------------
# Classe derivata: Assistente
# -------------------------------

# Importo la classe base
from squadra import MembroSquadra

class Assistente(MembroSquadra):
    # L'assistente eredita nome ed età
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    # Metodo specifico dell'assistente
    def supporta_team(self):
        print(f"{self.nome} supporta la squadra come {self.specializzazione}.")