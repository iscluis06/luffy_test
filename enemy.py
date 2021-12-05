from typing import Any

import pygame
import random

from utilities import resource_path
from pygame.sprite import Sprite
class SwordMan(Sprite):
    STANDING = [
        {"x": 9, "y": 2, "width": 43, "height": 48},
        {"x": 63, "y": 3, "width": 43, "height": 47},
    ]

    RUNNING_LEFT = [
        {"x": 23, "y": 59, "width": 29, "height": 57},
        {"x": 76, "y": 61, "width": 36, "height": 55},
        {"x": 132, "y": 59, "width": 30, "height": 57},
        {"x": 180, "y": 60, "width": 33, "height": 55},
    ]

    ATTACKING = [
        {"x": 20, "y": 136, "width": 43, "height": 49},
        {"x": 71, "y": 132, "width": 45, "height": 52},
        {"x": 123, "y": 127, "width": 60, "height": 57,},
        {"x": 192, "y": 141, "width": 55, "height": 44, "attacking": True},
        {"x": 4, "y": 198, "width": 51, "height": 39, "attacking": True},
        {"x": 64, "y": 195, "width": 48, "height": 42},
    ]

    DEFEATED = [
        {"x": 16, "y": 308, "width": 38, "height": 57},
        {"x": 75, "y": 308, "width": 38, "height": 57},
        {"x": 125, "y": 311, "width": 41, "height": 54},
        {"x": 11, "y": 373, "width": 43, "height": 42},
        {"x": 61, "y": 371, "width": 45, "height": 44},
        {"x": 113, "y": 399, "width": 51, "height": 17},
        {"x": 14, "y": 422, "width": 50, "height": 19},
        {"x": 73, "y": 419, "width": 47, "height": 22},
        {"x": 132, "y": 424, "width": 50, "height": 17},
    ]

    containers = None

    def __init__(self, screen_height):
        Sprite.__init__(self, self.containers)
        self.images = pygame.image.load(resource_path("Marine Swordsman.gif")).convert_alpha()
        self.image = pygame.Surface((0,0))
        self.is_defeated = False
        self.player_x = -1
        self.player_y = -1
        self.player_width = 0
        self.current_animation = self.STANDING
        appear = random.randrange(800,1000,40)
        self.x, self.y = appear, screen_height
        self.frame = 0
        self.attacking = False
        self.right = False
        self.elapsed_time = 0
        self.get_animation()
        self.speed = 0


    def update(self, *args: Any, **kwargs: Any) -> None:
        self.get_animation()
        if not self.is_defeated:
            self.update_player_pos(kwargs["player_x"], kwargs["player_y"], kwargs["player_width"])
            self.should_attack_player()
            self.move_close_to_player()
        #images_fps = 1000/len(self.current_animation)
        #self.elapsed_time += kwargs["time"]
        #if(self.elapsed_time//images_fps>0):
        self.elapsed_time = 0
        self.frame = self.frame + 1 if self.frame < len(self.current_animation) - 1 else 0
        if self.frame == 0 and self.attacking:
            self.attacking = False
            self.current_animation = self.STANDING
        if self.frame == 0 and self.is_defeated:
            self.remove(self.containers)
        self.x += self.speed

    def get_animation(self):
        current_sprite = self.current_animation[self.frame]
        if self.is_defeated:
            self.image = pygame.Surface((current_sprite["width"], 57))
        else:
            self.image = pygame.Surface((current_sprite["width"], current_sprite["height"]))
        self.image.set_colorkey((0, 0, 0))
        if self.is_defeated:
            self.image.blit(self.images, (0, 57 - current_sprite["height"]), (current_sprite["x"],
                            current_sprite["y"],
                            current_sprite["width"],
                            current_sprite["height"]))
        else:
            self.image.blit(self.images, (0, 0), (current_sprite["x"],
                                                  current_sprite["y"],
                                                  current_sprite["width"],
                                                  current_sprite["height"]))
        self.image = self.image if self.right == False else pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y - self.image.get_height()

    def update_player_pos(self, player_x: int = -1, player_y: int = -1, player_width: int = 0):
        self.player_x = player_x
        self.player_y = player_y
        self.player_width = player_width

    def defeated(self):
        self.current_animation = self.DEFEATED
        self.is_defeated = True
        self.speed = 0

    def move_close_to_player(self):
        print(f"enemy x: {self.x}")
        self.right = self.x < self.player_x
        self.speed = -4 if not self.right else 4
        if self.current_animation != self.RUNNING_LEFT and not self.attacking:
            self.current_animation = self.RUNNING_LEFT
            self.frame = 0

    def should_attack_player(self):
        attacking_space = 32 if self.right else -32
        attack = self.x + attacking_space if self.right else -attacking_space
        if self.attacking:
            return
        if(not self.right and self.x + attacking_space <= self.player_x + self.player_width):
            self.speed = 0
            self.frame = 0
            self.current_animation = self.ATTACKING
            self.attacking = True
        elif(self.right and self.x + self.image.get_width() + attacking_space >= self.player_x):
            self.speed = 0
            self.frame = 0
            self.current_animation = self.ATTACKING
            self.attacking = True