import os, sys
import time

class Item():
    def __init__(self, name: str, quality: int, cost: int, mats: int):
        self.name = name
        self.quality = quality
        self.cost = cost
        self.mats = mats
    def __repr__(self):
        return f"{self.name} ({self.cost})"
    def __str__(self):
        return f"{self.name} ({self.cost})"
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
    dp = {}
    q, _, m = best_weight(items, 0, 0, 0, 0, set(), dp)
    print(q*m)

def best_weight(items: list[Item], total_cost: int, index: int, total_quality: int, total_mats: int, visited: set[Item], dp: dict[tuple[int, int, int]]):
    if (index, total_cost, total_quality) in dp:
        return dp[(index, total_cost, total_quality)]
    if total_cost > 30:
        return -float("inf"), {}, float("inf")
    if index == len(items) or total_cost == 30:
        return total_quality, total_mats
    item = items[index]
    q1, m1 = best_weight(items, total_cost + item.cost, index + 1, total_quality + item.quality, total_mats + item.mats, visited | {item}, dp)
    q2, m2 = best_weight(items, total_cost, index + 1, total_quality, total_mats, visited, dp)
    if q1 > q2:
        dp[(index, total_cost, total_quality)] = (q1, m1)
        return q1, m1
    elif q1 == q2:
        if m1 > m2:
            dp[(index, total_cost, total_quality)] = (q2, m2)
            return q2, m2
        else:
            dp[((index, total_cost, total_quality))] = (q1, m1)
            return q1, m1
    else:
        dp[(index, total_cost, total_quality)] = (q2, m2)
        return q2, m2
    

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
