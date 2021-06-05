"""
В компьютерной игре есть юниты (персонажи).
Каждый юнит имеет такие характеристики:
имя
клан
здоровье    (int от 1 до 100. Начальное значение 100)
сила        (int от 1 до 10. Начальное значение 1)
ловкость    (int от 1 до 10. Начальное значение 1)
интелект    (int от 1 до 10. Начальное значение 1)

Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.

Есть три типа юнитов - маги, лучники и рыцари.
У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)

Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
Маг увеличивает интелект.
Лучник увеличивает ловкость.
Рыцарь увеличивает силу.
Написать метод увеличения базового навыка (в родительском классе).

Предложить свою реализацию классов Unit, Mage, Archer, Knight.
"""


class Unit:
    HEALTH = 100
    FORCE = 1
    AGILITY = 1
    INTELLIGENCE = 1

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = Unit.HEALTH
        self.force = Unit.FORCE
        self.agility = Unit.AGILITY
        self.intelligence = Unit.INTELLIGENCE
        self._skill = None

    def sleep(self):
        if self.health < 90:
            self.health += 10
        else:
            self.health = 100

    def increase_self_skill(self):
        if self._skill == "intelligence" and self.intelligence <= 9:
            self.intelligence += 1
        elif self._skill == "agility" and self.agility <= 9:
            self.agility += 1
        elif self._skill == "force" and self.force <= 9:
            self.force += 1

    def __repr__(self):
        return f"Имя: {self.name} | Клан: {self.clan} | "

    @property
    def stat_info(self):
        return f"{self.name}: " \
               f"Здоровье:{self.health} | Сила:{self.force} | Ловкость:{self.agility} | Интеллект:{self.intelligence}"


class Mage(Unit):
    def __init__(self, name, clan, atribut):
        super().__init__(name, clan)
        self.atr = atribut
        self._skill = "intelligence"

    def __str__(self):
        return super().__str__() + f"Тип магии: {self.atr}"


class Archer(Unit):
    def __init__(self, name, clan, atribut):
        super().__init__(name, clan)
        self.atr = atribut
        self._skill = "agility"

    def __str__(self):
        return super().__str__() + f"Тип лука: {self.atr}"


class Knight(Unit):
    def __init__(self, name, clan, atribut):
        super().__init__(name, clan)
        self.atr = atribut
        self._skill = "force"

    def __str__(self):
        return super().__str__() + f"Тип оружия: {self.atr}"


mage = Mage("Дубль'Вэ", "Телекинез", "Воздух")
archer = Archer("Рон", "В яблочко!", "Лук")
knight = Knight("Артер", "Обливион", "Пика")
print(mage)
mage.increase_self_skill()
print(mage.stat_info)
print(archer)
archer.increase_self_skill()
print(archer.stat_info)
print(knight)
knight.increase_self_skill()
print(knight.stat_info)
