class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        #nums=[100, 4, 200, 1, 3, 2]
        numset=set(nums)
        #numset={100,4,200,1,3,2}
        length=0
        for n in nums: #n=100
            if(n-1) not in numset: #is 99 in set? no. so length=0.
                length=0
                while(n+length) in numset: #while(100+0=100) in set:
                    length+=1 #length=1
                    longest=max(longest,length)        #longest=max(1,0)=1
        return longest #longest is 1 

    # again in iter 2 , n is 4. 4-1 not in the set? its there soo we dotn execute the if block. 