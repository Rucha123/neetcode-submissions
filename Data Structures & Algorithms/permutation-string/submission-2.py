class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        h={}

        for i in s1:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        
        i=j=0
        c=0
        for j in range(len(s2)):
            if h.get(s2[j],0) > 0:
                c+=1
            h[s2[j]]=h.get(s2[j],0)-1

            if j>=len(s1):
                if h.get(s2[i],0)>=0:
                    c-=1
                h[s2[i]]=h.get(s2[i],0)+1
                i+=1

            if c==len(s1):
                return True

        return False


        