class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nic = nickname
        self.super = superpower
        self.health_points = health_points
        self.catch = catchphrase

    def vivod(self):
        print(f'name:{self.name}')

    def multiplication(self):
        print(f'heal_point:{self.health_points * 2}')


    def __str__(self):
        return f'nickname: {self.nic}\n' \
               f'superpower: {self.super}\n' \
               f'heal_point: {self.health_points}\n' \
               f'catchphrase: {self.catch}\n' \




    def __phrase__(self):
        print(f'catchphrase:{len(self.catch)}')




Hero = SuperHero('Джорно', 'Kakugo', 'Gold Experience', 10, 'ВУРАВУРАВУРА')
Hero.vivod()
Hero.multiplication()
Hero.__phrase__()
print(Hero)

#класс 1

class DioDaun(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        dio = self.health_points ** 2
        self.health_points = dio

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

dio = DioDaun('Dio Brando', 'Vampire', 'За вардоо', 10, 'stop time')
dio.h()
print(dio)
print(f'Damage: {dio.damage}')
dio.f()
print(f'Fly: {dio.fly}')
dio.phrase()


#класс 2

class DestroyHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        vagonetka = self.health_points ** 2
        self.health_points = vagonetka

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

vagon = DestroyHero('Robāto Ī Ō Supīdowagon', 'SpeedWagon', 'Liana', 20, 'xz')
vagon.h()
print(vagon)
print(f'Damage: {vagon.damage}')
vagon.f()
print(f'Fly: {vagon.fly}')
vagon.phrase()

#

class Villain(DestroyHero):
    monster = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def gen_x(self):...

    def critdamage(self):
        print(f'Crit damage: {self ** 2}')

dragon = Villain('Kaido', 'The strongest being', 'Akuma no Mi ', '200', 'Lets start the greatest war the world has ever seen!')
print(dragon)
dragon.gen_x()
Villain.critdamage(dio.damage)

