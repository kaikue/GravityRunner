import pygame
import Game

class LevelObject(object):
  
    def __init__(self, imageurl, on_floor, image = None):
        self.on_floor = on_floor
        if image is not None:
            self.img = image
        else:
            self.img = pygame.image.load(imageurl).convert_alpha()
        if not self.on_floor:
            self.img = pygame.transform.flip(self.img, False, True)
        self.width, self.height = self.img.get_size()
        self.x = Game.SCREEN_WIDTH
        if self.on_floor:
            self.y = Game.FLOOR - self.height
        else:
            self.y = Game.CEILING
        self.update_bounding_box()
    
    def update_bounding_box(self):
        if self.on_floor:
            self.bounding_box = pygame.rect.Rect(self.x, self.y + self.height / 2, self.width, self.height / 2)
        else:
            self.bounding_box = pygame.rect.Rect(self.x, self.y, self.width, self.height / 2)
    
    def update(self, speed):
        self.x -= speed
        self.update_bounding_box()
    
    def render(self, screen):
        #pygame.draw.rect(screen, Game.BLACK, self.bounding_box)
        screen.blit(self.img, (self.x, self.y))