#classe che cotrolla gli accessi dei dipendenti

class ControlloAccessi:
    def __init__(self):
        #registro degli accessi effettuati dai dipendenti
        self._accessi_registrati = []
    # funzione per registrare un accesso di un dipendente    
    def registra_accesso(self, dipendente, badge):
        #controlla se il badge è attivo
        if badge.is_attivo():
            # registra l'accesso consentito
            accesso = f"Accesso consentito a {dipendente._nome} con badge {badge._id_badge}."
            # serve per salvare gli accessi in un registro con una lista
            #append aggiunge un elemento alla lista
            self._accessi_registrati.append(accesso)
            # stampa l'accesso consentito
            print(accesso)
        # se il badge non è attivo
        else:
            accesso = f"Accesso negato a {dipendente._nome}. Badge {badge._id_badge} non attivo."
            self._accessi_registrati.append(accesso)
            print(accesso)
            
    def mostra_accessi(self):
        print("Registro Accessi:")
        # con un for stampiamo tutti gli accessi registrati nella lista
        for accesso in self._accessi_registrati:
            print(accesso)