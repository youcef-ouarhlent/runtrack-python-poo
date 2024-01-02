class Operation:#Une classe Operation
    def __init__(self, nombre1, nombre2):#Une methode __init__ qui prend en parametre number1 et number2
        self.number1 = nombre1#self.number1 est egale a number1
        self.number2 = nombre2#self.number2 est egale a number2
afficher = Operation(12, 3)#Operation prend en parametre 1 et 2    
print("Le nombre1 est",afficher.number1)#Affiche Le nombre1 est 12
print("Le nombre2 est",afficher.number2)#Affiche Le nombre2 est 3


        