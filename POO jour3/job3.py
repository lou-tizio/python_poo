class Tache:
    
    
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "A faire"
    
    
class ListeDeTaches:
    
    def __init__(self, taches):
        self.taches = []
        
    def ajouterTache(self, taches):
        self.taches.append(taches)
        print(f"tache {taches.titre}")

    # def supprimerTache(self, taches):
    #     if taches in self.taches:
    #         self.taches.remove(taches)
    #         print(f"{taches.titre}")
    #     else:
    #         print("la taches n'est pas")
        
    # def marquerCommencerFinie(self, instance):
    #     if self._taches__statut == "A faire" :
            
        
taches1 = Tache("manger","dqsvbghjkg")
liste1 = ListeDeTaches("parler")

print()
