import random

def indovina_num():
    #genera num casuale da 1 a 100
    num_segreto = random.randint(1, 100)
    
    #ciclo infinito
    while True:
        tentativo =input("inserisci il numero: ")
        
        if tentativo == "esci":
            print("Hai scelto di uscire. Il numero da indovinare era: ", num_segreto)
            break
        
        
        tentativo = int(tentativo)
        if tentativo == num_segreto:
            print("Hai indovinato!", num_segreto)
            break
        elif tentativo < num_segreto:
            print("Il numero da indovinare è PIÙ ALTO.")
        else:
            print("Il numero da indovinare è PIÙ BASSO.")

# avvio gioco
indovina_num()


#esercizio 2

def num_fibonacci():
    n =int(input("Inserisci un numero: "))
    # primi due numeri di Fibonacci
    a = 0
    b = 1

    print("Sequenza di Fibonacci fino a", n, ":")

    while a <= n:
        print(a)
        # passo successivo: nuovo numero è somma dei due precedenti
        prossimo = a + b
        a = b
        b = prossimo

# avvio funzione
num_fibonacci()
                

        