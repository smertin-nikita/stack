

class Stack(list):

    def is_empty(self):
        return not self

    def push(self, item):
        super().append(item)

    def pop(self):
        return super().pop()

    def peek(self):
        return self[len(self) - 1]

    def size(self):
        return len(self)
