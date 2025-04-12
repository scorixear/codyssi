import os, sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from algorithms import dijkstra

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
    algo: dijkstra.Dijkstra[Node, int] = dijkstra.Dijkstra(lambda node: node.get_neighbours(), lambda node_a, node_b: node_a.get_cost(node_b), 0)
    
    start = nodes["STT"]
    algo.find_path(start, Node("END"))
    all_costs = [algo.get_cost(node) for node in nodes.values()]
    all_costs.sort()
    product = 1
    for i in range(len(all_costs) - 3, len(all_costs)):
        product *= all_costs[i]
    print(product)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
