def game_loop(pygame, screen):
    # Game Loop
    running = True
    while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False

        #RGB RED, GREEN, BLUE
        screen.fill((0, 0, 0))
        pygame.display.update()