def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    
    word = "XMAS"
    
    xmas_occurrences = set()
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    def check_direction(start_r, start_c, dr, dc):
        r, c = start_r, start_c
        
        for letter in word:
            if not is_valid(r, c) or grid[r][c] != letter:
                return False
            r += dr
            c += dc
        
        return True
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    occurrence = tuple(
                        (r + i*dr, c + i*dc) for i in range(len(word))
                    )
                    xmas_occurrences.add(occurrence)
    return len(xmas_occurrences)


grid = []
with open ('input.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    grid.append(line)

rows = len(grid)
cols = len(grid[0])

print(find_xmas(grid))