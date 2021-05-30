"""
В компьютерной игре есть юниты (персонажи).
Каждый юнит имеет такие характеристики:
имя
клан
здоровье    (int от 1 до 100. Начальное значение 100)
сила        (int от 1 до 10. Начальное значение 1)
ловкость    (int от 1 до 10. Начальное значение 1)
интелект    (int от 1 до 10. Начальное значение 1)
"""


class Units:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.dexterity = 1
        self.intelligence = 1

    def healing(self):
