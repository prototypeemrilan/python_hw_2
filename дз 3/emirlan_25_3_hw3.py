class Bank:
    bank = 'bank'

    def __init__(self,name,balance):
        self._name = name
        self._balance = balance

    def __str__(self):
        return (f'name:{self._name}'
                f'balance:{self._balance}')


    def moneyX(self):
        plus = int(input('канча акча хотите добавить:?'))
        self._balance += plus


    def _kill(self):
        self._balance = 0

    def __jackpot(self):
        self._balance *= 10


    def _copybalance(self):
        hero._balance+= hero2._balance


hero = Bank('Amira', 60000)
hero2 = Bank('Emka ', 70000)


print(hero)
hero.moneyX()
# hero._kill()
# hero._Bank__Jackpot()
# hero._copybalance()
print(hero)