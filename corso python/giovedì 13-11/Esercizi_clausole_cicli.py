# Inizio di un ciclo infinito
while True:
    # Chiedo all'utente se vuole inserire un numero (n) o una parola (p)
    # .lower() serve per trasformare la risposta in minuscolo
    tipo = input("Vuoi inserire un numero o una parola? (n/p): ").lower()

    # Se l'utente sceglie di inserire un numero
    if tipo == "n":
        # Chiedo il numero all'utente e lo trasformo in intero (int)
        numero = int(input("Inserisci un numero: "))

        # Uso l'operatore % per controllare se il numero è pari o dispari
        # Se il resto è 0 → il numero è pari, altrimenti è dispari
        if numero % 2 == 0:
            print("Il numero è pari.")
        else:
            print("Il numero è dispari.")

    # Se l'utente sceglie di inserire una parola
    elif tipo == "p":
        # Chiedo la parola e la salvo nella variabile "parola"
        parola = input("Inserisci una parola: ")

        # Stampo la parola inserita
        print("Hai scritto:", parola)

    # Se l'utente scrive qualcosa di diverso da 'n' o 'p'
    else:
        print("Scelta non valida.")

    # Alla fine di ogni ciclo, chiedo se vuole continuare
    
    # il ciclo si interrompe con break
    ripeti = input("Vuoi continuare? (s/n): ").lower()
    if ripeti != "s":
        print("Programma terminato.")
        break  # Esce dal ciclo e chiude il programma
        
        


