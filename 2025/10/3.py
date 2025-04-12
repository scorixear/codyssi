import os, sys
import time
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from algorithms import dijkstra

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [[int(c) for c in line.split(" ")] for line in lines]
    start = (0, 0)
    end = (len(grid[0]) - 1, len(grid) - 1)
    algo: dijkstra.Dijkstra[int, tuple[int, int]] = dijkstra.Dijkstra(
        lambda node: neighbour(node[0], node[1], grid),
        lambda _, nodeb: cost(nodeb[0], nodeb[1], grid), 0)
    algo.find_path(start, end)
    total = algo.get_cost(end) + grid[start[0]][start[1]]
    print(total)
def neighbour(x, y, grid):
    for dx in [0, 1]:
        for dy in [0, 1]:
            if dx == dy:
                continue
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
                yield (x + dx, y + dy)
def cost(x, y, grid):
    return grid[x][y] if x < len(grid) and y < len(grid[0]) else math.inf

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
