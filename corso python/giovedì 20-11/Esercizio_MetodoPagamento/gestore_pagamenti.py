# classe GestorePagamenti che utilizza il metodo di pagamento passato come parametro
class GestorePagamenti:
    def esegui_pagamento(self, metodo_pagamento, importo):
        metodo_pagamento.effettua_pagamento(importo)