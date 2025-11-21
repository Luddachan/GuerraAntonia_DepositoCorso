#classe che eredita da persona

from persona import Persona

class dipendente(Persona):
    def __init__(self, nome: str, conognome: str, eta: int, ruolo: str, stipendio: float):
        #chiamata al costruttore della superclasse
        super().__init__(nome, conognome, eta)
        self._badge = None #lo settiamo a none inizialmente
        self._ruolo = ruolo
        self._stipendio = stipendio
        
    def presenta_te_stesso(self):
        #override del metodo della superclasse
        super().presenta_te_stesso()
        print(f"Sono un {self._ruolo} e guadagno {self._stipendio} euro all'anno.")
        
    def assegna_badge(self, badge: str):
        self._badge = badge
    # metodi getter per ruolo e stipendio
    def get_ruolo(self):
        return self._ruolo
    
    def get_stipendio(self):
        return self._stipendio
    
    # metodi setter per ruolo e stipendio
    def set_ruolo(self, nuovo_ruolo: str):
        self._ruolo = nuovo_ruolo
    
    def set_stipendio(self, nuovo_stipendio: float):
        #controlla che lo stipendio non sia negativo
        if nuovo_stipendio < 0:
            print("Errore: lo stipendio non può essere negativo.")
        self._stipendio = nuovo_stipendio
    
    
    # polimorfismo con un metodo che ha lo stesso nome in classi diverse
    def descrizione_accesso(self):
        return f"Il dipendente {self._nome} ha accesso alle aree riservate con il badge {self._badge} e stipendio di {self._stipendio}€"
    
    
    
        