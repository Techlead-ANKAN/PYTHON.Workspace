# 1)
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(0,6):
#     for j in range(1,i+1):
#         print("*",end = " ")

#     print()


# 2)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i, end = " ")
#     print()


# 3)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end= " ")
#     print()


# 4)
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# for i in range(5,0,-1):
#     for j in range(6,i,-1):
#         print(i,end = " ")
#     print()


# 5)
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1


# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end = " ")

        
#     print()


# 6)
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j, end = " ")
#     print()


# 7)
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10

# for i in range(1,6):
#     for j in range(1,i+1):
#         print((j*2), end = " ")
    
#     print()


# 8) 
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# num = 1
# for i in range(1,5):
#     for j in range(1,i+1):
    
#         print(num, end = " ")
#         num +=1
#     print()


# 9) 
# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9

# for i in range(1,6):
#     for j in range(1,i+1):
#         print((i+j-1), end = " ")

#     print()


# 10) 
# 1
# 3 5
# 5 7 9
# 7 9 11 13
# 9 11 13 15 17

# for i in range(1,6):
#     t = i-1
#     for y in range(1,i+1):
#         print(t+i, end = " ")
#         t +=2
#     print()