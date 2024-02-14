class Livre:
    
    
    def __init__(self, titreLivre : str, auteurLivre : str, nbrPageLivre : int):
        self.__titre = titreLivre
        self.__auteur = auteurLivre 
        self.__nombrePage = nbrPageLivre
        self.__disponible = True
         
    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
        
    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
        
    def get_nbrPages(self):
        return self.__nombrePage

    def set_nbrPages(self, nbrPage : int):
        if nbrPage > 0 :
             self.__nombrePage = nbrPage 
        else:
             self.showErrorMessage()
        
    def set__disponible(self, isDispo : bool):
        self.__disponible = isDispo
        
    def showErrorMessage(self):
          raise ValueError("le nombre de page doit etre entier positif ")    
        
    def verification(self):
            return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.set__disponible(False)
             
    def rendre(self):
        if not self.verification():
            self.set__disponible(True)    
 
# livre1 = Livre("bon", "lol", 1)
#print(f"le livre est {livre1.get_titre()} de {livre1.get_auteur()} à la page {livre1.get_pages()}")
# livre1.set_nbrPages(10)
# print(f"le livre est {livre1.get_titre()} de {livre1.get_auteur()} à la page {livre1.get_nbrPages()}")
# print(livre1.verification)

