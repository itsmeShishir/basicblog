print("Conditions") 
# true or false

# Wap to check if a given number is even 
num = 3
if(num%2 == 0): #false
    print("it even")
else:
    print("its odd number")

# wap to check if given age is between 18 to 21 he can drive only bike, if his age is 
# less than 18 he cannot drive any things, if the age is greater than 60 he also cannot 
# drive any things, if his age is between 21 and 59 he can drive both if age is greater than 100 die
age = 400
if(age <=17) :
    print("he or she cannot drive")
elif(age >= 60 and age <100):
    print("he or she aso canot drive bue to age ")
elif (age >=18 and age <=20 ):
    print("he or she can drive only bike")
elif( age >=21 and age<=59):
    print("he or she can drive both boke and car")
else:
    print("he or she dies due to above 100")


# match condition

day = "s"

match day:
    case "Sunday":
        print("its sunday")
    case "Monday":
        print("its monday")
    case "Friday":
        print("its Friday")
    case "saturday":
        print("its saturday")
    case _:
        print("none of tha above")

# 5.Wap to check if the given numbe is palindrome #121 -> 121 

# 6.Write a Python program that checks if a number entered by the 
# user is positive, negative, or zero.

# 7.Write a Python program that checks if a number entered 
# by the user is divisible by both 2 and 3.

# 8.Write an if-else statement to check if a number entered by 
# the user is even or odd.

# 9.Write an if-else statement that checks if the age entered by 
# the user is under 18 and prints "Minor" if true, and "Adult" if false.

# 10.Write an if-else program that checks if a number entered by 
# the user is between 1 and 10, inclusive.

# 11.Write a program using elif that checks the day of the week 
# (entered by the user) and prints "Weekend" for Saturday and Sunday, 
# "Weekday" for Monday to Friday.

#12. Write an if-else statement to determine if a number entered 
# by the user is divisible by 5 or not.

#13. Write an if-elif-else statement to assign grades based on 
# the marks entered by the user (A for 90 and above, B for 75-89, C 
# for 60-74, F for below 60).

# 14.Write an if-else statement that checks whether a user's 
# inputted age is 16 or older and prints "Eligible for driving" 
# if true, otherwise prints "Not eligible for driving."

#15. Write a program that asks the user for a number and prints 
# "Positive" if the number is greater than 0, "Zero" if the number is 0, 
# and "Negative" if the number is less than 0.




