'''TASK
Context
Given a 6 X 6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Example

In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A.

Constraints

-9<=A[i][j]<=9
0<=i,j<=5

Output Format

Print the maximum hourglass sum in A.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19

Explanation

A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4 '''

#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass_sum(array,row,col):
    sum=0
    sum+=array[row-1][col-1]
    sum+=array[row-1][col]
    sum+=array[row-1][col+1]
    sum+=array[row][col]
    sum+=array[row+1][col-1]
    sum+=array[row+1][col]
    sum+=array[row+1][col+1]
    return sum

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

max_hourglasssum=-63
for i in range(1,5):
   for j in range(1,5):
      current_hourglasssum=hourglass_sum(arr,i,j)
      if current_hourglasssum>max_hourglasssum:
        max_hourglasssum=current_hourglasssum
print(max_hourglasssum)
