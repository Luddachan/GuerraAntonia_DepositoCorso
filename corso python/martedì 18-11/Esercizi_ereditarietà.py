# -------------------------------
# Classe padre: Animale
# -------------------------------


class Animale:
    #attributi di tutti gli animali
    def __init__(self, nome, eta):
        #attributi comuni a tutti gli animali
        self.nome = nome 
        self.eta=eta 
    #metodo fai_suono
    def fai_suono(self):
        print(f"{self.nome} fa questo suono generico.")
        

# -------------------------------
# Classe derivata: Leone
# -------------------------------
# La classe Leone eredita da Animale        
class Leone(Animale):
    
    def fai_suono(self):
        #riscirvo il metodo (override) della classe base
        print(f"{self.nome} ruggisce.")
    
    #funzione per la caccia
    def caccia(self):
        #metodo specifico per il leone
        print(f"{self.nome} caccia nel suo habitat.")
    #pass

#classe derivata Giraffa
class Giraffa(Animale):
    def fai_suono(self):
        #override
        print(f"{self.nome} non so che suono fa")
        
    def erbivoro(self):
        print(f"{self.nome} mangia foglie quindi è erbivoro.")
    
    #pass 

class Pinguino(Animale):
    def fai_suono(self):
        #override
        print(f"{self.nome} fa un garrito simile ai gabbiani.")
    
    def nuota(self):
        #metodo specifico
        print(f"{self.nome} sta nuotando tra i ghiacciai.")
    
    #pass

#casi di test
leone = Leone("Simba", 3)
giraffa = Giraffa ("Pippo", 6)
pinguino = Pinguino ("Pingu", 4)

#metodi del leone
leone.caccia()
leone.fai_suono()

#metodi giraffa
giraffa.fai_suono()
giraffa.erbivoro()

#metodi pinguino
pinguino.nuota()
pinguino.fai_suono()