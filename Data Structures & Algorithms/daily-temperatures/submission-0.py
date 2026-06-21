class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)

        st=[]
        i=0

        for i in range(len(temperatures)):
            while st and temperatures[i]>st[-1][0]:
                t,idx=st.pop()
                res[idx]=i-idx
            st.append([temperatures[i],i])

        return res
        