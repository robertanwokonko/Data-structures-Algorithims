class Array:

    def __init__(self):
        self.length = 0
        self.data = {}
        pass

    def append(self, item):
        self.data[self.length]  = item
        self.length = self.length + 1

    def get(self, index):
      return self.data[index]

    def delete(self, index):
      self.shiftElements(index)

    def shiftElements(self, index):
      for i in range(index, self.length - 1):
        self.data[index] = self.data[index+1]
      del self.data[self.length - 1]

    def pop(self):
      del self.data[self.length - 1]

     
        



newArray = Array()
newArray.append('a')

# newArray.pop()

# newArray.delete(1)
# newArray.shiftElements(1)

print(newArray.length)
print(newArray.data)