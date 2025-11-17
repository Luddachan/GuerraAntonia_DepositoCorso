#definiamo la classe
class Libro:
    # costruttore: inizializza gli attributi
    def __init__(self, titolo, autore, pagine):
        #attributi di istanza
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    # metodo che restituisce una descrizione del libro
    def descrizione(self):
        # usa una f-string per creare la frase richiesta
        return f"Libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."