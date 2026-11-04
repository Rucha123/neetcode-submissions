class MedianFinder:

    def __init__(self):
        self.arr1=[]
        self.arr2=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr1,-num)    
        heapq.heappush(self.arr2,-heapq.heappop(self.arr1))
        if len(self.arr1)<len(self.arr2):
            heapq.heappush(self.arr1,-heapq.heappop(self.arr2))
        

    def findMedian(self) -> float:

        if len(self.arr1)>len(self.arr2):
            return -self.arr1[0]
        else:
            return (-self.arr1[0]+self.arr2[0])/2
        