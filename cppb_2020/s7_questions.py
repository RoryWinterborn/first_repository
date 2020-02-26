# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:01:58 2020

@author: roryw
"""

"""
Question 1

Write code to check if the dictionary below contains a user inputted country.
If it is there print the capital, if not tell the user it is not there
"""
capitals = {"France": "Paris",
            "Spain": "Madrid",
            "United Kingdom": "London",
            "India": "New Deli",
            "United Steates": "Washington D.C.",
            "Italy": "Rome",
            "Denmark": "Copenhagen",
            "Germany": "Berlin",
            "Greece": "Athens",
            "Bulgaria": "Sophia",
            "Ireland": "Dublin",
            "Mexico": "Mexico CIty"}

# Define func[get_alpha_imput(message)] that takes one argument, message, and 
# returns a string, user_input. Check input is alpha, if not as for valid input
def get_alpha_input(message):
    go = True
    while go:
        user_input = input(message)
        if user_input.replace(" ", "").isalpha():
            return user_input
            go = False            
#m = ">>> "
#print(get_alpha_input(m))
# Define func[check_cap] That takes a string input and checks it against
# dict[capitals] if present: Print capital; if not print condolance 
def check_cap(country):
    country = country.title()
    if country in capitals:
        print(f"The capital of {country} is {capitals[country]}")
    else:
        print(f"No entry for {country}")
# Check input("Check the capital of a country:\n\t>>> ") using check_cap()
request = ""
check_cap(get_alpha_input("Check the capital of a country:\n\t>>> "))

###############################################################################
"""
Question 2

Write code that will generate the fibonacci sequence and stores in a dictionary
each term number and its term as key value pairs respectively.
""" 
# Define func[gen_fib(max_term)] Yeild all fibonacci numbers up to max_term
def gen_fib(max_term):
    sequence = {}                   # Define list[sequence] as []
    fib_num = 0                     # Define var[fib_num] as 0
    prv_num = 1                     # Define var[prv_num] as 1 
    for i in range(max_term):       # Loop through range(nax_term)
        sequence[i + 1] = fib_num
        prv_num, fib_num = fib_num, prv_num + fib_num 
    return sequence                 # Yeild sequence
"""
Takes one int argument (max_term) and returns a dictionary (with key value 
pairs equal to the term number and term respectively) up to max_term
""" 
#print(gen_fib(12))

###############################################################################
"""
Question 3

Create a dictionary to represent the open, high, low, close share price data
for 4 companies below
"""
companies = ["Python D.S.", "PythonSoft", "Pythazon", "Pybook"]
key_names = ["Open", "High", "Low", "CLose"]
data = [[12.87, 13.23, 11.42, 13.10],
        [23.54, 25.76, 21.87, 22.33],
        [98.99, 102.34,97.21, 100.065],
        [203.63,207.54,202.43,205.24]]

comb_data = {}

for i in range(len(companies)):
    comb_data[companies[i]] = dict(zip(key_names, data[i]))
    
print(comb_data)

###############################################################################
"""
Question 4
"""



###############################################################################
"""
QUestion 5

Create a dictionary containing the letters A-Z as keys and random numbers from
1 - 100 as values. Draw a bar graph of the results.
"""
import random
import matplotlib.pyplot as plt

keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dictionary_1 = {}

for letter in keys:
    dictionary_1[letter] = random.randint(1,100)

print(dictionary_1)

x, y = zip(*dictionary_1.items())

plt.figure(num=None, figsize=(30, 15), dpi=80, facecolor='w', edgecolor='k')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.bar(x, y)
plt.show()

###############################################################################
"""
Question 6

Create a dictionary representing a deck of playing cards with 4 suits of 13 
cards
"""
# Define list[suits] as ["Diamonds", "Spades", "Clubs", "Hearts"]
# Define list[cards] as ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
# "Jack", "Queen", "King"]
suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
cards = ["Ace", "2", "3", "4", "5", "6", "7", 
         "8", "9", "10", "Jack", "Queen", "King"]
deck_cards = {}                  # Define dict[playing_cards] as empty
# Create an entry in the dictionary for each suit, with the suit as key and 
# cards as the value
for suit in suits:
    deck_cards[suit] = cards
