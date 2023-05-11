
def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    stacks, moves = data.split("\n\n")

    stacks = stacks.split("\n")
    stacks = convert_stacks(stacks[:-1])

    for move in moves.split("\n"):
        quantity, source, target = [int(s) for s in move.split() if s.isdigit()]

        for step in range(0, quantity):
            item = stacks[source-1].pop(0)
            stacks[target-1].insert(0, item)

    result = [s[0] for s in stacks]
    result = "".join(result).replace("[", "").replace("]", "")
    return result


def convert_stacks(stacks):
    output_stacks = []
    stack_len = max(stacks, key=len)
    for item in range(0, len(stack_len), 4):
        index = 0
        output_stack = []
        for stack in stacks:
            element = stack[item:item+3]
            output_stack.append(element)
            index += 1

        output_stack = [s.strip() for s in output_stack if s.strip() != ""]
        output_stacks.append(output_stack)

    return output_stacks


def task2(data):
    stacks, moves = data.split("\n\n")

    stacks = stacks.split("\n")
    stacks = convert_stacks(stacks[:-1])

    for move in moves.split("\n"):
        quantity, source, target = [int(s) for s in move.split() if s.isdigit()]

        item = stacks[source-1][0:quantity]
        stacks[target-1] = item + stacks[target-1]
        for step in range(0, quantity):
            stacks[source - 1].pop(0)

    result = [s[0] for s in stacks]
    result = "".join(result).replace("[", "").replace("]", "")
    return result


data = read_file("input.txt")
print(task1(data))
print(task2(data))
