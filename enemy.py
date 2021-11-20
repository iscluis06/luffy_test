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

    DEFETEAD = [
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
