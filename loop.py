
"""

a = 1                                                      #while loop
while a <= 10:
    print('Loop runs for', a, 'as a value of a')
    a +=1





# example of for loop over fruits list
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
for x in fruits:
  print(x)


#for loop can be executed over strings as well
count = 0
for x in "A brown fox quickly jumps over the lazy dog":
  print(x)
count += 1
print(count)


"""

# # range() to get range of number :

# for i in range(1, 21):
#     if i % 3 == 0  and i % 5 ==0:
#         print("Fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



# # nested loop is loop inside loop
        
# for i in range(1, 11):
#     print("Muliplication table: ",i)
#     for j in range(1, 11):
#         print(i, "*",j, "=", i*j)



# a =['red' , 'blue','orange', 'black']
# b =['football', 'vollyball', 'basketball', 'baseball']

# for i in a:
#     for j in b:
#         print(i,j, end=" ") 



# x = 0
# while x<=10:
#     j = 0
#     while j <=10:
      
#         print(x, "*",j, "=", x*j)
#         j +=1
#     x +=1

#  # while loop inside for loop
# for i in range (1,11):
#   print("Multiplication table :", i)
#   j = 1
#   while j <=10:
#       print(i,'*',j,"=",i*j)
#       j+=1


# for loop inside while loop
i = 1
while i <= 10:
    print("Multiplication table:", i)
    for j in range(1, 11):
        print(i, '*', j, "=", i * j)
    i += 1


