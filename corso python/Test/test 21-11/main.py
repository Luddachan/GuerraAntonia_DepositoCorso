#importo tutte le classsi
from badge import Badge
from controllo_accessi import ControlloAccessi
from dipendente import dipendente
from turno import Turno


#creo un dipendente
dip1 = dipendente("Mario", "Rossi", 30, "Impiegato", 30000.0)
badge1 = Badge("ABC123")
turno1 = Turno("Lunedì", "09:00", "17:00")

dip1.assegna_badge(badge1)
controllo = ControlloAccessi()

#menù interattivo
def mostra_menu():
    print("\n--- MENU GESTIONALE ACCESSI ---")
    print("1) Registra accesso")
    print("2) Disattiva badge")
    print("3) Attiva badge")
    print("4) Mostra log accessi")
    print("5) Modifica stipendio")
    print("6) Mostra informazioni turno")
    print("7) Esci")
    return input("Scegli un'opzione: ")


while True:
    #uso il match case per gestire le opzioni del menù che l'utente sceglie
    match mostra_menu():
        case "1":
            print ("Registrazione accesso...")
            controllo.registra_accesso(dip1, badge1)
        case "2":
            badge1.disabilita()
            print("Badge disattivato.")
        case "3":
            badge1.abilita()
            print("Badge attivato.")
        case "4":
            print ("Mostra log accessi...")
            controllo.mostra_accessi()
        case "5":
            nuovo_stipendio = float(input("Inserisci il nuovo stipendio: "))
            dip1.set_stipendio(nuovo_stipendio)
            print(f"Stipendio aggiornato a {dip1.get_stipendio()} euro.")
        case "6":
            print("Informazioni turno di lavoro:")
            turno1.mostra_informazioni_turno()
        case "7":
            print("Uscita dal programma.")
            break
        # _ serve come default in caso non venga inserita una delle opzioni previste
        case _:
            print("Opzione non valida. Riprova.")
            
            

            

    
