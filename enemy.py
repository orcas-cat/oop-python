class Enemy:

    def __init__(self, type, health, attack):
        self.type = type
        self.health = health
        self.attack = attack
    
    def talk(self):
        print(f'I am a {self.type}. Grrr!')

    def move_forward(self):
        print(f'{self.type} moves forward.')

