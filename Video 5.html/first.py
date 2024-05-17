print("hello world")
class stack:
    def __init__(self):
        self.values = []
    def push(self,element):
        self.values.append(element)
    def pop(self):
        if not(self.isEmpty()):
            return self.values.pop()
        else:
            return "stack underflow"
    def size(self):
       return len(self.values)
    def isEmpty(self):
        return len(self.values) == 0
    def top(self):
        if not(self.isEmpty()):
            return self.values[-1]
        else:
            print("stack is empty")


s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.values)
s.pop()
s.pop()
s.pop()
# s.pop()
print(s.values)
print(" ")
print(s.size())
print(s.isEmpty())
# print(s.pop())
print(s.top())
