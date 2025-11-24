import numpy as np
# esempio ndarray

#creazione di un array unidimensionale
arr = np.array([1,2,3,4,5])

#creazione di un array bidimensionale
arr2d = np.array([1,2,3],[4,5,6])

# Creazione di un array
arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) # Output: (5,)
print("Dimensioni dell'array:", arr.ndim)# Output: 1
#parentesi implicite
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4

#esempio dtype
arr = np.array([1, 2, 3], dtype='int32')
print (arr.dtype)  # Output: int32

#esempio shape
arr = np.array([[1, 2, 3], [4, 5, 6]])
print (arr.shape)  # Output: (2, 3)

#esempio arange
arr = np.arange(10)
print (arr)  # Output: [0 1 2 3 4 5 6 7 8 9]

#esempio reshape
arr = np.arange(6)
arr = arr.reshape((2, 3))
print (arr)