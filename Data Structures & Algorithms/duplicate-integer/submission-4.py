from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      countnums=Counter(nums) 
      #returns a dict={1:1,2:3..}
      for c in countnums.values():
        #1,2,3...
        if c>1:
            #if counter is> 1
          return True
         
      return False  