import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    prev = -1
    for char in lines[0]:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            prev = ord(char) - ord("a") + 1
        elif ord(char) >= ord("A") and ord(char) <= ord("Z"):
            prev = ord(char) - ord("A") + 27
        elif prev != -1:
            prev = (prev * 2 - 5) % 52
            if prev < 1:
                prev += 52
        total += prev
    print(total)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
