'''
STRINGS:- https://www.includehelp.com/python/string-programs.aspx
'''

# 1) Python | Declare, assign and print the string (Different ways).

# # 1
# str1 = input("Enter any string: ") # Assign
# print(str1)
# # 2
# str2 = "Hi I am Ankan"  # Assign
# print(str2)


# 2) Python | Access and print characters from the string.

# str = input("Enter any string: ")
# L = len(str)

# print(str.index("A"))


# 3) Python program to print a string, 
# extract characters from the string.

# str = input("Enter a string: ")
# L = len(str)

# i = int(input("Enter the index: "))
# j = int(input("Enter last index: "))

# print(str[i])
# print(str[i:j])
# print(str[j])



# 4) Python | Program to print words with their length of a string.

# str = input("Enter any string: ")
# list = str.split(" ")

# for words in list:
#     print(f"{words}, {len(words)}")


# 5) Python | Print EVEN length words.

# str = input("Enter any string: ")
# list = str.split(" ")

# for words in list:
#     if (len(words))%2==0:
#         print(f"{words}, {len(words)}")


# 6) Python | Count vowels in a string.

# str = input("Enter a string: ")
# vow = ["a","e","i","o","u"]
# count = 0
# for char in str:
#     if char.lower() in vow:
#         count += 1

# print(f"No.of Vowels: {count}")


# 7) Python | Passing string value to the function.

# def show_msg(str):
#     print(str)

# show_msg("Hello World!")


# 8) Python | Create multiple copies of a string by 
# using multiplication operator.

# str = input("Enter string: ")
# n = int(input("Enter no.of copies: "))
# res = str  + " "
# print(f"{res * n} ")


# 9) Python | Appending text at the end of the 
# string using += Operator.

# str = input("Enter string: ")
# a1 = input("enter string to append: ")
# a2 = input("enter string to append: ")
# a3 = input("enter string to append: ")
# a4 = input("enter string to append: ")

# print(str + " " +a1 + a2 + a3 + a4)


# 10) Python | Concatenate two strings and assign in another 
# string by using + operator.

# str1 = input("Enter string: ")
# str2 = input("Enter string: ")

# str = str1 + " " + str2
# print(str)


# 11) Python | Check if a substring presents in a string using 'in' operator

# str = input("Enter a string: ")
# sub = input("Enter a string: ")

# if sub in str:
#     print("Present")
# else:
#     print("Not Present")


# 12) Python | Assign Hexadecimal values in the string and print it in the string format

# str1 = "\x41\x42\x43\x44"

# print(str1)

    
# 13) Python | How to print double quotes with the string variable?
# str = input("Enter string: ")

# print("\"%s\"" % str)


# 16) Python program to reverse a given string (5 different ways)

# str = input("Enter string: ")
# L = len(str)

# 1
# print(str[L::-1])

# 2
# rev = " "
# for i in range(L-1, -1, -1):
#     rev = rev + str[i]
# print(rev)


# 18) Python program to reverse a string using stack and reversed method

# str = input("Enter string: ")
# char = []
# for i in str:
#     char.append(i)
# print(char)


# 19) Python program for slicing a string

# str = input("Enter string: ") 

# print(str[0:3])


# 20) Python program to repeat M characters of a string N times

# str = input("Enter string: ")
# M = input("Enter the charcter: ")
# N = int(input("Enter no.of times: ")) 

# for char in str:
#     if char == M:
#         for i in range(0,N):
#             print(M)


# 21) Python program to swap characters of a given string 
# such that the first and the last characters have been exchanged.

# str = input("Enter string: ")
# L = len(str)
# f = str[0]
# m = str[1:-1]
# l = str[-1]
# res = l + m + f
# print(res)


# 22) Python program to remove a character from a specified index in a string

# str = input("Enter string: ")
# pos = int(input("Enter index: "))

# print(str.replace(str[pos],""))


# 23) Python program for adding given string with a fixed message

# name = input("Enter name: ")
# greet = "Hello"
# print(greet,name)


# 25) Python | Write a function to find sum of two integral numbers in string format.

# n1 = input("Enter number: ")
# n2 = input("Enter number: ")

# print(int(n1)+int(n2))


# 26) Python program to check whether a string contains a number or not

# str = input("Enter string: ")
# flag = False
# for char in str:
#     if char.isdigit():
#         flag = True
    
# if flag:
#     print("Present")
# else:
#     print("Not Present")


# 27) Python program to find the matched characters in a given string

# str = input("Enter string: ")

# c = input("Enter charcter: ")
# flag = False
# for char in str:
#     if c == char:
#         flag = True

# if flag:
#     print("Matched")
# else:
#     print("Not Matched")