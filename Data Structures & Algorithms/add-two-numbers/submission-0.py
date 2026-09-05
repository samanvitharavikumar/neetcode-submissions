# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode() 
        curr=dummy #dummy is beginning of the list
        while l1 or l2 or carry: 
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            total=v1+v2+carry
            carry=total//10 #find the carry like 1
            total=total%10 #find the total if its 7 and 1 carry, then its 7

            curr.next=ListNode(total) #beginning of the list is dummy.dummy after that is val 
            curr=curr.next #shift the curr value to second value
            
            l1=l1.next if l1 else 0
            l2=l2.next if l2 else 0
        return dummy.next
            