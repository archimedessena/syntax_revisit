# def brush_up():
#   a = int(input('Enter: '))
#   b = int(input('Enter: '))
#   return a + b

# print(brush_up())


# def even_number():
#    num = int(input('Enter: '))
#    if num % 2 == 0:
# print(num, "is an even number")
# else:
# print(num, "is not an even number")


# print(even_number())


# def quadratic_equation(a, b, c):


# my_list = [2, 3, 4, 5, 6, "food", "drink", "drugs", "pants", 5, 6, 6]
# a = my_list.append(my_list[0])
# b = my_list.append(my_list[5])
# c = my_list.append("gari")
# print(my_list)
# print(my_list.count(6))


for i in range(0, 20):
    my_list = i

# for i in my_list1: # want to see all items in the list
#    print(i)

# check if a specific item is in the list
# for i in my_list1:
#    if 30 in my_list1:
#        print("It is part of the list")
#        break
#    else:
#        print("It is not part of the list")

# if 10 in my_list1:
#    print("It is part of the list")
# else:
#    print("It is not part")


# def check_list():
#    num = input("Enter a number: ")
#    if num in my_list1:
#        print(num, "is not part of the list")
#    else:
#        print(num, "is part of the list")
#    return num


# check = check_list()
# print(check)


# def my_check():
#    nums = input("Enter a number: ")
#    for i in my_list1:
#        if i == nums:
#            print(nums, "is found")
#            break
#        else:
#            print(nums, "is not a valid number")
#    return nums


# p = my_check()
# print(p)


# def extra_check(a):
#    if a in my_list1:
#        print(a, "is available")
#    else:
#        print(a, "is not available")
#    return a
#
#
# extra_checks = extra_check(10)
# print(extra_checks)

# function for password creation, saving and retrieval


# for loop with ranges

# for i in range(0, 6):
#    print(i)

# num = []
# for i in range(5, 10, 1):
#    nums = i
#    num.append(nums) #how to use append in python
#    print(num)

nums = [2, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# how to use index in python
# print(nums)
# add_ = int(input("Enter an index between 0 and 9:"))
# add_num = int(input("Enter the number you want to add:"))
# nums.insert(add_, add_num)
# print(nums)


# nums.remove(1000)
# print(nums)

# print(nums.pop(-5))

# for i in range(20, 0,  -2):
#  print(i)

# my_list = []
# for i in range(0, 5):  # Work on this code later
#   my_list.append(i)
# print(my_list)
# user_guess = input("Please enter a number between 0 and 4: ")
# for i in my_list:
#    if user_guess in my_list:
#        print("found at position", my_list.index(user_guess))
#        break
#    else:
#        print("Number does not exist")


# How are calendars built


from random import *

# for i in range(5):
#    print(random.randint(0, 2))


def greetings():
    name = input("What is your name:?")
    print("Hi, {}".format(name))
    print(f"Hi, {name}")


# getting the index of a random element
import random

letters = ["a", "b", "c", "d", "e", "f"]
random_index = random.randint(0, len(letters) - 1)


# where randrange is used
letters = ["a", "b", "c", "d", "e", "f"]
random_index = random.randrange(len(letters))

# print(letters[random_index])


# The first method that we can make use of to select more than one element at random is random.sample(). It produces a sample, based on how many samples we'd like to observe:

letters = ["a", "b", "c", "d", "e", "f"]

# print(random.sample(letters, 3))


# Selecting Random n Elements with No Repetition


def select_random_Ns(lst, n):
    random.shuffle(lst)
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i : i + n])
    return result


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(select_random_Ns(lst, 2))


# Lotto game
lotto = []


def lotto_machine():
    numbers_one_to_ninety = range(1, 91)
    for i in numbers_one_to_ninety:
        lotto.append(i)
        lot = random.choice(lotto)
    return lot


l = lotto_machine()
# print(l)


