class Node:
    def __init__(self):
        self.child={}
        self.isEnd=False
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
        cur.isEnd=True

    def search(self,st):
        cur=self.root
        res=""

        for ch in st:
            if ch in cur.child and cur.c==1 and cur.isEnd==False:
                res+=ch
                cur=cur.child[ch]
            else:
                break

        return res


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie=Trie()

        for st in strs:
            trie.insert(st)

        return trie.search(st)


        