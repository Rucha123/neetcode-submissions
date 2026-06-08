class Solution:
    def compress(self, chars: List[str]) -> int:

        i=0
        j=0

        while j<len(chars):
            ch=chars[j]
            c=0

            while j<len(chars) and chars[j]==ch:
                c+=1
                j+=1

            chars[i]=ch
            i+=1

            if c>1:
                for k in str(c):
                    chars[i]=k
                    i+=1

        return i


        