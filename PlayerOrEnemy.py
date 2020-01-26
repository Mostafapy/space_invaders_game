class PlayerOrEnemy:
    def __init__(self, pygame, player_or_enemy_img_path, postion_x, postion_y):
         # Player / Enemy
         self.player_or_enemy_img = pygame.image.load(player_or_enemy_img_path)
         self.player_or_enemy_x = postion_x
         self.player_or_enemy_y = postion_y

    
    def add_player_or_enemy(self, screen):
        screen.blit(self.player_or_enemy_img, (self.player_or_enemy_x, self.player_or_enemy_y))
