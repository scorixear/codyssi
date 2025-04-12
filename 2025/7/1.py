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
            swaps.append((int(line.split('-')[0]) - 1, int(line.split('-')[1]) - 1))
        elif mode == 2:
            test = int(line) - 1
    for x, y in swaps:
        tracks[x], tracks[y] = tracks[y], tracks[x]
    print(tracks[test])

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
