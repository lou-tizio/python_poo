class Rectangle:
    
    
    def __init__(self, longueur : int, largeur : int):
        self.__longueur = longueur
        self.__largeur = largeur 
        
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
        
    def get_largeur(self):
        return self.__largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur
        
        
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(4, 2)
print(f"la valeur de la longueur est {rectangle1.get_longueur()} et la largeur est {rectangle1.get_largeur()}")
print(f"la valeur de la longueur est {rectangle2.get_longueur()} et la largeur est {rectangle2.get_largeur()}")

