#--------------------------
# creare una classe "ContoBancario" che incapsula le seguenti informazioni
# di un conto bancario e fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare
# l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto
# Creare anche il menù per interagire con l'utente
#--------------------------

class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        # attributi privati
        # set per incapsulamento
        self.set__titolare = titolare        
        self.set__saldo = saldo_iniziale
        
    # metodi getter e setter
    
    def get_titolare(self):
        return self.__titolare
    def __set_titolare(self, nuovo_titolare):
        # controllo di validità del nuovo titolare 
        #strip per rimuovere spazi bianchi
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip() != "":
            # assegnazione del nuovo titolare
            self.__titolare = nuovo_titolare
        else:
            print("Errore: Il nome del titolare deve essere una stringa non vuota.")
    # getter pubblico per saldo  
    def visualizza_saldo(self):
        return self.__saldo
    
# metodi pubblici per gestire il saldo in modo sicuro

    def deposita(self, importo):
        # controllo di validità dell'importo
        if importo <= 0:
            print("Errore: L'importo del deposito deve essere positivo.")
            return
        # fondi aggiunti al saldo
        if importo > self.__saldo:
            print("Errore: Fondi insufficienti")
            return
        # saldo aggiornato dopo il deposito
        self.__saldo += importo
        # messaggio di conferma
        print(f"Prelievo effettuato. Nuovo saldo: {self.__saldo}€")
        
# menù per interagire con l'utente

def menu():
    print ("===Conto Bancario===")
    print ("1. Visualizza saldo")
    print ("2. Deposita fondi") 
    print ("3. Preleva fondi")
    print ("4. Esci")
    scelta = input("Seleziona un'opzione (1-4): ")
    return scelta

# esempio di utilizzo della classe ContoBancario
conto = ContoBancario("Mario Rossi", 1000)

# ciclo per il menù
while True:
    scelta = menu()
    # esegui l'azione corrispondente alla scelta dell'utente
    if scelta == "1":
        # visualizza saldo via metodo pubblico
        print(f"Saldo attuale: {conto.visualizza_saldo()}€")
    # deposita fondi
    elif scelta == "2":
        importo = float(input("Inserisci l'importo da depositare: "))
        conto.deposita(importo)
    # preleva fondi
    elif scelta == "3":
        importo = float(input("Inserisci l'importo da prelevare: "))
        conto.preleva(importo)
    elif scelta == "4":
        # esci dal programma con break
        print("Uscita dal programma.")
        break
    # scelta non valida
    else:
        print("Opzione non valida. Riprova.")