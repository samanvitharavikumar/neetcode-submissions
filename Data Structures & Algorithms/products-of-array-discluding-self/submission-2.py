class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
  # Input: nums = [1,2,4,6]

        prefix=1
        postfix=1
        result=[1]*len(nums)
        for i in range (len(nums)):
            result[i]=prefix
            prefix=prefix*nums[i]
            #[1,1,2,8]
        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix    
            postfix=postfix*nums[i]
        return result    
