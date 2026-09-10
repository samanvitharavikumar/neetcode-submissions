class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums=[3,4,5,6] target=7
        seen={} #store key value pair
        for i,n in enumerate(nums): #iter 2,i=1
            complement=target-n #complement=7-3=4, comp=7-4=3
            if complement in seen: #its empty first so we add it to seen. is 3 in seen?yes
                return [seen[complement],i] #seen[3],1 which is [0,1]
            else:#since its in the first iter, seen is empty, add to seen. seen[n]=i which gives seen={3:0}    
                seen[n]=i   
