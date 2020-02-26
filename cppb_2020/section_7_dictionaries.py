# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:45:02 2020

@author: roryw
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

print(capitals["Germany"])
print()
print(capitals.get("Germany"))
print()

print(capitals)
print()
capitals["South Korea"] = "Seoul"
print(capitals)
print()

print(capitals.items())
print()

for country in capitals:
    print(country,end=" ")
print()
print()

for country, city in capitals.items():
    print(f"The capital city of {country} is {city}")
print()

print(capitals.keys())
print()
print(capitals.values())
print()

if "France" in capitals:
    print("dict[capitals] contains the key 'France'")    
print()

###############################################################################

list_of_numbers = [1,2,3,4,5]

print("list_of_numbers =", list_of_numbers)

print()

print("5 in list_of_numbers? ",5 in list_of_numbers)

print("7 in list_of_numbers? ", 7 in list_of_numbers)

###############################################################################

sherlock = """
Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent occasions when he was up all night, was seated at the breakfast table. I stood upon the hearth-rug and picked up the stick which our visitor had left behind him the night before. It was a fine, thick piece of wood, bulbous-headed, of the sort which is known as a “Penang lawyer.” Just under the head was a broad silver band nearly an inch across. “To James Mortimer, M.R.C.S., from his friends of the C.C.H.,” was engraved upon it, with the date “1884.” It was just such a stick as the old-fashioned family practitioner used to carry—dignified, solid, and reassuring.

“Well, Watson, what do you make of it?”

Holmes was sitting with his back to me, and I had given him no sign of my occupation.

“How did you know what I was doing? I believe you have eyes in the back of your head.”

“I have, at least, a well-polished, silver-plated coffee-pot in front of me,” said he. “But, tell me, Watson, what do you make of our visitor’s stick? Since we have been so unfortunate as to miss him and have no notion of his errand, this accidental souvenir becomes of importance. Let me hear you reconstruct the man by an examination of it.”

“I think,” said I, following as far as I could the methods of my companion, “that Dr. Mortimer is a successful, elderly medical man, well-esteemed since those who know him give him this mark of their appreciation.”

“Good!” said Holmes. “Excellent!”

“I think also that the probability is in favour of his being a country practitioner who does a great deal of his visiting on foot.”

“Why so?”

“Because this stick, though originally a very handsome one has been so knocked about that I can hardly imagine a town practitioner carrying it. The thick-iron ferrule is worn down, so it is evident that he has done a great amount of walking with it.”

“Perfectly sound!” said Holmes.

“And then again, there is the ‘friends of the C.C.H.’ I should guess that to be the Something Hunt, the local hunt to whose members he has possibly given some surgical assistance, and which has made him a small presentation in return.”

“Really, Watson, you excel yourself,” said Holmes, pushing back his chair and lighting a cigarette. “I am bound to say that in all the accounts which you have been so good as to give of my own small achievements you have habitually underrated your own abilities. It may be that you are not yourself luminous, but you are a conductor of light. Some people without possessing genius have a remarkable power of stimulating it. I confess, my dear fellow, that I am very much in your debt.”

He had never said as much before, and I must admit that his words gave me keen pleasure, for I had often been piqued by his indifference to my admiration and to the attempts which I had made to give publicity to his methods. I was proud, too, to think that I had so far mastered his system as to apply it in a way which earned his approval. He now took the stick from my hands and examined it for a few minutes with his naked eyes. Then with an expression of interest he laid down his cigarette, and carrying the cane to the window, he looked over it again with a convex lens. 
"""

# Define func[count_chars(input_string)] that yeilds a dictionary containing 
# each character type as keys and and their relative frequency as values
# Define dict[count] as {}
def count_chars(input_string):
    char_count = {}
# Traverse the string, for each character:
#   character = character.lower()
#   count[character] = count.get(character, 0) + 1
    for char in input_string:
        #char = char.lower()
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1 #*
    return char_count
# Define dict[c_c] as count_chars(sherlock)
c_c = count_chars(sherlock)
"""
IN* : char_count.get(char, 0) + 1  ; WHY does char not need .lower() ????? 

ANSWER: IT DOES!!
"""
import matplotlib.pyplot as plt
# Unpack data in c_c
sher_keys, sher_vals = zip(*c_c.items())
# Setup plot
plt.figure(num=None, figsize=(40, 15), dpi=80, facecolor='w', edgecolor='k')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# Plot data in c_c
plt.bar(sher_keys, sher_vals)
plt.show()
# Clean data in c_c
cc_clean = {}
for keys, vals in c_c.items():
    if keys.isalpha():
        cc_clean[keys] = vals
