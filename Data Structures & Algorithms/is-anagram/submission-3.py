class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts=Counter(s)
        countt=Counter(t)
        if countt==counts:
            return True
        return False    