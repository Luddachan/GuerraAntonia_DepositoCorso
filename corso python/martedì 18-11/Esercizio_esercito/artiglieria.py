from unita_militare import UnitaMilitare

#Classe figlia di UnitaMilitare
class Artiglieria(UnitaMilitare):
    #metodo esclusivo di questa classe
    def calibra_artiglieria(self):
        print(f"{self.nome} (Artiglieria): Calibra i pezzi per la precisione.")