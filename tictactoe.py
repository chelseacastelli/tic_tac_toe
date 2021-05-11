
#import modules
import pygame
from pygame.locals import *

pygame.init()

## Part 1:
# Create blank game window
screen_width = 300;
screen_height = 300;

# Displays screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

line_width = 6

# Create grid and setup the grid list
def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)

# Setup loop with exit event handler
run = True
while run:

    draw_grid()

    for event in pygame.event.get():
        # If we click exit button on window
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
        
pygame.quit()

## Part 2:
# Create event handler for clicking on a cell
# Check if cell is empty and place a marker
# Setup function for drawing markers onto the grid

## Part 3:
# Create check_winner() including checks for winning combos

# Create event handler for post game

# Reset game
