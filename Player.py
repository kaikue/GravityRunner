import pygame
import Game

class Player(object):
    
    FRAME_TIME = 15
    
    def __init__(self):
        #self.img = pygame.image.load("img/player.png").convert_alpha()
        #self.img_flip = pygame.transform.flip(self.img, False, True)
        self.run_images_down = [pygame.image.load("img/player_run1.png").convert_alpha(), pygame.image.load("img/player_run2.png").convert_alpha()]
        self.run_images_up = [pygame.transform.flip(self.run_images_down[0], False, True), pygame.transform.flip(self.run_images_down[1], False, True)]
        self.fall_image_down = pygame.image.load("img/player_fall.png").convert_alpha()
        self.fall_image_up = pygame.transform.flip(self.fall_image_down, False, True)
        self.width, self.height = 71, 91#self.run_images_down[0].get_size()
        self.x = Game.SCREEN_WIDTH / 5
        self.y = Game.FLOOR - self.height
        self.update_bounding_box()
        self.vel = 0
        self.acceleration = Game.GRAVITY
        self.frame = 0
        self.frame_timer = 0
    
    def flip(self):
        if self.vel == 0:
            self.acceleration *= -1
    
    def check_collision(self, obj):
        if self.bounding_box.colliderect(obj.bounding_box):
            return obj.__class__.__name__
    
    def update_bounding_box(self):
        self.bounding_box = pygame.rect.Rect(self.x, self.y, self.width, self.height)
    
    def update(self):
        self.vel += self.acceleration
        self.y += self.vel
        if (self.y + self.height) > Game.FLOOR:
            self.y = Game.FLOOR - self.height
            self.vel = 0
        if self.y < Game.CEILING:
            self.y = Game.CEILING
            self.vel = 0
        self.update_bounding_box()
        
        self.frame_timer += 1
        if self.frame_timer == Player.FRAME_TIME:
            self.frame_timer = 0
            self.frame += 1
            self.frame %= len(self.run_images_down)
    
    def render(self, screen):
        if self.acceleration < 0:
            if self.vel == 0:
                screen.blit(self.run_images_up[self.frame], (self.x, self.y))
            else:
                screen.blit(self.fall_image_up, (self.x, self.y))
        else:
            if self.vel == 0:
                screen.blit(self.run_images_down[self.frame], (self.x, self.y))
            else:
                screen.blit(self.fall_image_down, (self.x, self.y))