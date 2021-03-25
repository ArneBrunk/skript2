import random
class Monster_Zustand ():
    def fight(self, hero):
        pass
class Mon_Normal(Monster_Zustand):
    def fight(self,hero):
        self.dmg = random.randrange(1,5)
        self.hero = hero
        self.hero.hp -= self.dmg
        print("The monster dealt", self.dmg, "damage.")
class Mon_Rage(Monster_Zustand):
    def fight(self,hero):
        self.dmg = random.randrange(5,10)
        self.hero = hero
        self.hero.hp -= self.dmg
        print("The monster dealt", self.dmg, "damage.")
class Mon_Dead(Monster_Zustand):
    def fight(self,hero):
        print("Stop hit me, I am already dead :(!")

class Monster ():
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.zustand = Mon_Normal()
    def fight(self,hero):
        self.zustand.fight(hero)
        
class Hero():
    def __init__(self,name):
        self.name = name
        self.hp = 50
    def fight(self, monster):
        self.dmg = random.randrange(1,10)
        self.monster = monster
        self.monster.hp -= self.dmg
        print("You hit me ",self.dmg," points")
        print("Monster-HP: ",  self.monster.hp, "Hero-HP:",self.hp )
        if self.monster.hp <1:
            self.monster.zustand = Mon_Dead()
            print("Aaargh")
        elif self.monster.hp < 1:
            self.monster.zustand = Mon_Rage()
            print("Ich bin wütend!")
     

held1 = Hero("King Arthur")
monster1 = Monster("Gozilla")
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)
held1.fight(monster1)
monster1.fight(held1)