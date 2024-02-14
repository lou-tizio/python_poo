class Personne():
    
    def __init__(self, lastname, firstname):
        self.nom = lastname
        self.prenom = firstname

    def SePresenter(self):
        presentation = self.nom + self.prenom
        print(f"je me nomme : {presentation}")
       

humain = Personne("john", " Doe")
humain.SePresenter()

humain1 = Personne("Jean", " Dupond")
humain1.SePresenter()

print("je {}".format())
