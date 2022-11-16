class Monster:
    # attributes
    health = 50
    energy = 90


def __init__(self, health, energy):  # Dunder methods
    self.health = health
    self.energy = energy

    # methods


def attack(self, amount):
    print('the monster has attacked!')
    print(f'{amount} damage was dealt')


def move(self, speed):
    print('the monster has moved')
    print(f'it has a speed of {speed}')


monster1 = Monster(10, 20)
