#Imports

import math
from numpy import asarray

print(type(math))


# #Lists and Loops

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    lucky = False
    for i in nums:
        if i % 7 == 0:
            lucky = True
    
    return lucky
      
#     solution using list comprehension
#     def has_lucky_number(nums):
#     return any([num % 7 == 0 for num in nums])


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
#     Solution one
#     list = []
#     for i in L:
#         if i > thresh:
#             list.append(True)
#         else:
#             list.append(False)
#     return list

#list comprehension version
    return [element > thresh for element in L ]


def menu_is_boring(meals):
# """Given a list of meals served over some period of time, return True if the
# same meal has ever been served two days in a row, and False otherwise.
# """
#     solution using memory
#     prev = ""
#     for i in meals:
#         if i == prev:
#             return True
#         else:
#             prev = i
#     return False

# solution using range to index list
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False



#Example of Monte Carlo Method - need to expand
# def estimate_average_slot_payout(n_runs):
#     """Run the slot machine n_runs times and return the average net profit per run.
#     Example calls (note that return value is nondeterministic!):
#     >>> estimate_average_slot_payout(1)
#     -1
#     >>> estimate_average_slot_payout(1)
#     0.5
#     """
#     avgList = []
#     for i in range(n_runs):
#         avgList.append(play_slot_machine()) - 1
    
#     return sum(avgList) / len(avgList)


party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1


def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None    
    else:
        return L[1]


#Strings and Dictionaries

#use this backslash \' to type singlequotes within singlequote strings.
singlequote = '\'' 
print('What\'s up?')

# this backslash \" for doubleQuotes within doubleQuotes

doubleQuotes = "\""
print("That's \"cool\"")

#normal backslash
backslash = "\\" 
#"\"
print("Look, a mountain: /\\")


#creates a newline within the string
"\n"

print("1\n2 3")
#1
#2 3

#tripleqoutes create newlines by default when typing
print("""hello
world""")

# Indexing
planet = 'Pluto'
planet[0]

# Slicing
planet[-3:]

#Looping over strings:
[char+'! ' for char in planet]

#Strings are immutable

# Searching for the first index of a substring
claim = "Pluto is a planet!"
claim.index('plan')
#output: 11

#str.split() turns a string into a list of smaller strings, breaking on whitespace by default. 
#This is super useful for taking you from one big string to a list of words.

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year,month,day)

# str.join() takes us in the other direction, 
# sewing a list of strings up into one long string, using the string it was called on as a separator.

print('/'.join([month, day, year]))

print(' 👏 '.join([word.upper() for word in words]))

#concatenation works the same in python as swift by using "+" to join strings

planet + ",we miss you"

position = 9
planet + ", you'll always be the " + str(position) + "th planet to me."

#Build strings using format() method for cleaner code
"{}, you'll always be the {}th planet to me.".format(planet, position)

# the Python values we want to insert are represented with {} placeholders, 
# and .format even converts the int for us
# you can even preform calculations within .format

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

# 2 decimal points {:.2}   
# 3 decimal points, format as percent {:.3%}     
# separate with commas {:,}

print("""{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). 
It is home to {:,} Plutonians.""".format(planet, pluto_mass, pluto_mass / earth_mass, population,))

#you can also refer to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

#Dictionaries , built in data structure for mapping keys to values
numbers = {'one':1, 'two':2, 'three':3}
# Values are accessed via square bracket syntax similar to indexing into lists and strings.
print(numbers["one"])
#adding a new key value pair or changing an existing one is as easy as assigning it:
numbers["eleven"] = 11
numbers["three"] = 5

#heres an example of Dictionary Comprehensions with syntax similar to list comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#creates a dictionary using keys from the planet list with their initial as the value
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

# The in operator tells us whether something is a key in the dictionary

print("Saturn" in planet_to_initial)

#for loops will loop over dictionary keys
for k in numbers:
    print("{} = {}".format(k, numbers[k]))

#can also a list of all the keys or values with dict.keys or dict.values, respectively
allKeys = planet_to_initial.keys() 
print(allKeys)

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))

#dict.items lets you iterate over both keys and values simultaneously 
# (In Python jargon, an item refers to a key, value pair)

for planet,initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet,initial))



def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return zip_code.isdigit() and len(zip_code) == 5

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    list = []
    for i, doc in enumerate(doc_list):
        #split string into list of words
        words = doc.split()
        #remove unwanted punctuation and lowercase all characters
        readyForSearch = [word.strip(",.").lower() for word in words]
        #if it matches keyword add index to return list
        if keyword.lower() in readyForSearch:
            list.append(i)
    return list

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]

word_search(doc_list, "casino")

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    dict = {}
    for key in keywords:
        dict[key] = word_search(doc_list,key)
    return dict  



#hands are lists of strings following rules of blackjack
#here we write a helper function to make the next function cleaner
def checkHand(hand):
    aceCount = 0
    handSum = 0
    for card in hand:
        if card in ['J','K','Q'] :
            handSum += 10
        elif card == "A":
            aceCount += 1
        else:
             handSum += int(card) 

#add aces for now: this is the smallest count we can get from this hand
    handSum += aceCount
# "Upgrade" aces from 1 to 11 as long as it helps us get closer to 21
# without busting
    while handSum + 10 <= 21 and aceCount > 0:
        # Upgrade an ace from 1 to 11
        handSum += 10
        aceCount -= 1
    return handSum
        
        
            



def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand1 = checkHand(hand_1)
    hand2 = checkHand(hand_2)
    
    return hand1 <= 21 and (hand1 > hand2 or hand2 > 21)
    