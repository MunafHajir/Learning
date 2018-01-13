'''
Challenge
The function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Sample Test Cases

Input:"aa6?9"

Output:"false"

Input:"acc?7??sss?3rr1??????5"

Output:"true"

'''

a = "acc?7??sss?3"
incr = 0
anothernum = 0
newi = 0
for i in range(len(a)-1):
    if a[i].isnumeric():
        num = a[i]
        incr = i
        ques = 0
        while a[incr+1] == '?' or not a[incr+1].isnumeric():
            
            if a[incr+1] == '?':
                ques += 1
            incr += 1
            anothernum = a[incr+1]
            newi = incr
        new = int(num)+int(anothernum)
        if new == 10 and ques == 3:
            print('True')
            
        else:
            print('False')
            
    else:
        pass
             
