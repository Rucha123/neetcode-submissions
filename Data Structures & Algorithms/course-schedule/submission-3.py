class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        ind=[0]*numCourses
        adj={}

        for i in range(numCourses):
            adj[i]=[]

        for i in prerequisites:
            adj[i[1]].append(i[0])

        for i in prerequisites:
            ind[i[0]]+=1

        q=deque()

        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)

        while q:
            cur=q.popleft()
            c1=adj[cur]
            for i in c1:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)

        for i in range(numCourses):
            if ind[i]!=0:
                return False
           

        return True



        
        