class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        res=0

        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            else:
                b=st.pop()
                a=st.pop()
                if i == "+":
                    st.append(a+b)
                elif i == "-":
                    st.append(a-b)
                elif i == "*":
                    st.append(a*b)
                else:
                    st.append(int(a/b))

        return st.pop()


        
        