# Unpack cc_clean
sher_keys, sher_vals = zip(*cc_clean.items())
# Setup plot
plt.figure(num=None, figsize=(40, 15), dpi=80, facecolor='w', edgecolor='k')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# Plot data in cc_clean
plt.bar(sher_keys, sher_vals)
plt.show()
print()
##################### ASIDE:
#total = 0 # Define var[total] = 0
#for char, num in c_c.items(): # Iterate through dict[c_c] summing the values:
#    total += num
#print("total in c_c:", total)
#print()
##A better method?
#c_c_total = sum(c_c.values())
#print("total in c_c_total:", c_c_total)
#print()
#
#total = 0 # set total = 0
#for char in sherlock: # iterate over the list counting the characters:
#    total += 1
#print("total in sherlock:", total)
#print()
## A better method:
#print(len(sherlock))
######################

my_list_1 = [1, 2, 3, 4]
my_list_2 = ['a', 'b', 'c', 'd']
my_list_3 = ['x', 'y', 'z']
print()
joined = zip(my_list_1, my_list_2)
print("joined         =", joined)
print()
print("type of joined =", type(joined))
print()
joined = list(joined)
print("list(joined)   =", joined)
print()
"""
For lists of different length, zip() will continue until the end of the 
shorter of the lists
"""
print("Zip of 1 and 3 =" list(zip(my_list_1, my_list_3)))
print()
unzip_1, unzip_2 = zip(*joined)
print(f'my_list_1 = {unzip_1}; my_list_2 = {unzip_2}')
print()
###############################################################################
"""
Going vback to the first example, we can use the zip() function to unpack the 
dict[capitals] to yeild the keys and values separately 
"""
print(capitals.items())
print()
country, capital = zip(*capitals.items())

###############################################################################

split_1 = sherlock.split(' ')
#print(split_1)
#print()

#for i in range(len(split_1)):
#    split_1[i] = split_1[i].strip('\n')

clean_1 = []
for word in split_1:
    word = word.strip("\n")
    clean_1.append(word)
##print(clean_1)
#print()
#
split_2 = []
for item in clean_1:
   temp = item.split('\n')
   for temp_item in temp:
       split_2.append(temp_item)

#for word in split_2:
#    print(word)

clean_2 = []
for word in split_2:
    word = word.strip("\n")
    clean_2.append(word)

#for word in clean_2:
#    print(word)

#print(clean_2)

###############################################################################

"""
Tuples!
"""

my_tuple = (1, 2, 3, 4)
my_list = [5, 6, 7, 8]
my_string = 'Austrailia'

print("The first item in my_tuple is:", my_tuple[0])
print("The fourth item in my_tuple is:", my_tuple[3])
print()

print("my_list =", my_list)
my_list[0] = 1000
print("Now my_list =", my_list)
print()
"""
Tuples behave much like strings; They are imutable, so they cannot be changed
after they have been assigned. Thus the following statements will not work:
""" """
my_tuple(0) = 2000
my_string(0) = 'q'
""" """
Summary:
    Lists are MUTABLE
    Dictionaries are MUTABLE
    
    Tuples are IMUTABLE
    Strings are IMUTABLE
"""
###############################################################################
#A list of lists:-
my_list = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
# To access a list withing a list:-
print(my_list[0])
print(my_list[0][1])
print()
###############################################################################

countries = {
"France":        {"Capital": "Paris",           
                  "Language": "French"
                  },
"Spain":         {"Capital": "Madrid",          
                  "Language": "Spanish"
                  },
"United Kingdom":{"Capital": "London",          
                  "Language": "English"
                  },
"India":         {"Capital": "New Deli",        
                  "Language": "Hindi"
                  },
"United Steates":{"Capital": "Washington D.C.", 
                  "Language": "English"
                  },            
"Italy":         {"Capital": "Rome",            
                  "Language": "Italian"
                  },
"Denmark":       {"Capital": "Copenhagen",      
                  "Language": "Danish"
                  },
"Germany":       {"Capital": "Berlin",          
                  "Language": "German"
                  },
"Greece":        {"Capital": "Athens",          
                  "Language": "Greek"
                  },
"Bulgaria":      {"Capital": "Sophia",          
                  "Language": "Bulgarian"
                  },
"Ireland":       {"Capital": "Dublin",          
                  "Language": "Irish"
                  },
"Mexico":        {"Capital": "Mexico City",     
                  "Language": "Spanish"
                  }
            }

print("France", countries["France"])
for key, value in countries.items():
    print(key, value)
print()  
###################
# Accessing nested dictionaries
for key, value in countries.items():
    cap = value["Capital"]
    lang = value["Language"]
    print(f'The capital city of {key} is {cap}, where they speak {lang}')
print()
###################
# Adding items to nested dictionaries
for key, value in countries.items():
    value["Fire"] = "Yes"
print(countries)
print()
###############################################################################
"""
LIST/DICTIONARY COMPREHENSION:
The previous example can be completed using the Counter() method and dictionary
comprehension. This can be done in two lines of cade! Very concise and neet!
"""
from collections import Counter

#print(Counter(sherlock.lower()))

new_dict = dict(Counter(sherlock.lower()))

cln_dict = {k:v for k, v in new_dict.items() if k.isalpha()}
print(cln_dict)
print()
sqr_list = [x**2 for x in range(1,11)]
print(sqr_list)
