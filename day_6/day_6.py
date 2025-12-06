import sys

def part_1(problem):
    res = 0
    for col in range(len(problem[0])):
        numbers = []
        operation = problem[-1][col]
        assert operation == "*" or operation == "+"
        for row in range(len(problem) - 1):
            numbers.append(int(problem[row][col]))

        if operation == "+":
            res += sum(numbers)
        else:
            prod = numbers[0]
            for i in range(1, len(numbers)):
                prod *= numbers[i]
            res += prod

    print(res)

def part_2(problem):
    res = 0
    numbers = []
    operation = ""
    for col in reversed(range(len(problem[0]))):
        current_numbers = []
        for row in range(len(problem)):
            c = problem[row][col]
            if c == "+" or c == "*":
                operation = c
            else:
                current_numbers.append(c)
        n = "".join(current_numbers).strip()
        if n != "":
            numbers.append(int(n))
        
        if operation != "":
            if operation == "+":
                res += sum(numbers)
            else:
                prod = numbers[0]
                for i in range(1, len(numbers)):
                    prod *= numbers[i]
                res += prod
            numbers = []
            operation = ""
    
    print(res)


if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        input = f.readlines()
    
    problem = [line.strip().split() for line in input]
    problem2 = [[line[i] for i in range(len(line)) if line[i] != "\n"] for line in input]

    part_1(problem)
    part_2(problem2)