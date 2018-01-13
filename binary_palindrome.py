'''
Given a non-negative integer N. The problem is to check if binary representation of n is palindrome or not. Note that the actual binary representation of the number is being considered for palindrome checking, no leading 0’s are being considered.

Input:
The first line of the input contains a single integer T, denoting the number of test cases. Then T test case follows. Each test case contains a single line of input denoting the number N.

Output:
For each test case, print 1 if binary representation of N is palindrome; else print 0.

Constraints:
1<=T<=200
0<=N<=263-1

Example:

Input:
3
1
2
3

Output:
1
0
1

Explanation:
For testcase 2: The binary representation of 2 is 10, and of course, 10 is not a palindrome.
For testcase 3: The binary representation of 3 is 11, needless to say, 11 is a palindrome.
'''


def decToBin(x):
    return int(bin(x)[2:])

def revNum(y):
    reversed_num = str(y)[::-1]
    return int(reversed_num)

value = int(input("Enter Decimal Number: "))
bin_value = decToBin(value)

if bin_value == revNum(bin_value):
    print("Binary Number Of Value Is Palindrome")
    
else:
    print("Not Palindrome")
