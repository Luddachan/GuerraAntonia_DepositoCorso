from elettrodomestico import Elettrodomestico

class Lavatrice(Elettrodomestico):
    def __init__ (self, marca: str, modello: str, anno_acquisto: int, guasto: str, capacita_kg: float, giri_centrifuga: int):
        #richiamo il costruttore della classe base Elettrodomestico
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        # attributi specifici della lavatrice
        #self.set_ per incapsulamento
        self.set_giri_centrifuga = giri_centrifuga  # giri per minuto
        self.set_capacita_kg = capacita_kg  # capacità in kg
        
    # getter
    
    def get_capacita_kg(self):
        # ritorna la capacità in kg della lavatrice
        return self._capacita_kg
    
    def get_giri_centrifuga(self):
        # ritorna i giri per minuto della lavatrice
        return self._giri_centrifuga
    
    # setter
    
    def set_capacita_kg(self, capacita_kg: float):
        #imposta la capacità in kg della lavatrice
        if capacita_kg <= 0:
            print("Errore: La capacità in kg deve essere un valore positivo.")
        self._capacita_kg = capacita_kg
    
    def set_giri_centrifuga(self, giri_centrifuga: int):
        #imposta i giri per minuto della lavatrice
        if giri_centrifuga <= 0:
            print("Errore: I giri per minuto devono essere un valore positivo.")
        # assegnazione del valore
        self._giri_centrifuga = giri_centrifuga
    
    # override del metodo della classe base
    def stima_costo_base(self):
        
        #La lavatrice ha un costo che cresce con la capacità e con i giri.
        
        base = 100  # costo base
        # calcolo del costo extra in base a capacità e giri della centrifuga
        extra = (self._capacita_kg * 10) + (self._giri_centrifuga / 100)
        # ritorna il costo totale stimato
        return base + extra
        

class Frigorifero(Elettrodomestico):
    def __init__ (self, marca: str, modello: str, anno_acquisto: int, guasto: str, litri: float, ha_freezer: bool):
        #richiamo il costruttore della classe base Elettrodomestico
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        # attributi specifici del frigorifero
        self.set_litri = litri  # capacità in litri
        self.set_ha_freezer = ha_freezer # presenza del freezer (True/False)
        
    # getter
    def get_litri(self):
        # ritorna la capacità in litri del frigorifero
        return self._litri
    
    def get_ha_freezer(self):
        # ritorna se il frigorifero ha il freezer
        return self._ha_freezer
    
    #setter
    
    def set_litri(self, litri: float):
        #imposta la capacità in litri del frigorifero
        if litri <= 0:
            print("Errore: La capacità in litri deve essere un valore positivo.")
        self._litri = litri
        
    def set_ha_freezer(self, ha_freezer: bool):
        #imposta la presenza del freezer
        #isinstance per controllare che il tipo di dato sia corretto
        if not isinstance(ha_freezer, bool):
            print("Errore: Il valore deve essere True o False.")
        self._ha_freezer = ha_freezer
        
    # override del metodo della classe base
    def stima_costo_base(self):
        #Il frigorifero ha un costo che cresce con i litri e se ha il freezer.
        
        base = 120  # costo base
        # calcolo del costo extra in base ai litri e alla presenza del freezer
        #moltiplico i litri per 5 per ottenere il costo extra
        extra = (self._litri * 5)
        #controllo se ha il freezer
        if self._ha_freezer:
            extra += 50  # costo extra per il freezer
        # ritorna il costo totale stimato
        return base + extra
    
    
class Forno(Elettrodomestico):
    def __init__ (self, marca: str, modello: str, anno_acquisto: int, guasto: str, tipo_alimentazione: str, ha_ventilato: bool):
        #richiamo il costruttore della classe base Elettrodomestico
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        # attributi specifici del forno
        self.set_tipo_alimentazione = tipo_alimentazione  # tipo di alimentazione "elettrico", "gas"
        self.set_ha_ventilato = ha_ventilato  # presenza del ventilato (True/False)
        
    # getter
    def get_tipo_alimentazione(self):
        # ritorna il tipo di alimentazione del forno
        return self._tipo_alimentazione
    
    def get_ha_ventilato(self):
        # ritorna se il forno ha il ventilato
        return self._ha_ventilato  
    
    # setter
    
    def set_tipo_alimentazione(self, tipo_alimentazione: str):
        #imposta il tipo di alimentazione del forno
        # controllo che il tipo di alimentazione sia valido
        #lista di tipi validi
        if tipo_alimentazione not in ["elettrico", "gas"]:
            print("Errore: Il tipo di alimentazione deve essere 'elettrico' o 'gas'.")
        self._tipo_alimentazione = tipo_alimentazione
        
    def set_ha_ventilato(self, ha_ventilato: bool):
        #imposta la presenza del ventilato
        #isinstance per controllare che il tipo di dato sia corretto
        if not isinstance(ha_ventilato, bool):
            print("Errore: Il valore deve essere True o False.")
        self._ha_ventilato = ha_ventilato
        
    # override del metodo della classe base
    def stima_costo_base(self):
        #Il forno ha un costo che dipende dal tipo di alimentazione e se ha il ventilato.
        # costo base
        base = 20  
        # calcolo del costo extra in base al tipo di alimentazione e alla presenza del ventilato
        if self.__tipo_alimentazione == "elettrico":
            base += 10
        # controllo se ha il ventilato
        if self.__ha_ventilato:
            base += 5  
        return base