# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList2(self, head):#从前往后递归
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

    def reverseList3(self, head):#从后往前递归，最后一个节点为new_head
        if not head or not head.next:
            return head

        new_head = self.reverseList3(head.next)
        next_node = head.next  # head -> next_node
        next_node.next = head  # head <- next_node
        head.next = None  # [x] <- head <- next_node
        return new_head