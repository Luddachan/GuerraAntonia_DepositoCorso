#classe turno mostra informazioni sul turno di lavoro

class Turno:
    def __init__(self, giorno: str, orario_inizio: str, orario_fine: str):
        self._giorno = giorno
        self._orario_inizio = orario_inizio
        self._orario_fine = orario_fine
        
    def mostra_informazioni_turno(self):
        print(f"Turno del {self._giorno}: dalle {self._orario_inizio} alle {self._orario_fine}")