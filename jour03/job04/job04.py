class Joueur:
    def __init__(self, nom, numéro, position, nbButs, passeDecisive, cartonjaune, cartonrouge):
        self.__nom = nom
        self.__numéro = numéro
        self.__position = position
        self.__nbButs = nbButs
        self.__passeDecisive = passeDecisive
        self.__cartonjaune = cartonjaune
        self.__cartonrouge = cartonrouge
    def get_nom(self):
        return self.__nom
    
    def get_numéro(self):
        return self.__numéro
    
    def get_position(self):
        return self.__position
    
    def get_nbButs(self):
        return self.__nbButs
    
    def get_passeDecisive(self):
        return self.__passeDecisive
    
    def get_cartonjaune(self):
        return self.__cartonjaune
    
    def get_cartonrouge(self):
        return self.__cartonrouge
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_numéro(self, numéro):
        self.__numéro = numéro

    def set_position(self, position):
        self.__position = position

    def set_nbButs(self, nbButs):
        self.__nbButs = nbButs

    def set_passeDecisive(self, passeDecisive):
        self.__passeDecisive = passeDecisive

    def set_cartonjaune(self, cartonjaune):
        self.__cartonjaune = cartonjaune

    def set_cartonrouge(self, cartonrouge):
        self.__cartonrouge = cartonrouge

    def marquerbut(self):
        self.__nbButs += 1

    def effectuerpassedecisive(self):
        self.__passeDecisive += 1        

    def recevoircartonjaune(self):
        self.__cartonjaune += 1

    def recevoircartonrouge(self):
        self.__cartonrouge += 1

    def afficherstatistique(self):
        print("Nom:", self.__nom)
        print("Numéro:", self.__numéro)
        print("Position:", self.__position)
        print("Nombre de buts:", self.__nbButs)
        print("Nombre de passes décisives:", self.__passeDecisive)
        print("Nombre de cartons jaunes:", self.__cartonjaune)
        print("Nombre de cartons rouges:", self.__cartonrouge)
        print(" ")             
class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__joueurs = []

    def get_nom(self):
        return self.__nom
    
    def get_joueurs(self):
        return self.__joueurs
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_joueurs(self, joueurs):
        self.__joueurs = joueurs

    def ajouterjoueur(self, joueur):
        self.__joueurs.append(joueur)

    def afficherstatistiques(self):
        print("Equipe:", self.__nom)

        for joueur in self.__joueurs:
            joueur.afficherstatistique() 
               
    def mettreajourstatistiques(self, joueur, nbButs, passeDecisive, cartonjaune, cartonrouge):
        joueur.set_nbButs(nbButs)
        joueur.set_passeDecisive(passeDecisive)
        joueur.set_cartonjaune(cartonjaune)
        joueur.set_cartonrouge(cartonrouge)


joueur1 = Joueur("Griezmann", 10, "Attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Mbappe", 7, "Attaquant", 0, 0, 0, 0)
joueur3 = Joueur("Benzema", 19, "Attaquant", 0, 0, 0, 0)
joueur4 = Joueur("Pogba", 6, "Milieu", 0, 0, 0, 0)
joueur5 = Joueur("Kante", 13, "Milieu", 0, 0, 0, 0)
joueur6 = Joueur("Matuidi", 14, "Milieu", 0, 0, 0, 0)
joueur7 = Joueur("Varane", 4, "Défenseur", 0, 0, 0, 0)
joueur8 = Joueur("Umtiti", 5, "Défenseur", 0, 0, 0, 0)
joueur9 = Joueur("Pavard", 2, "Défenseur", 0, 0, 0, 0)
joueur10 = Joueur("Hernandez", 21, "Défenseur", 0, 0, 0, 0)
joueur11 = Joueur("Maignan", 16, "Gardien", 0, 0, 0, 0)

joueur12 = Joueur("Messi", 10, "Attaquant", 0, 0, 0, 0)
joueur13 = Joueur("Aguero", 19, "Attaquant", 0, 0, 0, 0)
joueur14 = Joueur("Di Maria", 7, "Attaquant", 0, 0, 0, 0)
joueur15 = Joueur("Paredes", 6, "Milieu", 0, 0, 0, 0)
joueur16 = Joueur("De Paul", 13, "Milieu", 0, 0, 0, 0)
joueur17 = Joueur("Lo Celso", 14, "Milieu", 0, 0, 0, 0)
joueur18 = Joueur("Otamendi", 4, "Défenseur", 0, 0, 0, 0)
joueur19 = Joueur("Romero", 5, "Défenseur", 0, 0, 0, 0)
joueur20 = Joueur("Tagliafico", 2, "Défenseur", 0, 0, 0, 0)
joueur21 = Joueur("Montiel", 21, "Défenseur", 0, 0, 0, 0)
joueur22 = Joueur("Martinez", 16, "Gardien", 0, 0, 0, 0)




equipe1 = Equipe("France")
equipe1.ajouterjoueur(joueur1)
equipe1.ajouterjoueur(joueur2)
equipe1.ajouterjoueur(joueur3)
equipe1.ajouterjoueur(joueur4)
equipe1.ajouterjoueur(joueur5)
equipe1.ajouterjoueur(joueur6)
equipe1.ajouterjoueur(joueur7)
equipe1.ajouterjoueur(joueur8)
equipe1.ajouterjoueur(joueur9)
equipe1.ajouterjoueur(joueur10)
equipe1.ajouterjoueur(joueur11)

equipe2 = Equipe("Argentine")
equipe2.ajouterjoueur(joueur12)
equipe2.ajouterjoueur(joueur13)
equipe2.ajouterjoueur(joueur14)
equipe2.ajouterjoueur(joueur15)
equipe2.ajouterjoueur(joueur16)
equipe2.ajouterjoueur(joueur17)
equipe2.ajouterjoueur(joueur18)
equipe2.ajouterjoueur(joueur19)
equipe2.ajouterjoueur(joueur20)
equipe2.ajouterjoueur(joueur21)
equipe2.ajouterjoueur(joueur22)



equipe1.afficherstatistiques()
equipe2.afficherstatistiques()

# Simulation d'actions pendant un match
# Supposons que joueur1 de l'équipe1 (France) marque un but
joueur1.marquerbut()

# Supposons que joueur2 de l'équipe1 (France) effectue une passe décisive
joueur2.effectuerpassedecisive()

# Supposons que joueur3 de l'équipe1 (France) reçoive un carton jaune
joueur3.recevoircartonjaune()

# Supposons que joueur12 de l'équipe2 (Argentine) reçoive un carton rouge
joueur12.recevoircartonrouge()

# Affichage des statistiques mises à jour des joueurs après les actions simulées
equipe1.afficherstatistiques()
equipe2.afficherstatistiques()





        