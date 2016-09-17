import pygame
import os
import sys
import Level

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

CEILING = SCREEN_HEIGHT / 5
FLOOR = SCREEN_HEIGHT * 4 / 5

GRAVITY = 0.5

BACKGROUND = (208, 244, 247, 255)
BLACK = (0, 0, 0, 255)

MENU = 0
RUNNING = 1
DEAD = 2

class Game:
    
    def __init__(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        self.mode = MENU
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.Font("future.ttf", 32)
        self.font_small = pygame.font.Font("future.ttf", 24)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Gravity Runner")
        self.lose_image = pygame.image.load("img/lose.png").convert_alpha()
        self.title_image = pygame.image.load("img/title.png").convert_alpha()
    
    def start(self):
        self.mode = RUNNING
        self.level = Level.Level(self)
        self.clock = pygame.time.Clock()
        self.run()
    
    def run(self):
        while True:
            self.clock.tick_busy_loop(60)
            self.update()
            self.render()
    
    def update(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_RETURN] and self.mode != RUNNING:
                    self.start()
        if self.mode == RUNNING:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                self.level.player.flip()
            self.level.update()
        self.render()
    
    def render(self):
        if self.mode == MENU:
            self.draw_menu()
        elif self.mode == RUNNING:
            self.level.render(self.screen)
        elif self.mode == DEAD:
            self.draw_menu(self.level.score)
        pygame.display.update()
    
    def draw_menu(self, score=None):
        self.screen.fill(BACKGROUND)
        if score is not None:
            score_text = self.font.render("Score: " + str(self.level.score), 1, BLACK)
            w = score_text.get_width()
            self.screen.blit(score_text, ((SCREEN_WIDTH - w) // 2, SCREEN_HEIGHT / 2 - 70))
            play_again_text = self.font_small.render("Press ENTER to play again", 1, BLACK)
            w = play_again_text.get_width()
            self.screen.blit(play_again_text, ((SCREEN_WIDTH - w) // 2, SCREEN_HEIGHT / 2))
            self.screen.blit(self.lose_image, (0, 0))
        else:
            title_text = self.font.render("GRA\\/ITY RUNNER", 1, BLACK)
            w = title_text.get_width()
            self.screen.blit(title_text, ((SCREEN_WIDTH - w) // 2, SCREEN_HEIGHT / 2 - 70))
            controls_text = self.font_small.render("Controls: SPACE to flip gravity", 1, BLACK)
            w = controls_text.get_width()
            self.screen.blit(controls_text, ((SCREEN_WIDTH - w) // 2, SCREEN_HEIGHT / 2 - 10))
            play_text = self.font_small.render("Press ENTER to play", 1, BLACK)
            w = play_text.get_width()
            self.screen.blit(play_text, ((SCREEN_WIDTH - w) // 2, SCREEN_HEIGHT / 2 + 30))
            self.screen.blit(self.title_image, (0, 0))

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()