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



