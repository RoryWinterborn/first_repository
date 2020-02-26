# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:31:32 2020

@author: roryw
"""
###############################################################################
"""for loops"""

for i in range(10):
    print(i)
print("\n")

for i in range(1, 10):
    print(i,end=" ")
print("\n")

for i in range(1, 11):
    print(i,end=" ")
print("\n")

for i in range(1, 11):
    print(i, end=" ")
print("\n")

for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

for i in range(0, 40, 4):
    print(i, end=" ")
print("\n")

for i in range(0, 42, 4):
    print(i, end=" ")
print("\n")

####################

word = "python"

for char in word:
    print(char)

####################

numbers = ["one", "two", "three", "four", "five"]

data = [53, 76, 25, 98, 56, 42, 69, 81]

print(numbers[0])
print(numbers[2])
print(numbers[0:2])
print(numbers[-1])
print(numbers[-4:-1])
print(numbers[1:-1])

for number in numbers:
    print(number,end=", ")
print("\n")

concat_list = ""

for number in numbers:
    concat_list = concat_list + number
print(concat_list)

for i in range(5):
    print(numbers[i])
    print(numbers[i-1])
    print()

print(sum(data))
print(max(data))

####################
"""BUbble Sort"""

data_copy = data[:]

for i in range(len(data_copy)):
    for j in range(0, len(data_copy)-i-1):
        if data_copy[j] > data_copy[j+1]:
            data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j]

print(data_copy)
print(data)

""" Don't rely on this for sorting in RL as it is very inefficient and besides,
python impliments much faster sorting natively with the sorted() function"""

print(sorted(data_copy))

my_list = [34, 76, 58]

my_list.append(100)

my_list.remove(34)

print(my_list.index(100))

my_list.reverse()

my_list.extend([66, 67, 68])

###############################################################################
"""While Loops"""

n = 10

while n > 0:
    print(n)
    n -= 1

####################

ages = []
user_input = int(input("Enter the age of a class member, enter -1 to EXIT\n\t>>>"))
while user_input > 0:
    ages.append(user_input)
    user_input = int(input("The next age, enter -1 to EXIT\n\t>>>"))
print("The ages of members:", ages)
                           
####################
count = 0
class_names = []
name = input("Input names of class members individually, Type 'n' to EXIT\n\t>>>")
while name != "n":
    count += 1
    class_names.append(name)
    print(f"{name} has been added")
    name = input("Input the next name, type 'n' to EXIT:\n\t>>>")

print(f"There are {count} class members, Their names are {class_names}")

###############################################################################
"""
Question 1

Ask the user for two numbers between 1 and 100, then count form the lower
number to the higher number
"""
# Define var[count] as int(0)
count = 0
no_1 = 0
no_2 = 0
# Define func[get_num_1_100] That takes one argument, a variable, and prompts
# the user to fill it with a number between 1 and 100. if out of range Message,
# prompt again for valid input untul true
# Define local var[num] as int(0)
def get_num_1_100():
    global count
    num = 0
# Check for valid input: Continue while not true
    while num < 1 or num > 100:
# Get user input and convert to str. Increment count
        if count == 0:
            num = int(input("Enter an integer between 1 and 100:\n\t>>>"))
            count += 1
        else:
            num = int(input("Enter another integer, between 1 and 100:\n\t>>>"))
            count += 1
# Check for valid input: Message("Out of range") if not
        if num < 1 or num > 100:
            print("Out of range")
    return num
        
# Define func[print_s2l] that takes two int arguments and prints from the lower
# of the two, to the greater, with step == 1. if equal: Message 
# Define local var[smaller] as 0
# Define local var[larger] as 0
def print_s2l(num_1, num_2):
    smaller = 0
    larger = 0
# Check if num_1 == num_2
    if num_1 != num_2:       
# Check which is bigger, set [larger, smaller] 
        if num_1 < num_2:
            smaller, larger = num_1, num_2    
        elif num_1 > num_2:
            larger, smaller =  num_1, num_2
# Count from smaller to larger, printing each value on the same line
        for i in range(smaller, larger):
            print(i,end=" ")
        print(larger)
# if num_1 = num_2: Message[num_1 = num_2]
    else:
        print(f"{num_1} = {num_2}")

# Define var[num_1] as get_num_1_100(num_1)
#
no_1 = get_num_1_100()
print(no_1)
## Define var[num_2] as get_num_1_100(num_2)

no_2 = get_num_1_100()
#print(no_2)
# call print_s2l on num_1 and num_2
print_s2l(no_1, no_2)

###############################################################################
"""
Question 2

Ask the user to input a string, and then print this in reverse order.
"""
# Define func[reverse_str](word):
def reverse_str(word):
# Define var[temp_str] as str
    temp_str = ""
# for char in word: temp_str = char + temp_string 
    for char in word:
        temp_str = char + temp_str
# Yeild temp_str
    return temp_str

# Define str[user_input] as input."Enter a string of characters:\n\t>>> "
user_input = input("Enter a string of characters:\n\t>>> ")

# Call reverse_str on user_input and print the output
print(reverse_str(user_input))


""" Learn more about strings. This is all of user_input with a step of 
minus one. There are other ways too (although this is not a bad way?)"""
# A sensible method
print(user_input[::-1])

###############################################################################
"""
Question 3

