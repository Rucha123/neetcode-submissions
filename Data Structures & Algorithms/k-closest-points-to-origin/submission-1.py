import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        arr=[]
        ans=[]

        for i in points:
            d=math.sqrt((i[0])**2 + (i[1])**2)
            heapq.heappush(arr,[d,i])
   

        while k>0:
            d,k1 =heapq.heappop(arr)
            ans.append(k1)
            k-=1

        return ans
               
                



 




        