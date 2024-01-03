class Commande:
    def __init__(self, numérodecommande, statutdelacommande):
        self.__numérodecommande = numérodecommande
        self.__plats_commandés = {}  # Utilisation d'un dictionnaire pour stocker les plats commandés
        self.__statutdelacommande = statutdelacommande

    def __ajouter_plat__(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandés:
            self.__plats_commandés[nom_plat] = {'prix': prix_plat, 'statut': self.__statutdelacommande}
        else:
            print("Ce plat est déjà dans la commande.")

    def __supprimer_plat__(self, nom_plat):
        if nom_plat in self.__plats_commandés:
            del self.__plats_commandés[nom_plat]
        else:
            print("Ce plat n'est pas dans la commande.")

    def __annuler_commande__(self):
        self.__statutdelacommande = "annulée"
        self.__plats_commandés.clear()  # Supprime tous les plats de la commande en cas d'annulation

    def __calculer_total__(self):
        total = sum(plat['prix'] for plat in self.__plats_commandés.values())
        return total

    def __calculer_tva__(self, taux_tva):
        total = self.__calculer_total__()
        tva = total * taux_tva
        return tva

    def __afficher_commande__(self):
        print(f"Numéro de commande : {self.__numérodecommande}")
        print("Plats commandés:")
        for plat, info in self.__plats_commandés.items():
            print(f"- {plat}: Prix - {info['prix']} | Statut - {info['statut']}")
        total = self.__calculer_total__()
        print(f"Total à payer : {total}")

    # Propriétés pour accéder en lecture seule aux attributs privés
    @property
    def numérodecommande(self):
        return self.__numérodecommande

    @property
    def statutdelacommande(self):
        return self.__statutdelacommande


# Exemple d'utilisation de la classe Commande
commande1 = Commande("CMD001", "en cours")

# Ajout de plats à la commande
commande1.__ajouter_plat__("Pizza", 10.99)
commande1.__ajouter_plat__("Salade", 5.50)
commande1.__ajouter_plat__("Boisson", 2.00)

# Affichage de la commande
commande1.__afficher_commande__()

# Calcul et affichage de la TVA
taux_TVA = 0.20  # 20%
tva = commande1.__calculer_tva__(taux_TVA)
print(f"TVA à payer : {tva}")

# Suppression d'un plat de la commande
commande1.__supprimer_plat__("Boisson")

# Affichage mis à jour de la commande
commande1.__afficher_commande__()

# Annulation de la commande
commande1.__annuler_commande__()

# Vérification du statut de la commande après annulation
print(f"Statut de la commande : {commande1.statutdelacommande}")
