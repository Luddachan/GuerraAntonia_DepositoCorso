#classe motocicletta
from veicolo import Veicolo

class Motocicletta(Veicolo):
    #costruttore della classe Motocicletta che estende Veicolo
    def __init__(self, marca, modello, anno, tipo):
        # chiamata al costruttore della classe base Veicolo
        super().__init__(marca, modello, anno)
        self.__tipo = tipo.lower  # es. "sportiva", "crossover", "naked" 
        
    # metodo specifico per fare una impennata
    def esegui_wheelie(self):
        if self._tipo == "sportiva":
            return "La motocicletta sportiva sta facendo una impennata!"
        else:
            return "Solo le motociclette sportive possono fare impennate!"
    
    
    # metodo per rappresentazione stringa della motocicletta
    def __str__(self):
        # richiamo il metodo della classe
        # super().___str__() per ottenere la rappresentazione della classe
        base = super().__str__()
        # aggiungo le informazioni specifiche della motocicletta
        return f"{base} - Tipo: {self._tipo}"  