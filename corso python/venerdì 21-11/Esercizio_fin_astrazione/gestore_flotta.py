
class GestoreFlotta:
    """
    Gestisce un elenco di veicoli.
    """
    def __init__(self):
        self.veicoli = []
    # funzione per aggiungere un veicolo alla flotta
    def aggiungi_veicolo(self, veicolo):
        self.veicoli.append(veicolo)
    # funzione per rimuovere un veicolo dalla flotta in base alla targa
    def rimuovi_veicolo(self, targa):
        self.veicoli = [v for v in self.veicoli if v._targa != targa]

    # funzione che calcola il costo totale della manutenzione
    def costo_totale_manutenzione(self):
        return sum(v.costo_manutenzione() for v in self.veicoli)
    # funzione per stampare i dettagli di tutti i veicoli
    def stampa_veicoli(self):
        for v in self.veicoli:
            print(v)
