#chiede di inserire un numero 

n = int(input("Inserisci un numero itero positivo: "))

#esercizio1
while n<=0:
    print ("No! Il numero deve essere positivo.")
    
    #richiede all'utente di inserire il numero
    n= int(input("Inserisci un numero itero positivo: "))
    
#ciclo termina quando l'utente ha inserito un numero maggiore di 0

print("Bravo! Hai inserito un numero potivo:", n)

#inizializiamo una variabile
somma_npari =0

#esercizio2
#andiamo da 1 fino a n incluso
for i in range (1, n+1):
    if i % 2 == 0:
        somma_npari += i #aggiungiamo il numero pari alla somma

#stampiamo il numero della somma
print(f"La somma dei numeri da 1 a {n} è: {somma_npari}")

#esercizio3
print ("i numeri dispari sono: ")

#ciclo for per i dispari
for i in range (1, n+1):
    #numeri dispari
    if i % 2 !=0:
        print(i, end =" ")