# Function in python def
def abc():
    print("my name is shishir baandari")
abc()  
abc()  
abc()  
abc()  
abc()  
abc()  

# wap to print your name and age function name should be myDetails

def myDetails():
    print("my name is shishir baandari and age is 27")
myDetails()  

# fucntion parameter and arguments
def myDetail(name, age):
    print(f"my name is {name} and age is {age}")
myDetail("shanskar", "17")  
myDetail("Shishir", "27")  
myDetail("Shreeya", "16") 

# wap to print the area of rectangle using function and parameter l*b
# 2, 5 = 10
# 7, 10 = 70

def rectangle(l, b):
    print(l*b)

rectangle(2,5)
rectangle(7,10)

# Function with and without parameter in python
# function with parameter but no return type
def rectangle(l, b):
    print(l*b)
rectangle(2,5)
rectangle(7,10)
# function with no parameter and no return type
def rectangle():
    print(5*5)

rectangle()
# function with parameter,  with return type
def rectangle(l, b):
   return l*b

print(rectangle(7,10))
# function with no parameter but with return type
def rectangle():
   return 2*2
print(rectangle())

#wap to print the area of square using function types 
# and parameter and return and no return (print)


# parameter type in function 
# default parameter
def DefaultParameter(l, b = 20):
   return l*b
print(DefaultParameter(7))
print(DefaultParameter(8, 10))
# Names parameter
def NamesParameter(l, b):
    print("hello")
    return l*b
    print("bye")

print(NamesParameter(b = 8, l = 10))
#args
def Argsi(*args):
    print(args)
Argsi(1,2,3,4,5)

#Kwargs
def Argsio(**Kwargs):
    print(Kwargs)
Argsio(
)


# WAP to print your favorite color using a function.

# WAP to add two numbers using a function and print the result.

# WAP to check if a number is even or odd using a function.

# WAP to find the square of a number using a function with a return type.

# WAP to greet the user with "Good Morning" using a function without parameters.

# WAP to print all numbers from 1 to 5 using a for loop.

# WAP to print the sum of all numbers from 1 to 10 using a loop.

# WAP to print only the odd numbers from 1 to 15.

# WAP to count the number of elements in a list using a loop.

# WAP to create a set with 3 fruits and print them one by one using a loop.

# WAP to create a dictionary with two key-value pairs and print only the keys.

# WAP to create a function that returns the cube of a number.

# WAP to create a function that takes a number and checks if it is greater than 10.

# WAP to create a tuple of 4 numbers and print them using a loop.

# WAP to create a list of your 3 favorite foods and print them using a loop.

