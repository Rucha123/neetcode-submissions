class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adj=[]
        d=[0]*numCourses
        q=deque()

        for i in range(numCourses):
            adj.append([])
        
        for i,j in prerequisites:
            adj[j].append(i)

        for i in prerequisites:
            d[i[0]]+=1

        for i in range(numCourses):
            if d[i]==0:
                q.append(i)

        while q:
            cur=q.popleft()
            for i in adj[cur]:
                d[i]-=1
                if d[i]==0:
                    q.append(i)

        for i in d:
            if i!=0:
                return False

        return True
        

        



        