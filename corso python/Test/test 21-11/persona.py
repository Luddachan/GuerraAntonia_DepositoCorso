#Classe base persona

class Persona():
    def __init__(self, nome: str, cognome: str, eta: int):
        #incapsulamento attributi sono privati
        self._cognome = cognome
        self._nome = nome
        self._eta = eta 
        
    def presenta_te_stesso(self):
        print(f"Ciao, mi chiamo {self._nome} {self._cognome} e ho {self._eta} anni.")
        
    
        
        
        