class TimeMap:

    def __init__(self):
        self.h={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.h:
            self.h[key]=[]
        self.h[key].append([value,timestamp])   
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        v=self.h.get(key,[])
        l=0
        r=len(v)-1

        while l<=r:
            m=(l+r)//2
            if v[m][1]<=timestamp:
                res=v[m][0]
                l=m+1
            else:
                r=m-1

        return res
        
