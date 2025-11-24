import numpy as np

# array di numeri casuali tra 10 e 50
array = np.random.randint(10, 50, size = 20)
print("Array di numeri casuali tra 10 e 50:", array)

#slicing primi 10 elementi
primi_10 = array[:10]
print("Primi 10 elementi:", primi_10)

#slicing ultimi 5 elementi
# : vanno messi dopo il -5 per indicare 
# che si vogliono gli ultimi 5 elementi
ultimi_5 = array[-5:]
print("Ultimi 5 elementi:", ultimi_5)

#slicing degli elementi dal 5 a 15 escluso
da_5_a_15 = array[5:15]
print("Elementi da 5 a 15 escluso:", da_5_a_15)

#slicing per estrarre ogni terzo elemento
#prende un elemento ogni tre
ogni_terzo = array[::3]
print ("Ogni terzo elemento: ", ogni_terzo)

# modifica tramite slicing: assegna 99 agli elementi da 5 a 10 escluso
array [5:10] = 99
print ("Modifica degli elementi da 5 a 10: ", array)

#stampa

print("\n------- Riepilogo------------")
print("Primi 10:", primi_10)
print("Ultimi 5:", ultimi_5)
print("Indice 5–15:", da_5_a_15)
print("Ogni terzo elemento:", ogni_terzo)








