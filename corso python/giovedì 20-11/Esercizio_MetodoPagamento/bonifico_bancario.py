from metodo_pagamento import MetodoPagamento

class Bonificobancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        #implementazione specifica per il pagamento con bonifico bancario
        print(f"Pagamento di {importo}€ effettuato con bonifico.")

