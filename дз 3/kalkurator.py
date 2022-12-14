# class Calculator:
#     def __init__(self, x):
#         self.x = x

#     def __add__(self, other):
#         return self.x + other.x

#     def __sub__(self, other):
#         return self.x - other.x

#     def __mul__(self, other):
#         return self.x * other.x

#     def __truediv__(self, other):
#         return self.x / other.x

# y1 = Calculator(24)
# y2 = Calculator(8)
# add = y1+y2
# sub = y1-y2
# mul = y1*y2
# truediv = y1/y2
# print(add, sub, mul, truediv)

# class Calcurator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


#     def __add__(self,):
#         print(self.x + self.y)

#     def __sub__(self):
#         print(self.x - self.y)

#     def __mul__(self):
#         print(self.x * self.y)

#     def __truediv__(self):
#         print(self.x / self.y)


# x = int(input('Введите любое число:'))
# y = int(input('Введите любое 2 число:'))

# calcur = Calcurator(x, y)

# print("1 = +")
# print("2 = -")
# print("3 = *")
# print("4 = %")

# any = int(input("Выберите действие"))

# if any == 1:
#     print(calcur.__add__())
# elif any == 2:
#     print(calcur.__sub__())
# elif any == 3:
#     print(calcur.__mul__())
# elif any == 4:
#     print(calcur.__truediv__())
# else:
#     print("Выбирети 4 действи, других действи нет")
