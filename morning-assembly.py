"""
Eveyone remember standing for queue in school assembly. One day few students were late in the morning assembly, so they just went and stood at the end of the queue. But their Principal was strict and made them stand in ascending order to their height.
Given an array of N elements representing the shortest person with 1 and tallest with N. He thought to arrange queue by following a trick,Trick was simple: pick a student and send him/her at last or first and to arrange according to height. But he needs your help to do so.
Cost is increased by one if one student is sent at first or last.

Input:
First line consists of T test cases. First line of test case consists of N. Second line of every test case consists of N elements.

Output:
Single line output, print the minimum cost to do so.

Constraints:
1<=T<=100
1<=N<=10^5

Example:
Input:
2
3
2 1 3
4
4 3 1 2
Output:
1
2
"""


task = int(input("Enter Number Of Task: "))
n_task = int(input("Enter Number Of Task Completed: "))
task_completed = []
remain = []

for i in range(n_task):
    task_completed.append(int(input()))

for i in range(1,task+1):
    if i in task_completed:
        pass
    else:
        remain.append(i)

print(remain)
