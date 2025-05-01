class Die:
    def __init__(self) -> None:
        self.face: int # Here we are just declaring that the face will be an integer
        self.roll()
        
    def roll(self) -> None:
        ...


from random import randint

class D4(Die):
    def roll(self):
        self.face = randint(1, 4)
        
    
class D6(Die):
    def roll(self):
        self.face = randint(1, 6)
    
class D8(Die):
    def roll(self):
        self.face = randint(1, 8)
        
class D10(Die):
    def roll(self):
        self.face = randint(1, 10)


d8 = D8()
d8.face=5
d8.roll()