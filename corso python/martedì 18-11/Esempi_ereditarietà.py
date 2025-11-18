#Classe Base

class Animale:
    def __init__(self, nome):
        self.nome = nome
    
    def parla(self):
        print(f"{self.nome} fa suono generico")

#classe derivata eredita da animale

class Cane(Animale):
    def parla(self):
        print(f"{self.nome} abbaia!")

animale_generico = Animale("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla() #output: animalegenerico fa suono generico
cane.parla() #output: fido abbaia

#Multiereditarietà

class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    def mostra_informazioni(self):
        print("Veicolo marca {self.marc}, modello {self.modello}")
        
class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
        
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: { ', '.join(self.dotazioni)}")
        
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)
        #alternatica a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli =cavalli
        
    def mostra_dotazioni(self):
        super().mostra_informazioni()
        # Chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        #possiamo chiamare i metodi di entrambe le superclassi
        