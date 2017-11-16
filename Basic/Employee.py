class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@domain.com'

    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

fname = input('First Name ')
lname = input('Last Name  ')
pay = int(input('Pay  '))

emp1 = Employee(fname,lname,pay)

print(emp1.email)

print(emp1.fullname())