#classe derivata da Posto

from posto import Posto

class PostoStandard(Posto):
    def __init__(self, numero: int, fila: str, costo: float):
        # richiama il costruttore della classe base
        super().__init__(numero, fila) 
        self.costo = costo
        
    def prenota(self):
        # richiama il metodo prenota della classe base
        super().occupa()
        if self.occupato():
            # stampa il costo del posto standard 
            #getter per accedere agli attributi privati della classe base
            print(f"Posto Standard {self.get_fila()}{self.get_numero()} prenotato con successo al costo di {self.costo}€.")
        else:
            print(f"Impossibile prenotare il posto standard {self.get_fila()}{self.get_numero()}.")
            
    
        
    

