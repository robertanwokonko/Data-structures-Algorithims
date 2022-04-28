class Solution:
  
  def topKFrequent(self, List, k):
    ans = []
    dict = {}
    self.k = k
    myset = set(List)
   
    if k > len(myset):
      return "k is out of range"
    for i in List:
      if dict.get(i):
        dict[i] += 1
      else:
        dict[i] = 1
        
    new_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
    

    for i in range(self.k):
      val = new_dict.popitem()
      val11, val12 = val
      ans.append(val11)
<<<<<<< HEAD
    
=======
          
>>>>>>> e692e9d6163fe6ecfa510610931671bd154f934f
    return ans

  
       
     
k = 4
List = [8,2,2,1,4,4,4,4,6,6,7,7,7,6]
newSol = Solution()
print(newSol.topKFrequent(List, k))