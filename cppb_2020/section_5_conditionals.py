# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:05:38 2020

@author: roryw
"""

###########################################################
## Define var[user_input] as Int.Prompt["Enter an integer between 1 and 5:"]
#user_input = int(input("Enter an integer between 1 and 5:\n\t>>>"))
#
## Define list[one_five] as (one, two, three, four, five)
#one_five = ["one", "two", "three", "four", "five"]
#
## if user_input = index[one_five] + 1: a; else: b
##   a) Message(one_five(index))
##   b) Message("Out of range.")
#if user_input > 0 and user_input <= 5 and type(user_input) == int:3
#    print(one_five[user_input - 1])
#else:
#    print("Out of range")



############################################################
## Define var[message] as str
#message = "none"
#
## Define var[user_input] as Lower.Prompt{"Enter a number between one and five"}
#user_input = input("Enter a number between one and five:\n\t>>>")
#user_input = user_input.lower()
#
## Define list[one_five] as (one, two, three, four, five)
#one_five = ["one", "two", "three", "four", "five"]
##
##################

## for item[one_five]:
##   if user_input = item: message = index + 1
##   else: pass
#for item in one_five:
#    if user_input == item: 
#        message = str(index(one_five[user_input] + 1)
#    else:
#        pass
#    
## if message = "": Message["Out of range"]
## else: pass
##if message == "none":
##    message = "Out of range"
#
## Message[message]
#print(message)

###############

# for counter in range[5]
#   if user_input = one_five[counter]: message = counter + 1
#   else: pass
#
#if user_input == "one":
#    print(1)
#elif user_input == "two":
#    print(2)
#elif user_input == "three":
#    print(3)
#elif user_input == "four":
#    print(4)
#elif user_input == "five":
#    print(5)
#else:
#    print("Out of range")
#

###################################################################
"""Question 4"""
## Ask the user to input their name and check length. If greater than or equal 
## to 5 characters print the length, if less than 5 print "I'm not telling you"
#
## Define var[user_name] as input["Input your name:\n\t>>>"]
#user_name = input("Input your name:\n\t>>>")
#
## define var[length] as len(user_name)
#length = len(user_name)
#
## if length >= 5: Message["Your name is {length} characters long"]
## else: Message["I'm not telling you"]
#if length >= 5:
#    print("Your name is {} characters long".format(length))
#else:
#    print("I'm not telling you!")

##################################################################
"""Question 5"""

"""  Ask the user to input two numbers between 1 and 20. If both are greater 
    than 15 return their product. If only one is greater than 15 return their 
    sum. If neither is greater than 15 return 0"""

import sys

## Define var[num_1] as input["input an integer between 1 and 20"]
#num_1 = input("Input a number between 1 and 20:\n\t>>>")
#
## Check if num_1 is int
#if num_1.isdigit():
#    num_1 = int(num_1)
#else:
#    print("That's not even an integer!!!!")
#    sys.exit()
#
## Define var[num_2] as input["input a number between 1 and 20"]
#num_2 = input("Input a number between 1 and 20:\n\t>>>")
#
## Check if num_2 is int
#if num_2.isdigit():
#    num_2 = int(num_2)
#else:
#    print("That's not even an integer!!!!")
#    sys.exit()
#
## Check num_1 and num_2 are between 1 and 20
#if num_1 > 0 and num_2 > 0 and num_1 <= 20 and num_2 <= 20:
## if num_1 > 15 and num_2 > 15: Message[num_1*num_2]    
#    if num_1 > 15 and num_2 > 15:
#        print(num_1 * num_2)
## elif num_1 > 15 or num_2 > 15: Message[num_1+num_2]
#    elif num_1 > 15 or num_2 > 15:
#        print(num_1 + num_2)
## else: Message[0]
#    else:
#        print(0)
#
## If number(s) out of range Message["Out of range"]
#else:
#    print("Out of range")
    
#################################################################
    
"""Question 6"""

"""  Ask the user to input two variables. Then internally switch the contents
    of these variables"""

# Define var[input_1] as input["input something:\n\t>>>"]
input_1 = input("Input something:\n\t>>>")

# Define var[input_2] as input["input something:\n\t>>>"]
input_2 = input("Input something:\n\t>>>")

# Print input_1 and input_2
print("input_1 = {} and input_2 = {}".format(input_1, input_2))

# Swap the variables
input_1, input_2 = input_2, input_1

# Print input_1 and input_2
print("input_1 = {} and input_2 = {}".format(input_1, input_2))
