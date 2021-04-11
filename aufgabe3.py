class IScoring():
    def score (self):
        raise NotImplementedError()

class Hardcore(IScoring):
    def score(self, player):
        points = 50*player.x - 5*player.s
        print(points)

class Intermediate(IScoring):
    def score(self, player):
        points = 60*player.x - 4*player.s
        print(points)
class Kinder(IScoring):
    def score(self, player):
        points = 80*player.x - 2*player.s
        print(points)

class Player():
    def __init__(self, name, score: IScoring()):
        self.name = name
        self.x = 5 
        self.s = 10
        self._score = score
    def doAction(self):
        self._score.score(self)


kind1 = Player("Markus", Kinder())
print(kind1.name)
kind1.doAction()
intermediate1 = Player("Klaus", Intermediate())
print(intermediate1.name)
intermediate1.doAction()
hardcore1 = Player("Arne", Hardcore())
print(hardcore1.name)
hardcore1.doAction()