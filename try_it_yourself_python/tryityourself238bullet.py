import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the mage"""

    def __init__(self, mg_game):
        """Create a bullet object at the mage's current position."""
        super().__init__()
        self.screen = mg_game.screen
        self.settings = mg_game.settings
        self.color = self.settings.bullet_color

        # Create the bullet image at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midleft = mg_game.mage.rect.midleft

        # Sotre the bullet's position as a float.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the right of the screen"""
        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed
        # Updage the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
