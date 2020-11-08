import pygame
import os

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

BLACK_BACKGROUND = pygame.image.load(os.path.join('assets', 'background_black.png'))


HEIGHT, WIDTH = 650, 650

WINDOW = pygame.display.set_mode((HEIGHT, WIDTH))