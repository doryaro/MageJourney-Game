# # # how to create an exe file #pyinstaller --onefile --windowed --name MageJourney --icon=MobliePics\icon.ico --add-data C:\Users\DorYaron\Desktop\MageJourney\MobliePics;MobliePics --add-data C:\Users\DorYaron\Desktop\MageJourney\Sounds;Sounds --add-data C:\Users\DorYaron\Desktop\MageJourney\config.ini;. main.py Mage.py MageSpells.py Monster.py Zombie.py Game.py
# # #
import configparser
import sys
import time

import pygame
from pygame.locals import *

from Game import Game, GamePhase
from Mage import Mage
from Monster import Monster
from Zombie import Zombie

monster_dict = {1: Zombie(1100, 300) , 2:Monster(1100,300)}  # number to 2. zombie starting from second
current_monster = 0
background_dict = {1: 'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\background.jpg' , 2:'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\background.jpg'}  # number to 2. zombie starting from second
current_background = 0


def create_tooltip_surface(width, height, title_color, title, text, text2):
    # Create the surface
    tooltip = pygame.Surface((width, height), pygame.SRCALPHA)
    tooltip.fill((0, 0, 0, 0))  # fill with a transparent color

    # Draw the rectangle
    rect_color = (0, 0, 0)  # black
    pygame.draw.rect(tooltip, rect_color, (0, 0, width, height - 10))

    # Draw the triangle
    pygame.draw.polygon(tooltip, rect_color, [(width / 2 - 5, height - 10), (width / 2 + 5, height - 10),
                                              (width / 2, height)])

    # Draw the text
    font_title = pygame.font.SysFont(None, 35)
    title_surface = font_title.render(title, True, title_color)  # white text
    tooltip.blit(title_surface, (10, 10))
    font_text = pygame.font.SysFont(None, 20)
    text_surface = font_text.render(text, True, (255, 255, 255))  # white text
    tooltip.blit(text_surface, (15, 40))
    if text2 != '':
        text2_surface = font_text.render(text2, True, (255, 255, 255))  # white text
        tooltip.blit(text2_surface, (15, 60))

    return tooltip

