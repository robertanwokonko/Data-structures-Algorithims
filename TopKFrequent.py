class Solution:
  
  def topKFrequent(self, List, k):
    ans = []
    dict = {}
    self.k = k

    for i in List:
      if dict.get(i):
        dict[i] += 1
      else:
        dict[i] = 1
        
    new_dict = {k: v for k, v in sorted(dict.items(), key=lambda  item: item[1])}

    for i in range(self.k):
      val = new_dict.popitem()
      val11, val12 = val
      ans.append(val11)
    
    
    # max_val = max(new_dict.values())
    # print(max_val)
    
    # for i in range(self.k):
    #   ans = []
    #   for key, value in list(new_dict.items()):
    #     if max_val == value:
    #       ans.append(key)
    #       del new_dict[key]
    #       return new_dict, ans
          
    return ans

  
       
     

    
k = 3
List = [8,2,2,1,4,4,4,4,6,6,7,7,6]
newSol = Solution()
print(newSol.topKFrequent(List, k))


        
