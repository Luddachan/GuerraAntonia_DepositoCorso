from abc import ABC, abstractmethod
# ==========================================================
# CLASSE ASTRATTA IMPIEGATO
# ==========================================================
# classi astratte con ABC
# Una classe astratta non può essere istanziata direttamente,
# ma serve come modello per le classi derivate.


class Impiegato(ABC):
    def __init__(self, nome: str, cognome: str, stipendio_base: int):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base
    #metodo astratto deve essere implementato dalle altre sottoclassi    
    @abstractmethod
    def calcola_stipendio(self):
        pass
    
    #stampa le info della persona
    def info_persona(self):
        return f"{self.nome} {self.cognome}"
        

# ==========================================================
# CLASSE DERIVATA: IMPIEGATO FISSO
# ==========================================================
# Lo stipendio è semplicemente quello base, senza modifiche.
class ImpiegatoFisso(Impiegato):

    def calcola_stipendio(self):
        # Nessun bonus: restituisce lo stipendio base
        return self.stipendio_base

# ==========================================================
# CLASSE DERIVATA: IMPIEGATO APROVvIGIONE
# ==========================================================

class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome: str, cognome: str, stipendio_base: int, vendite: float, percentuale_bonus: float):
        #richiama il costruttore della classe base
        super().__init__(nome, cognome, stipendio_base)
        
        self.vendite = vendite
        self.percentuale_bonus = percentuale_bonus
    
    def calcola_stipendio(self):
        # Calcola il bonus sulle vendite
        bonus = self.vendite * self.percentuale_bonus
        # Somma del base + bonus
        return self.stipendio_base + bonus
    
def stampa_stipendi(lista_impiegati):
    #impo singolo impiegato alla volta scorrendo con un ciclo for
    for imp in lista_impiegati:
        print(f"Impiegato: {imp.info()}")
        # Il metodo giusto viene scelto automaticamente
        # grazie al polimorfismo
        print(f"Stipendio mensile: {imp.calcola_stipendio()} €\n")
        
# Impiegato fisso: stipendio invariato
imp1 = ImpiegatoFisso("Mario", "Rossi", 1500)

# Impiegato a provvigione:
# base 1000 + 5% su 5000 € di vendite (250 €)
imp2 = ImpiegatoAProvvigione("Luca", "Bianchi", 1000, vendite=5000, percentuale_bonus=0.05)

# Lista degli impiegati
impiegati = [imp1, imp2]

# Stampa i risultati
stampa_stipendi(impiegati)
        



