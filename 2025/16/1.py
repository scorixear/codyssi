import os, sys
import time

class Face:
    def __init__(self, grid_size, idx: int):
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.idx = idx
        self.absorption = 0
    def sub_face(self, value):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] -= value
                self.grid[i][j] = self.grid[i][j] % 100
                if self.grid[i][j] < 0:
                    self.grid[i][j] += 100
        self.absorption += len(self.grid) * len(self.grid[0]) * value
    def sub_row(self, row, value):
        for j in range(len(self.grid[row])):
            self.grid[row][j] -= value
            self.grid[row][j] = self.grid[row][j] % 100
            if self.grid[row][j] < 0:
                self.grid[row][j] += 100
        self.absorption += len(self.grid[row]) * value
    def sub_col(self, col, value):
        for i in range(len(self.grid)):
            self.grid[i][col] -= value
            self.grid[i][col] = self.grid[i][col] % 100
            if self.grid[i][col] < 0:
                self.grid[i][col] += 100
        self.absorption += len(self.grid) * value
    def __repr__(self):
        return f"Face({self.idx}) [{self.absorption}]"
    def __str__(self):
        return f"Face {self.idx} [{self.absorption}]"

def main():
    with open(os.path.join(sys.path[0],"input.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
        lines = text.split("\n")
    grid_size = 80
    U = Face(grid_size, 4)
    C = Face(grid_size, 1)
    R = Face(grid_size, 6)
    B = Face(grid_size, 3)
    L = Face(grid_size, 5)
    D = Face(grid_size, 2)
    twists = [c for c in lines[-1]]
    index = 0
    for line in lines:
        if line == "":
            break
        if line.startswith("FACE"):
            v = int(line.split(" ")[-1])
            C.sub_face(v)
        elif line.startswith("ROW"):
            _, r, _, _, v = line.split(" ")
            r = int(r) - 1
            v = int(v)
            C.sub_row(r, v)
        elif line.startswith("COL"):
            _, c, _, _, v = line.split(" ")
            c = int(c) - 1
            v = int(v)
            C.sub_col(c, v)
        if index >= len(twists):
            break
        if twists[index] == "L":
            U, C, R, B, L, D = rotate_left(U, C, R, B, L, D)
        elif twists[index] == "R":
            U, C, R, B, L, D = rotate_right(U, C, R, B, L, D)
        elif twists[index] == "U":
            U, C, R, B, L, D = rotate_up(U, C, R, B, L, D)
        elif twists[index] == "D":
            U, C, R, B, L, D = rotate_down(U, C, R, B, L, D)
        index += 1
    absorptions = [U.absorption, C.absorption, R.absorption, B.absorption, L.absorption, D.absorption]
    absorptions.sort(reverse=True)
    print(absorptions[0] * absorptions[1])


def rotate_left(U, C, R, B, L, D):
    return (U, L, C, R, B, D)
def rotate_right(U, C, R, B, L, D):
    return (U, R, B, L, C, D)
def rotate_up(U, C, R, B, L, D):
    return (B, U, R, D, L, C)
def rotate_down(U, C, R, B, L, D):
    return (C, D, R, U, L, B)


if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
