# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new ListNode to store the sum of two ListNodes
        head = ListNode(0)
        curr = head
        # Will determine whehter the sum of l1.val and l2.val excess 9 or not
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            # Check l1 node value
            if l1 != None:
                x = l1.val
            else: 
                x = 0
            # Check l2 node value
            if l2 != None:
                y = l2.val
            else:
                y = 0
            
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next

            if l1 != None:
                l1 = l1.next
            else:
                l1 = None

            if l2 != None:
                l2 = l2.next
            else:
                l2 = None
        return head.next

            
            




        
