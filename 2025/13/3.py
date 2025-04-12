import os, sys
import time

class Node:
    def __init__(self, identifier: str):
        self.id = identifier
        self.neighbours: dict["Node", int] = {}
    def add_neighbour(self, neighbour, cost):
        self.neighbours[neighbour] =  cost
    def get_neighbours(self):
        return self.neighbours.keys()
    def get_cost(self, neighbour):
        if neighbour not in self.neighbours:
            raise ValueError(f"Node {neighbour} is not a neighbour of {self.id}")
        return self.neighbours[neighbour]
    def __repr__(self):
        return self.id
    def __str__(self):
        return self.id
    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id
    def __lt__(self, other):
        return self.id < other.id
class Dfs:
    def __init__(self):
        self.max_cycle_weight = 0
    def find(self, nodes):
        for node in nodes.values():
            self._dfs(node, [], set())
        return self.max_cycle_weight
    def _dfs(self, node, path, visited):
        for neighbour in node.get_neighbours():
            weight = node.get_cost(neighbour)
            edge = (node, neighbour, weight)
            cycle_start_indices = [i for i, e in enumerate(path) if e[0] == neighbour]
            if cycle_start_indices:
                i = cycle_start_indices[0]
                cycle_weight = sum(e[2] for e in path[i:]) + weight
                self.max_cycle_weight = max(self.max_cycle_weight, cycle_weight)
            elif neighbour not in visited:
                new_path = path + [edge]
                new_visited = visited.copy()
                new_visited.add(node)
                self._dfs(neighbour, new_path, new_visited)

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    nodes: dict[str, Node] = {}
    for line in lines:
        a, _, b, _, l = line.split(" ")
        l = int(l)
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)
        nodes[a].add_neighbour(nodes[b], l)
    dfs = Dfs()
    result = dfs.find(nodes)
    
    print(result)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
