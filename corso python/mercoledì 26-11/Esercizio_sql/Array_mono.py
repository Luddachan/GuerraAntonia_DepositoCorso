#import libreria numpy
import numpy as np


#STATISTTICHE DI BASE
def val_min(arr):  #valore minimo
    return np.min(arr)
def val_max(arr):  #valore massimo
    return np.max(arr)
def media(arr):   #media
    return np.mean(arr)
def dev_std(arr):  #deviazione standard
    return np.std(arr)

#ANALISI POSIZIONALE
def indice_val_min(arr): 
    return np.argmin(arr)  #indice del valore minimo
def indice_val_max(arr):
    return np.argmax(arr)  #indice del valore massimo
def mediana(arr):
    return np.percentile(arr, 50)  #mediana
def posiz_ord_inserimento(arr, x):
    return np.searchsorted(arr, x)  #trovare posizione ordinata di inserimento







