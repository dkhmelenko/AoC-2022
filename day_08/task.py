
def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    matrix = convert_data(data)

    counter = 0
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            curr = matrix[i][j]
            visible = is_visible_up(i - 1, j, matrix, curr) or is_visible_down(i + 1, j, matrix, curr) or\
                      is_visible_left(i, j-1, matrix, curr) or is_visible_right(i, j + 1, matrix, curr)
            if visible:
                counter += 1

    counter += len(matrix) * 2 + len(matrix[0]) * 2 - 4
    return counter


def task2(data):
    matrix = convert_data(data)

    max_score = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            curr = matrix[i][j]
            up = score_up(i - 1, j, matrix, curr)
            down = score_down(i + 1, j, matrix, curr)
            left = score_left(i, j - 1, matrix, curr)
            right = score_right(i, j + 1, matrix, curr)
            score = up * down * left * right
            if score > max_score:
                max_score = score

    return max_score


def score_up(i, j, matrix, curr):
    if i < 0:
        return 0
    visible = curr > matrix[i][j]
    if visible:
        return score_up(i - 1, j, matrix, curr) + 1
    else:
        return 1


def score_down(i, j, matrix, curr):
    if i >= len(matrix):
        return 0
    visible = curr > matrix[i][j]
    if visible:
        return score_down(i + 1, j, matrix, curr) + 1
    else:
        return 1


def score_left(i, j, matrix, curr):
    if j < 0:
        return 0
    visible = curr > matrix[i][j]
    if visible:
        return score_left(i, j - 1, matrix, curr) + 1
    else:
        return 1


def score_right(i, j, matrix, curr):
    if j >= len(matrix[0]):
        return 0
    visible = curr > matrix[i][j]
    if visible:
        return score_right(i, j + 1, matrix, curr) + 1
    else:
        return 1


def is_visible_up(i, j, matrix, curr):
    if i < 0:
        return True
    visible = curr > matrix[i][j]
    if visible:
        return is_visible_up(i - 1, j, matrix, curr)
    else:
        return False


def is_visible_down(i, j, matrix, curr):
    if i >= len(matrix):
        return True
    visible = curr > matrix[i][j]
    if visible:
        return is_visible_down(i + 1, j, matrix, curr)
    else:
        return False


def is_visible_left(i, j, matrix, curr):
    if j < 0:
        return True
    visible = curr > matrix[i][j]
    if visible:
        return is_visible_left(i, j - 1, matrix, curr)
    else:
        return False


def is_visible_right(i, j, matrix, curr):
    if j >= len(matrix[0]):
        return True
    visible = curr > matrix[i][j]
    if visible:
        return is_visible_right(i, j + 1, matrix, curr)
    else:
        return False


def convert_data(data):
    rows = data.split("\n")
    matrix = [[int(c) for c in r] for r in rows]
    return matrix


data = read_file("input.txt")
print(task1(data))

print(task2(data))
