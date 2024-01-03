class Livre:
    def __init__(self, auteur, titre, nbrPages, disponible=True):
        self.__auteur = auteur
        self.__titre = titre
        self.__nbrPages = nbrPages
        self.__disponible = disponible
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
    def __vérifierDisponibilité__(self):
        return self.__disponible
    def __emprunter__(self):
        if self.__vérifierDisponibilité__()==True:
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponibles.")
    def __rendre__(self):
        if self.__vérifierDisponibilité__()==False:
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre est disponiblex.")
        
livre = Livre("Victor Hugo", "Les Misérables", 1225)

print(livre.__vérifierDisponibilité__())
livre.__emprunter__()
livre.__rendre__()



