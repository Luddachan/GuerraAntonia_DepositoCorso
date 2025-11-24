import numpy as np

#creo una matrice 6x6 con numeri casuali interi tra 1 e 100
matrice = np.random.randint(1,101, size = (6,6))
print("Matrice 6x6 di numeri casuali tra 1 e 100:\n", matrice)

# Estraggo la sotto-matrice centrale 4x4
#    Indici: righe 1–4 (escluso 5), colonne 1–4 (escluso 5)
sotto = matrice[1:5, 1:5]
print("\nSotto-matrice centrale 4x4:\n", sotto)

#inverti le righe della matrice estratta
mat_invertita = sotto [::-1]
print("\nMatrice con righe invertite:\n", mat_invertita)

#diagonale principale della matrice invertita e crea un array 1D
#diag è un metodo di numpy
diagonale = np.diagonal(mat_invertita)
print("\nDiagonale principale della matrice invertita:\n", diagonale)

#sostituisco i valori della matrice invertita che sono multipli di 3 con -1

mat_invertita = mat_invertita.copy()
mat_invertita[mat_invertita % 3 == 0] = -1
print("\nMatrice invertita con multipli di 3 → -1:\n", mat_invertita)


#stampa i risultati 
print("\n------ RIEPILOGO ------")
print("Matrice originale:\n", matrice)
print("\nSotto-matrice 4x4:\n", sotto)
print("\nMatrice invertita:\n", mat_invertita)
print("\nDiagonale principale:\n", diagonale)
