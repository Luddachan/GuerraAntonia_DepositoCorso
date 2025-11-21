
from veicolo_trasporto import VeicoloTrasporto

class Motocarro(VeicoloTrasporto):
    """
    Sottoclasse per i motocarri.
    Costo manutenzione:
      - 50 € per ogni anno di servizio
    
    # funzione di inizializzazione della classe"""
    def __init__(self, targa: str, peso_massimo: int, anni_servizio: int):
        super().__init__(targa, peso_massimo)
        self.anni_servizio = anni_servizio

    # funzione che calcola il costo della manutenzione
    def costo_manutenzione(self) -> float:
        return 50 * self.anni_servizio
