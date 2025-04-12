import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for line in lines:
        kept = len(line) // 10
        new_line = line[:kept] + str(len(line) - kept * 2) + line[-kept:]
        for char in new_line:
            if char.isdigit():
                total += int(char)
            else:
                total += ord(char) - ord("A") + 1
    print(total)
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
