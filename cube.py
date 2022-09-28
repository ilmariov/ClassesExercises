class Cube:

    def __init__(self, lenght_side):
        self.lenght_side = lenght_side
    
    def getLenght(self):
        return self.lenght_side

    def surfaceArea(self):
        return 6 * self.lenght_side**2

    def volume(self):
        return self.lenght_side**3