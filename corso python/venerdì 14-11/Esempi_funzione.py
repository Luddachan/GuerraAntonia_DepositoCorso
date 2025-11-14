def saluta(nome):
    print ("Ciao,", nome)
    print ("BEnvenuto nel nostro programma!")
    saluta ("Alice") #output Ciao, alice

def somma(a,b):
    risultato = a+b 
    print("La somma è ", risultato)   
    somma(5,3)

def quadrato(numero):
 	return numero * numero
risultato = quadrato(4)
print(risultato)