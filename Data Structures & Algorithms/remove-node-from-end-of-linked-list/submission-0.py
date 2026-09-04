# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        slow,fast=dummy,dummy 
        for i in range(n): #2 is n
            fast=fast.next # slow and fast pointed to dummy. now fast is 2 in 1234
        while fast.next:
                slow=slow.next #slow is 1.then.2
                fast=fast.next #fast is 3  and then 4
        slow.next=slow.next.next #skip 3 and connect 2 to 4 
        return dummy.next        