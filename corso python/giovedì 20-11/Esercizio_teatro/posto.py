#classe base Posto

class Posto:
    def __init__(self, numero: int, fila: str, occupato: bool = False):
        #attributi privati
        self.__numero = numero
        self.__fila = fila
        self.__occupato = occupato
    
    # funzione per ottenere il numero del posto    
    def occupa(self):
        #controlla se il posto è già occupato
        if not self.__occupato:
            self.__occupato = True
            # metodi privati non accessibili dall'esterno
            print (f"Posto {self.__fila}{self.__numero} occupato.")
        else:
            print (f"Posto {self.__fila}{self.__numero} già occupato.")
            
    def libero(self):
        #controlla se il posto è già libero
        if self.__occupato:
            self.__occupato = False
            print (f"Posto {self.__fila}{self.__numero} liberato.")
        else:
            print (f"Posto {self.__fila}{self.__numero} già libero.")
            
    #metodi getter per accedere agli attributi privati
    def get_numero(self):
        #return del numero del posto
        return self.__numero
    
    def get_fila(self):
        #return della fila del posto
        return self.__fila
    
    # funzione per controllare se il posto è occupato
    def occupato(self):
        #return dello stato del posto
        return self.__occupato
            
        
    