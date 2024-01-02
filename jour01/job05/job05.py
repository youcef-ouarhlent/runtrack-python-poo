class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def AfficherLesPoints(self):
        return "P(" + str(self.x) + "," + str(self.y) + ")"
    def afficherX(self):
        return "P(" + str(self.x) + ")"
    def afficherY(self):
        return "P(" + str(self.y) + ")"
    def changerX(self, nvx):
        self.x = nvx
        return "P(" + str(self.x) + ")"
    def changerY(self, nvy):
        self.y = nvy    
        return "P(" + str(self.y) + ")"
print(Point(2, 3).AfficherLesPoints())
print(Point(2, 3).afficherX())
print(Point(2, 3).afficherY())
print(Point(2, 3).changerX(5))
print(Point(2, 3).changerY(6))        

    
