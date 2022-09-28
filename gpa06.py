from student import Student

def main():
    student = Student('n/n', 0, 0)
    letterGrade, credits = getInputs()
    while not(letterGrade == '' or credits == ''):
        student.addLetterGrade(letterGrade, float(credits))
        letterGrade, credits = getInputs()
    print('\nThe final GPA achieved is: {0:0.2f}'.format(student.gpa()))
        

def getInputs():
    letterGrade = input('Enter letter grade: ')
    credits = input('Enter number of credit hours: ')
    return letterGrade, credits

if __name__=='__main__':
    main()