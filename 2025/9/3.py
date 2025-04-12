import os, sys
import time

class User:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance
        self.depts: list[tuple[str, int]] = list()
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return self.name == other.name
    def __str__(self):
        return f"{self.name} {self.balance} {self.depts}"
    def __repr__(self):
        return f"{self.name} {self.balance} {self.depts}"
    def receive(self, amount: int, users: dict[str, "User"]):
        while amount > 0 and len(self.depts) > 0:
            dest, dept = self.depts[0]
            if amount > dept:
                amount -= dept
                self.depts.pop(0)
                users[dest].receive(dept, users)
            elif amount == dept:
                self.depts.pop(0)
                users[dest].receive(dept, users)
                return
            else:
                self.depts[0] = (dest, dept - amount)
                users[dest].receive(amount, users)
                return
        self.balance += amount
        

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    users: dict[str, User] = dict()
    mode = 0
    for line in lines:
        if mode == 0 and line == "":
            mode = 1
            continue
        if mode == 0:
            name, _, balance = line.split(" ")
            users[name] = User(name, int(balance))
        elif mode == 1:
            _, source, _, destination, _, amount = line.split(" ")
            amount = int(amount)
            if source not in users:
                users[source] = User(source, 0)
            if destination not in users:
                users[destination] = User(destination, 0)
            if amount > users[source].balance:
                users[source].depts.append((destination, amount - users[source].balance))
                amount = users[source].balance
            users[source].balance -= amount
            users[destination].receive(amount, users)
    balance_values = [user.balance if len(user.depts) == 0 else 0 for user in users.values()]
    balance_values.sort()
    print(sum(balance_values[-3:]))

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
