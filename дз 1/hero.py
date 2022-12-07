class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nic = nickname
        self.super = superpower
        self.health = health_points
        self.catch = catchphrase

    def vivod(self):
        print(f'name:{self.name}')

    def multiplication(self):
        print(f'heal_point:{self.health * 2}')


    def __str__(self):
        return f'nickname: {self.nic}\n' \
               f'superpower: {self.super}\n' \
               f'heal_point: {self.health}\n' \
               f'catchphrase: {self.catch}\n' \




    def phrase(self):
        print(f'catchphrase:{len(self.catch)}')




Hero = SuperHero('Джорно', 'Kakugo', 'Gold Experience', 10, 'ВУРАВУРАВУРА')
Hero.vivod()
Hero.multiplication()
Hero.phrase()
print(Hero)


# переменная = отрибут
# магический метод = __Init__
# функция = метод
# self = обязательный отрибут, ссылка
# объект это экземпляр
