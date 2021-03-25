class IScoring():
    def score (self):
        raise NotImplementedError()

class Hardcore(IScoring):
    def __init__(self):
        self.x = 5 
        self.s = 10
    def score(self):
        points = 50*self.x - 5*self.s
        print(points)

class Intermediate(IScoring):
    def __init__(self):
        self.x = 5 
        self.s = 10
    def score(self):
        points = 60*self.x - 4*self.s
        print(points)
class Kinder(IScoring):
    def __init__(self):
        self.x = 5 
        self.s = 10
    def score(self):
        points = 80*self.x - 2*self.s
        print(points)

class Player():
    def __init__(self, name, score: IScoring()):
        self.name = name
        self._score = score
    def doAction(self):
        self._score.score()


kind1 = Player("Markus", Kinder())
print(kind1.name)
kind1.doAction()
intermediate1 = Player("Klaus", Intermediate())
print(intermediate1.name)
intermediate1.doAction()
hardcore1 = Player("Arne", Hardcore())
print(hardcore1.name)
hardcore1.doAction()