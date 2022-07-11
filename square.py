
class Square:

    def __init__(self, image, name, id_rotated, rules):
        
        self.image = image
        self.name = name
        self.id_rotated = id_rotated
        self.rules = rules

    def showInfo(self):
        print(f"{self.name} : {self.id_rotated} -> {self.rules}")
