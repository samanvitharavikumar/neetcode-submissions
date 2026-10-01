class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countt=Counter(nums)
        for n in (nums):
            if countt[n]>1:
                return True
        return False         