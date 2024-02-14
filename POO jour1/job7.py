class Personnage:
    
    def __init__(self, x :int, y : int):
         self.x = x
         self.y = y
    
    def gauche (self):
        self.x -= 1
    
    def droite (self):
        self.x += 1
        
    def bas (self):
        self.y -= 1
        
    def haut (self):
        self.y += 1
        
    def position (self):
        return (self.x, self.y)
    
joueur = Personnage(1, 1)

joueur.gauche()
joueur.droite()
joueur.haut()
print(f"la position du joueur est : {joueur.position()}")