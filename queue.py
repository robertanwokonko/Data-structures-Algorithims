class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __repr__(self):
    return "{{Value: {}. Next: {}}}".format(self.value, self.next)

  

class Queue:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def __repr__(self):
    return "Top: {}.\nBottom: {}.\nLength: {}".format(self.top, self.bottom, self.length)

  def peek(self):
    if self.top == None:
      return None
    else:
      return self.top

  def enqueue(self, value):
    newNode = Node(value)
    # if self.length == 0:
    if self.peek() == None:
      self.top = newNode
      self.bottom = newNode
      self.length = self.length + 1
    else:
      self.bottom.next = newNode
      self.bottom = newNode
      self.length = self.length + 1
      
      
  def dequeue(self):
      if self.peek() == None:
        return None
      else:
        holdtop = self.top
        self.top = self.top.next
        self.length = self.length - 1
        return holdtop


newQueue = Queue()
# print(newQueue.peek())
newQueue.enqueue(13)
# newQueue.enqueue(14)
# newQueue.enqueue(15)
# newQueue.enqueue(16)

# newQueue.dequeue()
print(newQueue)

# cant run enqueue one at a time
  
    

    