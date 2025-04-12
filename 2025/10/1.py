import os, sys
import time
import math

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid = [[int(c) for c in line.split(" ")] for line in lines]
    width = len(grid[0])
    height = len(grid)
    safe = math.inf
    for i in range(height):
        danger = sum(grid[i])
        if danger < safe:
            safe = danger
    for j in range(width):
        danger = 0
        for i in range(height):
            danger += grid[i][j]
        if danger < safe:
            safe = danger
    print(safe)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
