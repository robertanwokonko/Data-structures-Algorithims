class Stacks:
  def __init__(self):
    self.array = []
    self.length = 0
    
  def peek(self):
    if self.length == 0:
      return None
    else:
      return self.array[self.length -1]

  def push(self, value):
    self.array.append(value)
    self.length = self.length + 1
    return self.array

  def pop(self):
    self.array.pop()
    return self.array
    
    
newStack = Stacks()

print(newStack.pop())
# newStack.push(1)
# newStack.push(1)
# print(newStack.peek())

