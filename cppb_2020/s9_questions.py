'''
Question 1
Create a class to represent a bank account. It will need to have a balance,
a method for withdrawing money, depositing money, and displaying the 
balance to the screen. Create an instance of the bank account class and 
check that the methods work as expected
''' 

class bank_account(object):
    '''
    docstring
    '''
    def __init__(self, balance=0.0):
        self.balance = balance
    
    def balance_enq(self):
        print(f"Your balance is {self.balance}")
    
    def deposit_funds(self, amount):
        self.balance += amount
    
    def withdraw_funds(self, amount):
        if amount > self.balance:
            print(f"You do not have sufficient funds")
        else:
            self.balance -= amount

# my_bank = bank_account(300)
        
# my_bank.balance_enq()

# my_bank.deposit_funds(300)

# my_bank.balance_enq()

# my_bank.withdraw_funds(200)

# my_bank.balance_enq()

# my_bank.withdraw_funds(400)

# my_bank.balance_enq()

# my_bank.withdraw_funds(400)

# my_bank.balance_enq()

'''
Question 2
Create a circle class that will take the value of a radius and
return the area of the circle
'''

import math

class circle(object):
    def __init__(self,radius):
        self.radius = radius
    
    def calc_area(self):
        area = math.pi * (self.radius)**2
        return area

my_circle = circle(10)
print(my_circle.calc_area())