from random import randint

# Dimensions of the grid
height = 100
width = 100

# Add random cells (live (1) or dead (0))
def randomize(grid, width, height):
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = randint(0,1)

grid_model = [0] * height # Current grid
next_grid_model = [0] * height # Next grid

for i in range(height):
    grid_model[i] = [0] * width
    next_grid_model[i] = [0] * width

randomize(grid_model, width, height)

# Main logic of the game
def next_gen():
    global grid_model, next_grid_model

    # Count the neighbors in each cell
    for i in range(0, height):
        for j in range(0, width):
            cell = 0
            count = count_neighbors(grid_model, i, j)
            # If it's dead
            if grid_model[i][j] == 0:
                # And the count is 3
                if count == 3:
                    # Revive it 
                    cell = 1
            # If it's alive
            elif grid_model[i][j] == 1:
                # If it either has 2 or 3 neighbors
                if count == 2 or count == 3:
                    # Let it live
                    cell = 1
            # Set that cell in the next gen as the previous
            next_grid_model[i][j] = cell
            
    # Set the present grid to the next one
    temp = grid_model
    grid_model = next_grid_model
    next_grid_model = temp

# Count adjacent neighbors
def count_neighbors(grid, row, col):
    count = 0
    if row-1 >= 0:
        count = count + grid[row-1][col]
    if (row-1 >= 0) and (col-1 >= 0):
        count = count + grid[row-1][col-1]
    if (row-1 >= 0) and (col+1 < width):
        count = count + grid[row-1][col+1]
    if col-1 >= 0:
        count = count + grid[row][col-1]
    if col + 1 < width:
        count = count + grid[row][col+1]
    if row + 1 < height:
        count = count + grid[row+1][col]
    if (row + 1 < height) and (col-1 >= 0):
        count = count + grid[row+1][col-1]
    if (row + 1 < height) and (col+1 < width):
        count = count + grid[row+1][col+1]
    return count

if __name__ == "__main__":
    next_gen()