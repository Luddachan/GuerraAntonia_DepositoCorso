from numpy import np 


arr = np.array([1, 2, 3, 4, 5])

#indexing
print(arr[0]) #output 1

#slicing
print(arr[1:3]) #output [2 3]

#boolean indexing

print(arr[arr > 2]) #output [3 4 5]

arr_2d = np.array([[1, 2, 3, 4], #posizione 0
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

#slicing sulle righe
print (arr_2d[1:3]) #output [[5 6 7 8]]
                        # [[9 10 11 12]]
                        
#slicing sulle colonne
print (arr_2d[:, 1:3]) #output [[2 3 ]
                       #         [6 7]
                       #        [10 11]]
                       
#slicing misto
print (arr_2d[1:, 1:3]) #output [[6 7]
                       #     [10 11]]
                        
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#slicing di base
print(arr[2:7]) #output [2 3 4 5 6]

#slicing con passo
print(arr[1:8:2]) #output [1 3 5 7]

#omettere start e stop

print(arr[:5]) #output [0 1 2 3 4]
print(arr[5:]) #output [5 6 7 8 9]

#utilizzare indici negativi
print(arr[-5:]) #output [5 6 7 8 9]
print(arr[:-5]) #output [0 1 2 3 4]

#esempi fancy indexing
arr = np.array([10, 20, 30, 40, 50])

#utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices]) #output [20 40]

#utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices]) #output [10 30 50]


                       
