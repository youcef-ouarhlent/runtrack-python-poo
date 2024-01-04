class Ville:
    def __init__(self, nom, nombreHabitants):
        self.__nom = nom
        self.__nombreHabitants = nombreHabitants

    def get_nom(self):
        return self.__nom
    
    def get_nombreHabitants(self):
        return self.__nombreHabitants
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_nombreHabitants(self, nombreHabitants):
        self.__nombreHabitants = nombreHabitants

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_age(self, age):
        self.__age = age

    def set_ville(self, ville):
        self.__ville = ville

    def ajouterPopulation(self):
        current_population = self.__ville.get_nombreHabitants()
        self.__ville.set_nombreHabitants(current_population + 1)


Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)
print("Population de la ville de",Paris.get_nom(),":",Paris.get_nombreHabitants(),"habitants")
print("Population de la ville de",Marseille.get_nom(),":",Marseille.get_nombreHabitants(),"habitants")    
John = Personne("John", 45, Paris)
John.ajouterPopulation()  # Ajouter John à la population de la ville de Paris
myrtille = Personne("Myrtille", 4, Paris)
myrtille.ajouterPopulation()  # Ajouter Myrtille à la population de la ville de Paris
print("Mise a jour de la population de la ville de",Paris.get_nom(),Paris.get_nombreHabitants(),"habitants")  # Vérifier le nombre d'habitants de Paris après l'ajout de Myrtille
chloe = Personne("Chloé", 18, Marseille)
chloe.ajouterPopulation()  # Ajouter Chloé à la population de la ville de Marseille
print("Mise a jour de la population de la ville de",Marseille.get_nom(),Marseille.get_nombreHabitants(),"habitants")  # Vérifier le nombre d'habitants de Marseille après l'ajout de Chloé




        

        
    
        
        




     
