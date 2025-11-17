#==============================================================
# #Creare una classe ristorante che permetta di creare alcune funzionalità di base
#==============================================================

#classe ristorante
class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.cucina = tipo_cucina
        self.aperto = False  # Ristorante chiuso di default
        self.menu = []  # Lista vuota per il menu
    
    #funzione per descrivere il ristorante
    def descrivi_ristorante(self):
        print(f"{self.nome} - Cucina:{self.cucina}")
    
    #funzione per stato del ristorante
    def stato_ristorante(self):
        #if else per verificare se è aperto o chiuso
        if self.aperto:
            print(f"{self.nome} è aperto!")
        else:
            print(f"{self.nome} è chiuso!")
    
    #funzione per ristorante aperto  
    def apri_ristorante(self):
        self.aperto = True
        print(f"{self.nome} è ora aperto.")
    #funzioe per ristorante chiuso    
    def chiudi_ristorante(self):
        #self.aperto diventa falso
        self.aperto = False
        print(f"{self.nome} è ora chiuso.")
    
    #funzione per aggiungere piatti al menu
    def aggiungi_piatto(self, piatto, prezzo):
        #self.menu è la lista vuota
        #append aggiunge un elemento alla lista
        self.menu.append((piatto, prezzo))
        print(f"{piatto} è stato aggiunto al menu.")

""" #funzione per togliere piatti dal menu forse    
    def togli_dal_menu(self, piatto):
        #self.menu è la lista vuota
        #for scorre gli elementi del menu
        for elemento in self.menu:
            #elemento[0] è il piatto nella tupla (piatto, prezzo)
            if elemento[0] ==piatto:
                #remove rimuove l'elemento dalla lista
                self.menu.remove(elemento)
                print(f"{piatto} è stato rimosso dal menu.")
                #return per uscire dalla funzione
                return
        #se il piatto non è trovato
        print(f"{piatto} non trovato nel menu.") 
    
    #funzione per visualizzare il menu
    def stampa_menu(self):
        #print per il menu
        print(f"menu di {self.nome}:")
        
        #controllo se il menu è vuoto
        if not self.menu:
            print("Il menu è vuoto.")
            return
        print("Menù ristorante:")
        
        #for per scorrere i piatti nel menu 
        for piatto, prezzo in self.menu:
            print(f"-Piatto{piatto}: €{prezzo:}") """
    
    