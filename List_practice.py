'''
LIST PRACTICE - https://www.includehelp.com/python/list-programs.aspx
'''

# 1) Python | Program to declare and print a list.

# list = ["ANKAN", 1, 19.85]
# print(list)

# 2) Python program to print list elements in different ways.
# list = ["ANKAN", 1,2, 19.5]

#     #1 (Indexing)
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])

#     #2 (for loop)
# for i in list:
#     print(i)


# 3) Python | Program for Adding, removing elements in the list.

# list = [1,2,3,45]
# #Adding
# list.append(99)
# list.insert(2,989)
# #Removing
# list.remove(989)
# list.clear()
# print(list)


# 4) Python | Program to print a list using ‘FOR and IN’ loop.

# list = []

# for i in range(1,101):
#     list.append(i)

# print(list)


# 5) Python | Program to add an element at specified index in a list.

# list = [1,2,3,45]
# list.insert(2,111)
# print(list)


# 6) Python | Program to remove first occurrence of a given element in the list.

# list = [1,2,13,1,545,1]
# list.remove(1)
# print(list)


# 7) Python | Remove all occurrences a given element from the list.

# list = [1,1,2,1,51,2,1,8]
# for i in list:
#     if i==1:
#         list.remove(i)
# print(list)


# 8) Python | Program to remove all elements in a range from the List.

# list = [15,48,78,98,54,26,35,14,78,45,78,2,56,3]
# for i in list:
#     if i in range(1,51):
#         list.remove(i)

# print(list)


# 9) Python | Program to sort the elements of given list in Ascending and 
# Descending Order.

# list = [15,48,78,98,54,26,35,14,78,45,78,2,56,3]
# list.sort()
# # Ascending
# print(list)
# # Descending
# print(list[-1::-1])


# 10) Python | Program to find the differences of two lists.

# list1 = [1,2,3,4,5]
# list2 = [3,4,5,6,7]

# print(set(list1) - set(list2))


# 11) Python | Program to Print the index of first matched element of a list.

# list = [1,6,2,3,4,5,6,7]
# n = 6
# if n in list:
#     print(list.index(6))


# 12) Python | Program to find the position of minimum and 
# maximum elements of a list.

# list = [15,48,78,98,54,26,35,14,78,45,78,2,56,3]
# print(list)
# list.sort()
# print(f"Max: {list[-1]}")
# print(f"Min: {list[0]}")


# 13) Python | Program to input, append and print the list elements.

# list = []

# for i in range(1,6):
#     n = int(input(f"Enter element no.{i}: "))
#     list.append(n)
# print(f"New List: {list}")


# 14) Python | Program to remove duplicate elements from the list.

# list = [1,6,2,3,3,3,4,2,1,2,4,5,6,7]
# dup = []

# for i in list:
#     if i not in dup:
#         dup.append(i)

# print(dup)


# 15) Python | Program to Create two lists with EVEN numbers and 
# ODD numbers from a list.

# list = [15,48,78,98,54,26,35,14,78,45,78,2,56,3]
# even = []
# odd = []

# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
        
# print(f"Even List: {even}")
# print(f"Odd List: {odd}")


# 16) Python | Program to print all numbers which are divisible
# by M and N in the List.

# m = int(input("Enter first divisor: "))
# n = int(input("Enter second divisor: "))

# list = [1,2,3,4,5,6,78,9,44,2,3,5,1,56,32,58,11,478,7,13,13,56,9,3,13,1,9]
# print(f"Numbers which are divisible by both {m} and {n} are: ")
# for i in list:
#     if i%m==0 and i%n==0:
#         print(i)
    

# 17) Python | Create a list from the specified start to end index of another list.

# list1 = [1,2,4,5,78,9,3,1]
# start = int(input("Enter start index: "))
# end = int(input("Enter end index: "))
# list2 = []

# for i in range(start,end+1):
#     list2.append(list1[i])

# print(list2)



