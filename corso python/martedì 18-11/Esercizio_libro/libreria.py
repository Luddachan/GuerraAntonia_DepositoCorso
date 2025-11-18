from libro import Libro

class Libreria():
    def __init__(self):
        #contiene la lista libri
        self.catalogo = []
        #pass
    
    def aggiungi_libro(self, libro):
        #aggiungi un libro con metodo append
        self.catalogo.append(libro)
        #pass
    
    def rimuovi_libro(self, isbn):
        #rimuove il libro tramire isbn
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print(f"Libro con ISBN {isbn} rimosso.")
                return
        print(f"Nessun libro trovato con ISBN {isbn}.")
        #pass
    
    def cerca_per_titolo(self, titolo):
        #lista di libri che hanno quel titolo
        risultati = []
        for libro in self.catagolo:
            if libro.titolo == titolo:
                risultati.append(titolo)
        return risultati
        #pass
    
    def mosta_catalogo(self):
        #Se la lista è vuota, allora not self.catalogo è True.
        if not self.catalogo:
            print("Il catalogo è vuoto")
        #se la lista non è vuota
        else:
            print("Catalogo libri:")
        #scorre ogni elemento della lista catalogo.
            for libro in self.catalogo:
                print(" -", libro.descrizione())
            
    
    
    
    