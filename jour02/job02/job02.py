class Livre:
    def __init__(self, auteur, titre, nbrPages):
        self.__auteur = auteur
        self.__titre = titre
        self.__nbrPages = nbrPages
    def __get__Auteur__(self):
        return self.__auteur
    def __get__Titre__(self):
        return self.__titre
    def __get__NbrPages__(self):
        return self.__nbrPages
    def __set__Auteur__(self, auteur):
        self.__auteur = auteur
    def __set__Titre__(self, titre):
        self.__titre = titre
    def __set__NbrPages__(self, nbrPages):
        if nbrPages > 0 and nbrPages==int(nbrPages):
            self.__nbrPages = nbrPages
        else:
            print("Le nombre de pages doit être supérieur à 0.")





livre = Livre("Victor Hugo", "Les Misérables", 1225)
print(livre.__get__Auteur__())
print(livre.__get__Titre__())
print(livre.__get__NbrPages__())
livre.__set__Auteur__("guy de maupassant")
livre.__set__Titre__("bel ami")
livre.__set__NbrPages__(70.5)
print(livre.__get__Auteur__())
print(livre.__get__Titre__())
print(livre.__get__NbrPages__())