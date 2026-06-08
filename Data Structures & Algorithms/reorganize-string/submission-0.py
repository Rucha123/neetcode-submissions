class Solution:
    def reorganizeString(self, s: str) -> str:
        h={}
        mx_c=0
        mx_ch=""

        for ch in s:
            if ch not in h:
                h[ch]=1
            else:
                h[ch]+=1

        print(h)
        for i in h:
            if h[i]>mx_c:
                mx_c=h[i]
                mx_ch=i

        if mx_c>(len(s)+1)//2:
            return ""
        res=['']*len(s)
        idx=0
        while h[mx_ch] >0:
            res[idx]=mx_ch
            idx+=2
            h[mx_ch]-=1

        for i in h:
            while h[i] >0:
                if idx >=len(s):
                    idx=1
                res[idx]=i
                idx+=2
                h[i]-=1

        return "".join(res)

        