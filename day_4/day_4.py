import sys

def check_neighbors(grid, r, c):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]):
            if grid[nr][nc] == '@':
                count += 1
    return count

def part_1(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '.': continue

            neighbors = check_neighbors(grid, r, c)
            if neighbors < 4:
                count += 1

    return count

def part_2(grid):
    count = 0
    keep_going = True
    while keep_going:
        inner_count = 0
        places_to_update = []
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '.': continue

                neighbors = check_neighbors(grid, r, c)
                if neighbors < 4:
                    inner_count += 1
                    places_to_update.append((r, c))

        if inner_count == 0:
            keep_going = False
        else:
            count += inner_count
            for r, c in places_to_update:
                grid[r][c] = '.'

    return count

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        grid = [list(list(line.strip())) for line in file.readlines()]

    result = part_2(grid)
    print(result)
