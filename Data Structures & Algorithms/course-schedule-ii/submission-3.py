class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj={}
        ind=[0]*numCourses

        for i in range(numCourses):
            adj[i]=[]

        for i in prerequisites:
            ind[i[0]]+=1

        for i in prerequisites:
            adj[i[1]].append(i[0])
        
        q=deque()
        res=[]
        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)

        while q:
            cur=q.popleft()
            res.append(cur)
            c1=adj[cur]
            for i in c1:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)

        return res if len(res)==numCourses else []
                
           
            