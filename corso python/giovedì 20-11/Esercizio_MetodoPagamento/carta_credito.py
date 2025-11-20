#classe derivata CartaDiCredito da MetodoPagamento

from metodo_pagamento import MetodoPagamento

class Cartacredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        #implementazione specifica per il pagamento con carta di credito
        print(f"Pagamento di {importo}€ effettuato con Carta di Credito.")

   