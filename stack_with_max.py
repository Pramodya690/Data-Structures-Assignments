class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if not self.stack:
            return None
        self.max_stack.pop()
        return self.stack.pop()

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


# Input
q = int(input())
max_stack = MaxStack()
output = []

for _ in range(q):
    query = input().split()

    if query[0] == "push":
        value = int(query[1])
        max_stack.push(value)
    elif query[0] == "pop":
        max_stack.pop()
    elif query[0] == "max":
        output.append(max_stack.get_max())

# Output
for result in output:
    print(result)
