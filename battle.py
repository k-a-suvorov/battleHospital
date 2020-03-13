from random import randint
from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init()

class Soldier:
    def makeHealth(self, value):
        self.health = value

    def makeKick(enemy):
        enemy.health -= randint(1, 5) + randint(1, 5)

class Battle:
    def battle(self, u1, u2):
        print(Fore.CYAN, Style.BRIGHT + f'Добро пожаловать в \"BattleHospitak\"! ver.0.1 written by Opsis')
        print(Fore.CYAN, Style.BRIGHT + f'Наблюдайте за битвой пациента и доктора, вы бессильны им помешать в этой битве!')
        while u1.health > 0 and u2.health > 0:
            sleep(2)
            n = randint(1,2)
            if n == 1:
                Soldier.makeKick(u2)
                print(Fore.GREEN, Style.BRIGHT + 'Доктор пробует лечить пациента от неизвестной болезни')
                print(Fore.RED, Style.BRIGHT + f'Пациент сопротивляется, здоровья осталось: {u2.health}')
                print()
            else:
                Soldier.makeKick(u1)
                print(Fore.GREEN, Style.BRIGHT + 'Пациент атакует доктора симптомами неизвестной болезни')
                print(Fore.RED, Style.BRIGHT + f'Доктор пробует самолечиться, здоровья осталось {u1.health}')
                print()

        if u1.health > u2.health:
            self.result = 'UDoctor Win'
        elif u2.health > u1.health:
            self.result = 'Patient Win'

    def whoWin(self):
        print(self.result)

doctor = Soldier()
patient = Soldier()
doctor.makeHealth(100)
patient.makeHealth(100)

b = Battle()
b.battle(doctor, patient)
b.whoWin()
