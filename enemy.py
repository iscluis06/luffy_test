from typing import Any

import pygame

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
        {"x": 123, "y": 127, "width": 60, "height": 57},
        {"x": 192, "y": 141, "width": 55, "height": 44},
        {"x": 4, "y": 198, "width": 51, "height": 39},
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
    images = []

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.images = pygame.image.load(resource_path("Marine Swordsman.gif")).convert_alpha()
        self.current_animation = self.STANDING
        self.x, self.y = 120, 0
        self.frame = 0
        self.attacking = False
        self.right = False
        self.elapsed_time = 0
        self.get_animation()
        self.speed = 0
        self.is_defeated = False


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
            if self.frame == 0 and self.is_defeated:
                self.remove(self.containers)
        self.x += self.speed

    def get_animation(self):
        current_sprite = self.current_animation[self.frame]
        self.image = pygame.Surface((current_sprite["width"], current_sprite["height"]))
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.images, (0, 0), (current_sprite["x"],
                        current_sprite["y"],
                        current_sprite["width"],
                        current_sprite["height"]))
        self.image = self.image if self.right == False else pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def defeated(self):
        self.current_animation = self.DEFEATED
        self.is_defeated = True