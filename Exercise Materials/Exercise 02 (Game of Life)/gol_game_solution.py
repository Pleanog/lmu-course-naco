# The pygame package needs to be installed first with:
# $     pip install pygame
# (don't forget to enter your virtual environment first)
import pygame
from typing import Tuple, List

def reset(screen:pygame.Surface, cell_size:int) -> Tuple[int, pygame.Surface, List[int]]:
    ''' returns fresh game setting and blank screen/ cell states '''
    rulesetcode = None
    generation = 0   
    screen.fill((255, 255, 255)) # fill screen white
    cells = [[0 for e in range(int(window_width/cell_size))] for _ in range(int(window_height/cell_size))] # initial cell states (off)
    return generation, screen, cells


def glider_pattern(cells:List[List[int]], x:int, y:int)-> List[List[int]]:
    '''sets the glider pattern to the specified position on board, returns cells array'''
    assert (x,y) <= (len(cells[0]), len(cells)+2), "Position outside of board dimensions"
    
    cells[y-1][x+2] = 1
    cells[y][x] = 1
    cells[y][x+2] = 1
    cells[y+1][x+1] = 1
    cells[y+1][x+2] = 1
    cells[y+1][x+2] = 1
    return cells


def rle_pattern(cells:List[List[int]], x:int, y:int, rle_string:str)-> List[List[int]]:
    '''sets the run-length encoded patterns to alife-state on given position, returns cells array'''
    assert (x,y) <= (len(cells[0]), len(cells)), "Position outside of board dimensions"
    assert rle_string[-1] == "!", "RLE string not properly terminated with '!' character"
    
    # For all rle_str lines (without that final "!" character)
    for y_offset, rowstr in enumerate(rle_string[:-1].split("$")):
        # decode each substring (e.g. "3o2b" -> "ooobb"): parse for digits by maintaining a digit_str
        # as long as digits are read. Then, the next time a letter is found, repeat that letter *
        # the previously collected digits (as int) and reset the factor. Works because the RLE format
        # is always of the form (int)(letter)(int)(letter), even if just implicitly "bobo" == "1b1o1b1o"
        i=0
        factor_str = ""
        decoded_str = ""
        while i < len(rowstr):
            if rowstr[i].isdigit(): # isdigit
                factor_str += rowstr[i]
                i += 1
            else: # isletter
                decoded_str += int(factor_str if factor_str else 1) * rowstr[i]
                factor_str = ""
                i += 1
        
        # finally, set all 'alive' cells to 1 (and repeat for the next rle_str lines)
        for x_offset, state in enumerate(decoded_str):
            if state == "o":
                cells[y+y_offset][x+x_offset] = 1
    return cells


def moore_surroundings(cells:List[List[int]], x:int, y:int) -> List[int]:
    '''given a board of cells and a center position, return all 8 surrounding (moore neighbourhood) states'''
    row_above = cells[y-1]
    row = cells[y]
    row_below = cells[(y+1)%len(cells)]
    surroundings = []
    surroundings.append(row_above[x-1])                    # top left
    surroundings.append(row_above[x])                      # top
    surroundings.append(row_above[(x+1)%len(row_above)])   # top right
    surroundings.append(row[x-1])                          # left
    surroundings.append(row[(x+1)%len(row)])               # right
    surroundings.append(row_below[x-1])                    # bottom left
    surroundings.append(row_below[x])                      # bottom
    surroundings.append(row_below[(x+1)%len(row)])         # bottom right
    return surroundings


# Initialize game, set screen parameters
window_height = 600
window_width = 600
cell_size = 10
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("NaCo - Exercise 2 (Solution)")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)

# Render the initial board and draw some GoL patterns
generation, screen, cells = reset(screen, cell_size)
#cells = glider_pattern(cells, x=10, y=10)

# (Bonus) Code the RLE decoding function above and test on the following RLE patterns:
cells = rle_pattern(cells, x=10, y=10, rle_string="bo$2bo$3o!")  # glider down right
# cells = glider_pattern(cells, x=10, y=10) # glider down right using the glider_pattern function
cells = rle_pattern(cells, x=20, y=10, rle_string="3o!")         # blinker
cells = rle_pattern(cells, x=30, y=10, rle_string="2o$2o!")      # block
cells = rle_pattern(cells, x=40, y=10, rle_string="bo$3o!")      # tetramino


done = False
while not done:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # quit window, exit loop
    
    # Loop through the cells in the current generation drawing each
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            if cell == 1:
                # If the cell size is a single pixel we can't use rect to draw it
                if cell_size > 1:
                    pygame.draw.rect(screen, (0, 0, 0), [i*cell_size, cell_size*j, cell_size, cell_size])
                else:
                    screen.set_at((i*cell_size, cell_size*generation), (0, 0, 0))

    # Loop through the cells, checking the cells' surroundings and calculating the subsequent generation state
    next_generation = [[0 for e in range(int(window_width/cell_size))] for _ in range(int(window_height/cell_size))]
    for y, row in enumerate(cells):
        for x, cell in enumerate(row):
            neighbors = moore_surroundings(cells, x, y)
            if cells[y][x] == 0 and sum(neighbors) == 3:
                next_generation[y][x] = 1
            elif cells[y][x] == 1 and sum(neighbors) in [2,3]:
                next_generation[y][x] = 1
    cells = next_generation

    # Draw generation-string on screen
    generation_string = font.render(f"GEN {int(generation)}", True, pygame.Color('black'))
    screen.blit(generation_string, (10, 10))

    # Render everything to the screen
    pygame.display.flip()
    generation += 1

    # Wait until the next generation
    timeout_in_ms = 100
    clock.tick(1000/timeout_in_ms)
    
# Be IDLE friendly
pygame.quit()