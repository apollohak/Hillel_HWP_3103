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
    _health = 100
    _force = 1
    _agility = 1
    _intelligence = 1

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan

    def sleep(self):
        """Метод увеличения здаровья"""
        if self._health < 90:
            self._health += 10
        else:
            self._health = 100

    @classmethod
    def increase_self_skill(cls):
        """Метод увеличения базового навыка"""
        if cls == Mage and Mage._intelligence <= 9:
            Mage._intelligence += 1
        elif cls == Archer and Archer._agility <= 9:
            Archer._agility += 1
        elif cls == Knight and Knight._force <= 9:
            Knight._force += 1

    def __str__(self):
        return f"Имя: {self.name} | Клан: {self.clan} | "

    @property
    def current_stat(self):
        """Метод показывающий текущие характеристики"""
        return f"                   «{self.name}»                   \n"\
               f"Здоровье:{self._health} | Сила:{self._force} | Ловкость:{self._agility} | Интеллект:{self._intelligence}"


class Mage(Unit):
    def __init__(self, name, clan, atribut):
        super().__init__(name, clan)
        self.atr = atribut

    def __str__(self):
        return super().__str__() + f"Тип магии: {self.atr}"


class Archer(Unit):
    def __init__(self, name, clan, atribut):
        super().__init__(name, clan)
        self.atr = atribut

    def __str__(self):
        return super().__str__() + f"Тип лука: {self.atr}"


class Knight(Unit):
    def __init__(self, name, clan, atribut):
        super().__init__(name, clan)
        self.atr = atribut

    def __str__(self):
        return super().__str__() + f"Тип оружия: {self.atr}"


mage = Mage("Дубль'Вэ", "lambda user's", "Воздух")
archer = Archer("Робин", "В худи", "Лук")
knight = Knight("Вейдер", "Орден ситхов", "Меч")
