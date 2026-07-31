class TrieNode:

    def __init__(self):
        self.child={}
        self.isEnd=False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:

        cur=self.root
        for w in word:
            if w not in cur.child:
                cur.child[w]=TrieNode()
            cur=cur.child[w]
        cur.isEnd=True
        

    def search(self, word: str) -> bool:

        def dfs(j,root):
            cur=root

            for i in range(j,len(word)):
                w=word[i]
                if w==".":
                    for ch in cur.child.values():
                        if dfs(i+1,ch):
                            return True
                    return False

                else:
                    if w not in cur.child:
                        return False
                    cur=cur.child[w]
            return cur.isEnd

        return dfs(0,self.root)


        
