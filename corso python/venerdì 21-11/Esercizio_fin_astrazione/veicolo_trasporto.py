from abc import ABC, abstractmethod

class VeicoloTrasporto(ABC):
    """
    Classe astratta che rappresenta un veicolo generico per il trasporto merci.
    """
    def __init__(self, targa: str, peso_massimo: int):
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = 0

    def carica(self, peso: int):
        """Aggiunge peso al carico se non supera la capacità."""
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            print(f"[OK] Caricati {peso} kg sul veicolo {self._targa}.")
        else:
            print(f"[ERRORE] Peso eccede la capacità! ({self._peso_massimo} kg)")

    def scarica(self):
        """Svuota completamente il carico."""
        self._carico_attuale = 0
        print(f"[OK] Il veicolo {self._targa} è stato scaricato.")

    @abstractmethod
    def costo_manutenzione(self) -> float:
        """Metodo astratto da implementare nelle sottoclassi."""
        pass
    # Rappresentazione testuale del veicolo
    def __str__(self):
        return f"{self.__class__.__name__} - Targa: {self._targa}"
