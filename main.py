import pygame

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

# Game Loop
running = True
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

    #RGB RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    pygame.display.update()