class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque()
        q.append(beginWord)
        count=0
        wordSet=set(wordList)


        while q:
            count+=1

            for i in range(len(q)):
                cur=q.popleft()

                if cur == endWord:
                    return count


                for i in range(len(cur)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c in cur[i]:
                            continue
                        nw=cur[:i]+c+cur[i+1:]

                        if nw in wordSet:
                            q.append(nw)
                            wordSet.remove(nw)

        return 0

            


        