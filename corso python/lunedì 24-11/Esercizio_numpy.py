import numpy as np

# 1. Creo un array di numeri interi da 10 a 49
array = np.arange(10, 50)
print("Array creato:", array)

#verifico il tipo di dato dell'array

print("Il tipo di dato dell'array è: ", array.dtype)

#converto l'array in un array di float in due modi
arr = np.array(array, dtype='float64')
print (arr.dtype) 

#astype serve per convertire il tipo di dato di un array
array_float = array.astype(float)
print("Array convertito in float:", array_float)

#stampa la forma dell'array
print ("La forma dell'array è", array.shape)