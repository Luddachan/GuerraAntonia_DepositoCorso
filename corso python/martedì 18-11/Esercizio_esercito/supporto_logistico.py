from unita_militare import UnitaMilitare

class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self):
        print(f"{self.nome} (Logistica): Gestisce rifornimento e manutenzione.")