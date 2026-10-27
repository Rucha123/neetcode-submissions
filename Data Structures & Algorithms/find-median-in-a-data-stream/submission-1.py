class MedianFinder:

    def __init__(self):
        self.arr=[]
        self.arr1=[]
        
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr,-num)

        heapq.heappush(self.arr1, -heapq.heappop(self.arr))

        if len(self.arr1)>len(self.arr):
            heapq.heappush(self.arr,-heapq.heappop(self.arr1))


    def findMedian(self) -> float:

        if len(self.arr)>len(self.arr1):
            return -self.arr[0]
        else:
            return (-self.arr[0]+self.arr1[0])/2


      


        
        