class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}#an empty dict to store the nums
        for i,n in enumerate(nums):#index and val-0 to 3 ,1 to 4 etc
            
            comp=target-n#comp=7-3
            if comp in seen: #is 4 in seen ? no cus seen is empty so we add 3 to seen. seen[3]=0. so we add {3:0}
                return [seen[comp],i]
            seen[n]=i