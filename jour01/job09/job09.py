class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prix = prixHT
        self.TVA = TVA
    def afficherNom(self):
        return "Nom du produit : " + self.nom    
    def afficherPrixHT(self):
        return "Prix HT : " + str(self.prix)
    def afficherTVA(self):
        return "TVA : " + str(self.TVA)
    def AfficherProduit(self):
        return "Nom du produit : " + self.nom + " Prix HT : " + str(self.prix) + " Prix TTC : " + str(self.CalculerPrixTTC())  
    def CalculerPrixTTC(self):
        return self.prix + self.prix * self.TVA / 100
    def modifierNom(self, nvnom):
            self.nom = nvnom
            return "Nom du produit : " + self.nom + " Prix HT : " + str(self.prix) + " Prix TTC : " + str(self.CalculerPrixTTC())
    def modifierPrixHT(self, nvprixHT):  
            self.prix = nvprixHT
            return "Nom du produit : " + self.nom + " Prix HT : " + str(self.prix) + " Prix TTC : " + str(self.CalculerPrixTTC())
    def modifierTVA(self, nvtva):
            self.TVA = nvtva
            return "Nom du produit : " + self.nom + " Prix HT : " + str(self.prix) + " Prix TTC : " + str(self.CalculerPrixTTC())
    
    
    
chocolat=Produit("chocolat", 2, 20)
banane=Produit("banane", 3, 20)
print(chocolat.afficherNom())
print(chocolat.afficherPrixHT())
print(chocolat.afficherTVA())
print(chocolat.AfficherProduit())
print(chocolat.modifierNom("chocolat noir"))
print(chocolat.modifierPrixHT(4))
print(chocolat.modifierTVA(10))
print(chocolat.CalculerPrixTTC())
print(banane.afficherNom())
print(banane.afficherPrixHT())
print(banane.afficherTVA())
print(banane.AfficherProduit())
print(banane.modifierNom("banane bio"))
print(banane.modifierPrixHT(5))
print(banane.modifierTVA(15))
print(banane.CalculerPrixTTC())