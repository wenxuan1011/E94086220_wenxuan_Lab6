import math
from abc import ABC, abstractmethod


def in_range(enemy, tower):
    x1, y1 = enemy.rect.center
    x2, y2 = tower.rect.center
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance <= tower.get_range():
        return True
    return False


"""
syntax: attack_strategy().attack(tower, enemy_group, cd_count)
It's something like you hire a "Strategist" to decide how to attack the enemy
You can add other ways of attack just by expand this module
"""


class AttackStrategy(ABC):
    """Abstract class of attack method"""
    @ abstractmethod
    def attack(self, enemies, tower, cd_count):
        raise NotImplementedError("Please implement this method")


class SingleAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies, tower, cd_count):
        for en in enemies.get():
            if in_range(en, tower):
                en.health -= tower.get_damage()
                cd_count = 0
                return cd_count
        return cd_count


class AOE(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies, tower, cd_count):
        for en in enemies.get():
            if in_range(en, tower):
                en.health -= tower.get_damage()
                cd_count = 0
        return cd_count


class Snipe(AttackStrategy):
    """(Bonus) eliminate an enemy all in once"""
    def attack(self, enemies, tower, cd_count):
        for en in enemies.get():
            if in_range(en, tower):
                en.health = 0  #因為 enemy 在範圍內被即殺, 故將血量歸零
                cd_count = 0  #將冷卻數值歸零重計
                return cd_count  #因為一次只能殺一隻, 故執行完一次就回傳 cd_count
        return cd_count
        pass




