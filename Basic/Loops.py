# Loops

condition = 1

print('while')

while condition < 10:
    print(condition)

    condition += 1
'''
Infinite Loop

while True:
    print('doing stuff')

'''
print('while ends')

print('\nFor loop start')

exampleList = [1, 2, 5, 6, 7, 20]

for eachNumber in exampleList:
    print(eachNumber)
    print("Indentation Matters\n")      #indendation matters

for x in range(1,10):                   #range is builtin function
    print(x)

print('for loops end')

print('\nif start')

a=5
b=5
x=3
y=8

if x<y>a>x:
    print('\ny is greater')

if a>y:
    print('\na is greater')

else:
    print('\ny is greater')

if(x>y):
    print('x is greater')

elif(y>x):
    print('y is greater')

else:
    print("None")