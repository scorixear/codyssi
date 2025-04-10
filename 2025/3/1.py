import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for line in lines:
        box_ranges = line.split(" ")
        for box_range in box_ranges:
            b_from = int(box_range.split("-")[0])
            b_to = int(box_range.split("-")[1])
            total += (b_to - b_from + 1)
    print(total)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
