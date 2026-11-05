class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        q=deque()
        q.append(source)
        h=defaultdict(list)
        vb=set()
        vb.add(source)
        vr=set()
        c=0

        if source == target:
            return 0

        for i in range(len(routes)):
            for j in routes[i]:
                h[j].append(i)
        
        while q:
            c+=1
            for i in range(len(q)):
                cur=q.popleft()
                for i in h[cur]:
                    if i in vr:
                        continue
                    vr.add(i)
                    for k in routes[i]:
                        if k==target:
                            return c
                        if k not in vb:
                            vb.add(k)
                            q.append(k)

        return -1



        