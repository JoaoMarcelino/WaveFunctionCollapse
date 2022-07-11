from PIL import Image
class Square:
    def __init__(self, image = Image.open("./images/non_existing.png"), name = 'non_existing.png', id_rotated = -1, rules = []):
        
        self.image = image
        self.name = name
        self.id_rotated = id_rotated
        self.rules = rules

    def showInfo(self):
        return "{self.name} : {self.id_rotated} -> {self.rules}"


class Grid:
    
    def __init__(self, options, width, height, collapsed = False):
        self.square = Square()
        self.options = options
        self.width = width
        self.height = height
        self.collapsed = False

    def showInfo(self):
        return f"{self.options}, {self.square.showInfo()}"
