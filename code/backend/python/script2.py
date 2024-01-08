"""import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read_obj_file(file_path):
    vertices = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parts = line.split()
                if len(parts) > 0:
                    if parts[0] == 'v':
                        vertex = list(map(float, parts[1:]))
                        vertices.append(vertex)
                    elif parts[0] == 'f':
                        face = [int(v.split('/')[0]) - 1 for v in parts[1:]]
                        # Check if the face has three vertices (assumed for triangular faces)
                        if len(face) == 3:
                            faces.append(face)
                        # For faces with more vertices, you might need different handling
                        # or triangulation if necessary
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return np.array([]), np.array([])
    except PermissionError:
        print(f"Error: Permission denied to open file '{file_path}'.")
        return np.array([]), np.array([])
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return np.array([]), np.array([])

    return np.array(vertices), np.array(faces)

def map_to_grid(vertices, grid_size):
    min_coords = np.min(vertices, axis=0)
    max_coords = np.max(vertices, axis=0)
    normalized_coords = (vertices - min_coords) / (max_coords - min_coords)
    scaled_coords = normalized_coords * (grid_size - 1)
    return scaled_coords

grid_size = 16

# Creating the 16x16x16 grid points
x_range = np.linspace(0, grid_size - 1, grid_size)
y_range = np.linspace(0, grid_size - 1, grid_size)
z_range = np.linspace(0, grid_size - 1, grid_size)
grid_points = np.array(np.meshgrid(x_range, y_range, z_range)).reshape(3, -1).T

# Mapped vertices from the OBJ file onto the grid
file_path = 'man.obj'
vertices, _ = read_obj_file(file_path)

# Check if vertices were loaded successfully
if vertices.size == 0:
    print("No vertices were loaded.")
    exit()  # Exit the script if there are no vertices

mapped_vertices = map_to_grid(vertices, grid_size)

# Get the coordinates for grid and mapped vertices
grid_coords = grid_points.astype(int)
mapped_coords = mapped_vertices.astype(int)

# Find common coordinates
common_coords = np.array([coord for coord in grid_coords if np.any(np.all(mapped_coords == coord, axis=1))])

# Plotting the 16x16x16 grid points, mapped vertices, and common points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Setting dark background color
# ax.set_facecolor('black')

# Plotting the 16x16x16 grid points
# ax.scatter(grid_points[:, 0], grid_points[:, 1], grid_points[:, 2], color='grey')

# Plotting the mapped vertices from the OBJ file
# ax.scatter(mapped_vertices[:, 0], mapped_vertices[:, 1], mapped_vertices[:, 2], color='yellow')

# Plotting the common points in red
if common_coords.size > 0:
    ax.scatter(common_coords[:, 0], common_coords[:, 1], common_coords[:, 2], color='red')

# Equal aspect ratio for all axes
ax.set_box_aspect([1, 1, 1])  # You can adjust these values for desired aspect ratio

plt.show()"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys


def read_obj_file(file_path):
    vertices = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) > 0 and parts[0] == "v":
                    vertex = list(map(float, parts[1:]))
                    vertices.append(vertex)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return np.array([])
    except PermissionError:
        print(f"Error: Permission denied to open file '{file_path}'.")
        return np.array([])
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return np.array([])

    return np.array(vertices)


def map_to_grid(vertices, grid_size):
    min_coords = np.min(vertices, axis=0)
    max_coords = np.max(vertices, axis=0)
    normalized_coords = (vertices - min_coords) / (max_coords - min_coords)
    scaled_coords = normalized_coords * (grid_size - 1)
    return scaled_coords


grid_size = 16

# Creating the 16x16x16 grid points
x_range = np.linspace(0, grid_size - 1, grid_size)
y_range = np.linspace(0, grid_size - 1, grid_size)
z_range = np.linspace(0, grid_size - 1, grid_size)
grid_points = np.array(np.meshgrid(x_range, y_range, z_range)).reshape(3, -1).T

# Reading OBJ file and mapping vertices to grid
file_path = sys.argv[1]
vertices = read_obj_file(file_path)

# Check if vertices were loaded successfully
if vertices.size == 0:
    print("No vertices were loaded.")
    exit()  # Exit the script if there are no vertices

mapped_vertices = map_to_grid(vertices, grid_size)

# Get the coordinates for grid and mapped vertices
grid_coords = grid_points.astype(int)
mapped_coords = mapped_vertices.astype(int)

# Find common coordinates
common_coords = np.array(
    [coord for coord in grid_coords if np.any(np.all(mapped_coords == coord, axis=1))]
)

# Create a binary matrix indicating common coordinates
binary_matrix = np.zeros((grid_size, grid_size, grid_size), dtype=int)

for coord in common_coords:
    binary_matrix[coord[0], coord[1], coord[2]] = 1

# Save the binary matrix to a text file (row-wise)
text_file_path = "common_matrix.txt"
np.savetxt(
    text_file_path,
    binary_matrix.reshape((grid_size**2, grid_size), order="C"),
    fmt="%d",
    delimiter=" ",
)

# Save the binary matrix to a .npy file
npy_file_path = "common_matrix.npy"
np.save(npy_file_path, binary_matrix)

# Plotting the 16x16x16 grid points, mapped vertices, and common points
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Setting dark background color
# ax.set_facecolor('black')

# Plotting the 16x16x16 grid points
# ax.scatter(grid_points[:, 0], grid_points[:, 1], grid_points[:, 2], color='grey')

# Plotting the mapped vertices from the OBJ file
# ax.scatter(mapped_vertices[:, 0], mapped_vertices[:, 1], mapped_vertices[:, 2], color='yellow')

# Plotting the common points in red
if common_coords.size > 0:
    ax.scatter(
        common_coords[:, 0], common_coords[:, 1], common_coords[:, 2], color="red"
    )

# Equal aspect ratio for all axes
ax.set_box_aspect([1, 1, 1])  # You can adjust these values for desired aspect ratio

plt.show()