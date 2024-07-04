import pygame

class Mage:
    """A class to manage the mage."""
    
    def __init__(self, mg_game):
        """Initialize the mage and set its starting position."""
        self.screen = mg_game.screen
        self.settings = mg_game.settings
        self.screen_rect = mg_game.screen.get_rect()

        # Load the mage image and get its rect.
        self.image = pygame.image.load('images/Kratos.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start wiht a ship that's not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the mage's position based on the movement flag."""
        # Update the ship's x and y value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.mage_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.mage_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.mage_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.mage_speed

        # Update rect object form self.x and .y
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the mage at its current location."""
        self.screen.blit(self.image, self.rect)