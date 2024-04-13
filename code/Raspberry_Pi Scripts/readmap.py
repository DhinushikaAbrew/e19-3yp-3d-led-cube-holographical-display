import os
import numpy as np

current_file_path = os.path.abspath(__file__)
map_file_path = os.path.join(os.path.dirname(current_file_path), 'map.txt')

cube = [[] for _ in range(16)]

with open(map_file_path, 'r') as file:
    layer = []
    for i, line in enumerate(file):
        layer.append([int(x) for x in line.strip().split()])
        
        # If this was the 16th row of the layer, add the layer to the cube
        if (i + 1) % 16 == 0:
            cube.append(layer)
            layer = []



print(cube)