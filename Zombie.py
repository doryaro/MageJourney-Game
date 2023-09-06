import pygame

from Monster import Monster


class Zombie(Monster):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.max_health = 25
        self.health = 25
        self.image = pygame.image.load('C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\Zombie.png')