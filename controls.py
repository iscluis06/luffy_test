import pygame
from pygame.event import Event

from luffy import Luffy


class Controls:
    def __init__(self, player: Luffy):
        self.luffy = player

    def manage_keyboard_events(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.luffy.running_right()
            if event.key == pygame.K_LEFT:
                self.luffy.running_left()
            if event.key == pygame.K_a:
                self.luffy.punch()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.luffy.standing()
