import Item

def read_file(name):
    f = open(name, "r")
    return f.read()


def task1(data):
    root = build_filesystem(data)
    sizes = collect_dir_sizes(root)
    sizes = list(filter(lambda s: s < 100_000, sizes))
    res = sum(sizes)
    return res


def task2(data):
    root = build_filesystem(data)
    sizes = collect_dir_sizes(root)
    free_space = 70_000_000 - max(sizes)
    needed_space = 30_000_000 - free_space
    sizes = list(filter(lambda s: s >= needed_space, sizes))
    res = min(sizes)
    return res


def build_filesystem(data):
    commands = data.split("\n")[1:]
    directory = Item.Dir("/")
    root = directory
    for i, command in enumerate(commands):
        if command[0] == "$":
            com = command.split(" ")
            if com[1] == "cd":
                dir_name = com[2]
                if dir_name == "..":
                    directory = directory.parent
                    continue

                new_dir = Item.Dir(dir_name)
                new_dir.parent = directory
                directory.add_item(new_dir)
                directory = new_dir
            elif com[1] == "ls":
                index = i+1
                while index < len(commands) and commands[index][0] != "$":
                    content = commands[index].split(" ")
                    if content[0] != "dir":
                        new_f = Item.File(content[1], content[0])
                        directory.add_item(new_f)
                    index += 1

    return root


def collect_dir_sizes(directory: Item.Dir):
    sizes = list()
    for i in directory.items:
        if isinstance(i, Item.Dir):
            size = collect_dir_sizes(i)
            sizes += list(size)

    size = directory.total_size(directory)
    sizes.append(size)
    return sizes


data = read_file("input.txt")
print(task1(data))

print(task2(data))
