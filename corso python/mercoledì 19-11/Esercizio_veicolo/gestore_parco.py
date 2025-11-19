# classe GestoreParcoVeicolo

class GestoreParcoVeicoli:
    def __init__(self):
        self.__parco_veicoli =[] #lista vuota di veicoli nel parco
    # metodo per aggiungere e rimuovere veicoli dal parco    
    def aggiungi_veicolo(self, veicolo):
        self.__parco_veicoli.append(veicolo)
    
    # metodo per rimuovere i veicoli
    def rimuovi_veicolo(self, veicolo):
    
        if veicolo in self.__parco_veicoli:
            self.__parco_veicoli.remove(veicolo)
        
    def lista_veicoli(self):
        if not self.lista_veicoli:
            print ("Auto non trovata nel parco.")
        else:
            print("Auto trovata!")
        
        
        