def key_strokes_controllers (pygame, event, playerx_change, player, bullet, screen, bullet_state):
    #Check keystroke pressed is right or left
    if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
          playerx_change.value = -5
       if event.key == pygame.K_RIGHT:
          playerx_change.value = 5
       if event.key == pygame.K_SPACE:
          bullet.add_object(screen, player.game_object_x, bullet_state)

    elif event.type == pygame.KEYUP:
       if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          playerx_change.value = 0

    
     