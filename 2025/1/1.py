import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    start = int(lines[0], 10)
    offsets = [int(x) for x in lines[1:-1]]
    signs = [True if x == "+" else False for x in lines[-1]]
    for sign, offset in zip(signs, offsets):
        if sign:
            start += offset
        else:
            start -= offset
    print(start)
    
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
