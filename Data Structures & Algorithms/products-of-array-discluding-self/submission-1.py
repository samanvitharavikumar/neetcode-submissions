class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums) 
        #nums=[1,2,4,6]
        #res=[1,1,1,1]
        prefix=1
        postfix=1
        for i in range (len(nums)):
            #i=0,n=1
            result[i]=prefix #initiallyy res[i]=1
            prefix=prefix*nums[i] #prefix=1*1
            #at the end result=[1,1,2,8]
        for i in range (len(nums)-1,-1,-1): #starts from i=3
            result[i]=result[i]*postfix    #res[3]=8*1
            postfix=postfix*nums[i] #postfix=1*6
            #i=2,res=12,post=24
            #i=1,res=24,post=48
            #i=0,res=48,post=
        return result