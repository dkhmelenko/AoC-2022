import ast
MATRIX_SIZE = 2000
SAND_SOURCE = [0, 500]


def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    walls = data.split("\n")
    walls_parsed = []

    for w in walls:
        coordinates = w.split(" -> ")
        wall = [ast.literal_eval(x) for x in coordinates]
        walls_parsed.append(wall)

    matrix = init_matrix()
    build_walls(matrix, walls_parsed)

    simulate(matrix)

    counter = 0
    for x in matrix:
        counter += x.count("o")

    return counter - 1


def simulate(matrix):
    sand_flows = True

    while sand_flows:
        pos = SAND_SOURCE
        while True:
            x, y = pos
            if pos == SAND_SOURCE and matrix[x][y] == "o":
                sand_flows = False
                break

            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix):
                sand_flows = False
                break
            if matrix[x][y] == ".":
                if x > 0:
                    matrix[x - 1][y] = "."
                matrix[x][y] = "o"
                pos = [x + 1, y]
                continue
            else:
                if matrix[x][y - 1] == ".":
                    matrix[x - 1][y] = "."
                    matrix[x][y - 1] = "o"
                    pos = [x + 1, y - 1]
                elif matrix[x][y + 1] == ".":
                    matrix[x - 1][y] = "."
                    matrix[x][y + 1] = "o"
                    pos = [x + 1, y + 1]
                else:
                    break


def build_walls(matrix, coordinates):
    for coord in coordinates:
        for i in range(len(coord) - 1):
            start = coord[i]
            end = coord[i + 1]

            if abs(start[0] - end[0]) == 0:
                start_x = min(start[1], end[1])
                end_x = max(start[1], end[1]) + 1
                for x in range(start_x, end_x):
                    matrix[x][start[0]] = "#"
            elif abs(start[1] - end[1]) == 0:
                start_y = min(start[0], end[0])
                end_y = max(start[0], end[0]) + 1
                for x in range(start_y, end_y):
                    matrix[start[1]][x] = "#"


def print_matrix(matrix):
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            print(matrix[i][j], end="")
        print("\n")


def init_matrix():
    matrix = []
    for i in range(MATRIX_SIZE):
        row = []
        for j in range(MATRIX_SIZE):
            row.append(".")
        matrix.append(row)
    return matrix


def add_bottom(matrix, bottom_val):
    for x in range(len(matrix)):
        matrix[bottom_val + 2][x] = "#"


def find_floor(walls_parsed):
    y_coordinates = sum([[y[1] for y in x] for x in walls_parsed], [])
    return max(y_coordinates)


def task2(data):
    walls = data.split("\n")
    walls_parsed = []

    for w in walls:
        coordinates = w.split(" -> ")
        wall = [ast.literal_eval(x) for x in coordinates]
        walls_parsed.append(wall)

    matrix = init_matrix()
    build_walls(matrix, walls_parsed)

    floor = find_floor(walls_parsed)

    add_bottom(matrix, floor)
    simulate(matrix)

    counter = 0
    for x in matrix:
        counter += x.count("o")

    return counter


data = read_file("input.txt")
print(task1(data))

print(task2(data))
