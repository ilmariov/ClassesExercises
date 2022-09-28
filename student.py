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

    def addLetterGrade(self, letterGrade, credits):
        if letterGrade == 'A':
            self.qpoints = self.qpoints + (4 * credits)
        elif letterGrade == 'B':
            self.qpoints = self.qpoints + (3 * credits)
        elif letterGrade == 'C':
            self.qpoints = self.qpoints + (2 * credits)
        elif letterGrade == 'D':
            self.qpoints = self.qpoints + (1 * credits)
        else:
            self.qpoints = self.qpoints
        self.credits = self.credits + credits
