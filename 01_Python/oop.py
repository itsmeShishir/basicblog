# OOP -> object oriented Programming
# class -> blueprint
# properties -> attributes
# object -> instance of class
# Methods -> function inside the class
# 4 Pillars
# 1. Abstraction -> hide the implementation
# 2. Encapsulation -> hide the data
# 3. Inheritance -> inheritance of properties
# 4. Polymorphism -> multiple forms

# Classes 
class Person:
    # Properties  -> attributes -> variables
    name = "shsihir"
    age = 27

    # Methods -> functions
    def getDetails(self):
        print(f"my name is {self.name} and age is {self.age}")


    @classmethod
    def abcd(cls):
        return cls.name

print(Person.abcd())

person1 = Person()
print(person1.name)
print(person1.age)
print(person1.getDetails())

# wap to create a class with person name and age , gender and a method to
# get the details and print the name and age, gender of the person
class Person:
    # Properties  -> attributes -> variables
    name = "shsihir"
    age = 27
    gender = "male"

    # Methods -> functions
    def getDetails(self):
        return f"my name is {self.name} and age is {self.age}, and gender is {self.gender}"
person1 = Person()
print(person1.name)
print(person1.age)
print(person1.gender)
print(person1.getDetails())


class DynamicPerson:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def getDetails(self):
        return f"my name is {self.name} and age is {self.age}, and gender is {self.gender}"

p3 = DynamicPerson("ram", 23, "male")
print(p3.getDetails())
p4 = DynamicPerson("Shyam", 20, "male")
print(p4.getDetails())
p5 = DynamicPerson("Sita", 20, "female")
print(p5.getDetails())


class Run:
    def __init__(self):
        print("run")
r1 = Run()
# wap to create a class with person name and age , gender and a method to
# get the details and print the name and age, gender of the person using constructor


