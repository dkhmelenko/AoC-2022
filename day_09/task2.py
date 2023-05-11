# NOT RESOLVED!

FIELD_SIZE = 3000

def read_file(name):
    f = open(name, "r")
    return f.read()


def task2(data):
    steps = data.split("\n")

    head_i = int(FIELD_SIZE/2)
    head_j = int(FIELD_SIZE/2)
    tail_i = int(FIELD_SIZE/2)
    tail_j = int(FIELD_SIZE/2)

    snake = []
    for i in range(10):
        snake.append([head_i, head_j])

    matrix = generate_playground()
    matrix[tail_i][tail_j] = 1

    for step in steps:
        direction, num = step.split(" ")
        num = int(num)
        if direction == "U":
            move_up(snake, num, matrix)
        elif direction == "D":
            move_down(snake, num, matrix)
        elif direction == "R":
            move_right(snake, num, matrix)
        elif direction == "L":
            move_left(snake, num, matrix)

        #print_matrix(step, matrix)
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


def move_up(snake, steps, matrix):
    for i in range(1, steps + 1):
        snake[0][0] -= 1
        for item in range(0, len(snake) - 1):
            new_head_i = snake[item][0]
            new_head_j = snake[item][1]
            new_tail_i = snake[item + 1][0]
            new_tail_j = snake[item + 1][1]
            if not is_tail_here(new_head_i, new_head_j, new_tail_i, new_tail_j):
                new_tail_i, new_tail_j = move_tail(new_head_i, new_head_j, new_tail_i, new_tail_j, matrix)
                snake[item + 1][0] = new_tail_i
                snake[item + 1][1] = new_tail_j
            else:
                break
        matrix[snake[9][0]][snake[9][1]] = 1


def move_down(snake, steps, matrix):
    for i in range(1, steps + 1):
        snake[0][0] += 1
        for item in range(0, len(snake) - 1):
            new_head_i = snake[item][0]
            new_head_j = snake[item][1]
            new_tail_i = snake[item + 1][0]
            new_tail_j = snake[item + 1][1]
            if not is_tail_here(new_head_i, new_head_j, new_tail_i, new_tail_j):
                new_tail_i, new_tail_j = move_tail(new_head_i, new_head_j, new_tail_i, new_tail_j, matrix)
                snake[item + 1][0] = new_tail_i
                snake[item + 1][1] = new_tail_j
            else:
                break
        matrix[snake[9][0]][snake[9][1]] = 1


def move_right(snake, steps, matrix):
    for i in range(1, steps + 1):
        snake[0][1] += 1
        for item in range(0, len(snake) - 1):
            new_head_i = snake[item][0]
            new_head_j = snake[item][1]
            new_tail_i = snake[item + 1][0]
            new_tail_j = snake[item + 1][1]
            if not is_tail_here(new_head_i, new_head_j, new_tail_i, new_tail_j):
                new_tail_i, new_tail_j = move_tail(new_head_i, new_head_j, new_tail_i, new_tail_j, matrix)
                snake[item + 1][0] = new_tail_i
                snake[item + 1][1] = new_tail_j
            else:
                break

        matrix[snake[9][0]][snake[9][1]] = 1


def move_left(snake, steps, matrix):
    for i in range(1, steps + 1):
        snake[0][1] -= 1
        for item in range(0, len(snake) - 1):
            new_head_i = snake[item][0]
            new_head_j = snake[item][1]
            new_tail_i = snake[item + 1][0]
            new_tail_j = snake[item + 1][1]
            if not is_tail_here(new_head_i, new_head_j, new_tail_i, new_tail_j):
                new_tail_i, new_tail_j = move_tail(new_head_i, new_head_j, new_tail_i, new_tail_j, matrix)
                snake[item + 1][0] = new_tail_i
                snake[item + 1][1] = new_tail_j
            else:
                break

        matrix[snake[9][0]][snake[9][1]] = 1



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
print(task2(data))
