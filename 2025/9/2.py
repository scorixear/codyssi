import os, sys
import time

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    balances = dict()
    mode = 0
    for line in lines:
        if mode == 0 and line == "":
            mode = 1
            continue
        if mode == 0:
            name, _, balance = line.split(" ")
            balances[name] = int(balance)
        elif mode == 1:
            _, source, _, destination, _, amount = line.split(" ")
            amount = int(amount)
            if source not in balances:
                balances[source] = 0
            if destination not in balances:
                balances[destination] = 0
            if amount > balances[source]:
                amount = balances[source]
            balances[source] -= amount
            balances[destination] += amount
    balance_values = list(balances.values())
    balance_values.sort()
    print(sum(balance_values[-3:]))
            

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
