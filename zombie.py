from enemy import *
import random  

class Zombie(Enemy):

    def __init__(self, health, attack):
        super().__init__(type = 'Zombie', 
                         health = health,
                         attack = attack)

    def talk(self):
        print('*Grumbling!*')

    def spread_disease(self):
        print('The zombie is trying to spread infection.')

    def special(self):
        did_special_work = random.random() < .50
        if did_special_work:
            self.health += 2
            print('Zombie regenerated 2 HP!')
