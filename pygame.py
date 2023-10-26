import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Piano Tiles Game")

# Colors
WHITE = (255, 255, 255)

# Clock for controlling the game's speed
clock = pygame.time.Clock()

# Tile dimensions and setup
TILE_WIDTH = WIDTH // 4  # Divide the screen into 4 columns
TILE_HEIGHT = HEIGHT // 5  # Height of each tile
tiles = []

# Load tile images (adjust file paths)
tile_images = [pygame.image.load("C:/Users/vansh/Downloads/chr1.png"),
               pygame.image.load("C:/Users/vansh/Downloads/chr2.png"),
               pygame.image.load("C:/Users/vansh/Downloads/chr3.png"),
               pygame.image.load("C:/Users/vansh/Downloads/chr4.png")]

# Tile class
class Tile:
    def __init__(self, x, y, image):
        self.rect = pygame.Rect(x, y, TILE_WIDTH, TILE_HEIGHT)
        self.image = image
        self.speed = 2  # Adjust the speed as needed

# Game variables
score = 0
font = pygame.font.Font(None, 36)
spawn_timer = 0  # Initialize the timer for spawning new tiles

# Scrolling background setup
bg_x = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for tile in tiles:
                if tile.rect.collidepoint(x, y):
                    tiles.remove(tile)
                    score += 1

    # Scrolling background (adjust background image)
    background = pygame.image.load("C:/Users/vansh/Downloads/forest background.jpg")
    SCREEN.blit(background, (bg_x, 0))
    SCREEN.blit(background, (bg_x + WIDTH, 0))
    bg_x -= 2
    if bg_x <= -WIDTH:
        bg_x = 0

    # Spawn new tiles periodically
    spawn_timer += 1
    if spawn_timer >= 60:  # Adjust the timer based on your preference
        x = random.randrange(4) * TILE_WIDTH
        tile_image = random.choice(tile_images)
        new_tile = Tile(x, 0, tile_image)
        tiles.append(new_tile)
        spawn_timer = 0

    # Move and draw tiles
    for tile in tiles:
        tile.rect.move_ip(0, tile.speed)
        SCREEN.blit(tile.image, tile.rect)

    # Remove tiles that go off the screen or are clicked
    tiles = [tile for tile in tiles if tile.rect.y < HEIGHT]

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    SCREEN.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
