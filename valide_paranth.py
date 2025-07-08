s = "{[]}"
class Stack:
    def __init__(self):
        self.arr = []
    
    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.arr:
            return self.arr.pop()
        return "Stack is empty"
        
    def is_empty(self):
        return len(self.arr) == 0

my_stack = Stack()

def valid_paranth(string):
    for item in s:
        if item in '({[':
            my_stack.push(item)
        if item in ')]}':
            if my_stack.is_empty():
                return False
            temp = my_stack.pop()
            if (temp == '(' and item != ')') or (temp == '[' and item != ']') or (temp == '{' and item != '}'):
                return False
    return my_stack.is_empty()

print(valid_paranth(s))