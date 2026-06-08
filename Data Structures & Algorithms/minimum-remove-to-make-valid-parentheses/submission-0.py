class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        st=[]
        visited=[False]*len(s)
        res=[]

        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            elif s[i]==")":
                if st:
                    st.pop()
                else:
                    visited[i]=True


        for i in st:
            visited[i]=True

        for i in range(len(s)):
            if not visited[i]:
                res.append(s[i])

        return "".join(res)
        