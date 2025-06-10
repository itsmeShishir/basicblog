# Classes 
class Person:
    # Encapsulation 
    def __init__(self, name, age, gender):
        self.name = name
        self._age = age
        self.__gender = gender
    # getter and setter methods
    def getGender(self):
        return self.__gender
    def setValue(self, value):
        self.__gender = value
    
p1 = Person("Shishir", 27, "Male")
print(p1.name)
print(p1._age)
p1.setValue("Female")
print(p1.getGender())