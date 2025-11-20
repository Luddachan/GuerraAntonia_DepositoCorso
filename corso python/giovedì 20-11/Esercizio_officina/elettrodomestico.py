#classe base elettrodomestico
from datetime import datetime
anno_corrente = datetime.now().year


class Elettrodomestico:
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str):
        self._marca = marca
        self._modello = modello
        self._anno_acquisto = anno_acquisto
        self._guasto = guasto

    # metodi getter e setter
    
    def get_marca(self):
        # ritorna la marca dell'elettrodomestico
        return self._marca
    
    def get_modello(self):
        # ritorna il modello dell'elettrodomestico
        return self._modello
    
    def get_anno_acquisto(self):
        # ritorna l'anno di acquisto dell'elettrodomestico
        return self._anno_acquisto
    
    def get_guasto(self):
        # ritorna il guasto dell'elettrodomestico
        return self._guasto
    
    # setter per aggiornare il guasto
    def set_guasto(self, guasto: str):
        #imposta la descrizione del guasto
        if not isinstance(guasto, str) or guasto.strip() == "":
            print("Errore: La descrizione del guasto deve essere una stringa non vuota.")
        self._guasto = guasto
    
    # setter per aggiornare la marca
    # controllo che la marca sia una stringa non vuota
    def set_marca(self, marca: str):
        #imposta la marca dell'elettrodomestico
        # isinstance serve per controllare che il tipo di dato sia corretto per evitare errori
        if not isinstance(marca, str) or marca.strip() == "":
            print("Errore: La marca deve essere una stringa non vuota.")
        self._marca = marca
    
    def set_modelllo(self, modello: str):
        #imposta il modello dell'elettrodomestico
        if not isinstance(modello, str) or modello.strip() == "":
            print("Errore: Il modello deve essere una stringa non vuota.")
        self._modello = modello
        
    def set_anno_acquisto(self, anno_acquisto: int):
        #controlla che l'anno di acquisto sia valido 
        #anno corrente ottenuto con datetime
        
        if anno_acquisto < 1900 or anno_acquisto > anno_corrente:
            print(f"Errore: L'anno di acquisto deve essere compreso tra 1900 e {anno_corrente}.")
        
        #imposta l'anno di acquisto dell'elettrodomestico
        if not isinstance(anno_acquisto, int) or anno_acquisto <= 0:
            print("Errore: L'anno di acquisto deve essere un intero positivo.")
        self._anno_acquisto = anno_acquisto
    
    def descrione(self):
        #restituisce una stringa con modello, marca e anno di acquisto
        return f"{self._modello} {self._marca}, acquistato nel {self._anno_acquisto}"
    
    def stima_costo_base(self):
        """
        Restituisce un costo base generico.
        Nelle sottoclassi potrà essere ridefinito (polimorfismo).
        """
        return 30.0  # costo simbolico della diagnosi