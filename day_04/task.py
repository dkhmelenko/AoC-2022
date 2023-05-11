
def read_file(name):
    f = open(name, "r")
    return f.read()

def task1(data):
    items = data.split("\n")

    counter = 0
    for item in items:
        first, second = item.split(",")
        if is_range_in_range(first, second) or is_range_in_range(second, first):
            counter += 1

    return counter


def is_range_in_range(check, target):
    start_check, end_check = check.split("-")
    start_target, end_target = target.split("-")

    start_check = int(start_check)
    end_check = int(end_check)
    start_target = int(start_target)
    end_target = int(end_target)

    if start_check in range(start_target, end_target + 1) and \
            end_check in range(start_target, end_target + 1):
        return True
    return False


def task2(data):
    items = data.split("\n")

    counter = 0
    for item in items:
        first, second = item.split(",")
        if is_range_overlaps(first, second) or is_range_overlaps(second, first):
            counter += 1

    return counter

def is_range_overlaps(check, target):
    start_check, end_check = check.split("-")
    start_target, end_target = target.split("-")

    start_check = int(start_check)
    end_check = int(end_check)
    start_target = int(start_target)
    end_target = int(end_target)

    if start_check in range(start_target, end_target + 1) or \
            end_check in range(start_target, end_target + 1):
        return True
    return False


data = read_file("input.txt")
print(task1(data))

print(task2(data))
