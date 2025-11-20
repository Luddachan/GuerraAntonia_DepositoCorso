#classe che non eredita da posto

class Teatro:
    def __init__(self):
        # attributo per memorizzare i posti nel tearo
        self._posti = []
        
    def aggiungi_posto(self, posto):
        # aggiunge un posto alla lista dei posti del teatro
        self._posti.append(posto)
    
    def prenota_posto(self, numero: int, fila: str):
        # cerca il posto specifico per numero e fila
        for posto in self._posti:
            # usa i metodi getter della classe Posto per confrontare numero e fila
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                return
        # se il posto non è trovato
        print(f"Posto {fila}{numero} non trovato nel teatro.")
    
    def stampa_posto_occupato(self):
        # stampa lo stato di tutti i posti nel teatro
        print("Stato dei posti nel teatro:")
        # ciclo attraverso tutti i posti
        for posto in self._posti:
            # usa il metodo is_occupato della classe Posto per controllare lo stato
            if posto.is_occupato():
                # stampa i dettagli del posto occupato con i metodi getter
                print(f"Posto occupato: {posto.get_fila()}{posto.get_numero()}")