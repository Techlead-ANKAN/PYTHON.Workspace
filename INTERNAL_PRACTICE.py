'''
w3resuorce--> Basic Part-1
'''

# 1) Write a Python program to print the following string in a specific format (see the output). 
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
# Output :
# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

# str = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 

# print("Twinkle, twinkle, little star,\n  How I wonder what you are!\n   Up above the world so high,\n   Like a diamond in the sky.\nTwinkle, twinkle, little star,\n  How I wonder what you are" )


# 2)  Write a Python program to get the Python version you are using.
# "python --version" in the terminal


# 3)  Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# import datetime
# now = datetime.datetime.now()
# print("Current Date and Time: ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))



# 4) Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# r = float(input("Enter radius of the circle: "))
# pi = 3.14
# area = pi*r**2
# print(f"Area of the circle is: {area}")



# 5) Write a Python program which accepts the user's first and last name and 
# print them in reverse order with a space between them.

# first = input("Enter your first name: ")
# last = input("Enter your last name: ")

# res = last +" "+ first
# print(res)



# 6) Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list 
# and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# data = input("Enter sequence numbers: ")
# print(f"List: {list(data)}")
# print(f"Tuple: {tuple(data)}")



# 7)  Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

# file_name = input("Enter file name: ")
# i = file_name.index(".")
# print(f"Extension name: {file_name[i+1:]}")



# 8) Write a Python program to display the first and last colors from the following list. 

# color_list = ["Red","Green","White" ,"Black"]
# print(f"First Colour: {color_list[0]}")
# print(f"Last Colour: {color_list[-1]}")



# 9) Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

# date = (11, 12, 2014)
# print(f"The Examination will start from: {date[0]}/{date[1]}/{date[2]}")



# 10) Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

# n = int(input("Enter number: "))
# print(f"n+nn+nnn = {n+n**2+n**3}")



# 11)  Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

# def built_in():
#     print('''
# Function	           Description
# abs()	           Returns the absolute value of a number
# all()	           Returns True if all items in an iterable object are true
# any()	           Returns True if any item in an iterable object is true
# ascii()	           Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()	           Returns the binary version of a number
# bool()	           Returns the boolean value of the specified object
# bytearray()	       Returns an array of bytes
# bytes()	           Returns a bytes object
# callable()	       Returns True if the specified object is callable, otherwise False
# chr()	           Returns a character from the specified Unicode code.
# classmethod()      Converts a method into a class method
# compile()	       Returns the specified source as an object, ready to be executed
# complex()	       Returns a complex number
# delattr()	       Deletes the specified attribute (property or method) from the specified object
# dict()	           Returns a dictionary (Array)
# dir()	           Returns a list of the specified object's properties and methods
# divmod()	       Returns the quotient and the remainder when argument1 is divided by argument2
# enumerate()	       Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()	           Evaluates and executes an expression
# exec()	           Executes the specified code (or object)
# filter()	       Use a filter function to exclude items in an iterable object
# float()	           Returns a floating point number
# format()	       Formats a specified value
# frozenset()	       Returns a frozenset object
# getattr()	       Returns the value of the specified attribute (property or method)
# globals()	       Returns the current global symbol table as a dictionary
# hasattr()	       Returns True if the specified object has the specified attribute (property/method)
# hash()	           Returns the hash value of a specified object
# help()	           Executes the built-in help system
# hex()	           Converts a number into a hexadecimal value
# id()	           Returns the id of an object
# input()	           Allowing user input
# int()	           Returns an integer number
# isinstance()	   Returns True if a specified object is an instance of a specified object
# issubclass()	   Returns True if a specified class is a subclass of a specified object
# iter()	           Returns an iterator object
# len()	           Returns the length of an object
# list()	           Returns a list
# locals()	       Returns an updated dictionary of the current local symbol table
# map()	           Returns the specified iterator with the specified function applied to each item
# max()	           Returns the largest item in an iterable
# memoryview()	   Returns a memory view object
# min()	           Returns the smallest item in an iterable
# next()	           Returns the next item in an iterable
# object()	       Returns a new object
# oct()	           Converts a number into an octal
# open()	           Opens a file and returns a file object
# ord()	           Convert an integer representing the Unicode of the specified character
# pow()	           Returns the value of x to the power of y
# print()	           Prints to the standard output device
# property()	       Gets, sets, deletes a property
# range()	           Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()	           Returns a readable version of an object
# reversed()	       Returns a reversed iterator
# round()	           Rounds a numbers
# set()	           Returns a new set object
# setattr()	       Sets an attribute (property/method) of an object
# slice()	           Returns a slice object
# sorted()	       Returns a sorted list
# staticmethod()	   Converts a method into a static method
# str()	           Returns a string object
# sum()	           Sums the items of an iterator
# super()	           Returns an object that represents the parent class
# tuple()	           Returns a tuple
# type()	           Returns the type of an object
# vars()	           Returns the __dict__ property of an object
# zip()	           Returns an iterator, from two or more iterators
# ''')

