import pygame
import os

pygame.font.init()

HEIGHT, WIDTH = 650, 650

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Loading Images

# Enemy Ships

RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue.png'))

# Player Ship

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))

# Laser hits

RED_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
GREEN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))
BLUE_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
YELLOW_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))

# Background

BLACK_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background_black.png')), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x=0, y=0, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.laser = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x=0, y=0, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)

def main():

    run = True
    FPS = 60
    level = 1
    lives = 5
    player_vel = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    player = Player(10, 10)
    clock = pygame.time.Clock()    

    def redraw():
        WINDOW.blit(BLACK_BACKGROUND, (0,0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 0, 0))

        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, ((WIDTH - (level_label.get_width()+10)), 10))
        player.draw(WINDOW)
        pygame.display.update()
    
    while True:
        clock.tick(FPS)
        redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_a]and player.x>=0):
            player.x -= player_vel
        if(keys[pygame.K_d] and player.x<=WIDTH-player.get_height()):
            player.x += player_vel
            print(player.x)
        if(keys[pygame.K_w] and player.y>=0):
            player.y -= player_vel
        if(keys[pygame.K_s] and player.y<=HEIGHT-player.get_width()):
            player.y += player_vel

main()