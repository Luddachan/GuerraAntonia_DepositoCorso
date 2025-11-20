#classe base MetodoPagamento

class MetodoPagamento:
    
    def _init_(self, metodo):
        self.metodo = metodo
    
    #metodo che ogni sottoclasse deve implementare
    def effettua_pagamento(self, importo):
        self.importo = importo
        