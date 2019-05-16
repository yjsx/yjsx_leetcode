# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        while(l1 != None):
            num1.append(str(l1.val))
            l1 = l1.next
        while (l2 != None):
            num2.append(str(l2.val))
            l2 = l2.next
        num1 = "".join(list(reversed(num1)))
        num2 = "".join(list(reversed(num2)))
        num1 = int(num1)
        num2 = int(num2)
        out = num1 + num2
        out = (list(reversed(list(str(out)))))
        node = ListNode(0)
        node = ListNode(int(out[0]))
        p = node
        for x in out[1:]:
            p.next = ListNode(int(x))
            p = p.next
        return node