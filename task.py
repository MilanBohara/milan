"""

Age = int(input("Enter your age : "))

if Age>=16:
    print("Eligible for citizenship",Age)
else:
    print(" Not eligible for citizenship",Age)


if Age%2==0:
    print("Age is even",Age)
else:
    print("Age is odd",Age)

    
"""

"""
#Write a fizzbuzz program. Take a integer input from the user , if input is multiple nof 3 and 5 , give output fizzbuzz, if input of 5, give output Buzz and if the input is multiple of 3 , give output fizz.

number = int(input())

if number % 3 == 0 and number % 5 ==0:
    print("Fizzbuzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
else:
    print(number)

"""



marks =int(input("Enter your marks:"))
if marks>=90:
  print("your grade is A+")
elif marks>=80:
  print("your grade is A")
elif marks>=70:
  print("your grade is B+")
elif marks>=60:
  print("your grade is B")
elif marks>=50:
  print("your grade is C+")
elif marks>=40:
  print("your grade is C")
else:
  print("your grade is F")