Ask the user for a number between 1 and 12, and then display the 1-12 times 
table for that input
"""
# Use a while loop to create a loop that gets user input and checks it is valid
# If invalid repeate the loop until the user enters a valid input.
go = True
while go:
    user_input = input("Enter a number between 1 and 12:\n\t>>> ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input >= 1 and user_input <= 12:
            go = False
    
# for i in 1-12: print(i*user_input) 
for i in range(1, 12):
    print(i * user_input, end=" ")
print(12 * user_input)

###############################################################################
"""
Question 4

Ammend the answer to Q3 so that no input is required
"""

for i in range(1, 13):
    for j in range(1, 12):
        print(i * j, end="\t")
    print(i * 12)

###############################################################################
"""
Question 5

Ask the user to input a sequence of numbers. Calculate and print the mean.
"""

# Define var[user_input] as input["Enter an integer type QUIT to exit."]
user_input = input("Enter a positive integer:\n\t>>> ")
# Define list[numbers]
numbers = []
## if user_input.upper() == QUIT: go = False; else go = True
#if user_input.lower() == "quit":
#    go = False
#else:
go = True
# if user_input is QUIT: exit and print mean. Wile user_input is not QUIT:
#   if user_input.upper() == QUIT: go = false
#   elif user_input isdigit: append int(user_input) to numbers 
#   else: Message["Enter and integer!"]
#   input["Enter an integer type QUIT to exit."]
while go:
    if user_input.lower() == "quit":
        go = False
    elif user_input.isdigit():
        numbers.append(int(user_input))
        user_input = input("Enter a positive integer. Type QUIT to exit:\n\t>>> ")
    else:
        print("Enter a positive integer!!")
        user_input = input("Enter a positive integer. Type QUIT to exit:\n\t>>> ")

# If len(numbers) != 0: calculate and print the mean
if len(numbers) != 0:
    print(f"\nThe mean is: {sum(numbers) / len(numbers)}")
    
###############################################################################
    
"""
Question 6

Write code that will calculate 15 factorial
"""
# Define func[calc_factorial(number)]:
def calc_factorial(number):
# If integer: for i in range(1, number): number = number * i
    if type(number) == int:
        for i in range(1, number):
            number = number * i
            print(number)
    return number

"""calculate 15 factorial"""
#factorial_15 = (calc_factorial(15))

################
# Define func[get_pos_int(message)] and yeilds u_in:
def get_pos_int():
# set go = True
    go = True
    u_in = ""
# While go:
    while go:
#   Define str[u_in] as input(message)
        u_in = input("Enter a positive integer:\n\t>>> ")
#   if u_in.isdigit() == true: u_in = int(u_in), go = False
        if u_in.isdigit() == True:
            u_in = int(u_in)
            go = False
#   else: print(please enter a positive integer)
        else:
            print("Enter a positive integer!!!!")
# Yeild u_in
    return u_in

print(calc_factorial(get_pos_int()))

###############################################################################
"""
Question 7

Write code to generate the fibonacci sequence. Create a list containing the
first 20 fibonacci numbers.
"""
# Define func[gen_fib(max_term)] that yeilds a list of all fibonacci numbers up
# to the max_term supplied
# Define list[sequence] as []
# Define var[fib_num] as 0
# Define var[prv_num] as 1
def gen_fib(max_term):
    sequence = []
    fib_num = 0
    prv_num = 1
# Loop through range(nax_term), for each iteration: 
#   append fib_num to sequence
#   prv_num, fib_num = fib_num, prv_num + fib_num 
    for i in range(max_term):
        sequence.append(fib_num)
        prv_num, fib_num = fib_num, prv_num + fib_num 
# Yeild sequence
    return sequence

"""Create and print a list containing the first 20 fibonacci numbers"""
#first_20 = gen_fib(20)
#print(first_20)

print(gen_fib(20))

###############################################################################
"""
Question 8

Comment previous code
"""
###############################################################################
"""
Question 9

Write python code that will produce the following output:
    
    *****
    *
    ***
    *
    *
    
"""
 Define list[upper_f] as lists that encode each line of the character
upper_f = [[0,1,1,1,1,1],
           [0,1,0,0,0,0],
           [0,1,1,1,0,0],
           [0,1,0,0,0,0],
           [0,1,0,0,0,0]]
 
# Define func[print_char] that prints the above pattern:
# Create for loop that iterates through each line sequentially
# Create for loop that iterates through each pixel sequentially
#   for pixel in line: if pixel = True: print("*"); else print(" ")
def print_char(lists):
    for line in lists:
        for pixel in line:
            if pixel:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

print_char(upper_f)

###############################################################################

"""
Question 10

Write python code that will determine all odd and even numbers between 1 and
100. Put all even in a list and all odd in another list
"""
# define func[odd_even(max_num)] that takes one argument, max_num, and
# yeilds dict[odds_evens] containing all odds, evens up to max_num
# Define dict[odds_evens] as {"evens":[], "odds":[]}
# Iterate 1 through max_num: if %2: append to odds; else: append to evens
# Yeild odds_evens
def odd_even(max_num):
    odds = []
    evens = []
    for i in range(1, max_num + 1):
        if i % 2:
            odds.append(i)
        else:
            evens.append(i)
    odds_evens = {"odds": odds, "evens": evens}
    return odds_evens

print(odd_even(100))
