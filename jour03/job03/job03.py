class Tache:
    def __init__(self, titre, description, statut="à faire" or "terminé"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    def get_titre(self):
        return self.__titre
    
    def get_description(self):
        return self.__description
    
    def get_statut(self):
        return self.__statut
    
    def set_titre(self, titre):
        self.__titre = titre

    def set_description(self, description):
        self.__description = description

    def set_statut(self, statut):
        self.__statut = statut

class ListeDeTaches:
    def __init__(self, nom):
        self.__nom = nom
        self.__taches = []       

    def get_nom(self):
        return self.__nom
    
    def get_taches(self):
        return self.__taches
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_taches(self, taches):
        self.__taches = taches

    def ajouterTache(self, tache):
        self.__taches.append(tache)

    def supprimerTache(self, tache):
        self.__taches.remove(tache)

    def marquercommefini(self, tache):
        tache.set_statut("terminé")

    def afficherlaliste(self):
        print("Liste de taches:", self.__nom)
        for tache in self.__taches:
            print("Tache:", tache.get_titre())
            print("Description:", tache.get_description())
            print("Statut:", tache.get_statut())
            print(" ")
            
    def filtre(self):
        print("Liste de taches:", self.__nom)
        for tache in self.__taches:
            if tache.get_statut() == "à faire":
                print("Tache:", tache.get_titre())
                print("Description:", tache.get_description())
                print("Statut:", tache.get_statut())
                print(" ")
            else:
                pass
# Votre code existant pour les classes Tache et ListeDeTaches...

# Création des tâches
tache1 = Tache("Faire les courses", "Acheter du pain")
tache2 = Tache("Faire le ménage", "Nettoyer la cuisine")
tache3 = Tache("Réviser pour l'examen", "Chapitres 4 et 5")

# Création d'une liste de tâches
liste_taches = ListeDeTaches("Ma liste")

# Ajout des tâches à la liste de tâches
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de la liste de tâches initiale
liste_taches.afficherlaliste()

# Modifier le statut d'une tâche
liste_taches.marquercommefini(tache2)

# Affichage de la liste de tâches mise à jour
liste_taches.afficherlaliste()

# Filtrer les tâches par statut (à faire)
print("Tâches à faire:")
liste_taches.filtre()

# Supprimer une tâche de la liste
liste_taches.supprimerTache(tache1)

# Affichage de la liste de tâches après suppression
liste_taches.afficherlaliste()