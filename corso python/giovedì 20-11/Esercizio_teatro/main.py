from posto import Posto
from posto_standard import PostoStandard
from posto_vip import PostoVIP
from teatro import Teatro

def main():
    t = Teatro()
    #crea menù principale del teatro
    print("Benvenuti al sistema di prenotazione del teatro!")
    print("-------------------------------------------")
    print("Seleziona un'opzione:")
    print("1. Prenota un posto standard")
    print("2. Prenota un posto VIP")
    print("3. Visualizza posti occupati")
    print("4. Esci")
    
    while True:
        scelta = input("Inserisci la tua scelta (1-4): ")
        
        if scelta == '1':
            print("\nAggiungi un nuovo posto:")
        
            tipo = input("Tipo (VIP/Standard): ").strip().lower()
            numero = int(input("Numero posto: "))
            fila = input("Fila (es. A): ").upper().strip()
            
            # continua il ciclo del menù per scegliere il posto VIP
        
            if scelta == 'vip':
                servizi = input("Servizi extra (separati da virgola): ").split(',')
            
    
    pass
    
   #t = Teatro()

    