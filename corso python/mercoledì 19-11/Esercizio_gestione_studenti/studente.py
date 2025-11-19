#classe studente che eredita da persona
from persona import Persona

class Studente(Persona):
    def __init__(self, nome: str, eta: int, voti: list[int]):
        # chiamata al costruttore della classe padre
        # inizializzazione degli attributi specifici della classe studente
        super().__init__(nome, eta)
        self.voti = voti
    # metodo per calcolare la media dei voti    
    def __calcola_media(self):
        # controllo se la lista dei voti è vuota
        if not self.voti:
            return 0
        # calcolo della media aritmetica dei voti
        return sum(self.voti) / len(self.voti)
    
    def presentazione(self):
        # ovride del metodo presentazione della classe padre
        # riscrive il metodo della classe padre
        presentazione_base = super().presentazione()
        # calcolo della media dei voti
        media_voti = self.__calcola_media()
        # restituzione della presentazione completa
        # 2f per formattare la media con 2 cifre decimali
        return f"{presentazione_base} Sono uno studente e la mia media dei voti è {media_voti:.2f}."
    
    