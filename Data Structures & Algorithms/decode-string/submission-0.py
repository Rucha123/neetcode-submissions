class Solution:
    def decodeString(self, s: str) -> str:
        st=[]

        for i in range(len(s)):
            if s[i] !="]":
                st.append(s[i])
            else:
                tp=""
                while st[-1] != "[":
                    tp=st.pop()+tp
                st.pop()

                k=""
                while st and st[-1].isdigit():
                    k=st.pop() + k
                
                st.append(tp*int(k))

        return "".join(st)
        