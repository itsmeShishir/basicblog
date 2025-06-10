def abc():
    return "my name is shishir baandari"
print(abc())
# wap to print your name and age
def Details(name, age):
    return f"my name is {name} and age is {age}"
print(Details("Shishir", "27"))
print(Details("ram", "20"))

# Parameter Type in function
# named parameter
def Details(name, age):
    return f"my name is {name} and age is {age} {1+2}"
print(Details(age = "17", name = "hari"))
# positional parameter -> jun postion me pass garna
def Details(name, age):
    return f"my name is {name} and age is {age}"
print(Details("27", "shishir"))
# default parameter
def Details(name, age = 40):
    return f"my name is {name} and age is {age}"
print(Details("shishir", 50))
print(Details("Laxman"))
# variable length parameter -> *args
def abc(abc, *hello):
    print(abc, hello)
abc(1,2,3,4,5,6) #tuple
# keyword variable length parameter -> **kwargsw
def abcd(**hello):
    print(hello)
abcd(a = 1, b = 2, c = 3)
#wap to that print all the odd number between 0 to 40 using function
def odd(a,b):
    for i in range(a,b):
        if i % 2 != 0:
            print(i)
            

odd(0, 41)

# Recursion -> a Function which call it itself is called Recursion
# def abc():
#     print("hello")
#     abc()
# abc()

# factorial of a number 5 ! = 5 * 4 * 3 * 2 * 1 = 120

def Recursions(n):
    if n== 1:
        return 1
    else:
        return n * Recursions(n-1)
print(Recursions(5))
# Print n to 1 without loop.
def LoopsOne(n):
    if n==1:
        return 1
    else:
        print(n)
        return LoopsOne(n-1)
print(LoopsOne(5))
# Mean of Array. -> sum / length
def Means(arr, n):
    if n==1:
        return arr[0]
    else:
        return arr[n-1]+ Means(arr, n-1)
    
def Sum(arr):
    total = Means(arr ,len(arr))
    return f"Mean : {total/ len(arr)}"
arr = [1,2,3,4,5]
print(Sum(arr))


# Sum of n  natural numbers.
def all(n):
    if n ==1:
        return 1
    else:
        return n + all(n-1)
print(all(5))

def adds(a,b):
    print(a+b)
adds(1,2)


# lmanda function -> annonymous function
x = lambda a,b : a+b
print(x(1,2))

b = lambda : print("hello")
b()

# wap to print the area of rectangle using lambda function and parameter l*b
# 2, 5 = 10
# 7, 10 = 70

