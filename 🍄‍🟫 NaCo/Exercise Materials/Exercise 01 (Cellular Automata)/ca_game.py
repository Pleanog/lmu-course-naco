# The pygame package needs to be installed first with ...
# $     pip install pygame
# (don't forget to enter your virtual environment first)
import pygame
import random
from typing import Tuple, List

def apply_rule(rule_number:int, neighborhood:Tuple[int, int, int]) -> int:
    ''' returns cell state of next generation given a cell (middle) and its neighbors '''
    # ***********************
    # your code here
    # ***********************
    pass

def reset(screen:pygame.Surface) -> Tuple[int, int, pygame.Surface, List[int]]:
    ''' returns fresh game setting and blank screen / cell states '''
    rule_number = random.randint(0, 255) # next rule number
    generation = 0   
    screen.fill((255, 255, 255)) # fill screen white
    cells = [0 for e in range(int(window_width/cell_size))] # initial cell states (off)
    cells[int(len(cells)/2)] = 1 # starting state (middle cell on)
    print("Current Rule: {0:d} \t({0:08b})".format(rule_number))
    return generation, rule_number, screen, cells


# initialize game, set screen parameters
window_height = 400
window_width = 800
cell_size = 5
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("NaCo - Exercise 1")
clock = pygame.time.Clock()

generation, rule_number, screen, cells = reset(screen)
done = False
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # quit window, exit loop
    
    # loop through the cells in the current generation drawing each
    for i, cell in enumerate(cells):
        if cell == 1:
            # if the cell size is a single pixel, we can't use rect to draw it
            if cell_size > 1:
                pygame.draw.rect(screen, (0, 0, 0), [i*cell_size, cell_size*generation, cell_size, cell_size])
            else:
                screen.set_at((i*cell_size, cell_size*generation), (0, 0, 0))

    # loop through the cells, select each cell's neighbors and calculate the subsequent generation
    #
    # ***********************
    # your code here
    # ***********************

    # if we've filled the screen, then pick a new rule and reset surface
    if (cell_size*generation) >= window_height:
        generation, rule_number, screen, cells = reset(screen)
    else:            
        # update only part of the screen so previous generations are left untouched
        pygame.display.update([0, cell_size*generation, window_width, window_height])
        generation += 1

    # wait until the next generation
    timeout_in_ms = 10
    clock.tick(1000/timeout_in_ms)
    
# be IDLE friendly
pygame.quit()