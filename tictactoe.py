
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

# Define variables
line_width = 6
markers = []
clicked = False
pos = []
player = 1

# Define colors (marker colors)
green = (0, 255, 0)
red = (255, 0, 0)

# Create grid and setup the grid list
def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)

for i in range(3):
    row = [0] * 3
    markers.append(row)


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width) 
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            
            y_pos += 1
        x_pos += 1

# Setup loop with exit event handler
run = True
while run:

    draw_grid()
    draw_markers()

    for event in pygame.event.get():

        # If we click exit button on window
        if event.type == pygame.QUIT:
            run = False
        
        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            click = False
            # Get (x,y) of mouse when clicked
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]

            if markers[cell_x // 100][cell_y // 100] == 0:
                markers[cell_x // 100][cell_y // 100] = player
                player *= -1

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
