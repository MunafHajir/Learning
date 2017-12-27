'''
Given an array, the task is to find maximum triplet sum in the array.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the maximum triplet sum in new line.

Constraints:
1<=T<=100
3<=N<=106
-105<=A[i]<=105

Example:
Input:
2
6
1 0 8 6 4 2
7
1 2 3 0 -1 8 10
Output:
18
21

'''


n = 6
l = [1,0,8,6,4,2]
j = 0

tot2 = 0
result = 0

while True:
    
    if (n-j)<2:
        break
        
    elif result==0:
        result = sum(l[j:j+3])
        j+=1
        
    else:
        tot2 = sum(l[j:j+3])
        
        result = tot2<result and result or tot2
        j+=1

        
print(result)
