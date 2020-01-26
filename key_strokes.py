def key_strokes_controllers (pygame, event):
    playerx_change = 0
    #Check keystroke pressed is right or left
    if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_LEFT:
          playerx_change = -0.3
       if event.key == pygame.K_RIGHT:
          playerx_change = 0.3
    elif event.type == pygame.KEYUP:
       if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          playerx_change = 0

    return playerx_change
    
     