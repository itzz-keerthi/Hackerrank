'''TASK
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has  parameters:
A string,firstName.
A string,lastName.
An integer,idNumber.
An integer array (or vector) of test scores,scores.

A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

GRADING SCALE:
LETTER       AVERAGE
O            90<=a<=100
E            80<=a<90
A            70<=a<80
P            55<=a<70       
D            40<=a<55
T            a<40

Input Format

The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. It also calls the calculate method which takes no arguments.

The first line contains firstName,lastName, and idNumber, separated by a space. The second line contains the number of test scores. The third line of space-separated integers describes scores.

Constraints
1<=length of firstName,length of lastName<=10
length of idNumber=7
0<=score<=100

Output Format
Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

Sample Input
Heraldo Memelli 8135627
2
100 80

Sample Output
Name: Memelli, Heraldo
ID: 8135627
Grade: O

Explanation

This student had 2 scores to average: 100 and 80. The student's average grade is (100+80)/2=90. An average grade of 90 corresponds to the letter grade O, so the calculate() method should return the character'O'. '''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

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
    def __init__(self,firstName,lastName,idNumber,scores):
        Person.__init__(self,firstName,lastName,idNumber)
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum=0
        for score in scores:
           sum+=score
        average=sum/len(scores)
        if average<40:
           return 'T'
        elif average<55:
           return 'D'
        elif average<70:
           return 'P'
        elif average<80:
           return 'A'
        elif average<90:
           return 'E'
        else:
           return 'O'
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
