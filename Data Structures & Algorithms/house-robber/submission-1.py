class Solution:
    def rob(self, nums: List[int]) -> int:
        p2=p1=0

        for i in nums:
            tp=max(p2+i,p1)
            p2=p1
            p1=tp

        return p1
        