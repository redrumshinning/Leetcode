import collections
class Solution(object):
    # BFS
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    def findOrder(self, numCourses, prerequisites):
        dic = {i: set() for i in range(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        print(dic)
        print(neigh)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            print(queue)
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)#将i与node的联系断掉
                if not dic[i]:
                    queue.append(i)

        return res if count == numCourses else []


    # DFS
    def findOrder1(self, numCourses, prerequisites):
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]
        res = []

        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)#因为是深度优先，所以每次经过node后就把它删除
        return res if not dic else []

S = Solution()
print(S.findOrder1(4, [[1,0],[2,0],[3,1],[3,2]]))