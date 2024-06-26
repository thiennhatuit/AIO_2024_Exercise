

class myStack:
    def __init__(self, capacity:int):
        self.__capacity = capacity
        self.__stack_list = []
    
    def is_empty(self):
        return len(self.__stack_list) == 0
    def is_full(self):
        return len(self.__stack_list) == self.__capacity
    def pop(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.__stack_list.pop()
    def push(self,value):
        if self.is_full():
            raise Exception("Overflow")
        self.__stack_list.append(value)
    def top(self):
        if self.is_empty():
            print("Stack is empyt")
            return 
        return self.__stack_list[-1]
    def show(self):
        print(self.__stack_list)
stack = myStack(capacity=5)

stack.push(1)
stack.push(2)

print(stack.is_full())
print(stack.is_empty())
stack.show()


        

