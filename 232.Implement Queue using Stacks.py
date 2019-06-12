class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):#利用s2缓存一下s1pop的值，然后将新值放入s1，再把s2的值pop放入s1
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1