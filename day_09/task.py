FIELD_SIZE = 1000

def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    steps = data.split("\n")

    head_i = int(FIELD_SIZE/2)
    head_j = int(FIELD_SIZE/2)
    tail_i = int(FIELD_SIZE/2)
    tail_j = int(FIELD_SIZE/2)
    matrix = generate_playground()
    matrix[tail_i][tail_j] = 1

    for step in steps:
        direction, num = step.split(" ")
        num = int(num)
        if direction == "U":
            head_i, head_j, tail_i, tail_j = move_up(head_i, head_j, tail_i, tail_j, num, matrix)
        elif direction == "D":
            head_i, head_j, tail_i, tail_j = move_down(head_i, head_j, tail_i, tail_j, num, matrix)
        elif direction == "R":
            head_i, head_j, tail_i, tail_j = move_right(head_i, head_j, tail_i, tail_j, num, matrix)
        elif direction == "L":
            head_i, head_j, tail_i, tail_j = move_left(head_i, head_j, tail_i, tail_j, num, matrix)

    visits = sum([sum(i) for i in matrix])
    return visits


def print_matrix(step, matrix):
    print(step)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="")
        print("\n")
    print("\n")
    print("\n")


def move_up(head_i, head_j, tail_i, tail_j, steps, matrix):
    new_head_i = head_i
    new_head_j = head_j
    new_tail_i = tail_i
    new_tail_j = tail_j
    for i in range(1, steps + 1):
        new_head_i = new_head_i - 1
        if not is_tail_here(new_head_i, new_head_j, new_tail_i, new_tail_j):
            new_tail_i, new_tail_j = move_tail(new_head_i, new_head_j, new_tail_i, new_tail_j, matrix)

    return new_head_i, new_head_j, new_tail_i, new_tail_j


def move_down(head_i, head_j, tail_i, tail_j, steps, matrix):
    new_head_i = head_i
    new_head_j = head_j
    new_tail_i = tail_i
    new_tail_j = tail_j
    for i in range(1, steps + 1):
        new_head_i = new_head_i + 1
        if not is_tail_here(new_head_i, new_head_j, new_tail_i, new_tail_j):
            new_tail_i, new_tail_j = move_tail(new_head_i, new_head_j, new_tail_i, new_tail_j, matrix)

    return new_head_i, new_head_j, new_tail_i, new_tail_j


def move_right(head_i, head_j, tail_i, tail_j, steps, matrix):
    new_head_i = head_i
    new_head_j = head_j
    new_tail_i = tail_i
    new_tail_j = tail_j
    for i in range(1, steps + 1):
        new_head_j = new_head_j + 1
        if not is_tail_here(new_head_i, new_head_j, new_tail_i, new_tail_j):
            new_tail_i, new_tail_j = move_tail(new_head_i, new_head_j, new_tail_i, new_tail_j, matrix)

    return new_head_i, new_head_j, new_tail_i, new_tail_j


def move_left(head_i, head_j, tail_i, tail_j, steps, matrix):
    new_head_i = head_i
    new_head_j = head_j
    new_tail_i = tail_i
    new_tail_j = tail_j
    for i in range(1, steps + 1):
        new_head_j = new_head_j - 1
        if not is_tail_here(new_head_i, new_head_j, new_tail_i, new_tail_j):
            new_tail_i, new_tail_j = move_tail(new_head_i, new_head_j, new_tail_i, new_tail_j, matrix)
    return new_head_i, new_head_j, new_tail_i, new_tail_j


def is_tail_here(head_i, head_j, tail_i, tail_j):
    i_close = head_i == tail_i or head_i+1 == tail_i or head_i-1 == tail_i
    j_close = head_j == tail_j or head_j+1 == tail_j or head_j-1 == tail_j
    return i_close and j_close


def move_tail(head_i, head_j, tail_i, tail_j, matrix):
    diff_i = head_i - tail_i
    diff_j = head_j - tail_j

    if (abs(diff_i) == 2 and abs(diff_j) == 1) or (abs(diff_i) == 1 and abs(diff_j) == 2):
        if diff_i > 0 and diff_j > 0:
            tail_i += 1
            tail_j += 1
        elif diff_i > 0 and diff_j < 0:
            tail_i += 1
            tail_j -= 1
        elif diff_i < 0 and diff_j > 0:
            tail_i -= 1
            tail_j += 1
        elif diff_i < 0 and diff_j < 0:
            tail_i -= 1
            tail_j -= 1
    elif abs(diff_i) == 2:
        if diff_i > 0:
            tail_i += 1
        else:
            tail_i -= 1
    elif abs(diff_j) == 2:
        if diff_j > 0:
            tail_j += 1
        else:
            tail_j -= 1

    matrix[tail_i][tail_j] = 1
    return tail_i, tail_j


def generate_playground():
    matrix = []
    for i in range(0, FIELD_SIZE):
        row = []
        for j in range(0, FIELD_SIZE):
            row.append(0)
        matrix.append(row)
    return matrix


data = read_file("input.txt")
print(task1(data))
