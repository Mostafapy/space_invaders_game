def game_loop(pygame, screen, player):
    # Game Loop
    running = True
    while running:
        #RGB RED, GREEN, BLUE
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False

        
        player.add_player(screen)

        pygame.display.update()