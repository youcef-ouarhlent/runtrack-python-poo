class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    def changerRayon(self, nvx):
        self.rayon = nvx
        return self.rayon
    def afficherInfos(self):
        return  "Cercle de rayon " + str(self.rayon),"Cercle de diametre " + str(self.rayon * 2),"Cercle de circonference " + str(2 * 3.14 * self.rayon),"Cercle d'aire " + str(3.14 * self.rayon * self.rayon)
    def circonference(self):
        return 2 * 3.14 * self.rayon
    def aire (self):
        return 3.14 * self.rayon * self.rayon
    def diametre(self):
        return 2 * self.rayon
cercle=Cercle(4)
cercle2=Cercle(7)
print(cercle.changerRayon(8),cercle2.changerRayon(9))
print(cercle.afficherInfos(),cercle2.afficherInfos())
print(cercle.circonference(),cercle2.circonference())
print(cercle.aire(),cercle2.aire())
print(cercle.diametre(),cercle2.diametre())





        