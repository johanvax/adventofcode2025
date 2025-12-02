import sys

def find_invalid_ids(id_range):
    sum = 0
    for id in range(id_range[0], id_range[1] + 1):
        str_id = str(id)
        if len(str_id) % 2 != 0:
            continue

        mid = len(str_id) // 2
        left_half = str_id[:mid]
        right_half = str_id[mid:]
        if left_half == right_half:
            sum += id
    return sum

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        input = f.read().strip().split(',')
    
    result = 0
    for section in input:
        start, end = map(int, section.split('-'))
        result += find_invalid_ids((start, end))

    print(result)
    