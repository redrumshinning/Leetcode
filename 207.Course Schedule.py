class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]#不是所有点都与其他点相连，比如有4门课，0，1-2,2-3，那么0就可以直接学不用考虑约束问题
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        #我们每次找到一个新的点，判断从这个点出发是否有环
        for i in range(numCourses):#从第一个点开始访问，每个点都做起始点的原因是可能所有点之间不是相连的，比如存在约束1->2 和3->4->3，这样也是错的
            if not self.dfs(i,visit,graph):
                return False
        return True

    def dfs(self,i,visit,graph):
        if visit[i] == 1:#如果为1，表示正在访问，说明成环了
            return False
        if visit[i] == -1:#如果为-1，说明已经访问过了，这条路可以走
            return True
        visit[i] = 1#设置为正在访问
        for j in graph[i]:
            if not self.dfs(j,visit,graph):
                return False
        visit[i] = -1#如果到这一步，说明该点后面的点都访问过了，遇到了死胡同，将该点设置为已访问（后面的点也都在返回时设置了-1）
        return True

S = Solution()
print(S.canFinish(4, [[0,1],[1,2],[2,3],[2,1]]))