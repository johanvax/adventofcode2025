import sys

def part_1(input):
    sum = 0
    for line in input:
        largest_idx = 0
        for i in range(len(line) - 1):
            if line[i] > line[largest_idx]:
                largest_idx = i

        second_largest_idx = largest_idx + 1
        for i in range(second_largest_idx, len(line)):
            if line[i] > line[second_largest_idx]:
                second_largest_idx = i

        sum += int(line[largest_idx] + line[second_largest_idx])
    
    return sum

def part_2(input):
    sum = 0
    for line in input:
        idxs = []
        for x in reversed(range(12)):
            largest_idx = 0 if len(idxs) == 0 else idxs[-1] + 1
            for i in range(largest_idx, len(line) - x):
                if line[i] > line[largest_idx]:
                    largest_idx = i
            idxs.append(largest_idx)

        sum += int("".join([line[i] for i in idxs]))

    return sum

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        input = f.read().strip().split("\n")

    result = part_2(input)
    print(result)
    