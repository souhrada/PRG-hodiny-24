import pygame
from utility import image_cutter
from player import Player
from settings import *


class Monster(Player):
    def __init__(self):
        super().__init__()
        self.x = screen_width - 100
        self.y = 300
        self.spritesheet = pygame.image.load("assets/characters/monsters/monster_spritesheet.png")
        self.image = image_cutter(self.spritesheet, 0, 0, 15, 16, 3)
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.index = 0
        self.speed = 1
    
    def update(self):
        self.rect.left -= self.speed


# TODO:
# 1. Pohyb zprava do leva zpět
# 2. Přidat animaci 
# 3. Při tvorbě instance monstra přidat možnost zvolit, 
# jak bude monstrum vypadat (tzn. vykreslovat jiné monstrum ze spritesheetu)
    
