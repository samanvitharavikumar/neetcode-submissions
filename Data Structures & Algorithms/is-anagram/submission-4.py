class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       countt=Counter(t) 
       counts=Counter(s)
       if countt==counts:
        return True
       return False 