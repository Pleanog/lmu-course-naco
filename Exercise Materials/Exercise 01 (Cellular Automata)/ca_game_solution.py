# The pygame package needs to be installed first with:
# $     pip install pygame
# (don't forget to enter your virtual environment first)
import pygame
import random
from typing import Tuple, List

def apply_rule(rule_number:int, neighborhood:Tuple[int, int, int]) -> int:
    ''' returns cell state of next generation given a cell (middle) and its neighbors '''
    # Decimal form of the (binary) neighborhood. Used to access a new cell from the ruleset array.
    rule_index = int(''.join(str(neighbor_state) for neighbor_state in neighborhood), 2)
    # converts decimal into an 8 bit number (represented as a list), reverse list for correct indexing
    rule_cases = list('{0:08b}'.format(rule_number))
    rule_cases.reverse()
    return int(rule_cases[rule_index])

def reset(screen:pygame.Surface) -> Tuple[int, int, pygame.Surface, List[int]]:
    ''' returns fresh game setting and blank screen / cell states '''
    rule_number = random.randint(0, 255) # next rule number
    generation = 0   
    screen.fill((255, 255, 255)) # fill screen white
    cells = [0 for e in range(int(window_width/cell_size))] # initial cell states (off)
    cells[int(len(cells)/2)] = 1 # starting state (middle cell on)
    print("Current Rule: {0:d} \t({0:08b})".format(rule_number))
    return generation, rule_number, screen, cells


# Initialize game, set screen parameters
window_height = 400
window_width = 800
cell_size = 5
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("NaCo - Exercise 1 (Solution)")
clock = pygame.time.Clock()

generation, rule_number, screen, cells = reset(screen)
done = False
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # quit window, exit loop
    
    # Loop through the cells in the current generation drawing each
    for i, cell in enumerate(cells):
        if cell == 1:
            # If the cell size is a single pixel we can't use rect to draw it
            if cell_size > 1:
                pygame.draw.rect(screen, (0, 0, 0), [i*cell_size, cell_size*generation, cell_size, cell_size])
            else:
                screen.set_at((i*cell_size, cell_size*generation), (0, 0, 0))

    # Loop through the cells, grabbing its neighbors and calculate the subsequent generation
    next_generation = []
    for i, cell in enumerate(cells):
        # wrap index if we're at the edge of the screen
        left = cells[(i-1)]
        middle = cell
        right = cells[(i+1) % len(cells)]
        next_cell_state = apply_rule(rule_number, (left, middle, right))
        # use new cell buffer so we don't overwrite cells while we're still using it
        next_generation.append(next_cell_state)
    cells = next_generation

    # If we've filled the screen then pick a new rule and reset surface
    if (cell_size*generation) >= window_height:
        generation, rule_number, screen, cells = reset(screen)
    else:            
        # Update only part of the screen so previous generations are left untouched
        pygame.display.update([0, cell_size*generation, window_width, window_height])
        generation += 1

    # Wait until the next generation (increase timeout to slow down animation)
    timeout_in_ms = 10
    clock.tick(1000/timeout_in_ms)
    
# Be IDLE friendly
pygame.quit()