# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys

import pygame

from controls import Controls
from luffy import Luffy


def print_hi(name):
    FPS = 30
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))

    player_group = pygame.sprite.Group()

    Luffy.containers = player_group

    controls = Controls(Luffy())

    while True:
        for event in pygame.event.get():
            controls.manage_keyboard_events(event)

        screen.fill((0, 0, 0))
        player_group.update(time=clock.get_time())
        player_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
