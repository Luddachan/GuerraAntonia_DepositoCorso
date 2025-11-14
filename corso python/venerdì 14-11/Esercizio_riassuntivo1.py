#----------------------------
# Immagina di avere una collezione di fumetti. 
# Ognuno ha un titolo e un numero di copie. 
# Noi vogliamo analizzarla e modificarla.
#----------------------------

#----------------------------------
# 1- lista fumetti gestita da tuple
#----------------------------------

# ogni fumetto è gestito da tuple così da non poter essere modificati (nome, num copie)
fumetti = [
    ("Dragon Ball", 5)
    ("One Piece", 1)
    ("Topolino", 8)
    ("Batman", 2)
    ("Superam", 15)
    ("I diari della speziale", 7)
    ("Slam Dunk", 10)
    
]

# lista vuota dove metteremo i titoli

fumetti_3opiu = []      
# cicliamo su ogni tupla della lista
for titolo, copie in fumetti:
    # controlliamo la condizione
    if copie >= 3: 
        # aggiungiamo solo il titolo     
        fumetti_3opiu.append(titolo)
print("Fumetti con almeno 3 copie: ", fumetti)  

#vogliamo calcolare il totale delle copie

for titolo, copie in fumetti:
    totale_copie += copie
print ("Il totale delle copie disponibili è:", totale_copie)

#----------------------------------------
#con range possiamo aggiungere nuovi fumetti
#----------------------------------------

#for i in range (1, 5):
    #nuovo_titolo = input(f"Fumetto {i}")
    #fumetti.append(nuovo_titolo, 1)
    

#------------------------
#cerchiamo un fumetto inserito dall'utente
#------------------------
while True:
    ricerca = input ("Inserisci un fumetto, altrimenti scrivi esci: ")
    #uscita per l'utente
    if ricerca.lower() == "esci":
        print("Arrivederci!")
        break #interrompe il programma altrimenti il while andrebbe all'infinito
    
    #settiamo una condizione a falso perchè il fumetto non è stato ancora trovato
    trovato = False 

    #ricerca del fumetto con il for
    for titolo, copie in fumetti:
        #lower perchè così ignora se l'utente da lettere maiuscole o minuscole
        if titolo.lower() == ricerca.lower():
            print(f"{titolo} presente con {copie} copie nella collezione.")
            trovato = True #settiamo a true perchè qui abbiamo delle condizioni
            break #ferma il ciclo

#quando non troviamo il fumetto
if not trovato:
    print("Fumetto non presente")
    
#----------------------
# fumetti con meno di due copie
#----------------------

#creiamo la lista vuota di appoggio
fumetti_pochi = []

for titolo, copie in fumetti:
    if copie < 2:
        fumetti_pochi.append(titolo)

print ("Fumetti con meno di 2 copie: ", fumetti_pochi)