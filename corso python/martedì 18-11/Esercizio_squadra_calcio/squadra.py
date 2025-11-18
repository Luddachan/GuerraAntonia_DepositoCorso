#classe base 

class MembroSquadra:
    def __init__(self, nome, eta):
        #attributi per tutti i membri
        self.nome = nome
        self.eta = eta
    
    #metodo comune a tutte le classi
    def descrizione(self):
        print(f"Mi chiamo {self.nome} e ho {self.eta} anni.")
    
    