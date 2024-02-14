class Rectangle :
    
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def perimètre(self):
        perimetre = (self.__longueur + self.__largeur)*2
        return perimetre
    def surface(self):
        surface = (self.__longueur * self.__largeur)
        return surface
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_lareur(self, largeur):
        self.__largeur = largeur
        
class Parallelepipede (Rectangle):
    
    def __init__(self, longueur, largeur,hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
        
    def volume(self):
        surface_base = super().surface()
        return surface_base * self.hauteur

rectangle1 = Rectangle(4, 5)
parallelepipede1 = Parallelepipede(4, 5, 1)

surface = rectangle1.surface()
perimetre = rectangle1.perimètre()
volume = parallelepipede1.volume()

print(f"Surface du rectangle : {surface}") 
print(f"Périmètre du rectangle : {perimetre}") 
print(f"Volume du parallélépipède : {volume}")


# print(parallelepipede1.volume())        