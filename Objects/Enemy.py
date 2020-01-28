from Objects.GameObject import GameObject
class Enemy(GameObject):
    def add_object(self, screen, args= None):
        screen.blit(self.game_object_img_or_font, (self.game_object_x, self.game_object_y))

    def object_movement(self, enemy_x_change, enemy_y_change):
        # Add game boundries for enemy
        self.game_object_x += enemy_x_change.value

        if self.game_object_x <= 0:
            enemy_x_change.value = 1
            self.game_object_y += enemy_y_change.value

        if self.game_object_x >= 736:
            enemy_x_change.value = -1
            self.game_object_y += enemy_y_change.value