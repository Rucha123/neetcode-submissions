class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj=[]
        d=[0]*numCourses
        q=deque()
        res=[]

        for i in range(numCourses):
            adj.append([])

        for i,j in prerequisites:
            adj[j].append(i)

        for i in prerequisites:
            d[i[0]]+=1

        print(adj,d)

        for i in range(numCourses):
            if d[i]==0:
                q.append(i)

        while q:
            cur=q.popleft()
            res.append(cur)

            for i in adj[cur]:
                d[i]-=1
                if d[i]==0:
                    q.append(i)

        return res if len(res)==numCourses else []


        