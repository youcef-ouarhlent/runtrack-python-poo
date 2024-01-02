class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        return "Je suis " + self.nom + " " + self.prenom 
print(Personne("John", "Doe").SePresenter())
print(Personne("Jean", "Dupond").SePresenter())

    

