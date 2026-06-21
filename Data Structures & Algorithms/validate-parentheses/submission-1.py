class Solution:
    def isValid(self, s: str) -> bool:
        h={")":"(","]":"[","}":"{"}
        op =["(","{","["]
        st=[]

        for i in range(len(s)):
            if s[i] in op:
                st.append(s[i])
            elif st and st[-1]==h[s[i]]:
                st.pop()
            else:
                return False
        return len(st) == 0
        