#----------------------------
#       esercizio 2
#----------------------------

#chiede all'utente l'età
eta = input ("Scrivi la tua età: ")

#fa un controllo sull'età 
if eta < 18:
    print ("Mi dispiace non puoi vedere questo film!")
else:
    print("Puoi vedere questo film!")
    


#----------------------------
#       esercizio 2
#----------------------------

#chiede l'inserimento di due numeri e l'operazione
x = int (input("Inserisci il primo numero: "))
y = int (input("Inserisci il secondo numero: "))

operazione = input ("Inserisci l'operazione (+, -, *, /): ")

#controllo per verificare l'operazione

if operazione == '+':
    risultato = x + y
    print ("Risultato: ", risultato)
elif operazione == '-':
    risultato = x-y
    print ("Risultato: ", risultato)
elif operazione == '*':
    risultato = x*y
    print ("Risultato: ", risultato)
elif operazione == '/':
    risultato = x/y
    print ("Risultato: ", risultato)
else:
    print ("Operazione non consentita!")
    
    


    
    
    

