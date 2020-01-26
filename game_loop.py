from key_strokes import key_strokes_controllers
def game_loop(pygame, screen, player):
    # Game Loop
    running = True

    while running:
        #RGB RED, GREEN, BLUE
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False
          
          #Check keystroke pressed is right or left
          playerx_change = key_strokes_controllers(pygame, event)

        player.player_x += playerx_change
        
        # Add game boundries
        if player.player_x <= 0:
            player.player_x = 0
        elif player.player_x >= 736:
            player.player_x = 736

        player.add_player(screen)

        pygame.display.update()