def main():
    global current_monster
    global current_background
    pygame.init()
    config = configparser.ConfigParser()
    config.read('C:\\Users\\DorYaron\\Desktop\\MageJourney\\config.ini')

    game_screen_height = config.getint('GameScreen', 'HEIGHT')
    game_screen_width = config.getint('GameScreen', 'WIDTH')
    background_image = pygame.image.load(
        'C:\\Users\\DorYaron\\Desktop\\MageJourney\\MobliePics\\background.jpg')
    background_image = pygame.transform.scale(background_image, (game_screen_width, game_screen_height))
    current_background += 1

    background_sound = pygame.mixer.Sound(
        'C:\\Users\\DorYaron\\Desktop\\MageJourney\\Sounds\\scary_sound.wav')
    background_sound.set_volume(0.1)
    background_sound.play(-1)

    win = pygame.display.set_mode((game_screen_width, game_screen_height))
    mage = Mage(100, 300)
    monster = Monster(1100, 300)
    current_monster += 1
    game = Game(mage, monster, win)

    health_potion_button_color = (0, 255, 0)
    health_potion_button_rect = pygame.Rect(game_screen_width / 3 - 125, game_screen_height - game_screen_height / 5,
                                            100, 50)
    font = pygame.font.SysFont(None, 35)
    health_potion_button_text = font.render('Use HP', True, (0, 0, 0))

    fireball_button_color = (250, 200, 0)
    fireball_button_rect = pygame.Rect(game_screen_width / 3, game_screen_height - game_screen_height / 5, 100, 50)
    fireball_button_text = font.render('Fireball', True, (0, 0, 0))

    meteor_shower_button_color = (250, 75, 0)
    meteor_shower_button_rect = pygame.Rect(game_screen_width / 3 + 125, game_screen_height - game_screen_height / 5,
                                            200, 50)
    meteor_shower_button_text = font.render('Meteor Shower', True, (0, 0, 0))

    fireball_tooltip = create_tooltip_surface(150, 100, (250, 200, 0), 'FireBall:',
                                              'dealing 3-6 damage', '* BaseDamage({})'.format(mage.base_damage))
    health_potion_tooltip = create_tooltip_surface(200, 75, (0, 255, 0), 'HealthPotion:',
                                                   'healing 10 HP', '')
    meteor_shower_tooltip = create_tooltip_surface(220, 100, (250, 75, 0), 'Meteor Shower:',
                                                   'dealing 1-15 damage', '* BaseDamage({})'.format(mage.base_damage))

    clock = pygame.time.Clock()  # initialize clock
    game.phase = GamePhase.PLAYER_TURN
    while True:
        clock.tick(60)  # set the game to run at 60 FPS
        while game.running:

            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.running = False
                    pygame.quit()  # This will close the pygame window
                    sys.exit()
                if game.phase == GamePhase.PLAYER_TURN:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if fireball_button_rect.collidepoint(mouse_pos):
                            if game.phase == GamePhase.PLAYER_TURN:
                                game.phase = GamePhase.ANIMATION_PHASE
                                mage.cast_fireball()
                        if health_potion_button_rect.collidepoint(mouse_pos):
                            if game.phase == GamePhase.PLAYER_TURN:
                                game.phase = GamePhase.ANIMATION_PHASE
                                mage.use_health_potion(win)
                        if mage.HasMeteorShower_spell:
                            if meteor_shower_button_rect.collidepoint(mouse_pos):
                                if game.phase == GamePhase.PLAYER_TURN:
                                    game.phase = GamePhase.ANIMATION_PHASE
                                    mage.cast_meteor_shower()

            # win.fill((0, 0, 0))
            win.blit(background_image, (0, 0))

            pygame.draw.rect(win, fireball_button_color, fireball_button_rect)
            pygame.draw.rect(win, health_potion_button_color, health_potion_button_rect)
            if mage.HasMeteorShower_spell:
                pygame.draw.rect(win, meteor_shower_button_color, meteor_shower_button_rect)

            win.blit(fireball_button_text,
                     (game_screen_width / 3 + 5, game_screen_height - game_screen_height / 5 + 11))
            win.blit(health_potion_button_text,
                     (game_screen_width / 3 + 10 - 125, game_screen_height - game_screen_height / 5 + 11))
            if mage.HasMeteorShower_spell:
                win.blit(meteor_shower_button_text,
                         (game_screen_width / 3 + 10 + 125, game_screen_height - game_screen_height / 5 + 11))

            if fireball_button_rect.collidepoint(mouse_pos):
                win.blit(fireball_tooltip,
                         (fireball_button_rect.x + 5, fireball_button_rect.y - fireball_tooltip.get_height() - 3))
            if health_potion_button_rect.collidepoint(mouse_pos):
                win.blit(health_potion_tooltip, (
                health_potion_button_rect.x + 5, health_potion_button_rect.y - health_potion_tooltip.get_height() - 3))
            if mage.HasMeteorShower_spell:
                if meteor_shower_button_rect.collidepoint(mouse_pos):
                    win.blit(meteor_shower_tooltip,
                             (meteor_shower_button_rect.x + 5,
                              meteor_shower_button_rect.y - meteor_shower_tooltip.get_height() - 3))

            mage.draw(win)
            monster.draw(win)
            pygame.display.update()

            message = mage.update(monster, win)
            if message == "monster done turn":
                game.phase = GamePhase.PLAYER_TURN
            if message == "done turn":
                game.phase = GamePhase.MONSTER_TURN
                game.monster_turn()

            game.check_win(current_monster)
            game.check_lose()
            if not game.running:
                background_sound.stop()
                break
            if monster.update(mage, win) == "player done turn":
                game.phase = GamePhase.MONSTER_TURN
                time.sleep(1)
                game.monster_turn()
                game.phase = GamePhase.ANIMATION_PHASE
                pass
            pygame.display.update()
            continue
        win = pygame.display.set_mode((game_screen_width, game_screen_height))
        mage = Mage(100, 300,mage.health, mage.health_potion_count)
        mage.HasMeteorShower_spell = True
        monster = monster_dict[current_monster]
        current_monster += 1
        game = Game(mage, monster, win)
        background_image = pygame.image.load(background_dict[current_background])
        background_image = pygame.transform.scale(background_image, (game_screen_width, game_screen_height))
        current_background += 1

        game.running = True


if __name__ == '__main__':
    main()
