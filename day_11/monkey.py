class Monkey:
    def __init__(self, number, items, operation, test, divide_by_three=True):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.divide_by_three = divide_by_three
        self.processed_items = 0

        self.action, self.second_op = self.parse_operation()
        self.divider, self.success, self.fail = self.parse_test()
        self.supermodulo = 0

    def add_item(self, item):
        self.items.append(item)

    def process_items(self, monkeys):
        while len(self.items) > 0:
            item = self.items.pop(0)
            new_val = self.do_operation(item)
            if self.supermodulo != 0:
                new_val = new_val % self.supermodulo
            to_monkey = self.do_test(new_val)
            monkeys[to_monkey].add_item(new_val)
            self.processed_items += 1

    def parse_operation(self):
        _, _, _, act, op2 = self.operation.split(" ")
        second_op = op2
        if op2 != "old":
            second_op = int(op2)
        return act, second_op

    def do_operation(self, value):
        old = value
        if self.second_op == "old":
            second_op = old
        else:
            second_op = self.second_op

        new = 0
        if self.action == "*":
            new = old * second_op
        elif self.action == "+":
            new = old + second_op

        if self.divide_by_three:
            new = int(new / 3.0)
        return new

    def parse_test(self):
        divider, success, fail = [int(s) for s in self.test.split() if s.isdigit()]
        return divider, success, fail

    def do_test(self, new_val):
        if new_val % self.divider == 0:
            return self.success
        else:
            return self.fail
