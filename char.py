##################################### 12 ######################################

import random

# Создание класса
class Character():
    # Создание конструктора
    def __init__(self, strength_value, hitPoint_value = 10, stamina_value = 10, level_value = 1):
        # Поля класса
        self.hitPoint = hitPoint_value
        self.stamina = stamina_value
        self.strength = strength_value
        self.level = level_value
    # Переменные
    exp = 0
    exp_bar = 10
    baseExpForEnemy = 10
    alive = True
    # Методы класса
    # Геттер на проверку силы
    @property
    def strength(self):
        return self._strength
    # Сеттер на проверку силы
    @strength.setter
    def strength(self, strength_value):
        if strength_value < 0:
            self._strength = 1
        elif strength_value > 5:
            self._strength = 5
        else: 
            self._strength = strength_value
    # Геттер на проверку ХП
    @property
    def hitPoint(self):
        return self._hitPoint
    # Сеттер на проверку ХП
    @hitPoint.setter
    def hitPoint(self, value):
        if value < 0:
            self._hitPoint = 0
        else:
            self._hitPoint = value
              
    # Метод физ атаки
    def atkPhys(self, enemy):
        if enemy.alive:
            if enemy.hitPoint > 0:
                if self.stamina > 3:
                    if random.randint(1,100) <= 90:
                        enemy.hitPoint -= self.strength
                        self.stamina -= 3
                        if enemy.hitPoint <= 0:
                            enemy.alive = False
                            self.__addExp__(self.baseExpForEnemy * enemy.level)
                            return "Враг повержен", f"+{self.baseExpForEnemy * enemy.level}exp"
                        return "Попадание", f"Выносливость {self.stamina}", f"HP Врага: {enemy.hitPoint}"
                    else:
                        self.stamina -= 3
                        return "Промах!", f"Выносливость {self.stamina}", f"HP противника: {enemy.hitPoint}"
                else:
                    return "Недостаточно выносливости", f"Выносливость {self.stamina}", f"HP противника: {enemy.hitPoint}"
        else: 
            return "Враг уже мёртв!"
    # Метод добавляющий опыт 
    def __addExp__(self, addedExp):
        self.exp += addedExp
        self.__addLvl__()
    # Метода добавляющий уровень
    def __addLvl__(self):
        if self.exp >= self.exp_bar:
            self.level += 1
            self.exp -= self.exp_bar
            self.exp_bar *= self.level
            self.__addLvl__()