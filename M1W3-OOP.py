class MyStack:
    def __init__(self,capacity):
        self.__capacity = capacity
        self.__stack = []
    def is_empty(self):
        return len(self.__stack) == 0
    def is_full(self):
        if len(self.__stack) == self.__capacity:
            return True
        else:
            return False
    def pop(self):
        if self.is_empty():
            print("Don't do!")
        else:
            return self.__stack.pop()
    def print(self):
        print(self.__stack)
   
    def push(self,value):
        if self.is_full():
            print("Don't do!")
        else:
            self.__stack.append(value)
    def top(self):
        if self.is_empty():
            print("Don't do!")
        else:
            return self.__stack[-1]
    def print(self):
        print(self._stack)
stack1 = MyStack(5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())