class Calculator:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        return self.x / other.x

y1 = Calculator(24)
y2 = Calculator(8)
add = y1+y2
sub = y1-y2
mul = y1*y2
truediv = y1/y2
print(add, sub, mul, truediv)