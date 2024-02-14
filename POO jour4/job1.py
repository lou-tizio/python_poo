class Personne : 
    
    
    def __init__(self, age = 14):
        self.age = age
        
    def afficherAge(self, age):
        return self.age
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, newAge : int):
        self.age = newAge
        return newAge
    
class Eleve (Personne):
    
    def __init__(self, age=14):
        super().__init__(age)
        
    def allerEnCour(self):
        print("je vais en cour")
        
    def afficherAge(self, age):
        return super().afficherAge(age)
    
class Professeur :
    
    def __init__(self, matiereEnseignée):
        self.__matiereEnsegnée = matiereEnseignée
        
    def get__matiereEnsegnée(self):
            return self.__matiereEnsegnée
            
    
    def enseigner(self):
        print("le cours va commencer")
    
henry = Personne()
eleve1 = Eleve()
matiere = Professeur("math")
print(f"l'age de henry est: {henry.age}")
print(f"l'age de henry est: {henry.modifierAge(newAge = 45)}")
henry.bonjour()
eleve1.allerEnCour()
print(f"J'ai {eleve1.afficherAge(age = 14)} ans")
print(f"La matiere enseigner est {matiere.get__matiereEnsegnée()}")
matiere.enseigner()

    