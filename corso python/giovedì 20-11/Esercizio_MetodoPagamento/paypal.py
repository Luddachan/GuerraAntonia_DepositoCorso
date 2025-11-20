from metodo_pagamento import MetodoPagamento

class Paypal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        #implementazione specifica per il pagamento con PayPal
        print(f"Pagamento di {importo}€ effettuato con PayPal.")

  