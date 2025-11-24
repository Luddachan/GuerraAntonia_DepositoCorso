from numpy import np

#crea un array ndarray utilizzando np.arange() con valori da 0 a 49 più altre 50 
#posizioni con valori casuali tra 49 e 101

array = np.arange(0,50)
array_random = np.random.randint(49, 102, size =50)

#unisci i due array in un unico array
# * unpacking degli array
ar = np.array([*array, *array_random])
#stampa l'array, il suo dtype e la sua shape
print ("Array unito: ", ar)
print ("Tipo di dato dell'array unito: ", ar.dtype)
print ("Forma dell'array unito: ", ar.shape)

#modifica il tipo di dato dell'array casuale in float64
array_random = np.array(array_random, dtype='float64')
print (array_random.dtype) 
#verifica e stampa dtyp e shape dell'array modificato
print ("Array casuale modificato: ", array_random)
print ("Tipo di dato dell'array casuale modificato: ", array_random.dtype)
print ("Forma dell'array casuale modificato: ", array_random.shape)

#punto 3: utilizzo dello slicing
#per ottenere i primi 10 elementi 
primi_10 = array[:10]
#ultimi 7
ultimi_7 = array[-7:]
#dal 5 al 20 escluso
dal_5_al_20 = array[5:20]
#ogni quarto elemento
#:: indica di prendere un elemento ogni quattro
ogni_quarto = array[::4]

#punto 4: modifica tramite slicing gli elementi dall'indice 10 al 15 escluso
#assegna il valore 999
array[10:15] = 999

#fancy indexing
#crea un array di indici
# elementi in posizioni specifiche
posizioni = [0, 3, 7, 12, 25, 33, 48]
selez_posizioni = array[posizioni]

# tutti gli elementi pari dell’array
pari = array[array % 2 == 0]

# tutti gli elementi maggiori della media
media = array.mean()
maggiori_media = array[array > media]

# stampa i risultati
print("\n------- Riepilogo------------")
print("Primi 10 elementi:", primi_10)
print("Ultimi 7 elementi:", ultimi_7)
print("Elementi dal 5 al 20 escluso:", dal_5_al_20)
print("Ogni quarto elemento:", ogni_quarto)
print("Array dopo la modifica (indici 10-15 escluso a 999):", array)
print("Elementi in posizioni specifiche:", selez_posizioni)
print("Elementi pari dell'array:", pari)
print("Elementi maggiori della media (", media, "):", maggiori_media)
