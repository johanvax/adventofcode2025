import sys
import math

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def part_1(boxes):
    all_possible_connections = []
    n = len(boxes)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.dist(boxes[i], boxes[j])
            all_possible_connections.append((dist, i, j))

    all_possible_connections.sort(key=lambda x: x[0])
    
    top_connections = all_possible_connections[:1000]

    uf = UnionFind(n)
    
    for _, box1_idx, box2_idx in top_connections:
        uf.union(box1_idx, box2_idx)

    circuit_sizes = {}
    for i in range(n):
        root = uf.find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1
    
    sorted_sizes = sorted(circuit_sizes.values(), reverse=True)

    if len(sorted_sizes) >= 3:
        result = sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]
    else:
        result = 1
        for s in sorted_sizes:
            result *= s
            
    print(result)

if __name__ == "__main__":
    input_file = sys.argv[1]
        
    with open(input_file, "r") as f:
        boxes = [[int(n) for n in line.split(",")] for line in f.read().splitlines() if line.strip()]

    part_1(boxes)