class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        i=j=0
        if len(t)==1 and len(s)==1:
            if t[0]!=s[0]:
                return 1

        while i<len(s) and j<len(t):
            if s[i]==t[j] and j<len(t):
                j+=1
                i+=1
            else:
                i+=1
           
        return len(t)-j
      
            
        