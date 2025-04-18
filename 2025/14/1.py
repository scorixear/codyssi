import os, sys
import time

class Item():
    def __init__(self, name: str, quality: int, cost: int, mats: int):
        self.name = name
        self.quality = quality
        self.cost = cost
        self.mats = mats
    def __repr__(self):
        return f"{self.name} ({self.quality})"
    def __str__(self):
        return f"{self.name} ({self.quality})"
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        if self.quality == other.quality:
            return self.cost == other.cost
        return self.quality == other.quality
    def __lt__(self, other):
        if self.quality == other.quality:
            return self.cost < other.cost
        return self.quality < other.quality
    def __gt__(self, other):
        if self.quality == other.quality:
            return self.cost > other.cost
        return self.quality > other.quality
    

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    items = []
    for line in lines:
        _, name, _, _, _, quality, _, _, cost, _, _, _, mats = line.split(" ")
        quality = int(quality[:-1])
        cost = int(cost[:-1])
        mats = int(mats)
        items.append(Item(name, quality, cost, mats))
    items.sort(reverse=True)
    total = sum([i.mats for i in items[:5]])
    print(f"Total: {total}")
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