# try and  except
def spam(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError as n:
        print("Error: Invalid Number: {}".format(n))


# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


def only_name():
    s = input("Enter your name: ")
    if not s.isalpha():
        print("It should not be number")
        only_name()
    else:
        print(s)


# only_name()


# name = input('Please enter your name: ')
# try:
# name_int = int(name)
# name_float = float(name)
# print('Please enter an alphabetical name.')
# except:
# pass
# print(name)


# s = input("Enter your name: ")
# if any(char.isdigit() for char in s):
# print("Please do not include digits in your name.")


# s = input("Enter your name: ")
# if s.isdigit():
# print("Your name cannot be a number.")


# num = input('Enter your favorite number:')
# try:
# num_alphabet = str(num)
# num_float = float(num)
# except ValueError as v:
# print('Enter a valid number: {}'.format(v))


# list
names_of_footballers = ["kofi", "Marthino", "Marthines", "Marth", "Mar", "Pluto"]
names_of_footballers[-2]
names_of_footballers[2]
names_of_footballers[0]

# slicing of list
# print(names_of_footballers[0:-1])
names_of_footballers[0:3]
names_of_footballers[0:3]
names_of_footballers[0:3]

names = names_of_footballers[:]
names.append("Archimedes")
# print(names[-1])

# reallocating
names[-1] = "Kofi"
names[3] = "Abigail"
# print(names)
# print(len(names))

combined_list = names + names_of_footballers
# print(combined_list)

naming = [1, 2, 3, 4]
del naming[0]
# print(naming * 2)


supplies = ["pens", "pencils", "books", "laptop", "mouse"]

# for i, supply in enumerate(supplies):
# print('Index {} in supplies is: {}'.format(str(i), supply))


age = [34, 20, 15, 45, 22]


# for i, n in zip(age, names_of_footballers):
# print('{} is {} year old'.format(n, i))

verify = "Marthino" in names_of_footballers
# print(verify)

# print(34 in age)

# favourites_now = ['CR7', 'Mega', 'Mini', 'm', 'k']

# names_of_footballers = favourites_now
# print(names_of_footballers)

# a, b = 'Archimedes', 'Cracklyn'
# b = a
# supply, footballers, num = ['pens', 'pencils', 'books', 'laptop', 'mouse'], ['Marthino', 'Marthines', 'Marth', 'Mar', 'Pluto'], 234

# print(supply + footballers)
# footballers = supply
# supply = footballers
# print(footballers)
# print(supply)


n = names_of_footballers.sort()

# print(supplies.index('pens'))

# [] = list
# () = tuple
# {} = dict

suppliers = sorted(supplies)
# print(suppliers)

list_ = ["pens", "pencils", "mouse", "computer", "lessons"]

tuple_ = ("books", "laptop", "mouse", "computer", "lessons")

# dict_ = {'dogs', 'pencils', 'books', 'laptop', 'lessons'}

# dict_lessons = {'pens', 'pencils', 'books', 'laptop', 'mouse', 'computer', 'lessons'}

late = [
    {"name": "Archimedes"},
    {"name": "Kofi"},
    {"name": "Cosmos"},
    {"married": "Brights"},
]

# print(list_[1])
# print(len(tuple_))

# for i in tuple_:
# print(i.upper())
# print(late[3].keys())

# dictionary
dic = (
    {"name": "Archimedes", "Mark": 90, "Level": 400, "Programme": "BSc Mathematics"},
    {"name": "Edwin", "Mark": 80, "Level": 300, "Programme": "BSc Accounting"},
    {"name": "Godsway", "Mark": 77, "Level": 200, "Programme": "BSc English"},
    {
        "name": "Celestine",
        "Mark": 700,
        "Level": 100,
        "Programme": "BSc Fashion and Design",
    },
)


def tested():
    for item in dic:
        name = item.values()
        print(name)


def tested1():
    for item in dic:
        properties = item.keys()
        print(properties)


dic_in_list = [
    [
      {"name": "Archimedes", "Mark": 90, "Level": 600, "Programme": "MPhil Computer Science"
       }
      ],
    [
      {"name": "Edwin", "Mark": 80, "Level": 500, "Programme": "MSc Accounting"
       }
      ],
    [
      {"name": "Godsway", "Mark": 77, "Level": 200, "Programme": "BSc English"
       }
      ],
    [
        {
            "name": "Celestine",
            "Mark": 700,
            "Level": 100,
            "Programme": "BSc Fashion and Design",
        }
    ],
]


# for i in dic_in_list():
#for i in dic_in_list:
 # print(i[0]["name"], i[0]["Level"], i[0]["Programme"])

# tested()

# mini database
# Pull details about someone
# name of person
# given to a function


current = {"name": "Archimedes", "Mark": 90, "Level": 400, "Programme": "BSc Mathematics"}

#for k, v in current.items():
 # x, y = k, v
 # print(x, y)
  #print(x)
  #print(y)


#for k in dic.keys():
#  x = k
#  for v in dic.values():
#    y = v
#    
#  print(x)
#  print(y)

# merging dic

# creating a set

set_ = {1, 2, 4, 6, 8, 5, 10, 8, 8, 8, 9}
set_1 = set([3, 5, 7, 9, 11, 3, 5, 7])

#print(set_1.intersection(set_))
#print(set_1.union(set_))
#print(set_1.isdisjoint(set_))
#print(set_1.pop())



# List comprehension
num = [1, 2, 3, 4, 5]

v = [i - 5 for i in num]
t = [i ** 2 for i in num]
#print(v)
#print(t)
#print(num[0:-3])

#set_comprehension  
set__ = {"ABCF", "DEG", "Archimedes"}

com = {i.partition("d") for i in set__}
#print(com)

# dictionary comprehension
dic_com = {"Girl":"Ama", "Age":"30", "School":"UCC"}

loop = {v: k for k,v in dic_com.items()}
#print(loop)


#name = input("What is my name?:")
#name1 = "Archimedes"
#print(f"My name is {name1} not {name}.")


def name_guess():
    name = input("What is my name?:")
    name1 = "Archimedes"
    if name == name1: 
        print("That is my name,", name )
    else: 
        print("My name is {} not {}".format(name1, name))
        
        
#name_guess()


# later
#import logging
#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#
#logging.debug('Start of program')
#
#def factorial(n):
#    logging.debug
#   total = 1 


# lambda 
#add = lambda y,z: y + z ** 4
#print(add(3,4))
#
#print((lambda x,y: x + y*4)(4,5))


# lambda in a function
def make_adder(n):
    return lambda x: x + n


# creating a function out of another function
plus_1 = make_adder(3)

#print(plus_1(30))


def make_multiplication(a, b, c):
    return lambda x, y, z: x + y + z + a * b * c


make = make_multiplication(1, 2, 3)
#print(make(1, 2, 63))

# an if statement in a single line 
age = 38
#print("That is not his age" if age <= 4 else "that is correct")

# passing multiple arguments into a function
# use *args(which means arbitrary), that is by packing the remaining arguments as tuple
def multiple(*args):
    return [x*2 for x in args]


#print(multiple(2, 3, 4, 5, 6, 7))


def more_args(*args):
    for i in args:
        if i == "Archimedes":
            print("It is found,")
        else:
            print("It is not part of the list")
            

#v = more_args("Sena", "Celestine", "Godsway", "Archimedes")
#print(v)


# putting in key value pairs using **kwargs
def key_value_pair(**kwargs):
    for i in kwargs:
        pass
        #print(i)
    
prin = key_value_pair(name = 'Archimedes', age = 35, programme = 'BSc Mathematics')
    
    
# How to run code if only it is a script
#if __name__ == "__main__":
  #  main()   
    

# Python program to execute function directly
def add(a, b):
    return a + b

add(400, 70)
# Now if we want to use that module by importing, we have to comment out our call, instead we can write like  this in cal.py
    
import cal
vb = cal.add(400, 70)
#print(vb)
