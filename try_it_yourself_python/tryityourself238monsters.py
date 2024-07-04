import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    """A class to represent a single golem in the fleet."""

    def __init__(self, mg_game):
        """Initialize the golem and set its starting position"""
        super().__init__()
        self.screen = mg_game.screen
        self.settings = mg_game.settings

        # Load a monster image and set its rect attribute.
        self.image = pygame.image.load('images/Ice Golem.bmp')
        self.rect = self.image.get_rect()
    
        # Start each new golem at the right of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the golem's exact horizontal position.
    
    def check_edges(self):
        """Return True if golem is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.top <= screen_rect.top) or (self.rect.bottom >= screen_rect.bottom)

    def update(self):
        """Move the golem down"""
        self.y -= self.settings.golem_speed * self.settings.fleet_direction_bottom
        self.rect.y = self.y