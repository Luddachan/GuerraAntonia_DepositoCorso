#classe eredita da Posto

from posto import Posto

class PostoVIP(Posto):
    def __init__(self, numero: int, fila: str, servizio_extra):
        # richiama il costruttore della classe base
        super().__init__(numero, fila)
        # attributo specifico per PostoVIP
        self.__servizio_extra = servizio_extra
    
    # metodo per ottenere il servizio extra
    def get_servizio_extra(self):
        return self.__servizio_extra
    
    # metodo per prenotare il posto VIP con servizi extra
    def prenota(self):
        # richiama il metodo prenota della classe base
        super().prenota()
        # conrolla se il posto è occupato per attivare i servizi extra
        if self.is_occupato():
            #.join serve per unire gli elementi della lista in una stringa separata da virgole
            print(f"Servizi VIP attivati: {', '.join(self.servizi_extra)}")
    