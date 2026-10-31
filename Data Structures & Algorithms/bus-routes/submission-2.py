class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        q=deque()
        q.append(source)
        h=defaultdict(list)
        c=0
        vr=set()
        vb=set()
        vb.add(source)

        if source == target:
            return 0

        for i in range(len(routes)):
            for j in routes[i]:
                h[j].append(i)

        while q:
            c+=1
            for i in range(len(q)):
                cur=q.popleft()

                for r in h[cur]:
                    if r in vr:
                        continue
                    vr.add(r)

                    for b in routes[r]:
                        if b==target:
                            return c
                        if b not in vb:
                            vb.add(b)
                            q.append(b)

        return -1

                    


                
                