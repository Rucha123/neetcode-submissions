class Solution:
    def customSortString(self, order: str, s: str) -> str:

        i=j=0
        s=list(s)
        print(s)

        h={}
        res=""

        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]]=1
            else:
                h[s[i]]+=1


        print(h)
        
        for i in order:
            if i in s:
                res+=i*h[i]
        for i in s:
            if i not in order:
                res+=i

        

    
        return res

        