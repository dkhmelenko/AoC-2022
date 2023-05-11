
def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    commands = data.split("\n")

    res1 = run_cycles(commands, 20) * 20
    res2 = run_cycles(commands, 60) * 60
    res3 = run_cycles(commands, 100) * 100
    res4 = run_cycles(commands, 140) * 140
    res5 = run_cycles(commands, 180) * 180
    res6 = run_cycles(commands, 220) * 220

    result = res1 + res2 + res3 + res4 + res5 + res6
    return result


def run_cycles(commands, cycles):
    curr_value = 1
    curr_cycle = 0
    for command in commands:
        if command == "noop":
            curr_cycle += 1
            if curr_cycle == cycles:
                break
        else:
            com, val = command.split(" ")
            curr_cycle += 1
            if curr_cycle == cycles:
                break
            curr_cycle += 1
            if curr_cycle == cycles:
                break
            curr_value += int(val)

    return curr_value


def task2(data):
    commands = data.split("\n")

    output, command_index, curr_value, mid = calculate_drawing(commands, 0, 40, 0, 1, False)
    print("".join(output))
    output, command_index, curr_value, mid = calculate_drawing(commands, 0, 40, command_index, curr_value, mid)
    print("".join(output))
    output, command_index, curr_value, mid = calculate_drawing(commands, 0, 40, command_index, curr_value, mid)
    print("".join(output))
    output, command_index, curr_value, mid = calculate_drawing(commands, 0, 40, command_index, curr_value, mid)
    print("".join(output))
    output, command_index, curr_value, mid = calculate_drawing(commands, 0, 40, command_index, curr_value, mid)
    print("".join(output))
    output, command_index, curr_value, mid = calculate_drawing(commands, 0, 40, command_index, curr_value, mid)
    print("".join(output))

    return 0


def calculate_drawing(commands, start, end, command_index, value, is_mid_pos):
    curr_value = value
    output = []

    curr_cycle = start
    index = command_index

    mid_position = is_mid_pos

    while curr_cycle != end:
        command = commands[index]
        index += 1
        if command == "noop":
            new_out = get_print_value(curr_cycle, curr_value)
            output.append(new_out)
            curr_cycle += 1
        else:
            com, val = command.split(" ")

            if not mid_position:
                new_out = get_print_value(curr_cycle, curr_value)
                output.append(new_out)
                curr_cycle += 1

                if curr_cycle == end:
                    mid_position = True
                    break

            new_out = get_print_value(curr_cycle, curr_value)
            output.append(new_out)
            curr_cycle += 1

            curr_value += int(val)
        mid_position = False

    # if cycle ends in the middle of the reading command, keep previous command
    if mid_position:
        index -= 1
    return output, index, curr_value, mid_position


def get_print_value(crt_row, register):
    if crt_row == register or crt_row + 1 == register or crt_row - 1 == register:
        return "#"
    else:
        return "."


data = read_file("input.txt")
# print(task1(data))

print(task2(data))
