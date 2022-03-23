/*TASK

Read 3 numbers from stdin and print their sum to stdout.

Input Format

One line that contains 3 space-separated integers: a,b and c.

Constraints: 1<=a,b,c<=1000

Output Format

Print the sum of the three numbers on a single line.

Sample Input
1 2 7

Sample Output
10

Explanation
The sum of the three numbers 1+2+7 is 10.*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int a,b,c;
    cin>>a>>b>>c;
    cout<<a+b+c; 
    return 0;
}
