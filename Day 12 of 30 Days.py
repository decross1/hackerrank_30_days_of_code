## Hackerrank: Day 12 of 30 Days of Code

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, score):
        Person.__init__(self, firstName, lastName, idNumber)
        self.score = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        total = sum(self.score)
        avg = total / len(self.score)
        if avg >= 90:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T'


line = 'Heraldo Memelli 8135627'.split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = 2
scores = map(int, '100 80'.split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()