# built_in()



# 12) Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

# import calendar

# y = int(input("Enter Year: "))

# for i in range(1,13):
#     print(calendar.month(y, i))



# 13) Write a Python program to print the following 'here document'. Go to the editor
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)



# 14)  Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# date1 =  (2014, 7, 2)
# date2 =  (2014, 7, 11)

# print(f"No.of days between 2 dates are: {date2[2] - date1[2]}")



# 15) Write a Python program to get the volume of a sphere with radius 6.
# r = float(input("Enter radius of a sphere: "))
# area = (4/3)*3.14*r**3
# print(area)


# 16)  Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.


# n = int(input("enter a number: "))

# if n > 17:
#     print(f"Double of the absolute difference between the given number and 17 is: {(n-17)*2}")
# else:
#     print(f"Difference between the given number and 17 is: {17 - n}")



# 17)  Write a Python program to test whether a number is within 100 of 1000 or 2000.



# 18)  Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))

# if n1==n2==n3:
#     print(f"Result: {(n1+n2+n3)*3}")
# else:
#     print(f"Result: {n1+n2+n3}")



# 19)  Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged

# str = input("Enter a string: ")
# word = "Is "
# if str.startswith("Is"):
#     print(f"No change: {str}")
# else:
#     print(f"After change: {word + str}")



# 20)  Write a Python program to get a string which is n (non-negative integer) copies of a given string
# str = input("Enter a string: ")
# n = int(input("Enter non-negative integer to make that no.of copies of the given string: "))
# space = " "
# if n<0:
#     print("Please enter a non_negative integer")
# else:
#     print(f"Result:{(str + space)*n}")



# 21)Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
# n = int(input("Enter a number: "))
# if n%2==0:
#     print(f"The number {n} is Even.")
# else:
#     print(f"The number {n} is Odd.")



# 22)  Write a Python program to count the number 4 in a given list

# list = [4,4,4,4,4,4,4,4]
# count = 0
# for i in list:
#     if i==4:
#         count += 1
# print(f"No.of times 4 is repeated in the lis is: {count}")



# 23) Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2.

# str = input("enter a string: ")
# n = int(input("Enter no.of copies: "))
# space = " "
# if len(str)<=2:
#     print(f"Result: {(str + space)*2}")
# else:
#     print(f"Result: {str[0:2] * 2}")




# 24)  Write a Python program to test whether a passed letter is a vowel or not.
# str = input("Enter a letter: ")
# vowel = ["a", "e", "i", "o", "u"]


# if str.lower() in vowel:
#     print("Vowel")
# else:
#     print("Not Vowel")



# 25)  Write a Python program to check whether a specified value is contained in a group of values. 
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


# n = int(input("Enter number: "))
# list = [1,2,3,4,5,6,7,8,9]
# if n in list:
#     print("True")
# else:
#     print("False")



# 26) Write a Python program to create a histogram from a given list of integers.


# 27) Write a Python program to concatenate all elements in a list into a string and return it.
# list = [1,2,3,4,5]
# string = " "
# for i in list:
#     string = string + str(i)
# print(string)



# 28) Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing 
# if any numbers that come after 237 in the sequence. 
# Sample numbers list :

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# even = []
# for i in numbers:
#     for i in range(1, 238):
#         if i%2==0:
#             even.append(i)

