
def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    collector = set()
    counter = 0
    for i in range(len(data)):
        for j in range(i, i + 4):
            char = data[j]
            if char not in collector:
                collector.add(char)
            else:
                collector.clear()
                break

        if len(collector) > 0:
            counter = i + 4
            break

    return counter


def task2(data):
    collector = set()
    counter = 0
    for i in range(len(data)):
        for j in range(i, i + 14):
            char = data[j]
            if char not in collector:
                collector.add(char)
            else:
                collector.clear()
                break

        if len(collector) > 0:
            counter = i + 14
            break

    return counter


data = read_file("input.txt")
print(task1(data))

print(task2(data))
