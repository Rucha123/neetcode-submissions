class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        q=deque()
        q.append(source)
        visitedstop=set()
        visitedstop.add(source)
        visitedRoute=set()
        h=defaultdict(list)
        c=0

        for i in range(len(routes)):
            for j in routes[i]:
                h[j].append(i)

        print(h)

        while q:
            c+=1

            for i in range(len(q)):
                cur=q.popleft()

                for k in h[cur]:
                    if k in visitedRoute:
                        continue
                    visitedRoute.add(k)

                    for st in routes[k]:
                        if st == target:
                            return c
                        if st not in visitedstop:
                            q.append(st)
                            visitedstop.add(st)


        return -1
                





        