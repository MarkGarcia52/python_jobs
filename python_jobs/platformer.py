import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    # Will load each sprite for hitting, falling, etc
    path = join("assets", dir1, dir2)
    # We can split images here.
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        # Loading images from file above
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            # srcaplha = load transparent images, 32 is depth
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            # rectangle where in this image, where we want to take an individ. image from and blit it
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            # In the top left color, im drawing the frame from the sprite sheet i want
            sprites.append(pygame.transform.scale2x(surface))
            # Stripped each frame

        if direction:
            # If you want a multidirectional animation then we 
            # appending each fram to each left and frames
            all_sprites[image.replace(".png", "") + "_right"] * sprites
            all_sprites[image.replace(".png", "") + "_left"] * flip(sprites)

        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


        # Load all different files, we need each individual image from sprite sheets



class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        # How fast we are moving our player in both directions
        #   he will keep moving until we stop him
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel):
        # Move the character to the left
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        # Move the character to the right
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        # Called once every frame, move character in right direction
       # self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1

    def draw(self, win):
        self.sprite = self.SPRITES["idle_" + self.direction][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y))


def get_background(name):
    # Returns the list of all the different background tiles.
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range (HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)


    return tiles, image

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update()

def handle_move(player):
    # Check the keys that are being pressed.
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    # Only want the person to move when we press a key.
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Purple.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        
        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)