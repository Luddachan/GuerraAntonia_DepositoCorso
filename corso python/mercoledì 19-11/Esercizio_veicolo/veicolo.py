#classe base Veicolo

class Veicolo:
    #attributi privati
    def __init__(self, marca: str, modello: str, anno: int, accensione: bool = False):
        #inizializzazione degli attributi
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = accensione
     
    # metodi generici per la classe Veicolo 
    # metodo per accendere il veicolo   
    def accendi(self):
        self.__accensione = True
    # metodo per spegnere il veicolo   
    def spegni(self):
        self.__accensione = False
        
    # metodo per verificare lo stato di accensione   
    def __str__(self):
        stato = "Acceso" if self._accensione else "Spento"
        return f"{self._marca} {self._modello} ({self._anno}) - {stato}"
    