from unita_militare import UnitaMilitare

class Fanteria(UnitaMilitare):
    #metodo esclusivo di questa classe
    def costruisci_trincea(self):
        print(f"{self.nome} (Fanteria): Costruisce difese temporanee.")