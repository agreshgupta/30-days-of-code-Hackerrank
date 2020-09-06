#A lot to explian here in simple way we are reusing our code from praent class
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
#declaring a class
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
    #initaiting the class
    def __init__(self, firstName, lastName, idNumber, scores):
        #getting the information from parent class
        super().__init__(firstName, lastName, idNumber )
        self.scores = scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    #
    def calculate(self):
        a = sum(self.scores)/len(self.scores)
        if a < 40:
            return "T"
        elif a >=40 and a < 55:
            return "D"
        elif a >= 55 and a< 70:
            return "P"
        elif a >= 70 and a< 80:
            return "A"
        elif a >= 80 and a<90:
            return "E"
        #elif a>= 90 and a<=100:
        #    return "O"
        else:
            return "O"
 
 # Function main
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
#Example of Inheritance
s.printPerson()
print("Grade:", s.calculate())
