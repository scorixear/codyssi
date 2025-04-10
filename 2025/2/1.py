import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    num_a = int(lines[0].split(' ')[-1])
    func_a = lambda x: x + num_a
    num_b = int(lines[1].split(' ')[-1])
    func_b = lambda x: x * num_b
    num_c = int(lines[2].split(' ')[-1])
    func_c = lambda x: x ** num_c
    
    qualities = [int(x) for x in lines[4:]]
    qualities.sort()
    median_quality = qualities[len(qualities)//2]
    result = func_a(func_b(func_c(median_quality)))
    print(result)
    
if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
