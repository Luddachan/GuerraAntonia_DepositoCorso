#classe padre persona
#attributi nome come stringa, cognome come stringa, eta come intero
# attributi nome ed eta privati
#metodi 
#--------------------------

class Persona:
    def __init__(self, nome: str, eta: int):
        self.__nome = nome
        self.__eta = eta
    
    #metodi getter e setter
    
    # getter per nome che restituisce il nome
    def get_nome(self):
        return self.__nome
    # setter per nome che permette di modificare il nome
    def set_nome(self, nuovo_nome):
        self.__nome = nuovo_nome
        
    # getter per eta che restituisce l'eta
    def get_eta(self):
        return self.__eta
    
    # setter per eta che permette di modificare l'eta
    def set_eta(self, nuova_eta):
        self.__eta = nuova_eta
        
    def presentazione(self):
        return f"Ciao, mi chiamo {self.__nome} e ho {self.__eta} anni."