from abc import ABCMeta, abstractmethod
class GameObject(metaclass=ABCMeta):
    def __init__(self, pygame, game_object_img_path, postion_x, postion_y):
         # Player / Enemy / Bullet
         self.game_object_img = pygame.image.load(game_object_img_path)
         self.game_object_x = postion_x
         self.game_object_y = postion_y

    @abstractmethod
    def add_object(self, screen, player_x_pos = None, bullet_state = None):
        pass

    @abstractmethod
    def object_movement(self, *change_movement_params):
        pass