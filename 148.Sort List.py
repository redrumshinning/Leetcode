# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        middle_node = self.find_middle_node(head)
        right_head = middle_node.next
        middle_node.next = None
        left = self.sortList(head)
        right = self.sortList(right_head)
        return self.mergeTwoLists(left,right)

    def find_middle_node(self,head):
        slow,fast = head,head
        while fast.next and fast.next.next:#对比下面，因为head在进来之前，已经判断过了是否为None，所以不用写fast
        #while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = slow.next.next
        return slow
    #21题照搬照抄
    def mergeTwoLists(self, l1, l2):
        result = ListNode(0)
        l = result
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        l.next = l1 or l2
        return result.next