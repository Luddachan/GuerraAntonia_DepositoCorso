# tipo int
# numeri positivi e negativi 
x = 10
y = -10

print (x,y)

# tipo float
a = 3.14
b = -1.0

#stringhe

#nome ='Alice'
#msg = "Ciao!"

#esempi stringhe
s = "Python"
print(s[0]) #output P
print(s[2]) #output t

#stringhe conatenate

saluto = "Ciao"
nome = "Alice"
messaggio = saluto + " " + nome
print (messaggio) # output:' Ciao Alice '

#esempi metodi delle stringhe

s= "Ciao, mondo!"
print (len(s)) #output 12, ci dice la lunghezza della stringa
print (s.upper()) # CIAO MONDO!, lo mette tutto in minuscolo
print (s.split(',')) #CIAO , MONDO divide le stringhe
print (s.replace('mondo', 'universo')) #sostituisce una parola con una nuova

#esempio carattere
carattere ='A'

#stampare booleani
x = True 
y = False 

#operazioni

x = 5
y = 10
z = 7 
print (x < y and y > z) #tue
print (x < y or z > y) #true
print (not (x < y)) #false

x = 5
y = 10

print(x ==y) #output false
print (x != y) #output true
print (x < y) #output true