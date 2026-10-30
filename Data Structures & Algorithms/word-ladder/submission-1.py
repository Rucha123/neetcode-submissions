class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque()
        c=0
        words=set(wordList)
        q.append(beginWord)

        while q:
            c+=1
            for i in range(len(q)):
                cur=q.popleft()
                if cur==endWord:
                    return c
                for i in range(len(cur)):
                    for ch in range(97,123):
                        if chr(ch) == cur[i]:
                            continue
                        neig=cur[:i]+chr(ch)+cur[i+1:]

                        if neig in words:
                            q.append(neig)
                            words.remove(neig)

        return 0


            


            
        