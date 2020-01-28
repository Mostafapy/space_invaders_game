from Objects.GameObject import GameObject

class Bullets(GameObject):
     def add_object(self, screen, bullet_state = None):
        if bullet_state is not None:
           bullet_state.value = "fire"
           screen.blit(self.game_object_img, (self.game_object_x + 16, self.game_object_y + 10))
    
     def object_movement(self, screen, bullety_change, bullet_state):
         if self.game_object_y <= 0:
            self.game_object_y = 480
            bullet_state.value = "ready" 

         if bullet_state.value is "fire":
             self.add_object(screen, bullet_state)
             self.game_object_y -= bullety_change.value