"""

#function is a block of code. we used function to reuse the code
#Two types of function
# 1.Build-in function
# 2.User defined function

# syntax :
# def function_name():
#     function body

# function()


# # simple program for user defined function:
# def function_code():
#     print("Hello world")

# function_code()



# #positional arguments-takes value according to proper positional order
# def hello(name,course_name):                #parameters
#     print("Hello" , name, "Welcome to web development training")
#     print(course_name)

# hello('Ram', 'Python with django')      #Arguments



# #keywords arguments-takes values according to keywords
# def hello(name,course_name):                #parameters
#     print("Hello" , name, "Welcome to web development training")
#     print(course_name)

# hello(course_name='Python with django', name='Ram')      #Arguments



# #default arguments
# def hello(name,course_name='python with django'):                #parameters
#     print("Hello" , name, "Welcome to web development training")
#     print(course_name)

# hello(name='Milan',course_name='python with django')



# def sum(a,b):
#     total = a+b
#     return total         #return gives result of function and stop the execution of function
# result = sum(2,3)
# print(result)





# def sum(*args):
#     total = args[0]+args[1]+args[2]
#     return total
# result = sum(2,3,5)
# print(result)   



# #arbitrary arguments - *args
# def sum(*args):
#     total =0
#     for n in args:
#         total+=n
#     return total 
# result = sum(2,3,5)
# print(result)



#
def hello(**kwargs):                #parameters
     print("Hello" , kwargs['name'], "Welcome to web development training")
     print(kwargs['course_name'])

hello(name='Ram',course_name='Python with data science', another_course='Python with data science')      #Arguments


#scope of variable
#global variable -> which can accesible 
"""
l = float(input("Enter a length : "))
w = float(input("Enter a width : "))

def area():
     #local variable -> that is defined inside the function and cannot accessible from outside the function. iths scope is only around the declered function.
     h = float(input("Enter a height : "))
     #global area_of_object
     area_of_object = l*w
    # volume = area_of_object * h
     return area_of_object


def volume():
     h = float(input("Enter a height : "))
     v = l*w*h
     return v
result = area()
result_volume = volume()
print(result)
print(result_volume)


# # lambda function : the function without name. it is used for instant use of its one-time uses.lambda keyword is used..

# x = lambda a, b : a + b
# sum = x(2,3)
# print(sum)

# x = lambda a, b : a * b
# area = x(2,3)
# print(area)

# recursive function - function calling itself again and again
# def factorial(n):
#   if (n==0 ):
#     return 1

#   else:
#     return n * factorial(n-1) # calling same function, called Recursion

# print(factorial(3))
# print(factorial(4))
# print(factorial(5))


# #filter()
# filtered_factorials = list(filter(lambda x: x != 1, factorials))
# print(filtered_factorials)

# #map()
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# numbers = [3, 4, 5]
# factorials = list(map(factorial, numbers))
# print(factorials)


