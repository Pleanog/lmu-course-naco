# nice progress bar animation, needs to be installed first with:
# $     pip install tqdm
# (don't forget to enter your virtual environment first)
from tqdm import tqdm,trange
from typing import Tuple

def apply_rule(rule_number:int, neighborhood:Tuple[int, int, int]) -> int:
    ''' returns cell state of next generation given a cell (middle) and its neighbors '''
    # Decimal form of the (binary) neighborhood. Used to acces a new cell from the ruleset array.
    rule_index = int(''.join(str(neighbor_state) for neighbor_state in neighborhood), 2)
    # converts decimal into an 8 bit number (represented as a list), reverse list for correct indexing
    rule_cases = list('{0:08b}'.format(rule_number))
    rule_cases.reverse()
    return int(rule_cases[rule_index])

# For a given smaller state-space (here 2^{board_with}) we brute force check if after application
# of all 256 rules (to any possible starting-configuration state in the cells list),
# there are state candidates left that were not found (i.e., 'orphans').
board_width = 10
for rule_number in trange(0,256):
    unreachable_states = [f'{state:010b}' for state in range(2**board_width)]
    for cells in [list(f'{state:010b}') for state in range(2**board_width)]:
        
        next_generation = []
        for i, cell in enumerate(cells):
            left = cells[(i-1)]
            middle = cell
            right = cells[(i+1) % len(cells)]
            next_cell_state = rules(rule_number, (left, middle, right))
            next_generation.append(next_cell_state)
        
        # convert [1,1,0,1...]:List[int] -> '11001...':str
        next_generation_state = "".join(str(cell) for cell in next_generation)
        # remove all reached states, i.e., any canidates left in the unreachable_states are our orphans 
        unreachable_states.remove(next_generation_state) if next_generation_state in unreachable_states else None

    tqdm.write(f"Rule: {rule_number:3}: found {len(unreachable_states):3} orphans for board width {board_width}.")