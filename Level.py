import random
import pygame
import Game
import Player
import Obstacle
import Collectible
import LevelObject

class Level(object):
    
    def __init__(self, game):
        self.game = game
        self.objects = []
        self.clouds = []
        self.score = 0
        self.floor_img = pygame.image.load("img/grass.png").convert_alpha()
        self.ceiling_img = pygame.transform.flip(self.floor_img, False, True)
        self.tile_width, self.tile_height = self.floor_img.get_size()
        self.dirt_img = pygame.image.load("img/dirt.png").convert_alpha()
        self.cloud_img = pygame.image.load("img/cloud.png").convert_alpha()
        self.player = Player.Player()
        self.set_difficulty(5)
        self.clear_timer = 0
        self.coin_timer = self.clear_time // 2
        self.cloud_timer = 30
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.speed = self.difficulty
        self.clear_time = int((2 * (Game.FLOOR - Game.CEILING - self.player.height) / Game.GRAVITY) ** 0.5) + (7 - min(self.difficulty, 5)) * self.player.width // self.speed
    
    def update(self):
        self.player.update()
        if self.clear_timer == 0:
            self.objects.append(Obstacle.Obstacle(random.random() > 0.5))
            self.clear_timer = self.clear_time
        if self.coin_timer == 0:
            self.objects.append(Collectible.Collectible(random.random() > 0.5))
            self.coin_timer = self.clear_time
        
        self.cloud_timer -= 1
        if self.cloud_timer == 0:
            self.cloud_timer = random.randrange(60, 120)
            cloud =  LevelObject.LevelObject(None, True, self.cloud_img)
            cloud.y = random.randrange(Game.CEILING, Game.FLOOR - cloud.img.get_height())
            self.clouds.append(cloud)
        
        for obj in self.objects:
            obj.update(self.speed)
            collision_type = self.player.check_collision(obj)
            if collision_type == "Obstacle":
                self.game.mode = Game.DEAD
            elif collision_type == "Collectible":
                self.score += 1
                self.set_difficulty(self.difficulty + 0.25)
                self.objects.remove(obj)
            if (obj.x + obj.width) < 0:
                self.objects.remove(obj)
        for cloud in self.clouds:
            cloud.update(self.speed)
        
        if self.clear_timer > 0:
            self.clear_timer -= 1
        if self.coin_timer > 0:
            self.coin_timer -= 1
    
    def render(self, screen):
        screen.fill(Game.BACKGROUND)
        for cloud in self.clouds:
            cloud.render(screen)
        for i in range(0, Game.SCREEN_WIDTH, self.tile_width):
            #render dirt
            screen.blit(self.dirt_img, (i, Game.FLOOR + self.tile_height))
            screen.blit(self.floor_img, (i, Game.FLOOR))
            screen.blit(self.dirt_img, (i, Game.CEILING - 2 * self.tile_height))
            screen.blit(self.ceiling_img, (i, Game.CEILING - self.tile_height))
        self.player.render(screen)
        for obj in self.objects:
            obj.render(screen)
        score_text = self.game.font.render("Score: " + str(self.score), 1, Game.BLACK)
        screen.blit(score_text, (10, 10))