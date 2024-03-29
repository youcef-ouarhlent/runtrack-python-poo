class Student:
    def __init__(self, nom, prenom, numeroEtudiant, nombredecredit=0, level=""):
        self.__nom = nom
        self.__prenom = prenom
        self.__numeroEtudiant = numeroEtudiant
        self.__nombredecredit = nombredecredit
        self.__level = level
        self.__studentEval__()
    def __ajouterCredit__(self, credit):
        if credit > 0 and isinstance(credit, int):
            self.__nombredecredit += credit
            self.__studentEval__()
        else:
            print("Le nombre de crédits doit être un entier positif.")

    def __get__Credit__(self):
        print(f"Le nombre de crédits de {self.__prenom} est de {self.__nombredecredit} crédits.")
        return self.__nombredecredit
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
john.__ajouterCredit__(10)
john.__ajouterCredit__(10)
john.__ajouterCredit__(10)


john.__get__Credit__()
john.__ajouterCredit__(40)

# Obtention du nombre de crédits de l'étudiant John
john.__studentinfo__()





