
def read_file(name):
    f = open(name, "r")
    return f.read()

def task1(data):
    items = data.split("\n")

    scores = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
               "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
               "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    score = 0
    for item in items:
        middle = int(len(item) / 2)
        first = item[:middle]
        second = item[middle:]
        common_item = list(set(first)&set(second))[0]
        if common_item.isupper():
            score += scores[common_item.lower()] + 26
        else:
            score += scores[common_item.lower()]

    return score

def task2(data):
    items = data.split("\n")

    scores = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
               "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
               "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

    score = 0
    for index in range(0, len(items), 3):
        first = items[index]
        second = items[index+1]
        third = items[index+2]
        common_item = list(set(first)&set(second)&set(third))[0]
        if common_item.isupper():
            score += scores[common_item.lower()] + 26
        else:
            score += scores[common_item.lower()]

    return score

data = read_file("input.txt")
print(task1(data))

print(task2(data))
