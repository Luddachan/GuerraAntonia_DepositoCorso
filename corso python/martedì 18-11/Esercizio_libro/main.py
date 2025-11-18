from libro import Libro 
from libreria import Libreria

if __name__ == "__main__":   
     
    #creiamo una nuova libreria
    lib = Libreria()
    
    # Creo alcuni libri
    libro1 = Libro("1984", "George Orwell", "111")
    libro2 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "222")
    libro3 = Libro("1984", "George Orwell", "333")
    
     # Aggiungiamo i libri alla libreria
    lib.aggiungi_libro(libro1)
    lib.aggiungi_libro(libro2)
    lib.aggiungi_libro(libro3)
    
    #mostra catalogo libri
    print ("ecco i libri della tua collezione: ")
    lib.mosta_catalogo()
    
    #cerca per titolo
    print ("\nRisultati ricerca per 1984: ")
    risultati = lib.cerca_per_titolo("1984")
    for libro in risultati:
        print (libro.descrizione())
        
     # Rimuovo un libro per ISBN
    lib.rimuovi_libro("222")

    # Catalogo finale
    print("\nDopo la rimozione:")
    lib.mostra_catalogo()
    

    
    