import collections
def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    matrix = convert_data(data)

    start_point = (-1, -1)
    end_point = (-1, -1)
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if col == "S":
                matrix[x][y] = "a"
                start_point = (x, y)
            if col == "E":
                matrix[x][y] = "z"
                end_point = (x, y)

    res = find_route(matrix, start_point, end_point)
    for x in res:
        for y in x:
            print(y, end="      ")
        print('\n')

    max_val = 0
    for x in res:
        for y in x:
            if y != 10000 and y > max_val:
                max_val = y

    res = max_val - 1
    return res


def generate_visits_matrix(matrix):
    visits = []
    for i in matrix:
        row = []
        for j in i:
            row.append(10000)
        visits.append(row)
    return visits


def convert_data(data):
    lines = data.split("\n")
    matrix = [list(x) for x in lines]
    return matrix


def get_val(matrix, x, y):
    return ord(matrix[x][y])


def find_route(matrix, start, end):
    queue = collections.deque([[start]])
    visits = generate_visits_matrix(matrix)
    visits[start[0]][start[1]] = 1
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        curr = get_val(matrix, x, y)

        if (x, y) == end:
            print(path)
            return visits

        adjacents = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
        for x2, y2 in adjacents:
            if 0 <= x2 < len(matrix) and 0 <= y2 < len(matrix[0]) and curr + 1 >= get_val(matrix, x2, y2):
                if visits[x2][y2] > visits[x][y] + 1:
                    visits[x2][y2] = visits[x][y] + 1
                    queue.append(path + [(x2, y2)])

def find_max(matrix):
    max_val = 0
    for x in matrix:
        for y in x:
            if y != 10000 and y > max_val:
                max_val = y

    return max_val


def task2(data):
    matrix = convert_data(data)

    end_point = (-1, -1)
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if col == "S":
                matrix[x][y] = "a"
            if col == "E":
                matrix[x][y] = "z"
                end_point = (x, y)

    start_points = []
    for x, row in enumerate(matrix):
        for y, col in enumerate(row):
            if col == "a":
                start_points.append((x, y))

    results = []
    for x in start_points:
        res = find_route(matrix, x, end_point)
        if res != None:
            max_val = find_max(res)
            results.append(max_val)

    res = min(results) - 2
    return res


data = read_file("input.txt")
print(task1(data))

print(task2(data))
