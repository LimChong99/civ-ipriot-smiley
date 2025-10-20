from smiley import Smiley

class Angry(Smiley):
    """
    Provides a Smiley with an angry expression.
    """
    def __init__(self):
        # Call the parent constructor and set the complexion to RED
        super().__init__(complexion=self.RED)
        
        # Draw the unique features for an angry face
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws a straight, angry mouth.
        """
        mouth = [41, 42, 43, 44, 45, 46]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self):
        """
        Draws angry, slanted eyes.
        """
        eyes = [10, 19, 13, 20] # These pixels create a \ / shape for the eyes
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK