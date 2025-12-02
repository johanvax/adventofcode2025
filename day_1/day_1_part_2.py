import sys

def process_input(input) -> list[tuple]:
    result = []
    for line in input:
        direction = line[0]
        value = int(line[1:])
        result.append((direction, value))
    return result

def count_right(current: int, input: int) -> tuple[int, int]:
    zeros = 0
    for _ in range(input):
        if current + 1 > 99:
            current = 0
            zeros += 1
        else:
            current += 1
    return current, zeros

def count_left(current: int, input: int) -> tuple[int, int]:
    zeros = 0
    for _ in range(input):
        if current - 1 < 0:
            current = 99
            zeros += 1
        else:
            current -= 1
    return current, zeros

def count_zeros(start, data):
    current = start
    zeros = 0
    for direction, value in data:
        if direction == "R":
            current, a = count_right(current, value)
            zeros += a
        elif direction == "L":
            current, b = count_left(current, value)
            zeros += b
    return zeros

if __name__ == "__main__":
    input_name = sys.argv[1]
    with open(input_name, "r") as f:
        input = f.read().splitlines()
    start = 50
    data = process_input(input)
    result = count_zeros(start, data)
    print(result)