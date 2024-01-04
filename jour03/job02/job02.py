class CompteBancaire:
    def __init__(self, numérodecompte, nom, prenom, solde, decouvert=True):
        self.__numérodecompte = numérodecompte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    # Les méthodes 'getters' et 'setters' peuvent être simplifiées en utilisant des propriétés Python

    
    def numérodecompte(self):
        return self.__numérodecompte

    
    def nom(self):
        return self.__nom

    
    def prenom(self):
        return self.__prenom

    
    def solde(self):
        return self.__solde

    
    def decouvert(self):
        return self.__decouvert

    
    def decouvert(self, value):
        self.__decouvert = value

    def afficher(self):
        print("Numéro de compte:", self.__numérodecompte)
        print("Nom:", self.__nom)
        print("Prénom:", self.__prenom)
        print("Solde:", self.__solde, "€")
        print("Découvert autorisé:", self.__decouvert)

    def afficherSolde(self):
        print("Solde:", self.__solde, "€")

    def versement(self, somme):
        self.__solde += somme

    def retrait(self, somme):
        if self.__solde - somme < 0 and not self.__decouvert:
            print("Opération impossible, le solde ne peut pas être négatif.")
        else:
            self.__solde -= somme
            print("Votre nouveau Solde est de:", self.__solde, "€")

    def agios(self, taux):
        if self.__solde < 0:
            self.__solde -= self.__solde * taux
            print("Des agios ont été appliqués.")
        else:
            print("Pas d'agios nécessaires, solde positif.")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Opération impossible, le solde ne peut pas être négatif.")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
            self.afficherSolde()
            compte_destinataire.afficherSolde()


# Création des comptes
julien = CompteBancaire("00000000000000000000000000", "Julien", "Dupont", 300)
julien.afficher()
julien.afficherSolde()
julien.versement(100)
julien.afficherSolde()
julien.retrait(100)
julien.retrait(150)  # Tentative de retrait avec découvert

# Création d'un deuxième compte en découvert
marie = CompteBancaire("11111111111111111111111111", "Marie", "Durand", -50, decouvert=True)
marie.afficher()
marie.afficherSolde()

# Effectuer un virement du compte de Julien (solde positif) vers le compte de Marie (en découvert)
julien.virement(marie, 50)  
