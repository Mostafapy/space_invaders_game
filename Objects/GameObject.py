from abc import ABCMeta, abstractmethod
class GameObject(metaclass=ABCMeta):
    def __init__(self, pygame, game_object_img_or_font_path, postion_x, postion_y):
         # Player / Enemy / Bullet
         if ".ttf" in game_object_img_or_font_path:
           self.game_object_img_or_font = pygame.font.Font(game_object_img_or_font_path, 32)
         else:
           self.game_object_img_or_font = pygame.image.load(game_object_img_or_font_path)
         self.game_object_x = postion_x
         self.game_object_y = postion_y

    @abstractmethod
    def add_object(self, screen, *args):
        pass

    @abstractmethod
    def object_movement(self, *change_movement_params):
        pass