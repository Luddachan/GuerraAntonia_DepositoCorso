from veicolo_trasporto import VeicoloTrasporto

class Furgone(VeicoloTrasporto):
    """
    Sottoclasse per i furgoni.
    Costo manutenzione:
      - elettrico: 200 €
      - diesel: 150 €
    """
    # funzione di inizializzazione della classe
    def __init__(self, targa: str, peso_massimo: int, alimentazione: str):
        #super richama il costruttore della classe base
        super().__init__(targa, peso_massimo)
        self.alimentazione = alimentazione.lower()
    # funzione che calcola il costo della manutenzione
    def costo_manutenzione(self) -> float:
        return 200 if self.alimentazione == "elettrico" else 150
