import math, random, time
from Objects.GameObject import GameObject

class Bullets(GameObject):
     def add_object(self, screen, bullet_state):
           bullet_state.value = "fire"
           screen.blit(self.game_object_img_or_font, (self.game_object_x + 8, self.game_object_y + 2))
    
     def object_movement(self, screen, bullety_change, bullet_state):
         if self.game_object_y <= 0:
            self.game_object_y = 480
            bullet_state.value = "ready" 

         if bullet_state.value is "fire":
             self.add_object(screen, bullet_state)
             self.game_object_y -= bullety_change.value

     def is_collision(self, enemy_x, enemy_y):
         distance = math.sqrt((math.pow(enemy_x - self.game_object_x, 2)) + (math.pow(enemy_y- self.game_object_y, 2)))
         if distance < 27:
             return True
         else:
             return False

     def add_collision(self, enemy, bullet_state, score, pygame):
         iscollide = self.is_collision(enemy.game_object_x, enemy.game_object_y)
         if iscollide:
             collision_sound = pygame.mixer.Sound("sounds/explosion.wav")
             sound_channel_A = collision_sound.play()
             self.game_object_y = 480
             bullet_state.value = "ready"
             score.value += 1
             enemy.game_object_x = random.randint(0, 735)
             enemy.game_object_y= random.randint(50, 150)
             time.sleep(1.8741949796676636)
             if sound_channel_A.get_busy():
                sound_channel_A.stop()

