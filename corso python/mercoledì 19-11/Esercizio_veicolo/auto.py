#------
# Classe auto
#------
from veicolo import Veicolo

class Auto(Veicolo):
    #costruttore della classe Auto che estende Veicolo
    def __init__(self, marca, modello, anno, numero_porte):
        
        # chiamata al costruttore della classe base Veicolo
        super().__init__(marca, modello, anno)
        self.__numero_porte = numero_porte
        
# metodo specifico per suona clacson
    def suona_clacson(self):
        return "Beep Beep!"
    
    # metodo per rappresentazione stringa dell'auto
    def __str__(self):
        # richiamo il metodo della classe
        # super().___str__() per ottenere la rappresentazione della classe
        base = super().__str__()
        # aggiungo le informazioni specifiche dell'auto
        return f"{base} - Porte: {self._numero_porte}"