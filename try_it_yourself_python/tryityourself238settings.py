class Settings:
    """A clas to store the background color of a pygame"""

    def __init__(self):
        """Initialize variables"""
        # Screen settings
        self.screen_width = 1250
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Bullet Settings
        self.bullet_speed = 4.5
        self.bullet_width = 8
        self.bullet_height = 8
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Mage settings
        self.mage_speed = 6

        # Golem settings
        self.golem_speed = 1.0
        self.fleet_drop_speed_left = -9
        # fleet direction
        self.fleet_direction_bottom = -1