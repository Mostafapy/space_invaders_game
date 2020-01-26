from key_strokes import key_strokes_controllers
def game_loop(pygame, screen, player, enemy, background_image):
    # Game Loop
    running = True

    while running:
        #RGB RED, GREEN, BLUE
        screen.fill((0, 0, 0))

        #Background
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False
          
          #Check keystroke pressed is right or left
          playerx_change = key_strokes_controllers(pygame, event)

          # Enemy change move
          enemyx_change = 4
          enemyy_change = 40

        # Add game boundries for player
        player.player_or_enemy_x += playerx_change
        
        if player.player_or_enemy_x <= 0:
            player.player_or_enemy_x = 0
        elif player.player_or_enemy_x >= 736:
            player.player_or_enemy_x = 736

        # Add game boundries for enemy
        enemy.player_or_enemy_x += enemyx_change

        if enemy.player_or_enemy_x <= 0:
            enemyx_change = 4
            enemy.player_or_enemy_y += enemyy_change

        elif enemy.player_or_enemy_x >= 736:
            enemyx_change = -4
            enemy.player_or_enemy_y += enemyy_change

        player.add_player_or_enemy(screen)
        enemy.add_player_or_enemy(screen)

        pygame.display.update()