from student import Student

def main():
    student = Student('n/n', 0, 0)
    gradePoint, credits = getInputs()
    while not(gradePoint == '' or credits == ''):
        student.addGrade(float(gradePoint), float(credits))
        gradePoint, credits = getInputs()
    print('\nThe final GPA achieved is: {0:0.2f}'.format(student.gpa()))
        

def getInputs():
    gradePoint = input('Enter gradePoints: ')
    credits = input('Enter number of credit hours: ')
    return gradePoint, credits

if __name__=='__main__':
    main()