from enemy import *
from ogre import *
from zombie import *
import random

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health > 0 and e2.health > 0:
        print('----------')
        e1.special()
        e2.special()

        print(f'{e1.get_type()} has {e1.health} HP left.')
        print(f'{e2.get_type()} has {e2.health} HP left.')

        e1.strikes()
        e2.health -= e1.attack
        e2.strikes()
        e1.health -= e2.attack

    print('----------')

    if e1.health > 0:
        print(f'{e1.get_type()} wins!')
    else:
        print(f'{e2.get_type()} wins!') 

ogre = Ogre(30, 3)
zombie = Zombie(20, 1)

battle(ogre, zombie)




