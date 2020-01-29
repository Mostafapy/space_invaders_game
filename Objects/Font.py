from Objects.GameObject import GameObject

class Font(GameObject):
    def add_object(self, screen, text):
        score = self.game_object_img_or_font.render(text, True, (255, 128, 0))
        screen.blit(score, (self.game_object_x, self.game_object_y))

    def object_movement(self, params = None):
        pass