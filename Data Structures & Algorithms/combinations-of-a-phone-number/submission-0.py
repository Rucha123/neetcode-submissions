class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitToChar = {}
        res=[]
        start_ascii = ord('a')  # starting letter
        for digit in range(2, 10):
            # digits 7 and 9 have 4 letters, others have 3
            letters_count = 4 if digit in (7, 9) else 3

            letters = ""
            for i in range(letters_count):
                letters += chr(start_ascii + i)

            digitToChar[str(digit)] = letters
            start_ascii += letters_count


        print(digitToChar)

        def backtrack(i,cur):
            if len(cur)==len(digits):
                res.append(cur)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1,cur+c)

        if digits:
            backtrack(0,"")

        return res

           
        