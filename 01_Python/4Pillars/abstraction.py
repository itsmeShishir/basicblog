# from abc import ABC, abstractmethod
# class MakeCoffee(ABC):
#     @abstractmethod
#     def make_coffee(self):
#         print("hello making coffee")
# class Espresso(MakeCoffee):
#     def make_coffee(self):
#         print("making espresso")
# class Latte(MakeCoffee):
#     def make_coffee(self):
#         print("making Latte")
        
# exp = Espresso()
# exp.make_coffee()
# exp1 = Latte()
# exp1.make_coffee()


#  first requirement to make abstract class
from abc import ABC, abstractmethod
class Tea(ABC):
    @abstractmethod
    def cooking(self):
        pass
    @abstractmethod
    def gason(self):
        pass
    @abstractmethod
    def materials(self):
        pass
    @abstractmethod
    def Pour(self):
        pass
    def details(self):
        self.cooking()
        self.gason()
        self.materials()
        self.Pour()

class WaterTea(Tea):
    def cooking(self):
        print("cooking")
    def gason(self):
        print("gason")
    def materials(self):
        print("add water and tea bag and sugar")
    def Pour(self):
        print("Pour in glass and then serve")

WaterTeas = WaterTea()
WaterTeas.details()