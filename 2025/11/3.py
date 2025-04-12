import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    all_bases: dict[str, int] = dict()
    for i in range(10):
        all_bases[str(i)] = i
    for i in range(26):
        all_bases[chr(ord("A") + i)] = i + 10
    for i in range(26):
        all_bases[chr(ord("a") + i)] = i + 36
    total = 0
    for line in lines:
        number, base = line.split(" ")
        base = int(base)
        counter = len(number) - 1
        num = 0
        for char in number:
            digit = all_bases[char]
            num += digit * (base ** counter)
            counter -= 1
        total += num
    current_base = 2
    while True:
        if current_base ** 4 > total:
            break
        current_base += 1
    print(current_base)
        

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
