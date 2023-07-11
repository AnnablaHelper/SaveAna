""" Task 2 [6 points]"""

"""
Write a function 'PrPrCounter' which takes a list of numbers as an argument
and returns True if the number of all prime numbers is prime, 
False otherwise.

You can only use lambda functions and HOFS:
takewhile, dropwhile, zip, filter, map, reduce, enumerate,
any, all, sum.
You are not allowed to use for and while loops.
!WRITE IN ONE LINE!
"""
# def PrPrCounter(lst):
#     return all(len(list(filter(lambda x:all (x % i != 0 for i in range(2,x))and x>1, lst)))  % i != 0 for i in range(2,len(list(filter(lambda x:all (x % i != 0 for i in range(2,x))and x>1, lst))))) 
# print(PrPrCounter([1,2,3,4,5,7]))

'''Write a function that takes a list of numbers and returns a new list containing only the even numbers.'''
# def func(lst):
#     return list(filter(lambda x: x%2 ==0,lst))
# print(func([1,2,3,4,5,6]))
''' Implement a function that takes a list of strings and returns a new list with all strings converted to uppercase.'''














# Aeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee














# def func(lststr):
#     return list(map(lambda str: str.upper(),lststr))
# print(func(['bla','eh','hmm']))
'''Create a function that takes a list of integers and returns the sum of all the numbers.'''
# from functools import reduce
# def func(lst):
#     return reduce(lambda x,y: x + y,lst)
# print(func([1,3,4]))
'''Write a function that takes a list of strings and returns a new list containing only the strings with more than five characters.'''
# def func(lst):
#     return list(filter(lambda x: len(x) > 5, lst))
# print(func(['blaaaa','hm','buu','mmmmmmm']))
'''Create a function that takes a list of integers and returns a new list containing only the prime numbers.'''
# from functools import reduce
# def get_prime_numbers(numbers):
#     return list(filter(lambda x: all(x % i != 0 for i in range(2, x)) and x > 1, numbers))
# print(get_prime_numbers([-10,1,2,3,4,5]))
'''Write a function that takes a list of strings and returns a new list containing the lengths of the strings.'''
# def func(lst):
#     return list(map(lambda x: len(x),lst))
# print(func(['nshi','ahus','pj']))
'''Create a function that takes a list of numbers and returns a new list with each number multiplied by 2.'''
# def func(lst):
#     return list(map(lambda x: x*2, lst))
# print(func([1,2,3,45]))

'''Write a function that takes a list of strings and returns a new list containing only the strings that start with a vowel. '''
# def func(lst):
#     return list(filter(lambda x: x[0]=='o' or x[0] =='u' or x[0]== 'e' or x[0] == 'a' or x[0] == 'i',lst))
# print(func(['abu','jksb','obns','url']))
'''Write a function that takes a list of numbers and returns the sum of all the even numbers.'''
# from functools import reduce
# def func(lst):
#     return sum(list(filter(lambda a: a% 2== 0,lst)))
# print(func([1,2,3,4]))

'''Implement a function that takes two lists and returns a new list containing the pairwise sum of corresponding elements.'''
# def func(lst1, lst2):
#     return list(map(lambda x: x[0] + x[1], zip(lst1, lst2)))
# print(func([1, 2, 3, 4], [1, 2, 3, 4]))

'''. Write a function that takes a list of numbers and returns the product of all the positive numbers.'''

# from functools import reduce
# def func(lst):
#     return reduce(lambda x,y: x * y,list(filter(lambda x: x>0,lst)))
# print(func([1,2,3,-1,-5]))
'''Implement a function that takes a list of strings and returns a new list with only the strings that have more than three characters.'''
# def func(lst):
#     return list(filter(lambda x: len(x) > 3,lst))
# print(func(['hmmmm','br','sububu']))
'''
Certainly! Here are some additional programming problems that you can solve using the remaining Higher-Order Functions (HOFs) in Python, such as `takewhile()`, `dropwhile()`, `zip()`, `enumerate()`, `any()`, `all()`, and `sum()`:
6. Create a function that takes a list of dictionaries and returns a new list with only the dictionaries that have all the specified keys.
7. Write a function that takes a list of strings and returns the count of all strings that have a length greater than five.
8. Implement a function that takes a list of numbers and returns the cumulative sum of the numbers.
9. Create a function that takes a list of dictionaries and returns a new list with only the dictionaries that have at least one key-value pair matching a specific condition.
10. Write a function that takes a list of strings and returns True if any of the strings have a length greater than ten, False otherwise.
These problems can be solved using the remaining HOFs along with lambda functions and appropriate conditions. Have fun solving them!
'''
'''Problem 1: Prime Number Check
Write a function that takes a list of numbers as input and returns True if any of the numbers in 
the list is prime, otherwise False '''
# def func(lst):
#     return any(list(filter(lambda x: all(x % i !=0 for i in range(2,x))and x> 1,lst)))
# print(func([4,6,8]))

