import sys, math

area = lambda x, y: (abs(x[0] - y[0]) + 1) * (abs(x[1] - y[1]) + 1)

def part_1(points):
    areas = []
    max_area = 0
    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                areas.append(area(points[i], points[j]))
                if areas[-1] > max_area:
                    max_area = areas[-1]

    print(max_area)


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        input = [tuple(map(int, line.split(","))) for line in f.read().splitlines()]

    part_1(input)