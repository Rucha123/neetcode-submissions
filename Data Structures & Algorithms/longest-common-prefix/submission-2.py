class Node:

    def __init__(self):
        self.child={}
        self.IsWord=False
        self.c=0


class Trie:

    def __init__(self):
        self.root=Node()

    def insert(self,st):
        cur=self.root
        for ch in st:
            if ch not in cur.child:
                cur.child[ch]=Node()
                cur.c+=1
            cur=cur.child[ch]
            
        cur.IsWord=True

    def search(self):
        cur=self.root
        res=""
        while cur.c==1 and cur.IsWord==False:
            for ch in cur.child:
                res+=ch
                cur=cur.child[ch]

        return res


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie=Trie()

        for st in strs:
            trie.insert(st)

        return trie.search()


        