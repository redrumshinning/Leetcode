class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):#模拟队列，将进入的值放在列表的尾部
        q = self._queue
        q.append(x)                            # 1.[1]
        for _ in range(len(q) - 1):           # 2.[1,2] -> [2,1]
            q.append(q.popleft())              # 3.[2,1,3] -> [1,3,2] -> [3,2,1]

    def pop(self):#
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)