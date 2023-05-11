import monkey
def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    monkeys_input = data.split("\n\n")
    monkeys = generate_monkeys(monkeys_input, True)

    for i in range(0, 20):
        for m in monkeys:
            monkeys[m].process_items(monkeys)

    res = [monkeys[x].processed_items for x in monkeys]
    res.sort(reverse=True)
    res = res[0] * res[1]
    return res


def generate_monkey(input_data, divide_by_three):
    lines = input_data.split("\n")
    monkey_number = get_numbers(lines[0].replace(":", ""))[0]
    items = get_numbers(lines[1].replace(",", " "))
    _, operation = lines[2].split("Operation: ")
    test = lines[3] + lines[4] + lines[5]

    m = monkey.Monkey(monkey_number, items, operation, test, divide_by_three)
    return m


def generate_monkeys(data_input, divide_by_three):
    monkeys = {}
    for m in data_input:
        mon = generate_monkey(m, divide_by_three)
        monkeys[mon.number] = mon
    return monkeys


def get_numbers(input_data):
    return [int(s) for s in input_data.split() if s.isdigit()]


def task2(data):
    monkeys_input = data.split("\n\n")
    monkeys = generate_monkeys(monkeys_input, False)

    dividers = [monkeys[x].divider for x in monkeys]
    import math
    supermodulo = math.prod(dividers)
    for x in monkeys:
        monkeys[x].supermodulo = supermodulo

    for i in range(0, 10000):
        for m in monkeys:
            monkeys[m].process_items(monkeys)

    res = [monkeys[x].processed_items for x in monkeys]
    res.sort(reverse=True)
    res = res[0] * res[1]
    return res


data = read_file("input.txt")
print(task1(data))

print(task2(data))
