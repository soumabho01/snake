import pygame
import time
import random

# Initialize pygame
pygame.init()

# Window dimensions
width = 600
height = 400

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

# Snake block size
block_size = 10
speed = 15

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Xenzia")

# Clock for controlling speed
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("bahnschrift", 20)


def draw_snake(block_size, snake_list):
    """Draws the snake on the screen."""
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])


def show_message(msg, color, x, y):
    """Displays a message on the screen."""
    message = font.render(msg, True, color)
    screen.blit(message, [x, y])


def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    # Snake starting position
    x, y = width // 2, height // 2
    dx, dy = 0, 0

    # Snake body
    snake_list = []
    length = 1

    # Food position
    food_x = random.randrange(0, width - block_size, block_size)
    food_y = random.randrange(0, height - block_size, block_size)

    while not game_over:
        while game_close:
            screen.fill(black)
            show_message("Game Over! Press R to Restart or Q to Quit", red, 100, height // 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -block_size, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = block_size, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -block_size
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, block_size

        # Update snake position
        x += dx
        y += dy

        # Check if snake hits the wall
        if x < 0 or x >= width or y < 0 or y >= height:
            game_close = True

        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        # Update snake body
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        # Check for collision with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - block_size, block_size)
            food_y = random.randrange(0, height - block_size, block_size)
            length += 1

        clock.tick(speed)

    pygame.quit()


# Start the game
game_loop()
