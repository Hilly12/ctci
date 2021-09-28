class SetOfStacks:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.stacks = []
        self.stack_index = -1

    def push(self, item):
        if self.stack_index == -1 or len(self.stacks[self.stack_index]) >= max_capacity:
            self.stack_index += 1
            if len(stacks) == self.stack_index:
                self.stacks.append([])

        self.stacks[self.stack_index].append(item)

    def pop(self):
        if self.stack_index == -1 or self.stack_index == 0 and len(self.stacks[self.stack_index]) == 0:
            raise Exception("Empty Stack")

        if len(self.stacks[self.stack_index]) == 0:
            self.stack_index -= 1

        self.stacks[self.stack_index].pop()

    def popAt(self, index):
        if len(self.stacks[index]) == 0:
            raise Exception("Empty Sub Stack")

        self.stacks[index].pop()
        
