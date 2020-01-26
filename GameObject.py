class GameObject:
    def __init__(self, pygame, game_object_img_path, postion_x, postion_y):
         # Player / Enemy / Bullet
         self.game_object = pygame.image.load(game_object_img_path)
         self.game_object_x = postion_x
         self.game_object_y = postion_y
         super.__init__()

    @abstractmethod
    def add_object(self, screen):
        pass

    