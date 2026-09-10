class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countnums=Counter(nums)
        for n in nums:
            if countnums[n]>1:
                return True
        return False    