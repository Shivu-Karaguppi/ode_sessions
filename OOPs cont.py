# +
# Polymorphism in Python is an object-oriented programming concept that means "many forms" — 
# the same function or method name can be used for different types of objects and behave differently.


# comple1 = 1 + 2i
# comple2  = 2 + 4i

# print(comple1 + comple2)
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def __mul__(self, another):
#         real = self.real + another.real
#         img = self.img + another.img
#         return Complex(real, img)

# c1 = Complex(2,3)
# c2 = Complex(4,5)

# c3 = c1 + c2

# print(c3.real, c3.img)



# Abstraction -


class Car :
    def __init__(self):
        self.acc = False
        self.brak = False
        self.Cluch = False


    def start(self):
        self.Cluch = True
        self.acc = True
        print("car has been started")



car1 = Car()
car1.start()



