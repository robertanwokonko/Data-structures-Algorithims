import json 

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def __repr__(self):
    return "{{Value: {}. Right: {}. Left: {}     }}".format(self.value, self.right, self.left)
   
class BinaryTree:
  def __init__(self):
    self.rootNode = None

  def __repr__(self):
    return "{{ Root Node: {} }}".format(self.rootNode)
    
  
  def lookup(self, value):
    if self.rootNode == None:
      return None
    currentNode = self.rootNode
    while currentNode:
      if value < currentNode.value:
        currentNode = currentNode.left
      elif value > currentNode.value:
        currentNode = currentNode.right
      elif value == currentNode.value:
        return currentNode
    return False

  def insert(self,value):
    newNode = Node(value)
    if self.rootNode == None:
      self.rootNode = newNode
      # print(self.rootNode)
    else:
      currentNode = self.rootNode
      while True:
        # left
        if value < currentNode.value:
          if currentNode.left == None:
            currentNode.left = newNode
            break
          else:
            currentNode = currentNode.left
        else: 
          if value >= currentNode.value:
            if currentNode.right == None:
              currentNode.right = newNode
              break
            else:
              currentNode = currentNode.right


  def delete(self, value):
    # 3 cases to consider
    
    # no right child
    def handleNoRightChild(self, currentNode, parentNode):
      if parentNode == None:
        self.rootNode = currentNode.left
      else:
        if currentNode.value < parentNode.value:
          parentNode.left = currentNode.left
        elif currentNode.value > parentNode.value:
          parentNode.right = currentNode.left

    # Right child which doesnt have a left child
    def handleRightChildWithNoLeftChild(self, currentNode, parentNode):
      currentNode.right.left = currentNode.left
      
      if parentNode == None:
        self.rootNode = currentNode.right
      else:
        if currentNode.value < parentNode.value:
          parentNode.left = currentNode.right
        elif currentNode.value > parentNode.value:
          parentNode.right = currentNode.right

    # Right child that has a left child
    def handleRightChildWithLeftChild(self, currentNode, parentNode):
      # find the Right child's left most child
      leftmost = currentNode.right.left
      leftmostParent = currentNode.right
  
      while leftmost.left != None:
        leftmostParent = leftmost
        leftmost = leftmost.left
  
      # Parent's left subtree is now leftmost's right subtree
      leftmostParent.left = leftmost.right
      leftmost.left = currentNode.left
      leftmost.right = currentNode.right
  
      if parentNode == None:
        self.rootNode = leftmost
      else:
        if currentNode.value < parentNode.value:
          parentNode.left = leftmost
        elif currentNode.value > parentNode.value:
          parentNode.right = leftmost
          
    
    #############################
    # Delete function starts here
    if self.rootNode == None:
      return False

    currentNode = self.rootNode
    parentNode = None

    while currentNode:
      if value < currentNode.value:
        parentNode = currentNode
        currentNode = currentNode.left
      elif value > currentNode.value:
        parentNode = currentNode
        currentNode = currentNode.right
      elif value == currentNode.value: # found node to be deleted

        # if no right child
        if currentNode.right == None:
          handleNoRightChild(self, currentNode, parentNode)

        # Right child which doesnt have a left child
        elif currentNode.right.left == None:
          handleRightChildWithNoLeftChild(self, currentNode, parentNode)

        # Right child that has a left child
        else:
          handleRightChildWithLeftChild(self, currentNode, parentNode)

        return True
    #BreadthfirstSearch
    def breadthFirstSearch(self):
      queue = []
      List = []
      currentNode = self.rootNode
      queue.append(currentNode)

      while len(queue) > 0:
        currentNode = queue.pop(0)
        List.append(currentNode.value)
        if currentNode.left:
          queue.append(currentNode.left)
        if currentNode.right:
          queue.push(currentNode.right)
          
      return List

def treeToDic(node):
  dict = {'value': node.value, 'right': None, 'left': None}
  if not node.right == None:
    dict['right'] = treeToDic(node.right)
  if not node.left == None:
    dict['left'] = treeToDic(node.left)
  return dict
  
newBT = BinaryTree()
newBT.insert(10)
newBT.insert(5)
newBT.insert(2)
newBT.insert(15)
newBT.lookup(15)
print(json.dumps(treeToDic(newBT.rootNode)))