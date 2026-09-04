class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for i,n in enumerate(nums):
            if count[n]>1:
                return True
        return False