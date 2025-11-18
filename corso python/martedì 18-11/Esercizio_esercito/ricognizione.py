from unita_militare import UnitaMilitare

class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"{self.nome} (Ricognizione): Conduce missione di sorveglianza.")
