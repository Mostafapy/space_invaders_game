class Player:
    def __init__(self, pygame, player_img_path):
         # Player
         self.player_img = pygame.image.load(player_img_path)
         self.player_x = 370
         self.player_y = 480

    
    def add_player(self, screen):
        screen.blit(self.player_img, (self.player_x, self.player_y))
