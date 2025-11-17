
#creiamo la classe biblioteca
class Biblioteca:
    def __init__ (self):
        self.libri = [] #lista per contenere i libri
        
    def libri_aggiunti(self, titolo, autore):
        #pass
         libro = Libro (titolo, autore) #crea nuovo libro
         self.libri.append(libro) #ci fa aggiugnere il libro alla biblioteca
    
    def stampa_libro(self):
        #scorre i libri
        for libro in self.libri:
            #stampa la descrizione dei libri
            print (libro.descrizione()) #stampa la descrizione

    
    
#creiamo la classe libro
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def descrizione(self):
        return f"Il libro {self.titolo} è stato scritto da {self.autore}."    