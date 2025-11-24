import numpy as np

# 1. Creiamo un array di numeri interi da 10 a 49
array = np.arange(10, 50)
print("Array creato:", array)

#verifichiamo il tipo di dato dell'array

print("Il tipo di dato dell'array è: ", array.dtype)

#convertiamo l'array in un array di float
#astype serve per convertire il tipo di dato di un array
array_float = array.astype(float)
print("Array convertito in float:", array_float)

#stampa la forma dell'array
print ("La forma dell'array è", array.shape)