''' Problem 2: List Equality Check
Write a function that takes two lists as input and returns True if all corresponding elements 
in the two lists are equal, otherwise False. The lists should have the same length.'''
# def func(lst1, lst2):
#     return all(x == y for x, y in zip(lst1, lst2))
# print(func([0, 2, 3], [1, 2, 3]))

''' Palindrome Check: Implement a function that takes a list of strings as input and returns True 
if any of the strings in the list are palindromes. Use the any() function to solve this problem.'''
# def func(lst):
#     return any(x[0:len(x)] == x[::-1] for x in lst) 
# print(func(['banana',"sul","abba"]))

'''Divisible Check: Create a function that takes a list of numbers and a divisor as input. The function 
should return True if all the numbers in the list are divisible by the given divisor. Use the all() function
to solve this problem.'''
# def func(lst,div):
#     return all(x % div == 0 for x in lst)
# print(func([4,6,10],2))

'''Even-Odd Check: Write a function that takes a list of integers as input and returns True if 
any of the numbers in the list are even. '''
# def func(lst):
#     return any(x % 2 == 0 for x in lst)
# print(func([1,3,5]))

'''Sum of Squares: Create a function that takes a list of numbers and returns the sum of the squares of 
all even numbers in the list. Use the sum() and map() functions in one line.'''
# def func(lst):
#     return sum(map(lambda x: x**2,filter(lambda x: x% 2 == 0,lst)))
# print(func([1,2,3,4]))

'''Character Count: Implement a function that takes a string as input and returns a dictionary containing 
the count of each character in the string. Use the collections.Counter() function in one line.'''
# def func(str):
    # m = list(map(lambda char: str.count(char),str))
    # return dict(zip(str,map(lambda char: str.count(char),str)))
    # return m
# print(func('ababhjja'))

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
    def __init__(self,name,age,id,passcode):
        self.name = name
        self.age = age
        self.__id = id
        self.passcode = passcode

    def getID(self):
        return self.__id
    
    @property
    def passcode(self):
        return self.passcode

class VisitorQueue:
    @staticmethod
    def isValidPasscode(str):
        if len(str) < 8:
            return False
        
        islower = False
        isupper = False
        isdigit = False
        for letter in str:
            if letter.islower():
                islower = True
            elif letter.isupper():
                isupper = True
            elif letter.isdigit():
                isdigit = True
        return islower and isupper and isdigit
    
    def __init__(self):
        self.queue = []

    def add(self,visitor):
        if self.isValidPasscode(visitor.passcode):
            self.queue.append(visitor)
            return True
        else:
            return False
        
    def next(self):
        if len(self.queue) > 0:
            return self.queue[0]
        elif len(self.queue) == 0:
            return None
        
    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        else:
            return False
        
"""
Write a function LonelyElement which takes a non-empty list(where every element
appears twice except for one) as an argument and returns the element that appears only once in this list. 
Hint: Use bitwise operations
"""
# def lonely_element(nums):
#     result = 0
#     for num in nums:
#         result ^= num
#     return result
# nums = [1, 2, 3, 2, 1]
# print(lonely_element(nums))  # Output: 3

"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
Write a function climbStairs, which takes an integer number n as an argument
and returns how many distinct ways you can climb to the top.
Ex:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# def climbStairs(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
    
#     return climbStairs(n - 1) + climbStairs(n - 2)
# print(climbStairs(4))

# def toBinary(decimal):
#     binary=""

#     while(decimal>0):
#         binary+=str(decimal%2)
#         decimal//=2
#     return binary
# print(toBinary(17))

# def toDecimal(binary):
#     return sum(int(2)**count * int(value) for count,value in enumerate(binary))
# print(toDecimal("10001"))

# binary = "10001"
# enum = list(enumerate(binary))
# print(enum)

