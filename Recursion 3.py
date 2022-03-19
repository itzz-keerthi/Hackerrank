'''TASK
Complete the factorial function in the editor below. Be sure to use recursion.

factorial has the following parameter:
int n: an integer

Returns

int: the factorial of n

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.

Input Format
A single integer,n(the argument to pass to factorial).

Constraints
2<=n<=12
Your submission must contain a recursive function named factorial.

Sample Input
3
Sample Output
6                  '''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n==1:
        print("1")
    else:
        f=1
        for i in range(1,n+1):
            f*=i
            i+=1
        print(f)
n=int(input(""))
factorial(n) 
           


