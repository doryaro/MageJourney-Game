import sys
import time

import pygame
from Mage import Mage
from enum import Enum


class GamePhase(Enum):
    PLAYER_TURN = 1
    MONSTER_TURN = 2
    ANIMATION_PHASE = 3


class Game:
    def __init__(self, player: Mage, monster, win):
        self.player = player
        self.monster = monster
        self.running = True
        self.win = win
        self.phase = GamePhase.PLAYER_TURN


    def final_screen(self):
        win = pygame.display.set_mode((500, 500))
        win.fill((0, 0, 0))
        font_large = pygame.font.SysFont(None, 75)
        font_small = pygame.font.SysFont(None, 45)
        font_smallest = pygame.font.SysFont(None, 30)

        win_message = font_large.render('YOU WIN!', True, (0, 255, 0))
        explain_message1 = font_small.render('Congratulations', True, (0, 255, 0))
        explain_message2 = font_small.render('Thanks for playing', True, (0, 255, 0))
        close_button = pygame.Rect(180, 300, 120, 50)
        while True:
            win.blit(win_message, (120, 100))
            win.blit(explain_message1, (117, 150))
            win.blit(explain_message2, (100, 220))

            pygame.draw.rect(win, (255, 0, 0), close_button)

            close_text = font_smallest.render('Exit Game', True, (255, 255, 255))
            win.blit(close_text, (190, 315))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 is the left mouse button
                    if close_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

    def continue_screen(self):
        win = pygame.display.set_mode((500, 500))
        win.fill((0, 0, 0))
        font_large = pygame.font.SysFont(None, 75)
        font_small = pygame.font.SysFont(None, 45)
        font_smallest = pygame.font.SysFont(None, 30)

        win_message1 = font_large.render('New Boss is ', True, (0, 255, 0))
        win_message2 = font_large.render('COMING!', True, (0, 255, 0))

        explain_message1 = font_small.render('would you like', True, (0, 255, 0))
        explain_message2 = font_small.render('to continue', True, (0, 255, 0))
        continue_button = pygame.Rect(100, 300, 120, 50)

        close_button = pygame.Rect(280, 300, 120, 50)
        while True:
            win.blit(win_message1, (100, 100))
            win.blit(win_message2, (120, 150))
            win.blit(explain_message1, (130, 220))
            win.blit(explain_message2, (142, 250))

            pygame.draw.rect(win, (0, 255, 0), continue_button)
            pygame.draw.rect(win, (255, 0, 0), close_button)

            continue_text = font_smallest.render('Kill it!', True, (255, 255, 255))
            close_text = font_smallest.render('Exit Game', True, (255, 255, 255))
            win.blit(continue_text, (120, 315))
            win.blit(close_text, (290, 315))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 is the left mouse button
                    if continue_button.collidepoint(event.pos):
                        return
                    if close_button.collidepoint(event.pos):
                        pygame.quit()
                        exit()

    def treasure_screen(self):
        win = pygame.display.set_mode((500, 500))
        win.fill((0, 0, 0))
        font_large = pygame.font.SysFont(None, 75)
        font_small = pygame.font.SysFont(None, 45)
        font_tiny = pygame.font.SysFont(None, 37)

        font_smallest = pygame.font.SysFont(None, 30)

        win_message1 = font_large.render('You found a', True, (0, 255, 0))
        win_message2 = font_large.render('TREASURE!', True, (0, 255, 0))

        explain_message1 = font_small.render('New Spell:', True, (255, 255, 255))
        explain_message2 = font_tiny.render('Meteor Shower', True, (255, 0, 0))
        continue_button = pygame.Rect(100, 300, 120, 50)

        close_button = pygame.Rect(280, 300, 120, 50)
        while True:
            win.blit(win_message1, (100, 100))
            win.blit(win_message2, (100, 150))
            win.blit(explain_message1, (117, 220))
            win.blit(explain_message2, (130, 260))

            pygame.draw.rect(win, (0, 255, 0), continue_button)
            pygame.draw.rect(win, (255, 0, 0), close_button)

            continue_text = font_smallest.render('Open it!', True, (255, 255, 255))
            close_text = font_smallest.render('Exit Game', True, (255, 255, 255))
            win.blit(continue_text, (120, 315))
            win.blit(close_text, (290, 315))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 is the left mouse button
                    if continue_button.collidepoint(event.pos):
                        self.continue_screen()
                        return
                    if close_button.collidepoint(event.pos):
                        pygame.quit()
                        exit()

    def winning_screen(self):
        win = pygame.display.set_mode((500, 500))
        win.fill((0, 0, 0))
        font_large = pygame.font.SysFont(None, 75)
        font_small = pygame.font.SysFont(None, 45)
        font_smallest = pygame.font.SysFont(None, 30)

        win_message = font_large.render('YOU WIN!', True, (0, 255, 0))
        explain_message1 = font_small.render('Congratulations', True, (0, 255, 0))
        explain_message2 = font_small.render('you found a TREASURE', True, (0, 255, 0))
        continue_button = pygame.Rect(100, 300, 120, 50)

        close_button = pygame.Rect(280, 300, 120, 50)
        while True:
            win.blit(win_message, (120, 100))
            win.blit(explain_message1, (117, 170))
            win.blit(explain_message2, (100, 200))

            pygame.draw.rect(win, (0, 255, 0), continue_button)
            pygame.draw.rect(win, (255, 0, 0), close_button)

            continue_text = font_smallest.render('Open it!', True, (255, 255, 255))
            close_text = font_smallest.render('Exit Game', True, (255, 255, 255))
            win.blit(continue_text, (120, 315))
            win.blit(close_text, (290, 315))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 is the left mouse button
                    if continue_button.collidepoint(event.pos):
                        self.treasure_screen()
                        return
                    if close_button.collidepoint(event.pos):
                        pygame.quit()
                        exit()

    def losing_screen(self):
        win = pygame.display.set_mode((500, 500))
        font = pygame.font.SysFont(None, 55)
        win_message = font.render('YOU DIED!', True, (0, 255, 0))
        win.blit(win_message, (100, 200))

        pygame.display.update()

    def player_turn(self):
        pass

    def monster_turn(self):
        self.monster.cast_base_attack()
        pass

    def check_win(self ,current_monster):
        # Code for checking win condition
        if self.monster.health <= 0:
            self.running = False
            if current_monster == 1:
                self.winning_screen()
            if current_monster == 2:
                self.final_screen()

    def check_lose(self):
        # Code for checking lose condition
        if self.player.health <= 0:
            self.running = False
            self.losing_screen()
