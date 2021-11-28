# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import threading
import time

import pygame
from pygame.sprite import Group

from controls import Controls
from enemy import SwordMan
from luffy import Luffy

def print_hi(name):
    pause = False
    FPS = 30
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))

    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    Luffy.containers = player_group
    SwordMan.containers = enemy_group

    player = Luffy()
    controls = Controls(player)
    SwordMan()

    while player.alive():
        for event in pygame.event.get():
            controls.manage_keyboard_events(event)

        screen.fill((0, 0, 0))
        player_group.draw(screen)
        enemy_group.draw(screen)

        # Comprobar colisiones
        collisions = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
        for key in dict.keys(collisions):
            swordman: SwordMan = collisions[key][0]
            if "attacking" in player.current_animation[player.frame]:
                swordman.defeated()
            if "attacking" in swordman.current_animation[swordman.frame]:
                player.die()

        if not pause:
            try:
                player_group.update(time=clock.get_time())
                enemy_group.update(time=clock.get_time(), player_x=player.x, player_y=player.y)
            except Exception:
                print(f"exception: {Exception}")

        if len(enemy_group) == 0:
            limit = 3
            for i in range(limit):
                SwordMan()

        pygame.display.update()
        clock.tick(FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
