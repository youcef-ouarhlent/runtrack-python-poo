class Personnage:
    def __init__(self, nom="", vie=100):
        self.__nom = nom
        self.__vie = vie

    def get_nom(self):
        return self.__nom

    def get_vie(self):
        return self.__vie

    def set_nom(self, nom):
        self.__nom = nom

    def set_vie(self, vie):
        self.__vie = vie

    def attaque(self, cible):
        print(self.__nom, "attaque", cible.get_nom())
        cible.set_vie(cible.get_vie() - 10)  # Réduire la vie de la cible lors d'une attaque


class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez un niveau de difficulté (1 facile, 2 moyen, 3 difficile) : "))

    def lancerJeu(self):
        self.choisirNiveau()
        if self.niveau == 1:
            joueur = Personnage("Joueur", 150)
            ennemi = Personnage("Ennemi", 100)
        elif self.niveau == 2:
            joueur = Personnage("Joueur", 160)
            ennemi = Personnage("Ennemi", 150)
        elif self.niveau == 3:
            joueur = Personnage("Joueur", 170)
            ennemi = Personnage("Ennemi", 200)
        else:
            print("Niveau invalide. Démarrez une nouvelle partie.")
            return

        while joueur.get_vie() > 0 and ennemi.get_vie() > 0:
            joueur.attaque(ennemi)
            ennemi.attaque(joueur)

            print("Vie du Joueur:", joueur.get_vie())
            print("Vie de l'Ennemi:", ennemi.get_vie())

        if joueur.get_vie() <= 0:
            print("L'ennemi a gagné!")
        elif ennemi.get_vie() <= 0:
            print("Le joueur a gagné!")


# Exemple d'utilisation
jeu = Jeu()
jeu.lancerJeu()
