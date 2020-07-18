# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n=head
        count=0
        while n.next is not None:
            count+=1
            n=n.next
        n=head
        no=0
        while n is not None:
            no+=n.val*(2**count)
            count-=1
            n=n.next
        return no
