class Solution:

    def encode(self, strs: List[str]) -> str:
        st=""
      
        for i in strs:
            st+=str(len(i))+"#"+i

        return st
         
        

    def decode(self, s: str) -> List[str]:

        a=[]
        i=0

        while i < len(s):
            j=i

            while s[j] != "#":
                j+=1
            l=int(s[i:j])
            a.append(s[j+1:j+1+l])
            i=j+1+l
        return a


        


        return
