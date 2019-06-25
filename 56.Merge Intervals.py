class Solution:
    '''
    排序是关键
    '''
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

S = Solution()
print(S.merge([[1,3],[2,6],[8,10],[15,18]]))