# print(even)



# 29)Write a Python program to print out a set containing all the colors from color_list_1
#  which are not present in color_list_2. 
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

# list1 = set(["White", "Black", "Red"])
# list2 = set(["Red", "Green"])
# res = []
# for i in list1:
#     if i not in list2:
#         res.append(i)

# print(f"Final List: {res}")




# 30) Write a Python program that will accept the base and height of a triangle and compute the area
# b = int(input("Enter base of triangle: "))
# h = int(input("Enter height of triangle: "))

# area = 0.5 * b * h
# print(area)



# 31)  Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# while x%y!=0:
#     rem = x % y
#     x = y
#     y = rem
# print(rem)



# 32) Write a Python program to get the least common multiple (LCM) of two positive integers.

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))

# if x>y:
#     max = x
# else:
#     max = y

# while (True):
#     if (max % x == 0   and  max % y == 0):
#         print(max)
#         break
#     max += 1



# 33) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# if a==b or b==c or c==a:
#     print(f"Sum = 0")
# else:
#     print(f"Sum = {a+b+c}")



# 34) Write a Python program to sum of two given integers. However, 
# if the sum is between 15 to 20 it will return 20.

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# sum = a+b

# if sum in range(15,21):
#     print(f"Sum = 20")
# else:
#     print(f"Sum = {sum}")



# 35) Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# if a==b:
#     print("True")
# elif (a+b) == 5:
#     print("True")
# elif (a-b) == 5:
#     print("True")
# else:
#     print("Fuck You  .!..")



# 36) Write a Python program to add two objects if both objects are an integer type.

# a = 25
# type_a = type(a)
# b = 25.0
# type_b = type(b)

# if type_a == type_b:
#     print(f"Sum of {a} and {b} = {a+b}")
# else:
#     print("Different Data Type")



# 37) Write a Python program to display your details like name, age, address in three different lines.
# name = input("Enter your name: ")
# address = input("Enter you address: ")
# age = int(input("Enter age: "))
# print(f'''Name:- {name},\nAddress:- {address},\nAge:- {age}''')



# 38)  Write a Python program to solve (x + y) * (x + y). Go to the editor
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# print(f"{(x+y)*(x+y)}")



# 39) Write a Python program to compute the future value of a specified principal amount, rate of interest,
#  and a number of years. Go to the editor
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
# FV = P(1 + r/n)^nt


# amt = int(input("Enter Principal Amount: "))
# int_ = float(input("Enter Rate of Interest: "))
# years = int(input("Enter Time Interval: "))

# fv = amt*(1+(0.001*int_))**years
# print(fv)



# 40)  Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# print(f"First Co-ordinate: {x1,y1}")

# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))
# print(f"First Co-ordinate: {x2,y2}")

# dist = (((x1+x2)**2) + ((y1+y2))**2)**0.5
# print(f"Distance between {x1,y1} and {x2,y2} is: {dist}")



# 41) Write a Python program to check whether a file exists.



# 42) Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
 
# import struct
# print(struct.calcsize("P")*8)


# 43) Write a Python program to get OS name, platform and release information.

# import platform
# import os
# print(f"Operating System: {os.name}")
# print(f"Platform: {platform.system()}")
# print(f"Release Date: {platform.release()}")


# 44) Write a Python program to get OS name, platform and release information.

# import site;
# print(site.getsitepackages())



# 45) Write a python program to call an external command in Python.

# from subprocess import call
# call(["ls", "-l"])



# 46) Write a python program to get the path and name of the file that is currently executing.

# import os
# print(f"Current file name: {os.path.realpath(__file__)}")



# 47) Write a Python program to find out the number of CPUs using.

# import multiprocessing
# print(multiprocessing.cpu_count())



# 48)  Write a Python program to parse a string to Float or Integer.

# str = input("Enter a string: ")
# print(f"In Float: {float(str)}")
# print(f"In Integer: {int(str)}")



# 49) Write a Python program to list all files in a directory in Python

# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/home/stduents') if isfile(join('/home/students', f))]
# print(files_list)



# 50) 