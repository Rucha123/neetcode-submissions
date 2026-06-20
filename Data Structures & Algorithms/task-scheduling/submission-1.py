class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q=deque()
        mh=[]
        t=0

        c=Counter(tasks)

        for i in c.values():
            heapq.heappush(mh,-i)

        while mh or q:
            t+=1

            if mh:
                cnt = 1+ heapq.heappop(mh)
                if cnt:
                    q.append([cnt,t+n])

            if q and q[0][1]==t:
                heapq.heappush(mh,q.popleft()[0])

        return t
            


        