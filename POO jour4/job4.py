import math


class Forme :
    
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon**2
    
cercle1= Cercle(3)

# Appel de la méthode aire de la classe Cercle
resultat_aire_cercle = cercle1.aire()

# Affichage du résultat pour le cercle
print(f"L'aire du cercle est : {resultat_aire_cercle}")

# Instanciation de la classe Rectangle
rectangle1 = Rectangle(5, 10)

# Appel de la méthode aire de la classe Rectangle
resultat_aire = rectangle1.aire()

# Affichage du résultat
print(f"L'aire du rectangle est : {resultat_aire}")
    