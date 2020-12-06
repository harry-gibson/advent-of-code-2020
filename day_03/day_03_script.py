import numpy as np
from io import StringIO
import math


def count_trees(arr, steps_right, steps_down):
    n_rows, n_cols = arr.shape    
    n_rows = math.floor(n_rows / steps_down)
    across_positions = [(steps_right * n)  % n_cols for n in range(n_rows)]
    flat_array_positions = [
        (rownum * n_cols * steps_down) + across_positions[rownum] for rownum in range(n_rows)]
    total_trees = arr.ravel()[flat_array_positions].sum()
    return total_trees

with open('input.txt', 'r') as f:
   data = f.read().replace('.', '0').replace('#', '1')
# using converters parameter to change #/. to 1/0 is a pain if 
# we don't know the number of columns. So string-replace them all first
trees_map = np.genfromtxt(StringIO(data), delimiter=1, dtype='uint8')

part_2_slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
part_1_slope = part_2_slopes[1]

print (f"Part 1: {count_trees(trees_map, *part_1_slope)} trees hit")

part_2_trees = [count_trees(trees_map, *s) for s in part_2_slopes]
part_2_res = np.prod(part_2_trees)
print (f"Part 2: Product of total trees hit is {part_2_res}")