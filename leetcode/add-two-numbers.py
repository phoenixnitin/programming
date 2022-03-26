from tokenize import Number
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: Number = val
        self.next : ListNode = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        res = root
        remainder = 0
        while l1 or l2 or remainder != 0:
            addition = remainder
            if l1:
                addition += l1.val
                l1 = l1.next
            if l2:
                addition += l2.val
                l2 = l2.next
            res.next = ListNode(val = addition % 10)
            res = res.next
            remainder = int(addition/10)
        return root.next
    
    def initListNode(self, l1):
        head = ListNode()
        root = head
        for index, num in enumerate(l1):
            if index != 0:
                root.next = ListNode()
                root = root.next
            root.val = num
        return head

    def printListNode(self, head: ListNode):
        items = []
        while head is not None:
            items.append(head.val)
            head = head.next
        print(items)

    def execute(self):
        l1 = self.initListNode([9,9,9,9,9,9,9])
        l2 = self.initListNode([9,9,9,9])
        res = self.addTwoNumbers(l1, l2)
        self.printListNode(res)
        
sol = Solution()
sol.execute()
exit()