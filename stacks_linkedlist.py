class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
  def __repr__(self):
    return "{{Value: {}. Next: {}}}".format(self.value, self.next)

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0
  def __repr__(self):
    return "Top: {}.\nBottom: {}.\nLength: {}".format(self.top, self.bottom, self.length)

  def peek(self):
    return self.top

  def push(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.top = newNode
      self.bottom = newNode
    else:
      holdPointer = self.top
      self.top = newNode
      self.top.next = holdPointer
    self.length = self.length + 1
      

  def pop(self):
    if self.length == 0:
      return None
    else:
      self.length = self.length - 1
      return self.top
      

  def pop2(self):
    if self.top == None:
      return None
    else:
      holdtop = self.top
      self.top.next = self.top
      self.length = self.length - 1
      return holdtop

    

newStack = Stack()

# print(newStack.peek())
newStack.push("google")
newStack.push("udemy")
# print(newStack.pop())
print(newStack)


