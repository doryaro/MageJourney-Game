import random
import time

import pygame

from Mage import Mage


class Monster:
    def __init__(self, x, y):
        self.max_health = 15
        self.health = 15
        self.x = x
        self.y = y
        self.health_bar_x = x + 105
        self.health_bar_y = y + 350
        self.border_thickness = 4
        self.health_bar_length = 100
        self.health_bar_height = 20
        self.casting_base_attack = False
        self.image = pygame.image.load('C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\monster.png')
        self.image.set_colorkey((255, 255, 255))  # This will make white color transparent
        self.blinking = False
        self.blink_count = 0
        self.burning = False
        self.burn_count = 0
        self.burning_image = pygame.image.load('C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\burned.png')
        self.push_to_attacking = False
        self.push_to_attack_count = 0

    def fireball_hit(self,damage, win):
        self.health -= damage
        fire_ball_hitting_sound = pygame.mixer.Sound('C:\\Users\\DorYaron\\Desktop\\MageJourney\\Sounds\\fire_ball_hitting_sound.wav')
        fire_ball_hitting_sound.play()
        self.blinking = True
        self.blink_count = 0

    def meteor_hit(self, damage, win):
        self.health -= damage
        fire_ball_hitting_sound = pygame.mixer.Sound(
            'C:\\Users\\DorYaron\\Desktop\\MageJourney\\Sounds\\meteor_hitting_sound.mp3')
        fire_ball_hitting_sound.play()
        self.blinking = True
        self.blink_count = 0
        self.burning = True
        self.burn_count = 0


    def base_attack(self):
        pass

    def update(self, player:Mage, win):
        if self.burning and self.blinking:
            self.blink_count += 1
            self.burn_count += 1
            time.sleep(0.2)   # for the blinks
            if self.blink_count > 7:  # Adjust this value to control the duration of the blinking
                self.blinking = False
                self.blink_count = 0
                self.burning = False
                self.burning = 0
                return "player done turn"
        elif self.blinking:
            self.blink_count += 1
            time.sleep(0.2)   # for the blinks
            if self.blink_count > 6:  # Adjust this value to control the duration of the blinking
                self.blinking = False
                self.blink_count = 0
                return "player done turn"
        elif self.push_to_attacking:
            self.push_to_attack_count += 1
            time.sleep(0.1)  # for the blinks
            if self.push_to_attack_count > 2:  # Adjust this value to control the duration of the blinking
                self.push_to_attacking = False
                self.push_to_attack_count = 0
                damage = random.randint(3, 6)
                player.base_attack_hit(damage,win)

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
        if self.push_to_attacking:
            win.blit(self.image, (self.x-100, self.y))
        elif self.burning and self.blinking:
            if self.blink_count % 2 == 1:
                win.blit(self.image, (self.x,self.y))
            image_height = self.image.get_height()
            burning_image_height = self.burning_image.get_height()
            win.blit(self.burning_image, (self.x, self.y + image_height - burning_image_height))
        elif self.blinking and self.blink_count % 2 == 1:
            pass
        else:
            win.blit(self.image, (self.x, self.y))
        # elif not self.blinking or self.blink_count % 2 == 0:
        #     win.blit(self.image, (self.x, self.y))

        self.DrawHealthBar(win)


    def player_use_potion(self):
        ### attack
        self.cast_base_attack()
        pass

    def cast_base_attack(self):
        self.push_to_attacking = True




