numero = 10
if numero > 0:
    print ("Il numero è positivo")
    
#if - else condizione
numero = -10
if numero > 0:
    print ("Il numero è positivo")
else:
    print ("Blocco Else")
    
#condizione elif

numero = -10
if numero > 0:
    print("Il numero è positivo")
    if numero == 100:
        print ("wow")
elif numero < 0:
    print ("il numero è negativo")
else:
    print ("Il numero è zero")
    

comando = input ("Inserisci un comando: ")

match comando:
    case "start":
        print ("Avvio del programma.")
    case "stop":
        print ("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")
        




