from enemy import *
import random 

class Ogre(Enemy):

    def __init__(self, health, attack):
        super().__init__(type = 'Ogre', 
                         health = health,
                         attack = attack)
    def talk(self):
        print(f'The Ogre is slamming hands all around.')

    def special(self):
        did_special_work = random.random() < .20
        if did_special_work:
            self.attack += 4
            print("Ogre's attack damage increased by 4!")
