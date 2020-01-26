def game_loop(pygame, screen, player):
    # Game Loop
    running = True

    playerx_change = 0

    while running:
        #RGB RED, GREEN, BLUE
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False
          
          #Check keystroke pressed is right or left
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                playerx_change = -0.3
              if event.key == pygame.K_RIGHT:
                playerx_change = 0.3
          elif event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerx_change = 0

        player.player_x += playerx_change
        player.add_player(screen)

        pygame.display.update()