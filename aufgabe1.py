class Hero ():
    def __init__ (self,name):
        self.name = name
        self.level = 1

class Mage (Hero):
    def __init__ (self):
        self.max_mana = 100
        self.current_mana = 100

class Bruiser (Hero):
    pass

class Krieger(Bruiser):
    def __init__ (self):
        self.max_rage = 100
        self.current_rage = 0

class Waldläufer(Bruiser):
    pet = "Hausschwein"

class  Priester (Mage):
    pass

class Zauberer (Mage):
    pass

zauberer1 = Zauberer("Gandalf")
priester1 = Priester("Harald")
krieger1 = Krieger("Joachim")
waldläufer1 = Waldläufer("Klaus")

from pprint import pprint
print(vars(priester1))
print(vars(krieger1))
print(vars(zauberer1))
print(vars(waldläufer1))
