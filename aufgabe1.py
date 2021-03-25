class Hero ():
    def __init__ (self,name):
        self.name = name
        self.level = 1

class Mage (Hero):
    max_mana = 100
    current_mana = 100

class Bruiser (Hero):
    pass

class Krieger(Bruiser):
    max_rage = 100
    current_rage = 0

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