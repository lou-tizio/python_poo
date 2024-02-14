class Personne : 
    
    
    def __init__(self, age = 14):
        self.age = age
        
class Eleve (Personne):
    
    def __init__(self, age=15):
        super().__init__(age)
        
    def bonjour(self):
        print("Bonjour")
        
    def allerEnCour(self):
        print("je vais au cour")
        
    def afficherAge(self, age):
        return self.age

        
class Professeur :
    
    def __init__(self, matiereEnseignée):
        self.__matiereEnsegnée = matiereEnseignée
        
    def bonjourProfesseur(self):
        print("Bonjour les Eleves")
        
    def afficherAgePro(self, agePro = 40):
        self.age = agePro
        return self.age
          
    def enseigner(self):
        print("le cours va commencer")
        
eleve1 = Eleve()
eleve1.bonjour()
eleve1.allerEnCour()
print(f"{eleve1.afficherAge(age=15)} ans")

print("***********************************")

professeur1 = Professeur("SVT")
professeur1.bonjourProfesseur()
print (f"l'age du professeur est : {professeur1.afficherAgePro(agePro=40)} ans")
professeur1.enseigner()



