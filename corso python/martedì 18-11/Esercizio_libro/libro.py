class Libro ():
    #insieriamo il numero di parametri
    def __init__(self, nome, autore, isbn):
        self.nome = nome 
        self.autore = autore
        self.isbn = isbn
    
    # Restituisce una descrizione completa del libro usando tutti e tre gli attributi.
        
    def descrizione(self): 
        return (f"Titolo: {self.nome} Autore: {self.autore} ISBN: {self.isbn}")
    
