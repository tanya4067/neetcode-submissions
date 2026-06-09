# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=[]

        while(head is not None):
            if(head in temp):
                return(True)
            else:
                temp.append(head)
            
            head=head.next
        return(False)