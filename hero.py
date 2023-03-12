class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name(self):
        return self.name()

    def Hp2x(self):
        return self.health_points * 2

    def __str__(self):
        return f'Прозвище героя: {self.nickname}\n' \
               f'Суперсила: {self.superpower}\n' \
               f'Здоровье героя: {self.health_points}'

    def __len__(self):
        return len(f'{self.catchphrase}')


hero = SuperHero('Tony Stark', 'Ironman', 'Iron armor', 100, 'I\'m Ironman')
print(hero.name)
print(hero.nickname)
print(hero.superpower)
print(hero.health_points)
print(hero.catchphrase)


class Hero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        print(f'Здоровье нашего героя: {self.health_points ** 2}')

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')

    # def crit(self):
    #     return self.damage ** 2


class SecondHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        print(f'Здоровье нашего героя: {self.health_points ** 2}')

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')


thor = Hero('thor', 'bog', 'grom', 200, 'хз', damage=300)
cap = SecondHero('cap', 'pon', 'hello', 150, 'ladno', damage=100)

thor.hp()
thor.fly_sky()
cap.hp()
cap.fly_sky()


class Villian(SecondHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        SuperHero.people = 'monster'

    def gen_X(self):
        pass

    def crit(self, hero):
        return hero.damage ** 2


tanos = Villian('tanos', 'tanka', 'kamni', 900, 'pon')
print(Villian.crit(tanos, thor))
print(Villian.crit(tanos, cap))
