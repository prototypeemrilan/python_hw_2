class A:
    def __init__(self,name):
        self.name = name

class B:
    def __init__(self,age):
        self.age = age

class C(A):
    def nickname(self):
        print(f'имя - {self.name}')

class D(B):
    def kb(self):
        print(f'Он родился в {2022 - self.age} году')

class G(C, D):
    def __init__(self, name ,age):
        C.__init__(self, name)
        D.__init__(self, age)

g = G('Тима', 20)
g.nickname()
g.kb()



