# The following packages needs to be installed first with:
# $     pip install pygame cmap
# (don't forget to enter your virtual environment first)
import pygame
import cmap
import random
from typing import Tuple, List

def reset(screen:pygame.Surface, cell_size:int, number_states:int) -> Tuple[int, pygame.Surface, List[int]]:
    ''' returns fresh game setting and blank screen/ cell states '''
    generation = 0
    cells = [[random.randint(0,number_states) for _ in range(int(window_width/cell_size))] for _ in range(int(window_height/cell_size))] # initial cell states (off)
    return generation, screen, cells

def kernel_surroundings(cells: List[List[int]], x: int, y: int, R: int, include_center:bool=False) -> List[int]:
    """
    Given a 2D array of cells and a central position, return all neighboring states within radius R.
    Wrap around the edges if necessary (toroidal wrapping).
    """
    surroundings = []
    num_rows = len(cells)
    num_cols = len(cells[0])

    for dy in range(-R, R + 1):
        for dx in range(-R, R + 1):
            if (dx == 0 and dy == 0):
                if include_center:
                    surroundings.append(cells[dy][dx])
                    continue
                else:
                    # Skip the center cell itself
                    continue
            wrapped_x = (x + dx) % num_cols
            wrapped_y = (y + dy) % num_rows
            surroundings.append(cells[wrapped_y][wrapped_x])

    return surroundings

def growth(neighbors:int, b:Tuple[int, int], s:Tuple[int, int]):
    '''b1..b2 is birth range, s1..s2 is stable range (outside s1..s2 is shrink range)'''
    b1, b2 = b[0], b[1]
    s1, s2 = s[0], s[1]
    return 0 + (int(neighbors>=b1)&int(neighbors<=b2)) - (int(neighbors<s1)|int(neighbors>s2))

def clip(a, a_min, a_max):
    return min(a_max, max(a, a_min))


# Initialize game, set screen parameters
window_height = 600
window_width = 600
cell_size = 10
assert cell_size > 1
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("NaCo - Exercise 2 (Primordia)")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)

# more ... parameters?
number_states = 10 # i.e., number_states = 10 -> [0, ..., 10] etc.
colormap = cmap.Colormap("viridis", interpolation="linear")
generation, screen, cells = reset(screen, cell_size, number_states)
birth_range = (0.20,0.25)
stable_range = (0.18,0.32)

# start and loop the game indefinitely
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # quit window, exit loop
    
    # Loop through the cells in the current generation drawing each (normalize values for colormap)
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            cell = cell / number_states
            pygame.draw.rect(screen, pygame.Color(colormap(cell).rgba8.r, colormap(cell).rgba8.b, colormap(cell).rgba8.g), [i*cell_size, cell_size*j, cell_size, cell_size])

    for y, row in enumerate(cells):
        for x, cell in enumerate(row):
            neighbors = kernel_surroundings(cells, x, y, 3)
            neighbors = [n/(number_states*len(neighbors)) for n in neighbors] # (normalized states and kernel)
            cells[x][y] = clip(cell + growth(sum(neighbors), birth_range, stable_range), 0, number_states)

    # Draw generation-string on screen
    generation_string = font.render(f"GEN {int(generation)}", True, pygame.Color('red'))
    screen.blit(generation_string, (10, 10))

    # Render everything to the screen
    pygame.display.flip()
    generation += 1

    # Wait until the next generation
    timeout_in_ms = 100
    clock.tick(1000/timeout_in_ms)
    
# Be IDLE friendly
pygame.quit()