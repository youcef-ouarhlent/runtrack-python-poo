class Livre:
    def __init__(self, auteur, titre, nbrPages):
        self.__auteur = auteur
        self.__titre = titre
        self.__nbrPages = nbrPages
    def get__Auteur(self):
        return self.__auteur
    def get__Titre(self):
        return self.__titre
    def get__NbrPages(self):
        return self.__nbrPages
    def set__Auteur(self, auteur):
        self.__auteur = auteur
    def set__Titre(self, titre):
        self.__titre = titre
    def set__NbrPages(self, nbrPages):
        if nbrPages > 0 and nbrPages==int(nbrPages):
            self.__nbrPages = nbrPages
        else:
            print("Le nombre de pages doit être supérieur à 0.")





livre = Livre("Victor Hugo", "Les Misérables", 1225)
print(livre.get__Auteur())
print(livre.get__Titre())
print(livre.get__NbrPages())
livre.set__Auteur("guy de maupassant")
livre.set__Titre("bel ami")
livre.set__NbrPages(70.5)
print(livre.get__Auteur())
print(livre.get__Titre())
print(livre.get__NbrPages())