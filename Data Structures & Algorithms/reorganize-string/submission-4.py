class Solution:
    def reorganizeString(self, s: str) -> str:
        mc=0
        mch=""
        h={}
        res=['']*len(s)
        idx=0

        for ch in s:
            if ch not in h:
                h[ch]=1
            else:
                h[ch]+=1

        for i in h:
            if h[i]>mc:
                mc=h[i]
                mch=i

        if mc > (len(s)+1)//2:
            return ""

        while h[mch] > 0:
            res[idx]=mch
            idx+=2
            h[mch]-=1

        for i in h:
            while h[i]>0:
                if idx>=len(s):
                    idx=1
                res[idx]=i
                idx+=2
                h[i]-=1

        return "".join(res)




