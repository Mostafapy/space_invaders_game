from helpers.key_strokes import key_strokes_controllers
from helpers.Value import Value
def game_loop(pygame, screen, player, enemy, bullet, background_image):
    # Game Loop
    running = True

    #Player
    playerx_change = Value(0)

    #Bullet
    bulletx_change = Value(0)
    bullety_change = Value(40)
    bullet_state = Value("ready")

    #Enemy
    enemyx_change = Value(4)
    enemyy_change = Value(40)
    while running:
        #RGB RED, GREEN, BLUE
        screen.fill((0, 0, 0))

        #Background
        screen.blit(background_image, (0, 0))
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False
          
          #Check keystroke pressed is right or left
          # Bullet change movement
          key_strokes_controllers(pygame, event, playerx_change, player, bullet, screen, bullet_state)

        #Player change movement
        player.object_movement(playerx_change)

        # Enemy change movement
        enemy.object_movement(enemyx_change, enemyy_change)
        
        #bullet
        bullet.object_movement(screen, bullety_change, bullet_state)

        player.add_object(screen)
        enemy.add_object(screen)

        pygame.display.update()