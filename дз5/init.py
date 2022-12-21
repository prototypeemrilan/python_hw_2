from classss import Hero
from classss import Hero_super

hero = Hero('Спидвагон', 'Леаны')
hero.vizivaem()

hero2 = Hero_super('Дио', 'Вампир')
hero2.nickname()
hero2.__str__()
hero2.phrase()
print(hero2)