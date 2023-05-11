
def read_file(name):
    f = open(name, "r")
    return f.read()

def task1(data):
    rounds = data.split("\n")

    rewards = {"X": 1, "Y": 2, "Z": 3}
    scores = {"AX": 3, "AY": 6, "AZ": 0, "BX": 0, "BY": 3, "BZ": 6, "CX": 6, "CY": 0, "CZ": 3}

    points = 0
    for round in rounds:
        opponent, you = round.split(" ")
        points += scores[opponent+you] + rewards[you]

    return points

def task2(data):
    rounds = data.split("\n")

    rewards = {"A": 1, "B": 2, "C": 3}
    scores = {"AX": 0, "AY": 3, "AZ": 6, "BX": 0, "BY": 3, "BZ": 6, "CX": 0, "CY": 3, "CZ": 6}
    combos = {"X": {"A": 3, "B": 1, "C": 2}, "Y": {"A": 1, "B": 2, "C": 3}, "Z": {"A": 2, "B": 3, "C": 1}}

    points = 0
    for round in rounds:
        opponent, you = round.split(" ")
        points += scores[opponent + you] + combos[you][opponent]

    return points

data = read_file("input.txt")
print(task1(data))

print(task2(data))
