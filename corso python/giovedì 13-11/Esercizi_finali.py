#----------------------
#      esercizio1
#----------------------


#inizializziamo una variabile per tenere la somma
somma = 0

#ciclo infinito 
while True:
    numero = int(input("Inserisci un numero (0 per terminare)"))
    
    #se l'utente inserisce 0 allora esce dal programma
    if numero == 0:
        break
    
    #altrimenti aggiungiamo il numero alla somma
    somma += numero
    
#stampiamo la somma quando il ciclo finisce
print ("La somma dei numeri inseriti è: ", somma)


#----------------------
#      esercizio2
#----------------------

#chiedo all'utente la parola
parola = input("Inserisci una parola: ")

#scorriamo ogni lettera della parola
for lettera in parola:
    #stampiamo ogni lettera
    print(lettera)
    