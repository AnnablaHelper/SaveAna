""" Task 4 [6 points]"""

"""
Write a function LonelyElement which takes a non-empty list(where every element
appears twice except for one) as an argument and returns the element that appears only once in this list. 
Hint: Use bitwise operations
"""

def lonelyElement(lst):
    lonelyElement = 0
# sheeesh
    for n in lst:
        lonelyElement ^= n
    return lonelyElement

print(lonelyElement([1,2,1,3,3]))
    
