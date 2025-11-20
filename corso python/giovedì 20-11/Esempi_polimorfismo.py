#Esempio overloadinf di metodi in Python

class Stampa:
    def mostra(self, a=None, b=None):
        if a is not None and b is not None:
            print(a+b)
        elif a is not None:
            print(a)
        else:
            print("Niente da mostrare")
            
#esempio duck typing
class Cane:
    def parla(self):
        return "bau bau"
class Gatto:
    def parla(self):
        return "miao miao"

def fai_parlare(animale):
    # non importa di che tipo sia animale,
    print(animale.parla())
cane = Cane()
gatto = Gatto()

fai_parlare(cane)
fai_parlare(gatto)

#duck typing con un ciclo polimorfico

class Cerchio:
    def disegna(self):
        print("Disegno un cerchio")

class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")
        
        
def disegna_figura(figura):
    # anche qui basta che figura abbia il metodo disegna
    figura.disegna()
    
#lista di oggetti di tipo diverso
#figure[0] è un oggetto di tipo Cerchio
#figure[1] è un oggetto di tipo Rettangolo
figure = [Cerchio(), Rettangolo()]

#ciclo polimorfico
#tutti gli oggetti in figure vengono trattati allo stesso modo
for figura in figure:
    disegna_figura(figura)
    
#funzione built-in len() è polimorfica
# lista
print(len([1,2,3]))
# output: 3

#esempio main è una convenzione in Python
if __name__ == "__main__":
    print("main")
else:
    print("import")