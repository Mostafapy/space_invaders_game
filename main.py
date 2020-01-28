import pygame
import random
from game_loop import game_loop
from Objects.Player import Player
from Objects.Enemy import Enemy
from Objects.Bullets import Bullets

if __name__ == '__main__':
    #Initialize pygame
    pygame.display.init()

    #initialize pygame font
    pygame.font.init()

    # Create a screen
    # Open a window on the screen
    screen_width=800
    screen_height=600
    screen = pygame.display.set_mode([screen_width,screen_height])

    #Background
    background_img = pygame.image.load("images/background.png")

    # Title and icon
    pygame.display.set_caption("Space Invadors")
    icon = pygame.image.load("images/ufo.png")
    pygame.display.set_icon(icon)

    # Player
    player = Player(pygame, "images/space-invaders.png", 370, 480)

    # Enemy
    num_of_enemies = 6
    enemy_position_x = list(range(num_of_enemies))
    enemy_position_y = list(range(num_of_enemies))
    enemies = list(range(num_of_enemies))
    for i in range(num_of_enemies):
     enemy_position_x[i] = random.randint(0, 735)
     enemy_position_y[i] = random.randint(50, 150)
     enemies[i] = Enemy(pygame, "images/enemy.png", enemy_position_x[i], enemy_position_y[i])

    #Bullets
    bullet = Bullets(pygame, "images/bullet.png", 0, 480)
    # Game Loop
    game_loop(pygame, screen, player, enemies, bullet, background_img, num_of_enemies)
