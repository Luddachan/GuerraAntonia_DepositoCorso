class Punto:
    def __init__ (self, x, y):
        #metodi costruttore
        self.x = x
        self.y = y 
    #definisci metodo muovi che prende 
    def muovi (self, dx, sx):
        self.dx += dx 
        self.sx += sx
    def distanza_da_origine(self):
        pass
#trovata su internet 
#return math.sqrt(self.x**2 + self.y**2)
        
    