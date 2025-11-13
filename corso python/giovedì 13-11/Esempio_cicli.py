#ciclo matematico

conteggio = 0
while conteggio < 5:
	print (conteggio)
	conteggio +=1
 
#ciclo booleano

controllo = True

while controllo:
    print (controllo)
    controllo = False
    

controllor = True
# ciclo booleano
while controllor:
    print (controllor)
    scelta = input ("vuoi continuare?")
    if scelta.lower() == "no":
        controllor = False
    else:
        print("Stai continuando")
        
#ciclo for

numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)
    
#esempio range

for i in range (5):
	print(i)
#il 5 è lo stop

#range con start e stop
for i in range (2, 8):
	print(i)
 #2 è lo start
 
for i in range (1, 10, 2):
	print(i)
