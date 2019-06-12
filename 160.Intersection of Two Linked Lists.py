# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):#与141题思想一样，如果有交点，肯定追的到，没有返回none
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB

        while p and q and p!=q:
            p = p.next
            q = q.next
            if p == q:
                return q
            if not p:
                p = headB
            if not q:
                q = headA
        return p

    def getIntersectionNode2(self, headA, headB):
        p = headA
        q = headB
        while p != q:
            p = p.next if p  else headB
            q = q.next if q  else headA
        return p