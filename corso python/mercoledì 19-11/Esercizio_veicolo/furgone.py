#------
#classe furgone
#------

from veicolo import Veicolo

class Furgone(Veicolo):
    #costruttore della classe Furgone che estende Veicolo
    def __init__(self, marca, modello, anno, capacita_carico):
        # chiamata al costruttore della classe base Veicolo
        super().__init__(marca, modello, anno)
        self.__capacita_carico = capacita_carico
        self.__capacita_carico = 0 # in kg
        
    # metodo specifico per caricare e scaricare merci
    def carica(self, peso):
        if peso <= self.__capacita_carico:
            return f"Caricato {peso} kg nel furgone."
        else:
            return "Superata la capacità di carico!"
    def scarica(self, peso):
        if peso <= self.__capacita_carico:
            return f"Scaricato {peso} kg dal furgone."
        else:
            return "Non ci sono così tanti kg da scaricare!"
    
    # metodo per rappresentazione stringa del furgone
    def __str__(self):
        # richiamo il metodo della classe
        # super().___str__() per ottenere la rappresentazione della classe
        base = super().__str__()
        # aggiungo le informazioni specifiche del furgone
        return f"{base} - Capacità di carico: {self._capacita_carico} kg"