"""Esercizio: andare a creare un filtro che controlli se elem x e elem x+1 
della lista sono superiori a elem n x+2 della lista 
con gli ultimi numeri usare due volte quelli presenti tranne l'ultimo"""

def filtro_lista(lista):
    # Controlla se gli elementi x e x+1 sono maggiori di x+2
    if len(lista)<3:
        # Se la lista ha meno di 3 elementi, non ci sono coppie da confrontare
        return []
    # Inizializza la lista per i risultati
    risultato = []
    
    # for per ogni elemento della lista fino al terzultimo
    for i in range(len(lista)-2):
        if lista[i] > lista[i+2] and lista[i+1] > lista[i+2]:
            # Aggiungi la tupla (x, x+1, x+2) alla lista dei risultati
            risultato.append((lista[i], lista[i+1], lista[i+2]))
    return risultato