# 18) Python | Create three lists of numbers, their squares and cubes.

# num = [1,2,3,4,5,6,7,8,9]
# sq = []
# cube = []

# for i in num:
#     sq.append(i**2)
#     cube.append(i**3)

# print(f"Numbers: {num}")
# print(f"Squares: {sq}")
# print(f"Cubes: {cube}")


# 19) Python | Create two lists with first half and 
# second half elements of a list.

# list = []
# n = int(input("Enter no.of elements: "))

# for i in range(1,n+1):
#     ele = int(input(f"Enter element no. {i}: "))
#     list.append(ele)

# print(f"List: {list}")
# L = len(list)

# print(f"First Half: {list[0:int(L/2)]}")
# print(f"Second Half: {list[int(L/2):]}")


# 20) Python | Iterate a list in reverse order.

# list = [1,2,4,5,78]
# print(list[-1::-1])


# 21) Python | print list after removing EVEN numbers.

# list = [1,2,3,4,5,6,7,5,2,1,8,52]

# for i in list: 
#     if i%2==0:
#         list.remove(i)
# print(list)


# 22) Python | print list after removing ODD numbers.


# list = [1,2,3,4,5,6,7,5,2,1,8,52]

# for i in list: 
#     if i%2!=0:
#         list.remove(i)
# print(list)


# 23) Python | Input comma separated elements, convert into list and print.

# ele = input("Enter comma separated elements: ")

# list = ele.split(",")
# res = []
# for i in list:
#     res.append(int(i))
# print(res)


# 24) Using List as Stack in Python.
# LIFO

# list = []
# list.append(1)
# list.append(2)
# list.append(3)
# list.append(4)
# list.append(5)
# print(list)

# list.pop()
# # list.pop()
# # list.pop()
# # list.pop()
# # list.pop()
# print(list)



# 25) Python | Extend a list using + Operator.

# list = [1,2,3]
# list_2 = [4,5,6]
# res = list + list_2
# print(res)



# 26) Python program to find N largest and 
# smallest elements from the list



# 27) Python program for various list operations
# Operations:-
#1) Declaring an integer list
#2) Printing the complete list
#3) Printing the first element of the list
#4) Printing ith element of the list
#5) Printing elements within the given indexes
#6) Printing a specific element using negative indexing
#7) Appending an element to the list
#8) Finding the index of a specific element in the list
#9) Sorting the list elements
#10) Popping an element from the list
#11) Removing specified element from the list
#12) Inserting an element at specified index
#13) Extending the list i.e. insert set of element (list) in the list
#14) Reversing list elements


# #1
# list = [2,1,4,5,7,8,9,6,3]

# #2 
# print(list)

# #3
# print(list[0])

# #4
# i = int(input("Enter the index: "))
# print(list[i])

# #5
# for pos in range(2,6):
#     print(list[pos])

# #6
# print(list[-1])

# #7
# list.append(10)
# print(list)

# #8
# ans = list.index(5)
# print(ans)

# #9
# list.sort()
# print(list)

# #10
# a = list.pop(2)
# print(a)

# #11
# list.remove(4)
# print(list)

# #12
# list.insert(2,99)
# print(list)

# #13
# list2 = [91,92,93,94,95,96]
# list.extend(list2)
# print(list)

# # 14
# list.reverse()
# print(list)



# 28) Find the index of an item given a list containing it in Python

# list = [1,2,3,4,56]

# a = list.index(56)
# print(a)


# 29) Remove falsy values from a list in Python
# In python, the values that evaluate to False are considered Falsy values.
# The values are False, None, 0 and "".

# my_list = ["", False,1,2]
# print(list(filter(None,my_list)))


# 30) Python program to remove multiple elements from 
# a list using list comprehension

# list = [1,2,1,2,1,45,7,8,5,3,9,1,1,52]
# new = []
# for i in list:
#     if i not in new:
#         new.append(i)
# print(new)
