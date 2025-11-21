#classe badge che non prende da nessuno

class Badge:
    def __init__(self, id_badge: str):
        self._id_badge = id_badge
        #settiamo lo stato del badge come attivo di default
        self._attivo = True
        
    #funzione per disabilitare il badge
    def disabilita(self):
        self._attivo = False
        
    #funzione per abilitare il badge
    def abilita(self):
        self._attivo = True
    # funzione per controllare se il badge è attivo
    def is_attivo(self):
        return self._attivo
    # funzione per mostrare le informazioni del badge  
    def mostra_informazioni(self):
        print(f"Badge Codice: {self._id_badge}")