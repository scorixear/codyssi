import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    tracks = []
    swaps = []
    test = 0
    mode = 0
    for line in lines:
        if mode == 0 and line == "":
            mode = 1
            continue
        if mode == 1 and line == "":
            mode = 2
            continue
        if mode == 0:
            tracks.append(int(line))
        elif mode == 1:
            x = int(line.split('-')[0]) - 1
            y = int(line.split('-')[1]) - 1
            if x > y:
                x, y = y, x
            swaps.append((x, y))
        elif mode == 2:
            test = int(line) - 1
    for x, y in swaps:
        max_l = min(y - x, len(tracks) - y)
        for i in range(max_l):
            x_swap = x + i
            y_swap = y + i
            tracks[x_swap], tracks[y_swap] = tracks[y_swap], tracks[x_swap]
    print(tracks[test])

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
