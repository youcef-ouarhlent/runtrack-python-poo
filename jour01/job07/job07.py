class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def gauche(self):
        self.x -= 1
        return "P(" + str(self.x) + "," + str(self.y) + ")"
    def droite(self):
        self.x += 1
        return "P(" + str(self.x) + "," + str(self.y) + ")"
    def haut(self):
        self.y += 1
        return "P(" + str(self.x) + "," + str(self.y) + ")"
    def bas(self):
        self.y -= 1
        return "P(" + str(self.x) + "," + str(self.y) + ")"
    def afficherPosition(self):
        return "P(" + str(self.x) + "," + str(self.y) + ")"
personnage=Personnage(0, 0)    
print(personnage.gauche())
print(personnage.droite())
print(personnage.haut())
print(personnage.bas())
print(personnage.afficherPosition())
