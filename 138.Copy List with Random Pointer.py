
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        完全复制一份链表，先把节点复制一份保存，再把next，random加入
        :type head: Node
        :rtype: Node
        """
        dic = dict()
        m = n = head
        while m:
            dic[m] = Node(m.val,None,None)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)


    def copyRandomList2(self, head):#defaultdict(lambda x) 当dic[n]中没有值时，返回x
        dic = collections.defaultdict(lambda: Node(0,None,None))
        dic[None] = None
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
