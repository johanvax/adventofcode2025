import sys

def find_invalid_ids(id_range):
    sum = 0
    for id in range(id_range[0], id_range[1] + 1):
        str_id = str(id)
        n = len(str_id)

        for i in range(1, (n // 2) + 1):
            if n % i == 0:
                pattern = str_id[:i]
                is_repeated = True
                for j in range(i, n, i):
                    current_window = str_id[j:j+i]

                    if current_window != pattern:
                        is_repeated = False
                        break

                if is_repeated:
                    sum += id
                    break

        
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
    