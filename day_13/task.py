import ast


def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    pairs = data.split("\n\n")

    indexes = []
    for i, p in enumerate(pairs):
        pair1, pair2 = p.split("\n")
        p1 = ast.literal_eval(pair1)
        p2 = ast.literal_eval(pair2)
        res = compare_pair(p1, p2)
        if res:
            indexes.append(i + 1)

    counter = sum(indexes)
    return counter


def compare_pair(pair1, pair2):
    for i, p in enumerate(pair1):
        # Right side ran out of items
        if i >= len(pair2):
            return False
        p2 = pair2[i]
        if isinstance(p, list) or isinstance(p2, list):
            p1 = convert_to_list(p)
            p2 = convert_to_list(p2)
            res = compare_pair(p1, p2)
            if res is not None:
                return res
        else:
            if p < pair2[i]:
                return True
            elif p > pair2[i]:
                return False
            else:
                continue

    if len(pair1) < len(pair2):
        return True
    elif len(pair1) > len(pair2):
        return False
    else:
        return None


def convert_to_list(val):
    new_val = val
    if isinstance(val, int):
        new_val = [val]
    return new_val


def compare(p1, p2):
    res = compare_pair(p2, p1)
    if res == True:
        return 1
    elif res == False:
        return -1
    else:
        return 0


def task2(data):
    pairs = data.replace("\n\n", "\n")
    pairs = pairs.split("\n")
    pairs.append("[[2]]")
    pairs.append("[[6]]")

    converted_pairs = []
    for p in pairs:
        converted_pairs.append(ast.literal_eval(p))

    import functools
    converted_pairs.sort(key=functools.cmp_to_key(compare))
    res = (converted_pairs.index([[2]]) + 1) * (converted_pairs.index([[6]]) + 1)
    return res


data = read_file("input.txt")
print(task1(data))

print(task2(data))
