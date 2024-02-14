from cmath import pi


class Cercle:
    
    def __init__(self, rayonInitial: int):
        self.rayon = rayonInitial
    
    def changerRayon(self, newrayon : int):
       self.rayon = newrayon
        
    def afficherInfos(self):
        print(f"le rayon est : {self.rayon}")
        
    def circonférence(self):
        return 2 * pi * self.rayon
    
    def aire(self):
        return pi * (self.rayon * self.rayon)
         
    def diametre(self):
        return 2 * self.rayon 
    
    
cercle1 = Cercle(4)
cercle1.afficherInfos()
print(f"La circonference du cercle1 est: {cercle1.circonférence()}, son diametre : {cercle1.diametre()}, et son aire : {cercle1.aire()}")

cercle2 = Cercle(7)
cercle2.afficherInfos()
print(f"les informations cercle2 sont sa circonference: {cercle2.circonférence()}, son diametre : {cercle2.diametre()}, et son aire : {cercle2.aire()}")
