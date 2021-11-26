from typing import Any

import pygame.image
from pygame.sprite import Sprite

from utilities import resource_path


class Luffy(Sprite):
    containers = None
    STANDING = [
        {"x": 13, "y": 13, "width": 33, "height": 46},
        {"x": 61, "y": 13, "width": 33, "height": 46},
        {"x": 108, "y": 13, "width": 33, "height": 46},
        {"x": 157, "y": 13, "width": 33, "height": 46},
    ]
    RUNNING_RIGHT = [
        {"x": 244, "y": 8, "width": 38, "height": 46},
        {"x": 296, "y": 8, "width": 28, "height": 46},
        {"x": 337, "y": 7, "width": 34, "height": 47},
        {"x": 384, "y": 11, "width": 33, "height": 44},
        {"x": 433, "y": 8, "width": 26, "height": 46},
        {"x": 474, "y": 6, "width": 33, "height": 48},
    ]
    PUNCH = [
        {"x": 11, "y": 2049, "width": 31, "height": 41},
        {"x": 59, "y": 2050, "width": 31, "height": 40},
        {"x": 110, "y": 2042, "width": 32, "height": 47},
        {"x": 159, "y": 2039, "width": 23, "height": 50},
        {"x": 201, "y": 2041, "width": 27, "height": 48},
        {"x": 241, "y": 2040, "width": 27, "height": 49},
        {"x": 290, "y": 2040, "width": 27, "height": 49},
        {"x": 346, "y": 2040, "width": 27, "height": 49},
        {"x": 392, "y": 2040, "width": 27, "height": 49},
        {"x": 432, "y": 2040, "width": 27, "height": 49},
        {"x": 477, "y": 2040, "width": 37, "height": 49},
        {"x": 529, "y": 2040, "width": 39, "height": 49},
        {"x": 579, "y": 2040, "width": 39, "height": 49},
        {"x": 641, "y": 2040, "width": 41, "height": 50},
        {"x": 695, "y": 2050, "width": 53, "height": 40},
        {"x": 759, "y": 2050, "width": 61, "height": 40},
        {"x": 830, "y": 2050, "width": 69, "height": 40},
        {"x": 23, "y": 2107, "width": 85, "height": 40},
        {"x": 122, "y": 2107, "width": 93, "height": 40},
        {"x": 226, "y": 2107, "width": 109, "height": 40},
        {"x": 346, "y": 2108, "width": 117, "height": 39},
        {"x": 474, "y": 2105, "width": 30, "height": 43},
        {"x": 518, "y": 2105, "width": 30, "height": 43},
    ]

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.images = pygame.image.load(resource_path("Luffy.gif")).convert_alpha()
        self.current_animation = self.STANDING
        self.attacking = False
        self.x, self.y = 0, 0
        self.left = False
        self.frame = 0
        self.elapsed_time = 0
        self.fixed_width = 0
        self.get_animation()
        self.speed = 0

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.get_animation()
        images_fps = 1000/len(self.current_animation)
        self.elapsed_time += kwargs["time"]
        if(self.elapsed_time//images_fps>0):
            self.elapsed_time = 0
            self.frame = self.frame + 1 if self.frame < len(self.current_animation) - 1 else 0
            if self.frame == 0 and self.attacking:
                self.attacking = False
                self.current_animation = self.STANDING
        self.x += self.speed
        print(f"current x: {self.x}")


    def get_animation(self):
        current_sprite = self.current_animation[self.frame]
        self.image = pygame.Surface((current_sprite["width"], current_sprite["height"]))
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.images, (0, 0), (current_sprite["x"],
                        current_sprite["y"],
                        current_sprite["width"],
                        current_sprite["height"]))
        self.image = self.image if self.left == False else pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        if self.left and self.attacking:
            self.rect.x = self.x + self.fixed_width - self.current_animation[self.frame]["width"]
        else:
            self.rect.x = self.x
        self.rect.y = self.y

    def running_right(self):
        self.fixed_width = 0
        self.frame = 0
        self.left = False
        self.current_animation = self.RUNNING_RIGHT
        self.speed = 6

    def running_left(self):
        self.fixed_width = 0
        self.frame = 0
        self.left = True
        self.current_animation = self.RUNNING_RIGHT
        self.speed = -6

    def standing(self):
        self.frame = 0
        self.current_animation = self.STANDING
        self.speed = 0

    def punch(self):
        if not self.attacking:
            self.frame=0
            self.current_animation = self.PUNCH
            self.attacking = True
            self.speed = 0
            if self.left:
                self.fixed_width = self.PUNCH[0]["width"]
