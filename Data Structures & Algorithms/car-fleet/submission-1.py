class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        res=[]
        st=[]

        for i in range(len(position)):
            res.append([position[i],speed[i]])

        res.sort(reverse=True)

        for p,s in res:
            t=(target-p)/s
            if not st or t>st[-1]:
                st.append(t)

        return len(st)
        