'''Create Student class, which has 3 attributes: name, id and grades. 'grades' should be a list of tuple,
where first element is grade and second one is credit.
Student class should have constractor which takes name and id as arguments and initializes them.
grades should be [] at first.
Student class should have addGrade method which takes grade and credit and appends tuple to the grades list.
Class should also have getGPA method which calculates and returns students GPA. GPA is equal to sum of grade multiplied
by credit divided by sum of credits.
'''
class Student:
    def __init__(self,name,id,grades):
        self.name = name
        self.id = id
        self.grades = []

    def addGrade(self,grade,credit):
        self.grades.append((grade,credit))
    
    def getGPA(self):
        return sum(i[1] * i[0] for i in self.grades)// sum(i[1] for i in self.grades)
    
'''Create a Course class, which has 3 attributes: name, credits and students. 'students' should be a 
list of Student-s
Course class should have constractor which takes name and credits as arguments and initializes them.
 students should be [] at first.
Student class should have registerStudents method which takes student and appends tuple to the students list.
Class should also have gradeStudents method which adds 4.0 grade to all students.'''

class Course:
    def __init__(self,name,credits):
        self.name = name
        self.credits = credits
        self.students = []
    
    def registerStudents(self,student):
        self.students.append(student)


"""
1. Write class Item . It should have:
   * Variable 'id_counter'
   * Attribute type
   * Property id - It should have only getter.
   * Property price - It should have both getter and setter.
                      Setter should check that price is always
                      assigned positive value.
   * Constructor - that takes type and price as arguments
        * initialise type and price attributes
        * Increment id_counter
        * Assign id_counter to attribute id
   * priceWithDiscount - Static method that takes two arguments: price
                         and discount. Discount is number from 0-100.
                         Method should return a new price after applying
                         discount. Ex.: price=200, discount=30, result=140.
2. Write classes Toy, Book and Painting. Each of them is child class of Item.
   Each class should have:
    * Constructor - that takes price as an argument. Type for each class should
                    be same as their name.
    * applyDiscount - Method that takes discount as an argument and calculates a
                      new price using priceWithDiscount method. Books get 10% additional
                      discount, while Paintings discount is deducted 10%.
"""

# class Item:
#     id_counter = 0
#     def __init__(self,type,price):
#         self.type = type
#         self.price = price
#         Item.id_counter += 1
#         self.__id = Item.id_counter
    
#     @property
#     def get_id(self):
#         return self.__id
    
#     @property
#     def price(self):
#         return self.price
    
#     @price.getter
#     def set_price(self,newprice):
#         if newprice > 0:
#             self.price = newprice
        
#     @staticmethod
#     def priceWithDiscount(price,discount):
#         if discount < 0 or discount > 100:
#             return None
#         else:
#             return (price - (price * discount)//100)
    
# class Toy(Item):
#     def __init__(self,price):
#         super().__init__(type="Toy", price=price)
    
# class Book(Item):
#     def __init__(self,price):
#         super().__init__(type="Book", price=price)
    
#     def applyDiscount(self,discount):
#         newprice = self.priceWithDiscount(self.price,discount + 10)
#         self.price = newprice

# class Painting(Item):
#     def __init__(self,price):
#         super().__init__(type="Paintin", price=price)
    
#     def applyDiscount(self,discount):
#         newprice = self.priceWithDiscount(self.price,discount - 10)
#         self.price = newprice


"""
Write a class Shop, that has:
* items - attribute. List to store items. These items can be instances of Toy, Book or Painting.
* Constructor - that initialises items with empty list.
* addItem - that takes item as an argument and adds to the list
* findItemByID - that takes id as an argument and return object from the list with the given id
                 or None if it does not exist.
* removeItemByID - that takes id as an argument and removes element with such id from the list.
* countItemWithType - that takes type as an argument and counts how many items have given type.
* applyDiscount - that takes discount as an argument and applies it to all items using applyDiscount method.
* totalSum - that calculates total sum of all items.
"""

# class Shop:
#     def __init__(self):
#         self.items = []
    
#     def addItem(self,item):
#         self.items.append(item)
    
#     def findItemByID(self,id):
#         for item in self.items:
#             if item.id == id:
#                 return item 
#         return None
    
#     def removeItemByID(self,id):
#         for item in self.items:
#             if item.id == id:
#                 self.item.remove(item)
    
#     def countItemWithType(self,type):
#         count = 0
#         for item in self.items:
#             if item.type == type:
#                 count += 1
#         return count
    
