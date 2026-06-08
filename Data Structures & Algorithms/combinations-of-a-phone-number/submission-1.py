class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        h={}
        res=[]
        st_asc=ord('a')

        for d in range(2,10):
            lc=4 if d in(7,9) else 3

            ltr=""
            for i in range(lc):
                asc=chr(st_asc+i)
                ltr+=asc
            h[str(d)]=ltr
            st_asc+=lc

        print(h)

        def backtrack(i,cur):
            if len(cur)==len(digits):
                res.append(cur)
                return res
            
            for c in h[digits[i]]:
                backtrack(i+1,cur+c)


        if digits:
            backtrack(0,"")

        return res

        