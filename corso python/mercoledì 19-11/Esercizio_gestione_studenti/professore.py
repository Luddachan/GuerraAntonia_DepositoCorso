from persona import Persona


class Professore(Persona):
    def __init__(self, nome: str, eta: int, materia: str):
        # chiamata al costruttore della classe padre
        super().__init__(nome, eta)
        self.materia = materia 
        
    def presentazione(self):
        # ovride del metodo presentazione della classe padre
        # riscrive il metodo della classe padre
        presentazione_base = super().presentazione()
        # presentazione completa
        return(f"{presentazione_base} Sono un professore e insegno {self.materia}")