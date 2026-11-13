class Solution:
    def decodeString(self, s: str) -> str:

        res=""
        n=0
        st=[]

        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=="[":
                st.append(res)
                st.append(n)
                res=""
                n=0
            elif i=="]":
                n1=st.pop()
                ps=st.pop()
                res=ps+n1*res
            else:
                res+=i
        return res



        


        
        