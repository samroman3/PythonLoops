#Lists and Loops

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

