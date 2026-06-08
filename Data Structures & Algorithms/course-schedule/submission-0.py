class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dep=[0]*numCourses
        adj=[]
        q=deque()

        for i in prerequisites:
            dep[i[0]]+=1

        print(dep)

        for i in range(numCourses):
            adj.append([])

        for i in prerequisites:
            adj[i[1]].append(i[0])

        print(adj)
        
        for i in range(numCourses):
            if dep[i]==0:
                q.append(i)

        while q:
            cur=q.popleft()
            c1=adj[cur]
            for j in c1:
                dep[j]-=1
                if dep[j]==0:
                    q.append(j)

        for i in range(numCourses):
            if dep[i]!=0:
                return False

        return True





            
        