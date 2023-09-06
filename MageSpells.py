import configparser

import pygame

config = configparser.ConfigParser()
config.read('C:\\Users\\DorYaron\\Desktop\\MageJourney\\config.ini')

game_screen_height = config.getint('GameScreen', 'HEIGHT')
game_screen_width = config.getint('GameScreen', 'WIDTH')


class MageSpells:
    def __init__(self, mage_position_x, mage_position_y):
        self.mage_position_x = mage_position_x
        self.mage_position_y = mage_position_y
        self.fireball_image = pygame.image.load(
            'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\Fireball.png')
        self.fireball_x = mage_position_x + 100
        self.fireball_y = mage_position_y + 50
        self.fireball_speed = 8.5
        self.meteor_shower_image = pygame.image.load(
            'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\MeteorShower.png')
        self.meteor_shower_x = game_screen_width / 7
        self.meteor_shower_y = -300
        self.meteor_shower_speed = 8

    def CastingMeteorShower(self):
        self.meteor_shower_x += self.meteor_shower_speed
        self.meteor_shower_y += self.meteor_shower_speed/1.4
        if self.meteor_shower_x > 1000:
            self.meteor_shower_x = game_screen_width / 7
            self.meteor_shower_y = -300
            return False
        return True

    def MeteorShower(self, win):
        win.blit(self.meteor_shower_image, (self.meteor_shower_x, self.meteor_shower_y))

    def CastingFireBall(self):
        self.fireball_x += self.fireball_speed
        if self.fireball_x > 1000:
            self.fireball_x = self.mage_position_x + 50
            return False
        return True

    def FireBall(self, win):
        win.blit(self.fireball_image, (self.fireball_x, self.fireball_y))

    # def DoneCastFireBall(self):
    #     self.fireball_x = self.mage_position_x + 100
    #     self.fireball_y = self.mage_position_y + 50
    #     self.fireball_speed = 8.5
