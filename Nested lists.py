#Python program to work with nested lists
'''Task
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Input Format
The first line contains an integer,N, the number of students.
The 2N  subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints
2<=N<=5
There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 
Berry
Harry'''
d={} 
for _ in range(int(raw_input())): 
    Name=raw_input() 
    Grade=float(raw_input()) 
    d[Name]=Grade 
v=d.values()
second=sorted(list(set(v)))[1] 
second_lowest=[] 
for key,value in d.items():  
    if value==second: 
        second_lowest.append(key) 
second_lowest.sort() 
for name in second_lowest: 
    print(name) 
 
