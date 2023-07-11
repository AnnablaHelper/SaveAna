""" Task 1 [6 points]"""

"""
Write 'sortValues' function, that takes arbitrary many arguments,
sorts them in decreasing order and returns the resulting sequence
in list.

Sorting sould be done using insertion sort algorithm (described bellow).
Solution that uses other algorithm or built in functions (like sort
and sorted) will not be accepted.

Insertion sort is a simple sorting algorithm: We assume that list is
divided into 2 imaginary parts - left, sorted part and right, unsorted
part. Values from the unsorted part are picked one by one and placed at
the correct position in the sorted part.

To sort a list with N elements follow these steps: 
1. Iterate from 1st to Nth element. 
2. For each element do following:
    2.1. Compare the current element to its predecessor. 
    2.2. If the current element is smaller than its predecessor,
         Swap them and go back to step 2.1.
    2.3. If the current element is greater than its predecessor,
         leave it and continue iteration to the next element.
"""

def sortValues(*args):
    values = list(args)
    length = len(values)

    for i in range(1, length):
        current_value = values[i]
        j = i - 1

        while j >= 0 and values[j] < current_value:
            values[j + 1] = values[j]
            j -= 1

        values[j + 1] = current_value

    return values

    
