class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cur = tot = start = 0

        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            tot += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
        return start if tot >= 0 else -1


