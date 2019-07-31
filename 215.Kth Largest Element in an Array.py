import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        最好不要这么写，体现不出算法能力！
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums,reverse=True)[k-1]

    def findKthLargest2(self, nums, k):#最小堆模拟最大堆
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res


class Quantity:
    def __init__(self,storage_name):
        self.storage_name = storage_name
    def __set__(self,instance,value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')
class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self,discription,weight,price):
        self.discription = discription
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

truffle = LineItem('White truffle', 100, 1)
print(truffle.price)


