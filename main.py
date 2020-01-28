import pygame
import random
from game_loop import game_loop
from Objects.Player import Player
from Objects.Enemy import Enemy
from Objects.Bullets import Bullets

if __name__ == '__main__':
    #Intialize pygame
    pygame.display.init()

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
    enemy_position_x = random.randint(0, 735)
    enemy_position_y = random.randint(50, 150)
    enemy = Enemy(pygame, "images/enemy.png", enemy_position_x, enemy_position_y)

    #Bullets
    bullet = Bullets(pygame, "images/bullet.png", 0, 480)

    # Game Loop
    game_loop(pygame, screen, player, enemy, bullet, background_img)
