class Solution(object):#暴力解时间复杂度太高
    def maxArea(self, height):
        """
        双指针法
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l = 0
        r = len(height) - 1

        while l < r:
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea

    def maxArea2(self, height):
        """
        与上同理，但这个时间快一点
        :type height: List[int]
        :rtype: int
        """
        ptr1 = 0
        ptr2 = len(height) - 1
        area = 0
        while ptr1 < ptr2:
            a = 0
            if height[ptr1] > height[ptr2]:
                a = (ptr2 - ptr1) * height[ptr2]
                ptr2 -= 1
            else:
                a = (ptr2 - ptr1) * height[ptr1]
                ptr1 += 1
            area = max(a, area)

        return area

S = Solution()
print(S.maxArea([1,8,6,2,5,4,8,3,7]))
