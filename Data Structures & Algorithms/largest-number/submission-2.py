class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        st=[]
        for i in nums:
            st.append(str(i))

        st.sort(key=lambda x:x*10,reverse=True)
        print(st)
        st="".join(st)
        return st if st[0] !="0" else "0"
        