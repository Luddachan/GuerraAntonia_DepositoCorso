from giocatore import Giocatore
from allenatore import Allenatore
from assistente import Assistente

def main():
    # Creo un giocatore
    g = Giocatore("Simone", 24, "attaccante", 9)
    g.descrivi()
    g.gioca_partita()

    # Creo un allenatore
    a = Allenatore("Marco", 50, 20)
    a.descrivi()
    a.dirige_allenamento()

    # Creo un assistente
    s = Assistente("Chiara", 35, "fisioterapista")
    s.descrivi()
    s.supporta_team()

if __name__ == "__main__":
    main()