#creazione classe
class Automobile:
    #attributo della classe
	numero_di_ruote = 4
    #metodo costruttore
	def __init__(self, marca, modello):
        #attributi di istanza
		self.marca = marca
		self.modello = modello
	#metodo di istanza
    def stampa_info(self):
	    print("l'automobile è una", self.marca, self.modello)
    def __str__(self):
        return f"Automobile(nome ={self.nome}, eta={self.eta})"
 
 
#self è il nome dell'oggetto
# crea un oggetto di automobile
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info() #stampa l'automobile è una fiat 500
auto2.stampa_info() #stampa l'uatomobile è una bmw x3

