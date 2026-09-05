"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #a-b-c is the linked list
        oldtocopy={None:None}
        curr=head
        while curr:
            copy=Node(curr.val) #copy=a'
            oldtocopy[curr]=copy #this gives a' to a in the hashmap
            curr=curr.next
        curr=head
        while curr:
            copy=oldtocopy[curr] #it gives copy as a' 
            copy.next=oldtocopy[curr.next] #a' next is the same as a next  
            copy.random=oldtocopy[curr.random] 
            curr=curr.next
        return oldtocopy[head]    
        