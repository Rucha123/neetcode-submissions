class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        res=[]

        adj=defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        print(adj)

        for i,j in adj.items():
            j.sort(reverse=True)

        print(adj)
        st=["JFK"]

        while st:
            cur=st[-1]
            if not adj[cur]:
                res.append(st.pop())
            else:
                st.append(adj[cur].pop())

        return res[::-1]





        