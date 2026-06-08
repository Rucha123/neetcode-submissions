class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        print(s)

        return s

    def decode(self, s: str) -> List[str]:

        i=0
        res=[]

        while i<len(s):
            j=i

            while s[j]!="#":
                j+=1
            l=int(s[i:j])
            res.append(s[j+1:j+1+l])
            i=j+1+l

        return res

        return
