class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def __get__Longueur__(self):
        return self.__longueur
    def __get__Largeur__(self):
        return self.__largeur
    def __set__Longueur__(self, longueur):
        self.__longueur = longueur
    def __set__Largeur__(self, largeur):
        self.__largeur = largeur
rectangle = Rectangle(10, 5)
print(rectangle.__get__Longueur__())
print(rectangle.__get__Largeur__())
rectangle.__set__Longueur__(9)
rectangle.__set__Largeur__(4)
print(rectangle.__get__Longueur__())
print(rectangle.__get__Largeur__())

        


   
