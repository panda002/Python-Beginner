class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        val = 6
        head = [1, 2, 6, 3, 4, 5, 6]
        temp = ListNode(-1)
        temp.next = head
        currentnode = head
        print(currentnode)

        while currentnode.next is None:
            if currentnode.next.val == val:
                currentnode.next = currentnode.next.next
            else:
                currentnode = currentnode.next
        return head