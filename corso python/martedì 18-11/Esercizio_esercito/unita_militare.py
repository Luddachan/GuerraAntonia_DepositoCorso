#Classe Base
class UnitaMilitare:
    def __init__(self, nome, num_soldati):
        self.nome = nome
        self.num_soldati = num_soldati
    
    # metodi generici condivisi da tutti
    def muovi(self):
        print (f"{self.nome} si sta muovendo.")
        #pass 
    
    def attacca(self):
        print(f"{self.nome} sta attaccando.")
        pass 
    
    def ritira(self):
        print(f"{self.nome} si sta ritirando!")
        pass