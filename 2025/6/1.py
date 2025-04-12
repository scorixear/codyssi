import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for char in lines[0]:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            total += 1
        elif ord(char) >= ord("A") and ord(char) <= ord("Z"):
            total += 1
    print(total)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
