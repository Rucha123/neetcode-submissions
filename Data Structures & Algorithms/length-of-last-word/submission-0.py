class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=[]
        s=s.lstrip()
        s=s.strip()
        s=s.split(" ")
        print(s)

        return len(s[-1])

        