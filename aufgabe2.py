
class IMove():
    def move(self):
        raise NotImplementedError

class diagonal(IMove):
    def move(self, alien):
        alien.x += 5 
        alien.y += 5
        print("%d,%d" %(alien.x, alien.y))

class up (IMove):
    def move(self, alien):
        alien.y += 5
        print("%d,%d" %(alien.x, alien.y))

class normal (IMove):
    def move(self, alien):
        alien.x += 5 
        print("%d,%d" %(alien.x, alien.y))

class Alien ():
    def __init__(self, name, mode: IMove):
        self.name = name
        self._mode = mode
        self.x = 0
        self.y = 0
        

    def move (self):
        self._mode.move(self)
        


alien1 = Alien("Harald", normal())
alien1.move()
alien1.move()
alien1._mode = diagonal()
alien1.move()
alien1.move()
alien1._mode = up()
alien1.move()
alien1.move()