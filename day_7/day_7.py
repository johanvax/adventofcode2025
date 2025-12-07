import sys

def part_1(manifold):
    ROWS = len(manifold)
    COLS = len(manifold[0])

    start = -1
    for c in range(COLS):
        if manifold[0][c] == "S":
            start = c
            break
    
    assert start != -1
    manifold[1][c] = "|"

    count_splits = 0
    for r in range(2, ROWS):
        for c in range(COLS):
            if manifold[r-1][c] == "|":
                if manifold[r][c] == "^":
                    count_splits += 1
                    manifold[r][c-1] = "|"
                    manifold[r][c+1] = "|"
                else:
                    manifold[r][c] = "|"
    
    print(count_splits)
    return manifold

def part_2(paths):
    ROWS = len(manifold)
    COLS = len(manifold[0])

    dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for c in range(COLS):
        if paths[0][c] == "S":
            dp[0][c] = 1
            break

    for r in range(ROWS - 1):
        for c in range(COLS):
            if dp[r][c] > 0:
                curr = paths[r][c]
                curr_paths = dp[r][c]

                if curr == "S" or curr == "|":
                    if paths[r+1][c] != ".":
                        dp[r+1][c] += curr_paths

                elif curr == "^":
                    if c > 0 and paths[r+1][c-1] != ".":
                        dp[r+1][c-1] += curr_paths

                    if c < COLS and paths[r+1][c+1] != ".":
                        dp[r+1][c+1] += curr_paths

    print(sum(dp[-1]))


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        input = f.readlines()

    manifold = [[line[i] for i in range(len(line)) if line[i] != "\n"] for line in input]

    paths = part_1(manifold)
    part_2(paths)
    