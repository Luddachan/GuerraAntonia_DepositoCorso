file = open ("esempio.txt", "r")
contenuto = file.read() #legge tutto il contenuto del file
riga = file.readline() #legge una riga del file


file = open ("esempio.txt", "w")
file.write("Ciao mondo!\n") #scrive nel file
file.close()

with open ("esempio.txt", "a") as file: #apre il file in modalitá append
    contenuto = file.read() #aggiunge una riga alla fine del file
