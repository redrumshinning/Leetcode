# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        这种让返回链表的题一定要定义一个dummy放在开头
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        first = head
        length = 0
        while first:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length > 0:
            first = first.next
            length -= 1
        first.next = first.next.next
        return dummy.next

    def removeNthFromEnd2(self, head, n):
        '''
        双指针，先将一个指针定位，然后再同时移动
        :param head:
        :param n:
        :return:
        '''
        end = head
        track = head

        for i in range(n):
            if not end.next:#如果删掉的是head，则返回head.next
                if i == n - 1:
                    return head.next
            end = end.next

        while end.next:
            track = track.next
            end = end.next

        track.next = track.next.next
        return head
