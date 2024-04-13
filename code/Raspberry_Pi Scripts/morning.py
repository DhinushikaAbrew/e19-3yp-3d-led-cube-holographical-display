
# Read the map.txt file
with open('map.txt', 'r') as file:
    # Create an empty 3D list
    cube = []
    
    # Iterate over each line in the file
    for line in file:
        # Remove any leading or trailing whitespace
        line = line.strip()
        
        # Create a 2D list for each line
        layer = [[int(char) for char in row] for row in line]
        
        # Add the layer to the cube
        cube.append(layer)
