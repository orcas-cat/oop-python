from random import *

class Enemy:

    def __init__(self, type, health, attack):
        self.__type = type
        self.health = health
        self.attack = attack

    def get_type(self):
        return self.__type
    
    def talk(self):
        print(f'I am an {self.__type}. Be prepared to fight!')

    def move_forward(self):
        print(f'{self.__type} moves closer to you.')

    def strikes(self):
        print(f'{self.__type} attacks you for {self.attack} damage!')

    def special(self):
        print('Enemy has no special attack.')
        