#     def applyDiscount(self,discount):
#         for item in self.items:
#             item.applyDiscount(discount)

#     def totalSum(self):
#         return sum(item.price for item in self.items)

"""
Write a BinarySearchTree class. BST should consist
of Node class objects. It shoud have 1 attribute:
root - denoting the first element of the list.
The class should have following methods:
* Constructor - It creates root attribute and assigns None at first.
* isEmpty - Returns true if there no elements in the list, false otherwise.
* size - Returns number of elements
* leafCount - Returns number of leaf nodes in the tree.
* contains - Returns true if the given data exists in the list, false otherwise.
* insert - Adds a new element in the tree
"""

class BinarySearchTree:
    def __init__(self,root):
        self.root = None

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    
    def size(self):
        return len(self.root)
    
    def leafCount(self):
        pass




"""
Write a class Course.
Course should have 3 attributes:
   * name - name of the course, public attribute
   * credits - integer number of credits, public attribute
   * advanced - true iff course is advanced, public attribute
   * id - unique id, property
and a class variable 'id_counter'.
Class should have a constructor, that takes name, credits and advanced
as an argument and stores them in attributes. advanced should have
default value - False. 'id_counter' should be used to generate an unique
id - just add 1 to counter and assign it to the attribute.
Class should also have getter property method for the id.

Write a class Student.
Student should have 3 attributes:
   * name - name of the student, protected attribute
   * id - id, hidden attribute
   * enrolledCourses - list of Courses, public attribute
Class should have following methods:
   * constructor - takes name and id and assigns them to attributes. Also assigns
                   an empty list to the enrolledCourses
   * totalCredits - returns sum of credits of all courses.
   * enroll - gets a course as an argument and adds as an enrolled course.
   * isEnrolledAt - gets an id of the course. Returns true if student is enrolled at such course.
   * removeCourseWithID - gets an id of the course and removes it from the enrolled list if it exists.
   * advancedCoursesCount - returns how many advanced course student is registered at.
"""
class Course:
    id_counter = 0
    def __init__(self,name,credits,advanced=False):
        self.name = name
        self.credits = credits
        self.advanced = advanced
        self.__id = Course.id_counter
        Course.id_counter += 1
    
    @property
    def id(self):
        return self.__id

class Student:
    def __init__(self,name,id):
        self._name = name
        self.__id = id
        self.enrolledCourses = []
    
    def totalCredits(self):
        return sum(i.credits for i in self.enrolledCourses)
    
    def enroll(self,course):
        self.enrolledCourses.append(course)
    
    def isEnrolledAt(self,id):
        for i in self.enrolledCourses:
            if i.__id == id:
                return True
        return False
    
    def removeCourseWithID(self,id):
        for i in self.enrolledCourses:
            if i.__id == id:
                self.enrolledCourses.remove(i)
    
    def advancedCoursesCount(self):
        return sum(i for i in self.enrolledCourses if i.advanced == True)
    
'''
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
'''

class Visitor:
    static_passcode = 0
    def __init__(self,name,age,id,passcode):
        self.name = name
        self.age = age
        self.__id = id
        Visitor.static_passcode += 1
        self.passcode = str(Visitor.static_passcode) + passcode
    
    @property
    def getPasscode(self):
        return self.passcode
    
    def getID(self):
        return self.__id
    

class VisitorQueue:
    def isValidPasscode(self,inp):
        if len(inp) < 8:
            return False
        
        isupper = False
        islower = False
        isdigit = False

        for i in inp:
            if i.islower():
                islower = True
            elif i.isupper():
                isupper = True
            elif i.isdigit():
                isdigit = True

        return isupper and isdigit and islower
    
    def __init__(self):
        self.queue = []
    
    def add(self,visitor):
        if self.isValidPasscode(visitor.passcode):
            self.queue.append(visitor)
            return True
        else:
            return False
    
    def next(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None
    
    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        else:
            return False
    
visit1 = Visitor('luka',20,'miyviris','vermitTns8')
visit2 = Visitor('ana',20,'sawyali','Uyvirian6')

vis = VisitorQueue()


for i in range(101):
    visitor = Visitor("LukaSoCool",20,"1" + str(i),"passcT1")
    visitor2 = Visitor("MariSoCute",19,"1" + str(i),"passcT1")
    vis.add(visitor)
    vis.add(visitor2)

print(vis.next().name)
vis.remove()
print(vis.next().name)



