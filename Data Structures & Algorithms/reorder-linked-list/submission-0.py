# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #2-4-6-8
        slow=head #2
        fast=head.next #4
        while fast and fast.next: #4 and 6 exist
            slow=slow.next #4
            fast=fast.next.next #8
        second=slow.next #4 as thats the middle
        prev=None
        slow.next=None #4-none
        while second:    #6
            #reverse this half of the list for 2 iterations
            temp=second.next #assign 6- link to temp
            second.next=prev #6 to none
            prev=second #make prev point  to 6 and 8 in second iteration
            second=temp #8
            #new order is 8-6-none
        first=head #2 and second is 8
        second=prev #prev is 8 
       
        while second:
            temp1=first.next #4
            temp2=second.next #6
            first.next=second #2-8
            second.next=temp1 #2-8-4
            first=temp1
            second=temp2