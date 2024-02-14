class Student :
   
    
    def __init__(self, nom : str, prenom : str, nummeroEtudiant : int, nombreCredits : int):
        self.__nomEtudiant = nom
        self.__prenomEtudiant = prenom
        self.__numEtudiant = nummeroEtudiant
        self.__nbreCreditsEtudiant = nombreCredits
    
    def get__nombreCredits(self):
        return self.__nbreCreditsEtudiant
       
    def add_credits(self, nbre : int ):
        if nbre > 0 :
            self.__nbreCreditsEtudiant = self.__nbreCreditsEtudiant + nbre 
        

etudiant1 = Student("John", "Doe", 145, 0)

etudiant1.add_credits(1)
etudiant1.add_credits(4)
etudiant1.add_credits(7)
print(f"le credits total {etudiant1.get__nombreCredits()}")
        