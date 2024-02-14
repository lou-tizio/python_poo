# class MaClasse:
#     def __init__(self, valeur):
#         self.__attribut_prive = valeur

# class AutreClasse:
#     def recuperer_attribut(self, instance_de_ma_classe):
#         return instance_de_ma_classe._MaClasse__attribut_prive

# # Instanciation de MaClasse
# objet_ma_classe = MaClasse(42)

# # Instanciation de AutreClasse
# objet_autre_classe = AutreClasse()

# # Récupération de l'attribut privé de MaClasse dans AutreClasse
# valeur_attribut = objet_autre_classe.recuperer_attribut(objet_ma_classe)

# # Affichage de la valeur de l'attribut privé
# print("Valeur de l'attribut privé:", valeur_attribut)


class Ville:
    
    def __init__(self, nom, nombreHabitants):
        self.__nom = nom
        self.__nombreHabitants = nombreHabitants
        
    
class Personne:
    
    def __init__(self, nom, age, ville):
        self.__nomPerson = nom
        self.__agePerson = age
        self.__ville = ville
        
    def recupe(self, instance):
        return instance._Ville__nombreHabitants
    
    def recupeVille (self,instance):
        return instance._Ville__nom
        
    def  ajoiuterPopulation (self,instance):
        instance._Ville__nombreHabitants += 1
        return instance._Ville__nombreHabitants
            
ville1 = Ville("Paris", 1000000)
ville2 = Ville("Marseille", 861635)

person1 = Personne ("john", 45, ville1)
person2 = Personne ("Myrtillle", 4, ville1)
person3 = Personne ("Chloé", 18, ville2)


print(f"population de la ville de Paris : {person1.recupe(ville1)}")
print(f"population de la ville de Marseille : {person1.recupe(ville2)}")
print("*******************************************************************")
print(f"La mise a jour de la population de la ville de Paris : {person1.ajoiuterPopulation(ville1)} habitants")
print(f"La mise a jour de la population de la ville de Paris : {person2.ajoiuterPopulation(ville1)} habitants")
print(f"La mise a jour de la population de la ville de marseille : {person3.ajoiuterPopulation(ville2)} habitants")
