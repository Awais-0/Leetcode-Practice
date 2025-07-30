class Stack:
    def __init__(self):
        self.arr = []
        
    def push(self):
        while (entry := input("Enter number(q to quit): ")) != 'q':
            try:
                self.arr.append(int(entry))
            except ValueError:
                print('Pls enter a digit')

    def pop_(self):
        if self.arr:
            return self.arr.pop()
        else:
            print('Stack is empty')

    def show(self):
        return self.arr
    

my_stack = Stack()

my_stack.push()

print("bottom ->",my_stack.show(),"<- top")

print(my_stack.pop_())
print(my_stack.pop_())

print("bottom ->",my_stack.show(),"<- top")