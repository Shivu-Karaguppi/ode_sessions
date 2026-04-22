#########Classes and Objects - Day 6#######

# Class = Blueprint to create objects

# class Car:
    
#     def __init__(self,name):
#         self.num_wheels = 4
#         self.engine = True
#         self.metal = "Alumnium"
#         self.name = name

#     @staticmethod
#     def drive():
#         print("Car is driving")

# i20 = Car("I20")
# bmw = Car("BMW")

# # print(i20.num_wheels , i20.engine, i20.name)
# # print(bmw.num_wheels , bmw.engine, bmw.name)

# i20.drive()


######### OOPS  - Day 6#######
# 1. Encapsulation
# 2. Inheritance
# 3. Abstraction
# 4. Polymorphism


# Encapsulation in Python is an OOP concept, wrapping data (variables) and methods (functions) together inside a class, 
# and restricting direct access to some of the object's components to protect the data.


# class Bank:
#     def __init__(self,bal,name):
#         self.__balance = bal ## private variable
#         self.name = name
    
#     def __show_balance(self):
#         return self.__balance
    
#     def show_actualbal(self):
#         return self.__show_balance()

# cust1 = Bank(999,"shiv")
# print(cust1.show_actualbal())



# Inheritance -- in Python is an object-oriented programming concept 
# where one class acquires the properties (variables) and methods of another class.

class Animal:
    def __init__(self, name):
        self.name = name

    def walk_crawl(self):
        print(f"{self.name} can walk or crawl")

    def has_legs():
        print("It has 4 legs")
    
    def no_legs():
        print("It has no legs")

    def crawl(self):
        print(f"Animal can crawl")

class Snake:
    def __init__(self, name):
        self.name = name

    def crawl(self):
        print("Snake can crawl")

class Lion(Snake,Animal):
    def __init__(self, name):
        self.name = name

    def roars(self):
        print("It roars")


# l1 = Lion("lion")
# l1.

    
