class Student:
    def __init__(self, nom, prenom, numeroEtudiant, nombredecredit=0, level=""):
        self.__nom = nom
        self.__prenom = prenom
        self.__numeroEtudiant = numeroEtudiant
        self.__nombredecredit = nombredecredit
        self.__level = level
        self.__studentEval__()  # Évaluer le niveau lors de la création de l'étudiant

    def __ajouterCredit__(self, credit):
        if credit > 0 and isinstance(credit, int):
            self.__nombredecredit += credit
            self.__studentEval__()  # Mettre à jour le niveau après l'ajout de crédits
        else:
            print("Le nombre de crédits doit être un entier positif.")
    
    def __studentEval__(self):
        if self.__nombredecredit >= 90:
            self.__level = "Excellent"
        elif self.__nombredecredit >= 80:
            self.__level = "Très bien"
        elif self.__nombredecredit >= 70:
            self.__level = "Bien"
        elif self.__nombredecredit >= 60:
            self.__level = "Passable"
        else:
            self.__level = "Insuffisant"

    def __studentinfo__(self):
        print(f"Nom: {self.__nom}\nPrenom: {self.__prenom}\nid: {self.__numeroEtudiant}\nNombre de crédits: {self.__nombredecredit}\nNiveau: {self.__level}")

# Création d'un étudiant
john = Student("John", "Doe", 145)

# Ajout de crédits à l'étudiant John
john.__ajouterCredit__(25)
john.__ajouterCredit__(25)
john.__ajouterCredit__(25)
john

# Obtention des informations de l'étudiant John
john.__studentinfo__()
