class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}  #store key value pair
        for i,n in enumerate(nums):
            comp=target-n
            if comp in seen: #initially not 
                return [seen[comp],i]
            else:
                seen[n]=i #initially since its empty we add seen[3]=0. seen={3:0}
