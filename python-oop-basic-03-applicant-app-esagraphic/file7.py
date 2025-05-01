from abc import ABC, abstractmethod

class Die(ABC):
    def __init__(self) -> None:
        self.face: int # Here we are just declaring that the face will be an integer
        self.roll()
        
    @abstractmethod
    def roll(self) -> None:
        ...
        
    def __str__(self) -> str:
        return f'{self.face}'
    



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
        
class D11(Die):
    pass

d4 = D4()
d6 = D6()
d8 = D8()
d10 = D10()
# d11 = D11()

from typing import Type

class DiceBoard:
    # Type[Die] means it will be a class that has as parent Die
    def __init__(self, *die_classes: Type[Die]):
        self.dice: list[Die] = [die() for die in die_classes]
            
    def roll_all_dice(self):
        # This method will roll all the dice
        for die in self.dice:
            die.roll()
            
    # TODO: Create a property called `total` that will return the total sum of all dice

    @property
    def total(self):
        return sum (Die.face for die in self.dice)


dice_board = DiceBoard(D4,D8,D10)
dice_board.total()
