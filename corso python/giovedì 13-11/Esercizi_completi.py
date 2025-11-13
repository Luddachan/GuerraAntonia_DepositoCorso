#------------------
    #esercizio1
#------------------


#chiede all'utente di inserire un numero
numero = int (input("Inserisci un numero: "))

#controlla con la condizione se il numero è pari o dispari (% da il resto)
if numero % 2 == 0:
    print ("Pari!")
else:
    print ("Dispari!")
    


#------------------
    #esercizio2
#------------------
#ciclo infinito
while True: 
    n = int(input("Inserisci un numero: "))

    if n >= 0:
        # Creiamo un range da n a 0 (incluso)
        numeri = range(n, -1, -1)
        i = 0  # indice per scorrere il range

        # ciclo while per stampare ogni elemento del range
        while i < len(numeri):
            print(numeri[i])
            i += 1  # passa al numero successivo
    else:
        print("Numero non valido! Inserisci un numero positivo.")
        

#esercizio 3

numeri_input = input("Inserisci una lista di numeri separati da spazi: ")
    
