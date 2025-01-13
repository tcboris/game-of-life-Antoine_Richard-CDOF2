import time
import os
import random

def create_grid(rows, cols, live_density=0.5, pattern=None):
    """Create a grid with customizable live density or predefined pattern."""
    if pattern:
        return [[pattern.get((x, y), " ") for y in range(cols)] for x in range(rows)]
    else:
        return [
            ["#" if random.random() < live_density else " " for _ in range(cols)]
            for _ in range(rows)
        ]

def print_grid(grid):
    """Print the grid to the console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print("".join(row))

def count_live_neighbors(grid, x, y):
    """Count live neighbors for a cell."""
    rows, cols = len(grid), len(grid[0])
    neighbors = [
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
        (x, y - 1),             (x, y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1),
    ]
    count = 0	
    for nx, ny in neighbors:
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "#":
            count += 1
    return count

def next_generation(grid):
    """Compute the next generation of the grid."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[" " for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_live_neighbors(grid, x, y)
            if grid[x][y] == "#" and live_neighbors in [2, 3]:
                new_grid[x][y] = "#"
            elif grid[x][y] == " " and live_neighbors == 3:
                new_grid[x][y] = "#"
    return new_grid

def main():
    """Run Conway's Game of Life."""
    rows, cols = 20, 40  # Grid size
    grid = create_grid(rows, cols)

    while True:
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
