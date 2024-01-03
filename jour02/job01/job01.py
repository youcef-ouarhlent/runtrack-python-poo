class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def get__Longueur(self):
        return self.__longueur
    def get__Largeur(self):
        return self.__largeur
    def set__Longueur(self, longueur):
        self.__longueur = longueur
    def set__Largeur(self, largeur):
        self.__largeur = largeur
rectangle = Rectangle(10, 5)
print(rectangle.get__Longueur())
print(rectangle.get__Largeur())
rectangle.set__Longueur(9)
rectangle.set__Largeur(4)
print(rectangle.get__Longueur())
print(rectangle.get__Largeur())

        


   
