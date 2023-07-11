""" Task 3 [6 points]"""

"""
Write a class Visitor.
Vistor should have 4 attributes:
   * name - name of the visitor, public attribute
   * age - age of the visitor, public attribute
   * id - id of the visitor, hidden attribute
   * passcode - unique passcode of the visitor, property
Class should have a constructor, that gets all 4 value as arguments
and stores them as attributes. Class also should have 'getID' function
that returns id and property getter function for passcode.


Write a class VisitorQueue.
VisitorQueue class should have one static method = 'isValidPasscode'. This
function takes string as an argument and checks if it is valid code. Code is
valid if:
    1. It contains at least 8 characters
    2. All characters are either upper or lower case letters or numbers.
    3. There is at least 1 upper case letter, at least 1 lower case letter
       and at least 1 number.
Class shouls also have one attribute - a list to store visitors, which are in queue.
Furthermore, class should have following methods:
* constructor - To initialise visitor queu attribute with empty list.
* add - Gets visitor as an argument. Visitor's passcode should be checked with 'isValidPasscode'
        function. If visitor has a valid passcode, add him/her at the end of the queue and return
        True. If visitor does not have a valid passcode, do not add him/her into the queue and 
        return False.
* next - Returns the next visitor in the queue. Next visitor is one in the begining of the queue.
         If there is no one in the queue, return None.
* remove - Removes the visitor from the begining of the queue. If visitor is removed from the queue
           function should return True. If there is no one to remove, function should return False.

"""

class Visitor:
    pass

class VisitorQueue:
    pass