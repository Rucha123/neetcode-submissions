class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        c=[0]*n
        av=[]
        busy=[]
        for i in range(n):
            heapq.heappush(av,i)

        meetings.sort()

        for st,end in meetings:

            while busy and busy[0][0]<=st:
                end_t,room=heapq.heappop(busy)
                heapq.heappush(av,room)

            if av:
                room=heapq.heappop(av)
                heapq.heappush(busy,(end,room))
            else:
                ed_t,room=heapq.heappop(busy)
                dur=end-st
                nw_end=ed_t+dur
                heapq.heappush(busy,(nw_end,room))

            c[room]+=1

        print(c)

        ans = 0

        for i in range(n):
            if c[i] > c[ans]:
                ans = i

        return ans

        