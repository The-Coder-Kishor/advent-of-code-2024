def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                if i-1 >= 0 and j-1 >= 0 and i+1 < rows and j+1 < cols:
                    if (grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M'):
                        if i-1 >= 0 and j+1 < cols and i+1 < rows and j-1 >= 0:
                            if (grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S') or (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'):
                                count += 1
    return count



grid = []
with open ('input.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    grid.append(line)

rows = len(grid)
cols = len(grid[0])
print(find_xmas(grid))