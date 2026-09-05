class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0] #first element slow is 1
        fast = nums[0] #first ele fast is 1
        while True: #consider 1-2-3-2-2
        #this is done to find the meeting point (3,3)
            slow = nums[slow] # slow=nums[1] which is 2 . #iter 2 slow=3
            fast = nums[nums[fast]] # fast=nums[nums[1]]
                                    #fast=nums[2] which is 3 #iter 2 ,fast=3

            if slow == fast:
                break #3=3

        slow = nums[0] #slow=1 

        while slow != fast: # 1!=3
            slow = nums[slow] #slow=2
            fast = nums[fast] #fast=2

        return slow