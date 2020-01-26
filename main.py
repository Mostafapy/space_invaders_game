import pygame
import random
from game_loop import game_loop
from PlayerOrEnemy import PlayerOrEnemy

if __name__ == '__main__':
    #Intialize pygame
    pygame.display.init()

    # Create a screen
    # Open a window on the screen
    screen_width=800
    screen_height=600
    screen = pygame.display.set_mode([screen_width,screen_height])

    # Title and icon
    pygame.display.set_caption("Space Invadors")
    icon = pygame.image.load('ufo.png')
    pygame.display.set_icon(icon)

    # Player
    player = PlayerOrEnemy(pygame, "space-invaders.png", 370, 480)

    # Enemy
    enemy_position_x = random.randint(0, 800)
    enemy_position_y = random.randint(50, 150)
    enemy = PlayerOrEnemy(pygame, "enemy.png", enemy_position_x, enemy_position_y)

    # Game Loop
    game_loop(pygame, screen, player, enemy)
