from helpers.key_strokes import key_strokes_controllers
from helpers.Value import Value
def game_loop(pygame, screen, player, enemies, bullet, background_image, num_of_enemies, font):
    # Game Loop
    running = True

    #Player
    playerx_change = Value(0)

    #Bullet
    bulletx_change = Value(0)
    bullety_change = Value(40)
    bullet_state = Value("ready")

    #Enemy
    enemyx_change = list(range(num_of_enemies))
    enemyy_change = list(range(num_of_enemies))
    for j in range(num_of_enemies):
     enemyx_change[j] = Value(1)
     enemyy_change[j] = Value(40)

    #Score
    score_value = Value(0)

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
        for i in range(num_of_enemies):
          enemies[i].object_movement(enemyx_change[i], enemyy_change[i])
          #collision
          bullet.add_collision(enemies[i], bullet_state, score_value, pygame)

          enemies[i].add_object(screen)

        #bullet
        bullet.object_movement(screen, bullety_change, bullet_state)


        player.add_object(screen)
        font.add_object(screen, score_value)
  
        pygame.display.update()