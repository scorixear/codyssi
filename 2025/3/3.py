import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    max_boxes = 0
    for i in range(0, len(lines)-1, 1):
        pile_a = lines[i].split(" ")
        pile_b = lines[i+1].split(" ")
        numbers = set()
        for box_range in pile_a:
            b_from = int(box_range.split("-")[0])
            b_to = int(box_range.split("-")[1])
            for j in range(b_from, b_to + 1):
                numbers.add(j)
        for box_range in pile_b:
            b_from = int(box_range.split("-")[0])
            b_to = int(box_range.split("-")[1])
            for j in range(b_from, b_to + 1):
                numbers.add(j)
        if len(numbers) > max_boxes:
            max_boxes = len(numbers)
    print(max_boxes)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
