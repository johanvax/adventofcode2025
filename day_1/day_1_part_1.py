import sys

def process_input(input) -> list[tuple]:
    result = []
    for line in input:
        direction = line[0]
        value = int(line[1:])
        result.append((direction, value))
    return result

def count_right(current: int, input: int) -> int:
    for _ in range(input):
        if current + 1 > 99:
            current = 0
        else:
            current += 1
    return current

def count_left(current: int, input: int) -> int:
    for _ in range(input):
        if current - 1 < 0:
            current = 99
        else:
            current -= 1
    return current

def count_zeros(start, data):
    current = start
    zeros = 0
    for direction, value in data:
        if direction == "R":
            current = count_right(current, value)
        elif direction == "L":
            current = count_left(current, value)
        if current == 0:
            zeros += 1
    return zeros

if __name__ == "__main__":
    input_name = sys.argv[1]
    with open(input_name, "r") as f:
        input = f.read().splitlines()
    start = 50
    data = process_input(input)
    result = count_zeros(start, data)
    print(result)