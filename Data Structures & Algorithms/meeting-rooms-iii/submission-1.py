class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        av=[]
        busy=[]
        for i in range(n):
            heapq.heappush(av,i)
        c=[0]*n
        meetings.sort()

        for st,end in meetings:

            while busy and busy[0][0]<st:
                end_t,room=heapq.heappop(busy)
                heapq.heappush(av,room)

            if av:
                room=heapq.heappop(av)
                heapq.heappush(busy,(end,room))
            else:
                end_t,room=heapq.heappop(busy)
                dur=end-st
                new_end=dur+end_t
                heapq.heappush(busy,(new_end,room))

            c[room]+=1

        ans=0
        for i in range(n):
            if c[i]>c[ans]:
                ans=i

        return ans


        