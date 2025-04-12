import os, sys
import time
import math

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    closest = math.inf
    islands = []
    for line in lines:
        parts = line.split(",")
        x = int(parts[0][1:])
        y = int(parts[1][1:-1])
        islands.append((x, y))
    closest_island = (math.inf, math.inf)
    for x, y in islands:
        dist = manhatten(x, y, 0, 0)

        if dist < closest:
            closest_island = (x, y)
            closest = dist
        elif dist == closest:
            if x < closest_island[0]:
                closest_island = (x, y)
            elif x == closest_island[0] and y < closest_island[1]:
                closest_island = (x, y)
    current_position = closest_island
    total = closest
    islands.remove(current_position)
    while len(islands) > 0:
        dist, new_pos = find_shortest(current_position[0], current_position[1], islands)
        total += dist
        current_position = new_pos
    print(total)

def manhatten(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
def find_shortest(x, y, islands: list):
    closest = math.inf
    closest_island = (math.inf, math.inf)
    for (x1, y1) in islands:
        dist = manhatten(x, y, x1, y1)
        if dist < closest:
            closest = dist
            closest_island = (x1, y1)
        elif dist == closest:
            if x1 < closest_island[0]:
                closest_island = (x1, y1)
            elif x1 == closest_island[0] and y1 < closest_island[1]:
                closest_island = (x1, y1)
    islands.remove(closest_island)
    return closest, closest_island
    
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
