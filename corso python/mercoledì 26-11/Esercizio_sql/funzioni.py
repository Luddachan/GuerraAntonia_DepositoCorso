import numpy as np

# --- Aggregazioni per colonne e righe ---
def somma_colonne(matrix):
    return np.sum(matrix, axis=0)

def somma_righe(matrix):
    return np.sum(matrix, axis=1)

def media_colonne(matrix):
    return np.mean(matrix, axis=0)

def media_righe(matrix):
    return np.mean(matrix, axis=1)

def min_colonne(matrix):
    return np.min(matrix, axis=0)

def max_colonne(matrix):
    return np.max(matrix, axis=0)

def std_colonne(matrix):
    return np.std(matrix, axis=0)

# --- Operazioni matriciali e algebriche ---
def trasposta(matrix):
    return np.transpose(matrix)

def prodotto_matriciale(A, B):
    return np.dot(A, B)

def norma(matrix):
    return np.linalg.norm(matrix)

def covarianza(matrix):
    return np.cov(matrix.T)

# --- Filtri semplici ---


# --- Report automatico ---
def report_descrittivo(matrix, colonne_nomi):
    report = {}
    report["Media"] = media_colonne(matrix)
    report["Deviazione standard"] = std_colonne(matrix)
    report["Minimi"] = min_colonne(matrix)
    report["Massimi"] = max_colonne(matrix)
    report["Somma colonne"] = somma_colonne(matrix)
    report["Somma righe"] = somma_righe(matrix)
    report["Norma matrice"] = norma(matrix)
    report["Covarianza"] = covarianza(matrix)
    report["Trasposta matrice"] = trasposta(matrix)
    return report