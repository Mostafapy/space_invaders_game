from GameObject import GameObject
class Player(GameObject):
    def add_object(self, screen):
        screen.blit(self.game_object_img, (self.game_object_x, self.game_object_y))