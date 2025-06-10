# type conversion
# str() -> string
# int() -> integer
# float() -> float

a = "245"
b = int(a)
print(type(b))
print(b)

#b = int  = 245
c = float(b)
print(type(c))
print(c)

# c = 245.0 = float
d = str(c)
print(type(d))
print(d)

# Operators and operands 
# operator -> sign + , -
# operands -> VAlues 

# 1. Arthmetic Operators -> -,+,*,/,%, //, **
print(5+5) # 10
print(5-5) # 0
print(5*5) # 25
print(25/5) # 5.0
print(36%5) # 1
print(2**3) #8
print(8.8//2) # 4 

# 2. Asignmant Operators -> =, +=, -=, /=, *=, %=, //=, **=
a = 30
a+=30
# a = a+30
print(a)
a-=30
# a = a-30
print(a)
a*=30
# a = a*30
print(a)
a/=30
# a = a/30
print(a)
a//=30
# a = a//30
print(a)
a = 30
a%=3
print(a)

# 3. Comparison Operators >, < , >=, <=, ==, !=
print(5>5) #False
print(5<5) #False
print(5>=6) #False
print(5<=5) #True
print(5!=6) #True
print(5!=5) #Flase
print(5==6) #False


# 4. Logical Operator -> and , or , not
# and gate
print(True and True) # True
print(False and True) # false
print(True and False) # false
print(False and False) # false

# or gate
print(True or True) # True
print(False or True) # True
print(True or False) # True
print(False or False) # false

# not gate
print(not True) # false
print(not False) # True


# Membership Operators -> in and not in
a = "shishir"
print("b" not in a) #ture
print("b" in a) #False
print("h" in a) #true

# identifier Operatior -> is and is not 
a = "shishir"
print(a is "shishir") #True
print(a is not "shishir") # false

# Bitwise Operator -> |, &
print(5 & 6)
print(5 | 6)

# Ternary Operators
age = 27
print("he or she can drive") if (age > 18) else print("he or she cannot drive")