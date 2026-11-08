"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        h={node:Node(node.val)}
        q=deque()
        q.append(node)

        while q:
            cur=q.popleft()
            for i in cur.neighbors:
                if i not in h:
                    h[i]=Node(i.val)
                    q.append(i)
                h[cur].neighbors.append(h[i])

        return h[node]


        