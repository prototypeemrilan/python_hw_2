class Hero:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability

    def vizivaem(self):
        print(f'Имя героя: {self.name}\n'
              f'Абилка перснонажа: {self.ability}')

class Hero_super(Hero):
    def __init__(self,name,ability):
        super().__init__(name,ability)

    def nickname(self):
        print(f'Имя человека: {self.name}')


    def __str__(self):
        print(f'Абилка человека: {self.ability}')

    def phrase(self):
        print(f'this is my house')
