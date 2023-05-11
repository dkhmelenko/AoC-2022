class Item:
    pass


class File(Item):
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir(Item):
    def __init__(self, name):
        self.name = name
        self.items = []
        self.parent = None

    def add_item(self, item):
        self.items.append(item)

    def total_size(self, directory):
        result = 0
        for i in directory.items:
            if isinstance(i, File):
                result += int(i.size)
            else:
                result += self.total_size(i)

        return result
