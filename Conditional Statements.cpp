/*TASK

Given a positive integer , do the following:
If 1<=n<=9, print the lowercase English word corresponding to the number (e.g., one for 1, two for 2, etc.).
If n>9, print Greater than 9.

Input Format
A single integer,n .

Constraints
1<=n<=10^9

Output Format
If 1<=n<=9, then print the lowercase English word corresponding to the number (e.g., one for 1, two for 2, etc.); otherwise, print Greater than 9.

Sample Input 0
5

Sample Output 0
five

Explanation 0
five is the English word for the number 5.

Sample Input 1
8

Sample Output 1
eight

Explanation 1
eight is the English word for the number 8.

Sample Input 2
44

Sample Output 2
Greater than 9

Explanation 2
n=44 is greater than 9, so we print Greater than 9. */

#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    if(n==1)
    {
        cout<<"one";
    }
    else if(n==2)
    {
        cout<<"two";
    }
    else if(n==3)
    {
        cout<<"three";
    }
    else if(n==4)
    {
        cout<<"four";
    }
    else if(n==5)
    {
        cout<<"five";
    }
    else if(n==6)
    {
        cout<<"six";
    }
    else if(n==7)
    {
        cout<<"seven";
    }
    else if(n==8)
    {
        cout<<"eight";
    }
    else if(n==9)
    {
        cout<<"nine";
    }
    else 
    {
     cout<<"Greater than 9";
    }
    return 0;
}
