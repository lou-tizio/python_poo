class CompteBancaire:

    def __init__(self, numeroCompte : int, nom:str, prenom:str):
        self.__numeroCompte = numeroCompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = 0
        self.__decouvert = False
        
    
    def afficher(self):
       print(f"le numero de ce compte est : {self.__numeroCompte}, le nom : {self.__nom}, prenom : {self.__prenom}")
 
    
    def afficherSolde(self):
        return self.__solde
    
    def versement(self, montantVersement):
        self.__solde = self.__solde + montantVersement
        print(f"le montant versement est : {montantVersement}")
        
    def retrait(self, montantARetirer : float):
        if self.__solde > 0 and montantARetirer >= self.__solde:
             self.__solde = self.__solde - montantARetirer 
        elif self.__decouvert == True :
            self.__solde = self.__solde - montantARetirer 
        elif self.__decouvert ==False: 
            raise ValueError("votre solde est insuffissant")
        print(f"le nouveau solde est : {self.__solde}")
 
    def activeDecouvert(self):
        self.__decouvert = True
        
    def desactiverDecouvert(self):
        self.__decouvert = False
 
    def agios(self, montantAgios : float):
        if self.__solde < 0 :
            self.__solde = self.__solde - montantAgios
            
    
    def virement(self, compteDestinataire, montant):
        if montant > 0 :
            self.__solde >= montant
            compteDestinataire += montant
            print(f"vous avez reçu un montant de {montant}") 
        else: 
           raise ValueError("votre virement recontre des difficulté") 
        
                   
compte1 = CompteBancaire(1234,"koffi","yao")
compte2 = CompteBancaire(23, "lou", "loiu")
compte1.afficher()
# print(f"le solde actuel est : {compte1.afficherSolde()}")
compte1.versement(10000)
print(f"le solde actuel est : {compte1.afficherSolde()}")
compte1.retrait(10400)
compte1.agios(2)
# compte1.versement(10000)
# print(f"le solde actuel est : {compte1.afficherSolde()}")
compte1.retrait(15000)
#compte1.activeDecouvert()
# compte1.retrait(15000)
compte1.desactiverDecouvert()
# compte1.retrait(15000)
