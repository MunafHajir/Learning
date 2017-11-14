"""
We have Infinitely Many Choclates and infinitely many children . And, We want to give them to children, But we will not give More than 'N' choclates to any one child. And, we want to give 'N' choclates to exactly 1 child.
And, We want to give thechoclates to as many children possible, in a beautiful sequence only.
A beautiful sequence is an increasing sequence, in which a term Ai divides all Aj, where j>i. 
Forexample: 3, 6, 24 is a beautiful sequence of length 3.

3 divides 6 and 24
6 divides 24
We would give

A0 choclates to the first child,
A1 choclates to the second child
...and so on
We want maximum Children to get thechoclates. Output the Beautiful Sequence of maximum length.
 
 
Input
Then Each of the next T lines, contains an integer denoting -'N'.

Output
For each testcase, Print the beautiful sequence of maximum length.
Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000
Example
Input: 
10
4
24
3
Output:
1 5 10
1 2 4
1 3 6 12 24
1 3
"""


#program:

n = int(input("Enter N Value: "))

l = []
l.append(n)
for i in range(n-1,0,-1):
    if n%i == 0:
        l.append(i)
        n=i
        
print(l[-1:0:-1])
