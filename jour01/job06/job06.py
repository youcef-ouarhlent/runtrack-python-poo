class Animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom
    def veillir(self):
        self.age += 1
        return self.age
    def nommer(self, prenom):
        self.prenom = prenom
        return self.prenom
Luna = Animal()
    
print("L'age de l'animal",Luna.age,"ans")
print("L'age de l'animal",Animal(0, "Luna").veillir(),"ans")
print("L'animal se nomme",Animal(0, "Luna").nommer("Luna"))    

    
           