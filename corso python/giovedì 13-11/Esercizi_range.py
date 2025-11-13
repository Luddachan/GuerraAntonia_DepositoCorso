#variabile di controllo per il while
ripeti = "si"


while ripeti == "si":
    #chiede all'utente di inserire un numero
    numero_input = input("Inserisci un numero: ")
    #converte in un num intero
    numero = int(numero_input)

    # range parte da numero, arriva a -1 (quindi si ferma a 0), passo -1
    for n in range(numero, -1, -1):
        print(n)

    ripeti = input("Vuoi ripetere? (si/no): ")

print("Programma terminato.")

#esercizio2
pari_trovati = []   # lista dei numeri pari salvati

# il ciclo continua finché non abbiamo 5 numeri pari
while len(pari_trovati) < 5:

    numero_input = input("Inserisci un numero: ")
    numero = int(numero_input)

    # controllo pari
    if numero % 2 == 0:
        print("Il numero è pari.")
        pari_trovati.append(numero)
        print("Numeri pari salvati:", pari_trovati)
    else:
        print("Il numero non è pari.")

print("Hai trovato 5 numeri pari!")
print("Lista finale:", pari_trovati)


