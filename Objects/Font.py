from Objects.GameObject import GameObject

class Font(GameObject):
    def add_object(self, screen, score_value):
        score = self.game_object_img_or_font.render("Score: " + str(score_value.value), True, (255, 128, 0))
        screen.blit(score, (self.game_object_x, self.game_object_y))

    def object_movement(self, params = None):
        pass