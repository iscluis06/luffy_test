from typing import Any

import pygame.image
from pygame.sprite import Sprite

from utilities import resource_path


class Luffy(Sprite):
    containers = None
    STANDING = [
        {"x": 15, "y": 10, "width": 30, "height": 50},
        {"x": 45, "y": 10, "width": 30, "height": 50},
        {"x": 75, "y": 10, "width": 30, "height": 50},
        {"x": 105, "y": 10, "width": 30, "height": 50},
    ]

    def __init__(self):
        Sprite.__init__(self, self.containers)
        self.images = pygame.image.load(resource_path("Luffy.png")).convert_alpha()
        self.current_animation = self.STANDING
        self.frame = 0
        self.get_animation()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.get_animation()
        kwargs["tick"]
        self.frame = self.frame + 1 if self.frame < len(self.STANDING) - 1 else 0

    def get_animation(self):
        current_sprite = self.STANDING[self.frame]
        self.image = pygame.Surface((current_sprite["width"], current_sprite["height"]))
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.images, (0, 0), (current_sprite["x"],
                        current_sprite["y"],
                        current_sprite["width"],
                        current_sprite["height"]))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

