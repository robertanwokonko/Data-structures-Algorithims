class Graph:
  def __init__(self):
    self.NumberofNodes = 0
    self.adjacentList = {}
    
  def __repr__(self):
    return "graph: {}. len: {}".format(self.adjacentList, self.NumberofNodes)
    
  def addVertex(self, node):
    self.adjacentList[node] = []
    self.NumberofNodes += 1


  def addEdge(self, node1, node2):
    self.adjacentList[node1].append(node2)
    self.adjacentList[node2].append(node1)
    
    


graph = Graph()
graph.addVertex(10)
graph.addVertex(5)
graph.addVertex(7)
graph.addEdge(5, 10)
graph.addEdge(5, 7)
graph.addEdge(10, 7)
print(graph)