# Esempio di incapsulamento in Python

class Computer:

	def __init__(self):
		self.__processore = "Intel i5"

	def get_processore(self):
		return self.__processore

pc = Computer()
# Accesso all'attributo privato tramite metodo getter
print(pc.get_processore())
# Modifica dell'attributo privato tramite metodo setter
pc.set_processore("AMD Ryzen 5")
print(pc.get_processore())

#esempio variabile globale
numero = 10  # Variabile globale

def funzione_esterna():
    numero = 5  # Variabile locale
    print("Numero dentro funzione_esterna (locale):", numero)
    
    def funzione_interna():
    #utilizzo di nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero  # Riferimento alla variabile locale di funzione_esterna
        numero = 3
        print("Numero dentro funzione_interna (modificato):", numero)
    
    funzione_interna()
    
print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)

#ESEMPIO METODO PRIVATO

class MiaClasse:
    def __init__(self):
        self.__variabile_privata = "Sono privata"
    
    def __metodo_privato(self):
        return "Questo è un metodo privato"
    
obj = MiaClasse()
# Accesso alla variabile privata tramite name mangling
# print (obj.__variabile_privata)  # Questo genererebbe un errore
# L'accesso corretto (che va evitato) sarebbe:
print(obj._MiaClasse__variabile_privata) #funziona ma non è buona prassi

#altro esempio protetti 

class ClasseBase:
    def __init__(self):
        self._variabile_protetta = "Sono protetta"
    
class Sottoclasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print(self._variabile_protetta)  # Accesso consentito alle variabili protette
        
obj = Sottoclasse()