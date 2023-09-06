import random
import time

import pygame

from MageSpells import MageSpells


class Mage:
    def __init__(self, x, y, health=30, health_potion_amount=9):
        self.max_health = 30
        self.health = health
        self.health_potion_count = health_potion_amount
        self.base_damage = 1
        self.x = x
        self.y = y
        self.health_bar_x = x + 75
        self.health_bar_y = y + 350
        self.border_thickness = 4
        self.Spells = MageSpells(x, y)
        self.health_bar_length = 100
        self.health_bar_height = 20
        self.HasMeteorShower_spell = False
        self.casting_fireball = False
        self.casting_meteor_shower = False
        self.image = pygame.image.load('C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\Mage.png')
        self.image.set_colorkey((255, 255, 255))
        # self.fireball_image = pygame.image.load(
        #     'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\Fireball.png')
        self.scratch_image = pygame.image.load(
            'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\Scratch.png')
        self.scratch_image.set_colorkey((255, 255, 255))
        self.health_potion_image = pygame.image.load(
            'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\HealthPotion.PNG')
        self.health_potion_image.set_colorkey((255, 255, 255))
        self.blinking = False
        self.blink_count = 0
        self.scratching = False
        self.drinking_health_potion = False

    def cast_fireball(self):
        self.casting_fireball = True

    def cast_meteor_shower(self):
        self.casting_meteor_shower = True

    def base_attack_hit(self, damage, win):
        self.health -= damage
        base_attack_hitting_sound = pygame.mixer.Sound(
            'C:\\Users\\DorYaron\\Desktop\\MageJourney\\Sounds\\base_attack_hit.wav')
        base_attack_hitting_sound.play()
        self.scratching = True
        self.blinking = True
        self.blink_count = 0

    def update(self, monster, win):
        if self.casting_fireball:
            if not self.Spells.CastingFireBall():
                self.casting_fireball = False
                damage = random.randint(3, 6) * self.base_damage
                monster.fireball_hit(damage, win)
        if self.casting_meteor_shower:
            if not self.Spells.CastingMeteorShower():
                self.casting_meteor_shower = False
                damage = random.randint(1, 15) * self.base_damage
                monster.meteor_hit(damage, win)
        if self.scratching and self.blinking:
            self.blink_count += 1
            time.sleep(0.2)  # for the blinks
            if self.blink_count > 3 + 5:  # Adjust this value to control the duration of the blinking
                self.blinking = False
                self.scratching = False
                self.blink_count = 0
                return "monster done turn"
        if not self.scratching and self.blinking:
            self.blink_count += 1
            time.sleep(0.2)  # for the blinks
            if self.blink_count > 6:  # Adjust this value to control the duration of the blinking
                self.blinking = False
                self.blink_count = 0
                return "monster done turn"
        if self.drinking_health_potion:
            time.sleep(1)
            self.health_potion_count -= 1
            if self.health_potion_count < 0:
                self.health_potion_count = 0
                self.drinking_health_potion = False
                monster.player_use_potion()
                return
            self.health += 10
            if self.health > 100:
                self.health = 100
            self.drinking_health_potion = False
            monster.player_use_potion()

    def DrawHealthBar(self, win):
        # Draw health bar
        health_percentage = self.health / self.max_health
        gradient_color = (255 * (1 - health_percentage), 255 * health_percentage, 0)
        border_color = (0, 0, 0)
        pygame.draw.rect(win, border_color,
                         (self.health_bar_x - self.border_thickness, self.health_bar_y - self.border_thickness,
                          self.health_bar_length + 2 * self.border_thickness,
                          self.health_bar_height + 2 * self.border_thickness))
        pygame.draw.rect(win, gradient_color, (
            self.health_bar_x, self.health_bar_y, self.health_bar_length * health_percentage, self.health_bar_height))
        font = pygame.font.SysFont(None, 25)
        text = font.render(f'{self.health}/{self.max_health}', True, (255, 255, 255))
        # win.blit(text, (self.x + self.health_bar_length / 2 - text.get_width() / 2,
        #                 self.y - 20 + self.health_bar_height / 2 - text.get_height() / 2))
        win.blit(text, (self.health_bar_x + self.health_bar_length / 2 - text.get_width() / 2,
                        self.health_bar_y + self.health_bar_height / 2 - text.get_height() / 2))

    def draw(self, win):
        self.DrawHealthBar(win)
        white_border_color = (255, 255, 255)
        pygame.draw.rect(win, white_border_color, (self.x + 75, self.y + 420, 110, 60))
        win.blit(self.health_potion_image, (self.x + 75, self.y + 425))
        self.health_potion_count_image = pygame.image.load(
            'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\x{}.png'.format(self.health_potion_count))
        self.health_potion_count_image.set_colorkey((255, 255, 255))
        win.blit(self.health_potion_count_image, (self.x + 75 + 50, self.y + 425))

        if self.blinking and self.blink_count < 3:
            win.blit(self.image, (self.x, self.y))
            win.blit(self.scratch_image,
                     (self.x + (self.image.get_width() / 4), self.y + (self.image.get_height() / 10)))
            return
        elif self.blinking and self.blink_count % 2 == 1:
            return
        elif self.casting_fireball:
            self.Spells.FireBall(win)
        elif self.casting_meteor_shower:
            self.Spells.MeteorShower(win)

        win.blit(self.image, (self.x, self.y))

    def cast_shield(self):
        # Code for casting shield
        pass

    def use_health_potion(self, win):
        # todo sound
        drinking_health_potion_sound = pygame.mixer.Sound(
            'C:\\Users\\DorYaron\\Desktop\\MageJourney\\Sounds\\DrinkHealthPotion.mp3')
        drinking_health_potion_sound.play()
        self.drinking_health_potion = True
        pass
