class Node:
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class LRUCache(object):
    '''
    利用链表来存储数据，同时将节点放入字典用来与缓存能力比较
    关键1：存储方式，利用双向链表存储，类似于栈的后进先出的结构，head连接栈底，tail连接栈尾
    关键2：get和put方法类似，如果get了新的key，value，则放在栈尾，与tail连接，如果key相同，value不同，则
           移除旧节点，再把新节点放在栈尾；put同理，如果存在key，则把该节点放在栈尾
      tail       
    | 2,2  |
    | 1,1  |
    |______|
      head


    '''
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key,value)
        self._add(n)
        self.dic[key] = n
        if self.capacity < len(self.dic):
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _add(self,node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p

    def _remove(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
