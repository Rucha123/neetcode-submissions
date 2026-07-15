class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res=[]
        q=deque()
        d=[0]*numCourses
        adj=[]

        for i in range(numCourses):
            adj.append([])

        for i in prerequisites:
            d[i[0]]+=1

        for i in prerequisites:
            adj[i[1]].append(i[0])

        for i in range(numCourses):
            if d[i]==0:
                q.append(i)

        while q:
            cur=q.popleft()
            res.append(cur)
            c1=adj[cur]

            for i in c1:
                d[i]-=1
                if d[i]==0:
                    q.append(i)

        return res if len(res)==numCourses else []

        