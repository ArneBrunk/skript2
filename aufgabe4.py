from random import random

dmg = random.randrange(1.10)
class Monster_Zustand ():
    def fight():
        pass
class Mon_Normal(Monster_Zustand()):
    def fight():
        pass
class Mon_Rage(Monster_Zustand()):
    def fight():
        pass
class Mon_Dead(Monster_Zustand()):
    def fight():
        pass

class Monster ():
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.zustand = Mon_Normal()
class Hero():
    def __init__(self,name):
        self.name = name
        self.hp = 50
    def fight(self):
        pass