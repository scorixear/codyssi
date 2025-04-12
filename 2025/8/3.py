import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    total = 0
    for line in lines:
        i = 0
        while i < len(line) - 1:
            left = line[i]
            right = line[i+1]
            if (left.isnumeric() and right.isalpha()) or (left.isalpha() and right.isnumeric()):
                line = line[:i] + line[i+2:]
                i = 0
            else:
                i += 1
        total += len(line)
            
    print(total)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
