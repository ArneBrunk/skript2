
class IMove():
    def move(self):
        raise NotImplementedError

class diagonal(IMove):
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self):
        self.x += 5 
        self.y += 5
        print("%d,%d" %(self.x, self.y))

class up (IMove):
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self):
        self.y += 5
        print("%d,%d" %(self.x, self.y))

class normal (IMove):
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self):
        self.x += 5 
        print("%d,%d" %(self.x, self.y))

class Alien ():
    def __init__(self, name, mode: IMove):
        self.name = name
        self._mode = mode
        

    def move (self):
        self._mode.move()
        


alien1 = Alien("Harald", normal())
alien1.move()
alien1.move()
alien2 = Alien("Harry", diagonal())
alien2.move()
alien2.move()
alien3 = Alien("Howard", up())
alien3.move()
alien3.move()

