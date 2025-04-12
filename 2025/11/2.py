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
    all_bases["!"] = 62
    all_bases["@"] = 63
    all_bases["#"] = 64
    all_bases["$"] = 65
    all_bases["%"] = 66
    all_bases["^"] = 67
    reversed_bases = dict()
    for key, value in all_bases.items():
        reversed_bases[value] = key
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
    current = len(str(total))
    target_base = len(all_bases)
    result = ""
    while current >= 0:
        exp = target_base ** current
        div = total // exp
        if div > 0:
            result += reversed_bases[div]
            total = total % exp
        elif result != "":
            result += "0"
        current -= 1
        if total == 0:
            break
    print(result)
        

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
