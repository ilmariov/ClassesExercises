class Student:
    def __init__(self, name, credits, qpoints):
        self.name = name
        self.credits = float(credits)
        self.qpoints = float(qpoints)
    
    def getName(self):
        return self.name
    
    def getCredits(self):
        return self.credits

    def getQpoints(self):
        return self.qpoints
    
    def gpa(self):
        return self.qpoints / self.credits

    def addGrade(self, gradePoint, credits):
        self.qpoints = self.qpoints + (gradePoint * credits)
        self.credits = self.credits + credits