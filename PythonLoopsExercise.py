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
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
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