
def read_file(name):
    f = open(name, "r")
    return f.read()

def task1(data):
    calories = data.split("\n\n")
    calories = [cal.split("\n") for cal in calories]
    calories = [[int(c) for c in cal] for cal in calories]
    calories_sum = [sum(cal) for cal in calories]
    return max(calories_sum)

def task2(data):
    calories = data.split("\n\n")
    calories = [cal.split("\n") for cal in calories]
    calories = [[int(c) for c in cal] for cal in calories]
    calories_sum = [sum(cal) for cal in calories]
    calories_sum.sort(reverse=True)
    return calories_sum[0] + calories_sum[1] + calories_sum[2]

data = read_file("input.txt")
print(task1(data))

print(task2(data))