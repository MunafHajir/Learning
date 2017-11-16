# Function

#simple function
def example():
    print("Basic Function")
    z = 5 + 6
    print(z)


example()

#passing parameter
def sum_addition(num1, num2):
    print("\nNum1 is", num1)
    answer = num1 + num2
    print("Answer is", answer)


sum_addition(5, 3)             #or we can write as sum_addition(num1=5,num2=3)

#default functions
def sum_example(num1,num2=5):
    print("\n",num1,num2)

sum_example(2)

#example of default function
def basic_window(width,height,font='TNR',bgc='w'):
    print(width,height,font,bgc)

basic_window(500,300)
basic_window(500,300,font='monospaced')

m=6                                                         #global variable

def example():
    z=5                                                     #local variable
    global m                                                #you have to notify that m is global
    print(m)
    m+=5
    print(m)
    return m

example()
new=example()

print(new)