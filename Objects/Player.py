from Objects.GameObject import GameObject
class Player(GameObject):

    def add_object(self, screen, player_x_pos= None, bullet_state = None):
        if player_x_pos is None and bullet_state is None:
            screen.blit(self.game_object_img, (self.game_object_x, self.game_object_y))

    def object_movement(self, player_x_change):
         # Add game boundries for player
        self.game_object_x+= player_x_change.value
        
        if self.game_object_x <= 0:
           self.game_object_x = 0
        elif self.game_object_x >= 736:
            self.game_object_x = 736