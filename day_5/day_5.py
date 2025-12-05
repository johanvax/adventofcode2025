import sys

def part_1(ranges, ids):
    count = 0
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                count += 1
                break
    return count

def part_2(ranges):
    merged_ranges = []
    for start, end in sorted(ranges):
        if not merged_ranges or merged_ranges[-1][1] < start - 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    total_covered = 0
    for start, end in merged_ranges:
        total_covered += end - start + 1

    return total_covered

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    ranges = []
    ids = []

    add_ranges = True
    for line in lines:
        line = line.strip()

        if add_ranges:
            if line == "":
                add_ranges = False
                continue
            start, end = line.split("-")
            ranges.append((int(start), int(end)))
        else:
            ids.append(int(line))

    result = part_2(ranges)
    print(result)