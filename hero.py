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