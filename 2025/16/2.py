import os, sys
import time

class Face:
    def __init__(self, grid_size, idx: int):
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        self.idx = idx
        self.absorption = 0
    def add_face(self, value):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] += value
                self.grid[i][j] = self.grid[i][j] % 100
        self.absorption += len(self.grid) * len(self.grid[0]) * value
    def add_row(self, row, value):
        for j in range(len(self.grid[row])):
            self.grid[row][j] += value
            self.grid[row][j] = self.grid[row][j] % 100
        self.absorption += len(self.grid[row]) * value
    def add_col(self, col, value):
        for i in range(len(self.grid)):
            self.grid[i][col] += value
            self.grid[i][col] = self.grid[i][col] % 100
        self.absorption += len(self.grid) * value
    def find_dominant(self):
        max_row = 0
        for i in range(len(self.grid)):
            row_sum = sum(self.grid[i]) + len(self.grid[i])
            max_row = max(max_row, row_sum)
        max_col = 0
        for j in range(len(self.grid[0])):
            col_sum = sum(self.grid[i][j] for i in range(len(self.grid))) + len(self.grid)
            max_col = max(max_col, col_sum)
        return max(max_row, max_col)
    def rotate_left(self):
        size = len(self.grid)
        new_grid = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                new_grid[size - 1 - j][i] = self.grid[i][j]
        self.grid = new_grid
    def rotate_right(self):
        size = len(self.grid)
        new_grid = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                new_grid[j][size - 1 - i] = self.grid[i][j]
        self.grid = new_grid
    def __repr__(self):
        return f"Face({self.idx}) [{self.absorption}]"
    def get_row_strings(self):
        result = []
        for row in self.grid:
            row_str = ""
            for val in row:
                if len(str(val)) == 1:
                    row_str += f"{val}  "
                else:
                    row_str += f"{val} "
            result.append(row_str.strip())

        return result

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
    #print_faces(U, C, R, B, L, D, grid_size)
    twists = [c for c in lines[-1]]
    index = 0
    for line in lines:
        if line == "":
            break
        if line.startswith("FACE"):
            v = int(line.split(" ")[-1])
            C.add_face(v)
        elif line.startswith("ROW"):
            _, r, _, _, v = line.split(" ")
            r = int(r) - 1
            v = int(v)
            C.add_row(r, v)
        elif line.startswith("COL"):
            _, c, _, _, v = line.split(" ")
            c = int(c) - 1
            v = int(v)
            C.add_col(c, v)
        #print_faces(U, C, R, B, L, D, grid_size)
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
    dominants = [U.find_dominant(), C.find_dominant(), R.find_dominant(), B.find_dominant(), L.find_dominant(), D.find_dominant()]
    result = 1
    for dominant in dominants:
        result *= dominant
    print(result)


def rotate_left(U, C, R, B, L, D):
    U.rotate_left()
    D.rotate_right()
    return (U, L, C, R, B, D)
def rotate_right(U, C, R, B, L, D):
    U.rotate_right()
    D.rotate_left()
    return (U, R, B, L, C, D)
def rotate_up(U, C, R, B, L, D):
    L.rotate_left()
    R.rotate_right()
    return (B, U, R, D, L, C)
def rotate_down(U, C, R, B, L, D):
    L.rotate_right()
    R.rotate_left()
    return (C, D, R, U, L, B)
def print_faces(U, C, R, B, L, D, grid_size):
    faces = {}
    faces[U.idx] = U.get_row_strings()
    faces[C.idx] = C.get_row_strings()
    faces[R.idx] = R.get_row_strings()
    faces[B.idx] = B.get_row_strings()
    faces[L.idx] = L.get_row_strings()
    faces[D.idx] = D.get_row_strings()

    value_space = "  "
    row_space = value_space * (grid_size) + " "
    for i in range(grid_size):
        print(row_space + value_space + faces[1][i])
    for i in range(grid_size):
        print(faces[5][i] + value_space + faces[2][i] + value_space + faces[6][i])
    for i in range(grid_size):
        print(row_space + value_space + faces[3][i])
    for i in range(grid_size):
        print(row_space + value_space + faces[4][i])



if __name__ == "__main__":
    before = time.perf_counter()
    main()
    print(f"Time: {time.perf_counter() - before:.6f}s")
