# Debut creation de la class Animal
class Animal:
    
    def __init__(self):
        self.age = 0
        self.prenom = " "
        
    def vieillir (self):
        self.age +=1
    
    def nommer (self, prenom: str):
        self.prenom = prenom
        
# Fin creation de la class     
          
chien = Animal()

print(f"L'age de l'animal est :{chien.age} ans" )
chien.vieillir()
print(f"L'age de l'animal est :{chien.age} ans")
chien.nommer("Luna")
print(f"L'animal se nomme {chien.prenom}")
         