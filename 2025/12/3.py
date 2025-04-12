import os, sys
import time
from enum import StrEnum

MOD = 1073741824

class ActionType(StrEnum):
    ADD = "ADD",
    SUB = "SUB",
    MULTIPLY = "MULTIPLY",
    SHIFT = "SHIFT",
class ActionSubType(StrEnum):
    ROW = "ROW",
    COL = "COL",
    ALL = "ALL",
class Action:
    def __init__(self, line: str):
        parts = line.split(" ")
        if parts[0] != ActionType.SHIFT:
            self.type = ActionType(parts[0])
            self.amount = int(parts[1])
            self.sub_type = ActionSubType(parts[2])
            if self.sub_type != ActionSubType.ALL:
                self.index = int(parts[3]) - 1
        else:
            self.type = ActionType.SHIFT
            self.amount = int(parts[4])
            self.sub_type = ActionSubType(parts[1])
            self.index = int(parts[2]) - 1
    def perform(self, grid: list[list[int]]):
        if self.type != ActionType.SHIFT:
            perform_action = lambda x: x
            if self.type == ActionType.ADD:
                perform_action = lambda x: (x + self.amount) % MOD
            elif self.type == ActionType.SUB:
                perform_action = lambda x: (x - self.amount) % MOD
            elif self.type == ActionType.MULTIPLY:
                perform_action = lambda x: (x * self.amount) % MOD
            if self.sub_type == ActionSubType.ROW:
                for i in range(len(grid[self.index])):
                    grid[self.index][i] = perform_action(grid[self.index][i])
                    if grid[self.index][i] < 0:
                        grid[self.index][i] += MOD
            elif self.sub_type == ActionSubType.COL:
                for i in range(len(grid)):
                    grid[i][self.index] = perform_action(grid[i][self.index])
                    if grid[i][self.index] < 0:
                        grid[i][self.index] += MOD
            elif self.sub_type == ActionSubType.ALL:
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        grid[i][j] = perform_action(grid[i][j])
                        if grid[i][j] < 0:
                            grid[i][j] += MOD
        else:
            if self.sub_type == ActionSubType.ROW:
                amount = (-1*self.amount % len(grid[self.index]))
                if amount < 0:
                    amount += len(grid[self.index])
                grid[self.index] = grid[self.index][amount:] + grid[self.index][:amount]
            elif self.sub_type == ActionSubType.COL:
                current = (-1*self.amount % len(grid))
                if current < 0:
                    current += len(grid)
                new_col = []
                for i in range(len(grid)):
                    new_col.append(grid[current][self.index])
                    current = (current + 1) % len(grid)
                for i in range(len(grid)):
                    grid[i][self.index] = new_col[i]

class Control:
    def __init__(self):
        self.current = None
    def perform_control(self, control: str, grid: list[list[int]], instructions: list[Action]):
        if control == "TAKE":
            if len(instructions) == 0:
                return False
            self.current = instructions.pop(0)
        elif control == "CYCLE":
            instructions.append(self.current)
        elif control == "ACT":
            self.current.perform(grid)
        return True
              
                    

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid: list[list[int]] = []
    instructions: list[Action] = []
    control = Control()
    controls: list[str] = []
    mode = 0
    for line in lines:
        if mode == 0 and line == "":
            mode = 1
            continue
        if mode == 1 and line == "":
            mode = 2
            continue
        if mode == 0:
            grid.append([int(x) % MOD for x in line.split(" ")])
        elif mode == 1:
            instructions.append(Action(line))
        elif mode == 2:
            controls.append(line)
    current_control = 0
    while(control.perform_control(controls[current_control], grid, instructions)):
        current_control = (current_control + 1) % len(controls)
    total = 0
    for i in range(len(grid)):
        total = max(total, sum(grid[i]))
    for i in range(len(grid[0])):
        total = max(total, sum(grid[j][i] for j in range(len(grid))))
    print(total)

if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
