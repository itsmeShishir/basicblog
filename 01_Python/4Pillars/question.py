# Write a program to check whether a number is even or odd.
one = int(input("enter the  1st number"))
two = int(input("enter the 2nd number"))
three = int(input("enter the 3rd number"))
# ODD or even number
if(one % 2 == 0):
    print("its even number")
else:
    print("its odd number")
# Write a program to swap two numbers using a variable process.
temp = None
one, two = two, one
print(one, two)

# Write a program to find the largest number among three numbers entered by the user.
if(one > two and one > three):
    print(one)
elif(two > one and two > three):
    print(two)
else:
    print(three)
# Create a function that takes two numbers as input and returns their sum.
def add(a,b):
    return a+b
print(add(one, two))
# Write a function to check if a number is prime.
def isPrime(num):
    if (num==1):
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
            else:
                return num

if(isPrime(one)):
    print("its prime number")
else:
    print("its not prime number")

# Create a function that returns the factorial of a number using recursion.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
# Write a function that takes a list of numbers and returns the maximum number.
def abcdef(arrs):
    if not arrs:
        return None
    
    vars = arrs[0]
    for i in arrs[1:]:
        if i > vars:
            vars = i
    return vars

print(abcdef([1,2,3,4,5]))


# Create a function that checks whether a given string is a palindrome.
def slicing(strs):
    if(strs == strs[::-1]):
        return "its palindrome"
    else:
        return "its not palindrome"
    
print(slicing("malayalam"))
print(slicing("nepla"))
print(slicing("mom"))

# Create a class Car with attributes like brand, model, and year. Add a method to display the car details.

# Create a class Rectangle with methods to calculate area and perimeter. Use a constructor to initialize 
# length and breadth.



