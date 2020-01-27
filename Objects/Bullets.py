from Objects.GameObject import GameObject

class Bullets(GameObject):
     def add_object(self, screen, player_x_pos = None, bullet_state = None):
        if player_x_pos is not None and bullet_state is not None:
           bullet_state.value = "fire"
           screen.blit(self.game_object_img, (player_x_pos + 16, self.game_object_y + 10))
    
     def object_movement(self, screen, player_x, bullety_change, bullet_state):
         if bullet_state.value is "fire":
             self.add_object(screen, player_x, bullet_state)
             self.game_object_y -= bullety_change.value