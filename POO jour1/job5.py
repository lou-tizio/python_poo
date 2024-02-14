class Point:
    
    def __init__(self, x, y):
        self.pointx = x
        self.pointy = y
    
    def afficherLesPoint(self):
        affichage = self.pointx + self.pointy
        print(f"affiche les coordonnée des points : {affichage}")
        
    def afficheX(self):
        return self.pointx
    
    def afficheY(self):
        return self.pointy
    
    def changerX(self, a):
        self.pointx = a
        
    def changerY(self, b):
        self.pointy = b
        
valeur = Point(3, 6)
valeur.afficherLesPoint()
print(valeur.afficheX())
print(valeur.afficheY())
valeur.changerX(10)
print(f"la nouvelle valeur de x est : {valeur.afficheX()}")
valeur.changerY(20)
print(f"la nouvelle valeur de y est : {valeur.afficheY()}")
  
        
    
        