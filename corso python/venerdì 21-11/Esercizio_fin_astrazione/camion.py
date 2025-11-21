# camion.py
from veicolo_trasporto import VeicoloTrasporto

class Camion(VeicoloTrasporto):
    #Sottoclasse per i camion.
    #Costo manutenzione = 100 € per asse + 1 € per kg di carico massimo.
    def __init__(self, targa: str, peso_massimo: int, numero_assi: int):
        super().__init__(targa, peso_massimo)
        self.numero_assi = numero_assi
    
    #->float vuol dire che il metodo ritorna un valore di tipo float
    def costo_manutenzione(self) -> float:
        # Calcola il costo della manutenzione del camion
        return 100 * self.numero_assi + 1 * self._peso_massimo
