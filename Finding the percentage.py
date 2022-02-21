#Python program for finding the percentage
'''Task:
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input Format
The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. 
The final line contains query_name, the name of a student to query.

Constraints
2<=n<=10
0<=marks[i]<=100
length of marks arrays=3

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 
56.00'''
a=int(input(""))
d=[]
for i in range(a):
    b=input("")
    c=b.split()
    d.append(c)    
f=input("")
for i in range(len(d)):
   if f==d[i][0]:
      g=(float(d[i][1])+float(d[i][2])+float(d[i][3]))/3
      print("{:.2f}".format(g))
   
